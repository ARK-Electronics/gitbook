---
description: >-
  Guide for using ST-LINK to flash firmware and access the debug console on ARK products.
---

# ST-LINK Flashing Guide

## Overview

### What is SWD?

SWD (Serial Wire Debug) is a two-wire debug interface for ARM microcontrollers. It provides programming and debugging capabilities using just two signals (SWDIO and SWCLK) plus ground. All ARK products with STM32 microcontrollers include an SWD interface on their debug connector.

### What is ST-LINK?

ST-LINK is a programmer/debugger from STMicroelectronics designed for their STM32 microcontroller family. It connects to your computer via USB and to the target board via the SWD interface, allowing you to flash firmware and debug applications.

### Why ST-LINK V3 Mini?

We recommend the **ST-LINK V3 Mini** because it is a composite USB device that provides both the programmer interface and a virtual serial port in a single USB connection. This means you can flash firmware and access the UART debug console without needing a separate USB-to-serial adapter.

When you connect an ST-LINK V3 Mini to your computer, it creates multiple USB interfaces:

**Example `dmesg` output:**

```
usb 1-3: new high-speed USB device number 66 using xhci_hcd
usb 1-3: New USB device found, idVendor=0483, idProduct=3754, bcdDevice= 1.00
usb 1-3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
usb 1-3: Product: STLINK-V3
usb 1-3: Manufacturer: STMicroelectronics
usb 1-3: SerialNumber: 003500313133510F37363734
cdc_acm 1-3:1.1: ttyACM0: USB ACM device
```

The `ttyACM0` device is the virtual serial port you can use for UART debug console access.

***

## What You'll Need

* **[ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/)** - Includes 6-pin and 10-pin JST-SH debug cables
* **ST-LINK V3 Mini** (recommended) or ST-LINK V2
* **Computer** running Ubuntu or Windows
* **Firmware binary file** (.bin)

***

## Hardware Setup

The [ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/) makes connecting an ST-LINK to ARK products simple - no manual wiring required.

1. Connect the ST-LINK V3 Mini to the adapter's STDC14 connector using the cable that comes with the ST-LINK
2. Connect the appropriate JST-SH debug cable (6-pin or 10-pin) from the adapter to your ARK product's debug port
3. Connect the ST-LINK to your computer via USB

The adapter routes SWD signals (SWDIO, SWCLK, GND) and UART signals (TX, RX) between the ST-LINK and the Pixhawk Standard Debug connector.

{% hint style="warning" %}
**Power:** The ST-LINK can provide 3.3V power to the target. If your board is already powered from another source (battery, USB, etc.), the adapter handles this safely. However, for boards that draw significant current, power from an external source is recommended.
{% endhint %}

***

## Software Installation

### Ubuntu

Install the stlink tools from the official repository:

```bash
sudo apt install stlink-tools
```

Alternatively, you can build from source by following the instructions on the [stlink-org/stlink GitHub page](https://github.com/stlink-org/stlink).

**Permissions:** If you encounter permission errors, add your user to the `dialout` group:

```bash
sudo usermod -aG dialout $USER
```

Log out and back in for the change to take effect.

### Windows

1. Download the **ST-LINK Utility** from the [STMicroelectronics website](https://www.st.com/en/development-tools/st-link-v2.html#tools-software)
2. Install the utility and USB drivers
3. Refer to the [ST-LINK documentation](https://www.st.com/en/development-tools/stsw-link007.html#documentation) for detailed usage instructions

***

## Flashing Firmware

### Ubuntu

#### Test the Connection

After connecting your ST-LINK to both your computer and the target board, verify the connection:

```bash
st-info --probe
```

**Expected output (example for ARK FPV):**

```
Found 1 stlink programmers
  version:    V3J8
  serial:     003800333433510937363934
  flash:      2097152 (pagesize: 131072)
  sram:       131072
  chipid:     0x450
  dev-type:   STM32H74x_H75x
```

**Expected output (example for ARK 4IN1 ESC):**

```
Found 1 stlink programmers
  version:    V2J45S7
  serial:     543C0A135550
  flash:      32768 (pagesize: 1024)
  sram:       4096
  chipid:     0x0440
  dev-type:   STM32F03x/STM32F05x
```

If you see an error or no device found, check your wiring connections.

#### Erase Flash Memory (Optional)

Before flashing new firmware, you may want to erase the existing flash. On PX4 boards with FLASH based parameters (ARK FPV, ARK Pi6X) this will also wipe all parameters back to default. If you don't mass erase, parameters will remain unchanged.

```bash
st-flash erase
```

#### Flash Firmware

Navigate to the directory containing your firmware binary, then flash:

```bash
st-flash write firmware.bin 0x08000000
```

**Expected output:**

```
st-flash 1.8.0
2025-01-15T10:30:00 INFO common.c: STM32H74x: 128 KiB SRAM, 2048 KiB flash
file firmware.bin md5 checksum: abc123..., stlink checksum: 0x00abcdef
2025-01-15T10:30:00 INFO common.c: Attempting to write 524288 (0x80000) bytes to stm32 address: 134217728 (0x8000000)
2025-01-15T10:30:05 INFO common.c: Flash written and verified! jolly good!
```

### Windows

1. Open **ST-LINK Utility**
2. Click **Target > Connect** to connect to your board
3. Click **File > Open File** and select your firmware binary (.bin file)
4. Click **Target > Program & Verify**
5. Verify the success message in the log window

***

## UART Debug Console

The debug connector provides a serial console (UART) for viewing system output and debugging. This is useful for accessing the NuttX shell, viewing boot messages, and debugging issues.

### Connection

When using the ARK Pixhawk Debug Adapter with an ST-LINK V3 Mini, the UART signals are routed through the adapter. The ST-LINK V3 Mini's composite USB creates a virtual serial port (`/dev/ttyACM0` on Linux, `COMx` on Windows) that provides access to the debug console.

No additional wiring or adapters are needed.

### Serial Terminal Settings

* **Baud rate:** 57600
* **Data bits:** 8
* **Stop bits:** 1
* **Parity:** None
* **Flow control:** None

### Ubuntu

Using `screen`:

```bash
screen /dev/ttyACM0 57600
```

To exit screen, press `Ctrl+A` then `K`, then `Y` to confirm.

### Windows

Use a serial terminal application such as:

* **PuTTY** - Select "Serial" connection type, enter the COM port, and set speed to 57600
* **Tera Term** - Select serial port and configure 57600 baud, 8N1

***

## Troubleshooting

### "No ST-LINK detected"

* Check that the USB cable is connected properly
* Try a different USB port
* Verify the ST-LINK USB drivers are installed (Windows)
* Check `dmesg` output (Linux) to see if the device is recognized

### "Target voltage detected" or Similar Errors

* Ensure proper power configuration - either power from ST-LINK OR external source, not both.
* Disconnect peripheral devices in case they are drawing too much power.

### Permission Denied (Linux)

Add your user to the dialout group:

```bash
sudo usermod -aG dialout $USER
```

Then log out and back in.

### Flash Verification Failed

* Ensure the correct firmware binary for your target
* Try erasing flash first with `st-flash erase`
* Check that the flash address (0x08000000) is correct for your target

### Serial Console Shows Garbage Characters

* Verify the baud rate is set to 57600
* Check TX/RX connections are not swapped
* Ensure common ground between ST-LINK and target board
