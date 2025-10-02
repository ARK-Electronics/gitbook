---
description: >-
  This page details flashing the bootloader firmware using am32-configurator or
  SWD.
---

# Flash Bootloader

## Flashing Bootloader via AM32&#x20;

You can update the bootloader using the [AM32 Configurator](https://am32.ca/configurator). Once connected select "Flash firmware" and select the "Bootloader" tab. Download the **AM32-bootloader-updaters-amj.zip** from the [AM32-bootloader release artifacts](https://github.com/am32-firmware/AM32-bootloader/releases). Select the **AM32\_F051\_BL\_UPDATER\_PB4\_V15.amj.**

***

## Flashing Bootloader via SWD

If you're flashing an ESC without firmware or the firmware has become corrupted, you can reflesh the ESC with SWD to bring it back to a fresh state.

#### What You'll Need

* ARK 4IN1 ESC
* ST-Link V2 or V3 programmer
* Power supply for the ESC (3s-8s LiPo or bench power supply, 6-33V)
* Computer running Windows or Ubuntu 22.04+
* AM32 bootloader file (AM32\_F051\_BOOTLOADER\_PB4.bin)

#### Hardware Setup

You will flash one MCU at a time, connecting three wires from your ST-Link to the appropriate pins on the debug connector:

* ST-Link SWDIO → Corresponding ESC SWDIO pin
* ST-Link SWCLK → Corresponding ESC SWCLK pin
* ST-Link GND → Pin 10 (GND)

**Important:** Do NOT connect the 3.3V pin from the ST-Link. Power the ESC through its main battery input (6-33V). It's recommended to flash without motors connected.

#### Software Installation

**Windows**

1. Download the latest Windows release from the [stlink releases page](https://github.com/stlink-org/stlink/releases)
2. Choose the correct version for your system (i686 for 32-bit or x86\_64 for 64-bit)
3. Extract the archive to `C:\Program Files\stlink` or `C:\Program Files (x86)\stlink`
4. Add the stlink folder to your system PATH:
   * Open System Properties → Advanced → Environment Variables
   * Edit the PATH variable and add the stlink installation directory
   * Click OK to save

**USB Driver Setup:**

Windows requires USB driver installation for the ST-Link:

1. Download and install [Zadig](https://zadig.akeo.ie/)
2. Connect your ST-Link to your computer
3. Open Zadig and select your ST-Link device from the dropdown
4. Select WinUSB driver
5. Click "Replace Driver" or "Install Driver"

**Verify Installation:**

Open Command Prompt or PowerShell and run:

```bash
st-info --version
```

**Ubuntu**

Follow the instructions on the official [stlink-org github page](https://github.com/stlink-org/stlink) to install the stlink tools.

#### Flashing Process

You must flash the bootloader to each of the four MCUs individually.

**Step 1: Connect to MCU**

For each ESC:

1. Power off the ESC
2. Connect your ST-Link to the corresponding SWD pins
3. Power on the ESC (6-33V on main battery input)
4. Connect the ST-Link to your computer via USB

**Step 2: Verify Connection**

Test the connection to ensure the MCU is detected:

```bash
st-info --probe
```

You should see output similar to:

```
Found 1 stlink programmers
  version:    V2J45S7
  serial:     543C0A135550
  flash:      32768 (pagesize: 1024)
  sram:       4096
  chipid:     0x0440
  dev-type:   STM32F03x/STM32F05x
```

If you see an error, check your wiring and ensure the ESC is powered.

**Step 3: Erase Flash Memory**

Before flashing the bootloader, erase the flash:

```bash
st-flash erase
```

**Step 4: Flash the Bootloader**

Navigate to the directory containing AM32\_F051\_BOOTLOADER\_PB4.bin, then flash it:

```bash
st-flash write AM32_F051_BOOTLOADER_PB4.bin 0x08000000
```

You should see output indicating successful flash:

```
st-flash 1.8.0
2025-10-01T12:34:56 INFO common.c: F0xx (Low/Medium): 4 KiB SRAM, 32 KiB flash in at least 1 KiB pages.
file AM32_F051_BOOTLOADER_PB4.bin md5 checksum: a3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8, stlink checksum: 0x001234ab
2025-10-01T12:34:56 INFO common.c: Attempting to write 6144 (0x1800) bytes to stm32 address: 134217728 (0x8000000)
2025-10-01T12:34:56 INFO common.c: Flash written and verified! jolly good!
```
