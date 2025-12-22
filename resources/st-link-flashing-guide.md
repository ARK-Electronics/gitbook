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

* **ST-LINK V3 Mini** (recommended) or ST-LINK V2
* **Debug cable** - 6-pin or 10-pin JST-SH depending on your product
* **Computer** running Ubuntu or Windows
* **Firmware binary file** (.bin)

***

## Hardware Setup

# TODO: for hardware setup we should say just get the ARK debug adaptor (look it up if you need to), the stlink v3 mini, and the jst sh cable. Since this is all that is needed, the ark debug adaptor makes it easy to connect the stlink and the jst sh debug cable without having to do any manual pinouts.

# TODO: we should put the below 4-in-1 specific SWD stuff in the ESC page.

To flash each ESC, connect your ST-LINK to the corresponding SWDIO/SWCLK pair:

**Example for ESC 1:**

| ST-LINK V3 Pin | Debug Connector Pin | Signal |
|----------------|---------------------|--------|
| Pin 1 (VCC) | Pin 1 | 3.3V (**do not connect if ESC is externally powered**) |
| Pin 2 (SWCLK) | Pin 3 | SWCLK 1 |
| Pin 4 (SWDIO) | Pin 2 | SWDIO 1 |
| Pin 3 or 5 (GND) | Pin 10 | GND |

Repeat for ESC 2-4 using their respective SWDIO/SWCLK pins.

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

### Connection Methods

**Using ST-LINK V3 Mini (Recommended):**

The ST-LINK V3 Mini's composite USB creates a virtual serial port (`/dev/ttyACM0` on Linux, `COMx` on Windows) that you can connect to debug pins 2 (TX) and 3 (RX) as shown in the hardware setup section above.

**Using ST-LINK V2 with Separate USB-Serial Adapter:**

If using an ST-LINK V2 (which does not have a built-in serial port), connect a separate USB-to-serial adapter:

| USB-Serial Adapter | Debug Connector Pin | Signal |
|--------------------|---------------------|--------|
| RX | Pin 2 | Debug TX |
| TX | Pin 3 | Debug RX |
| GND | Pin 6 | GND |

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
