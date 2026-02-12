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

### SWD vs Other Flashing Methods

| Method | Interface | When to Use |
|--------|-----------|-------------|
| **SWD** | Debug connector | Initial bootloader flash, recovery, debugging |
| **DroneCAN** | CAN bus | Routine firmware updates on CAN nodes |
| **USB DFU** | USB | Bootloader-mode firmware updates (some boards) |
| **SD Card** | SD slot | PX4 firmware updates on flight controllers |

SWD is the only method that works regardless of the state of the bootloader or firmware. If a board is completely bricked, SWD can recover it.

## How ARK Products Use It

All ARK products with STM32 MCUs include a **Pixhawk Standard Debug Connector** (6-pin JST-SH) that exposes SWD and UART signals:

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3.3V | 3.3V |
| 2 | UART TX | 3.3V |
| 3 | UART RX | 3.3V |
| 4 | SWDIO | 3.3V |
| 5 | SWCLK | 3.3V |
| 6 | GND | GND |

Common SWD use cases:

* **Flash a bootloader** onto a new or recovered [ARK CANnode](../sensor/ark-cannode/README.md), [ARK Flow](../sensor/ark-flow/README.md), or other DroneCAN sensor so it can accept CAN firmware updates.
* **Flash PX4 or ArduPilot** directly onto an [ARKV6X](../flight-controller/arkv6x/README.md) or [ARK FPV](../flight-controller/ark-fpv/README.md) during development.
* **Access the NuttX debug console** for troubleshooting via the UART lines on the same connector.

## Common Pitfalls

* **Skipping the debug adapter** — the ST-LINK's STDC14 connector does not directly plug into the JST-SH debug port on ARK boards. You need the ARK Pixhawk Debug Adapter or manual wiring.
* **Wrong flash address** — STM32 flash typically starts at `0x08000000`. Using the wrong address will produce a seemingly successful flash but a non-functional board.
* **Powering conflicts** — the ST-LINK can supply 3.3V to the target. If the board is already powered externally, this is usually fine, but avoid powering high-current peripherals through the debug connector.
* **Permission errors on Linux** — if `st-flash` or `st-info` reports permission denied, add your user to the `dialout` group: `sudo usermod -aG dialout $USER` and re-login.

## Further Reading

* [ST-LINK Flashing Guide](../resources/st-link-flashing-guide.md) — step-by-step flashing procedure for ARK products
* [ARM SWD Protocol Overview](https://developer.arm.com/documentation/ihi0031/a/The-Serial-Wire-Debug-Port--SW-DP-)
* [stlink-org/stlink on GitHub](https://github.com/stlink-org/stlink) — open source ST-LINK tools
