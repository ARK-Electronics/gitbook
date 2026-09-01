---
description: >-
  What SWD is, how it works, what hardware you need, and when to use it.
---

# SWD Programming

## What is SWD?

SWD (Serial Wire Debug) is a two-wire debug and programming interface for ARM microcontrollers. It lets you flash firmware, set breakpoints, inspect memory, and access a debug console — all through a physical connection to the chip.

Every ARK product with an STM32 [microcontroller](microcontrollers.md) exposes SWD through a debug connector. It is the most reliable way to flash firmware and the only way to recover a board with a corrupted bootloader.

## How It Works

SWD uses two signals plus ground:

| Signal | Name | Direction | Purpose |
|--------|------|-----------|---------|
| SWDIO | Serial Wire Data I/O | Bidirectional | Data transfer between debugger and MCU |
| SWCLK | Serial Wire Clock | Debugger → MCU | Clock signal driven by the debugger |
| GND | Ground | — | Common reference |

The debugger (e.g., ST-LINK) connects to the MCU's internal debug port, giving it direct access to flash memory, registers, and peripherals. This works even if the firmware is completely broken — SWD operates at the hardware level, below any software.

### What You Need

* **[ST-LINK V3 Mini](https://www.digikey.com/en/products/detail/stmicroelectronics/STLINK-V3MINIE/16284301)** — programmer/debugger that connects to your computer via USB. The V3 Mini is recommended because it also provides a virtual serial port for [UART debug console](serial-communication-uart.md) access through the same USB connection.
* **[ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/)** — routes the ST-LINK's STDC14 connector to the Pixhawk Standard 6-pin or 10-pin JST-SH debug connector found on ARK boards. Includes debug cables.

The connection chain looks like this:

```
Computer ↔ USB ↔ ST-LINK V3 Mini ↔ STDC14 Cable ↔ ARK Debug Adapter ↔ JST-SH Cable ↔ Board Debug Port
```

### When to Use SWD

Most firmware updates don't require SWD. The day-to-day methods depend on the type of board:

* **Flight controllers** (ARKV6X, ARK FPV, etc.) — firmware is typically loaded via QGroundControl over USB. SWD is not needed for routine updates.
* **DroneCAN nodes** (ARK CANnode, ARK Flow, ARK MAG, etc.) — the flight controller pushes firmware from its SD card to the node over the [CAN bus](can-bus.md), or you can use the [DroneCAN GUI Tool](dronecan-gui-tool-guide.md) directly. This is the normal update path once a bootloader is installed.
* **USB DFU** — a fallback used on some boards (like the [ARK FPV](../flight-controller/ark-fpv/README.md)) to flash a bootloader over USB when the board is placed into DFU mode. Rarely needed.

SWD is for situations where none of the above work:

* **Initial bootloader flash** — a brand-new or factory-fresh DroneCAN node has no bootloader. SWD is the only way to install one so the node can accept CAN firmware updates going forward.
* **Recovery** — if a bootloader becomes corrupted or a bad firmware flash leaves the board unresponsive, SWD can overwrite flash directly and bring it back.
* **Development and debugging** — SWD lets you set breakpoints, step through code, and inspect memory. Not required for firmware development, but useful when you need it.

SWD operates at the hardware level, below any software on the chip. As long as the board is not physically damaged, SWD can recover it — regardless of the state of the bootloader or firmware.

## Debug Connector Pinouts

ARK products use one of two **Pixhawk Standard Debug Connectors** (both JST-SH). The [ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/) includes cables for both.

### 6-Pin Debug Connector

Used on most ARK DroneCAN sensors and smaller boards.

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3.3V | 3.3V |
| 2 | UART TX | 3.3V |
| 3 | UART RX | 3.3V |
| 4 | SWDIO | 3.3V |
| 5 | SWCLK | 3.3V |
| 6 | GND | GND |

### 10-Pin Debug Connector

Used on flight controllers like the [ARKV6X](../flight-controller/arkv6x/README.md). Adds a second UART and reset line.

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3.3V | 3.3V |
| 2 | UART5 TX (Debug Console) | 3.3V |
| 3 | UART5 RX (Debug Console) | 3.3V |
| 4 | FMU SWDIO | 3.3V |
| 5 | FMU SWCLK | 3.3V |
| 6 | SWO | 3.3V |
| 7 | IO SWDIO | 3.3V |
| 8 | IO SWCLK | 3.3V |
| 9 | nRST | 3.3V |
| 10 | GND | GND |

## Software Setup

Install the stlink tools from source for the most up-to-date version with the best device support:

```bash
sudo apt install build-essential cmake libusb-1.0-0-dev
git clone https://github.com/stlink-org/stlink.git
cd stlink
cmake .
make
sudo make install
sudo ldconfig
```

{% hint style="info" %}
**Prefer building from source** over `sudo apt install stlink-tools`. The packaged version in most distributions is outdated and may not support newer STM32 chips or ST-LINK firmware versions. See the [stlink-org/stlink GitHub page](https://github.com/stlink-org/stlink) for full build instructions and troubleshooting.
{% endhint %}

If you encounter permission errors after installation, add your user to the `dialout` group:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in for the change to take effect.

## Common Pitfalls

* **Skipping the debug adapter** — the ST-LINK's STDC14 connector does not directly plug into the JST-SH debug port on ARK boards. You need the ARK Pixhawk Debug Adapter or manual wiring.
* **Wrong bootloader for the firmware stack** — PX4 CAN nodes need the PX4 `canbootloader`, and AP\_Periph nodes need the ArduPilot CAN bootloader. Flashing the wrong bootloader means the node won't accept firmware updates over CAN. If a node isn't picking up firmware, check which bootloader is installed.
* **Wrong flash address** — STM32 flash starts at `0x08000000` (the bootloader). On ARK CAN nodes the application is at `0x08010000`. On PX4 STM32H7 flight controllers (ARKV6X, ARKV6S, ARK FPV, ARK Pi6X) the application is at `0x08020000`. See the [ST-LINK Flashing Guide](st-link-flashing-guide.md).
* **`.px4` over SWD** — `st-flash` takes a `.bin`. `_bootloader.px4` from PX4 GitHub releases is the USB uploader envelope.
* **Outdated stlink tools** — the version from `apt install stlink-tools` is often too old to recognize newer STM32 chips or ST-LINK firmware. Build from source (see [Software Setup](#software-setup) above).
* **Powering conflicts** — the ST-LINK can supply 3.3V to the target. If the board is already powered externally, this is usually fine, but avoid powering high-current peripherals through the debug connector.

## Further Reading

* [ST-LINK Flashing Guide](st-link-flashing-guide.md) — step-by-step flashing procedure for ARK products
* [ARM SWD Protocol Overview](https://developer.arm.com/documentation/ihi0031/a/The-Serial-Wire-Debug-Port--SW-DP-)
* [stlink-org/stlink on GitHub](https://github.com/stlink-org/stlink) — open source ST-LINK tools
