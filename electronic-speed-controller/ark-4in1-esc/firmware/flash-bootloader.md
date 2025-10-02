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

If you're flashing an ESC without firmware or the firmware has become corrupted, you can reflash the ESC with SWD to bring it back to a fresh state.

#### What You'll Need

* ARK 4IN1 ESC
* ST-Link V2 or V3 programmer
* Computer running Windows or Ubuntu
* [AM32 bootloader file](./#am32-bootloader-firmware)

#### Hardware Setup

Connect and program each MCU. If your ESC is powered with a power supply or battery **do not** connect the 3.3V

* ST-Link SWDIO → Corresponding ESC SWDIO pin
* ST-Link SWCLK → Corresponding ESC SWCLK pin
* ST-Link GND → Pin 10 (GND)
* ST-Link 3.3V → Pin 1 (3.3V) — **do not connect if ESC is externally powered**

#### Software Installation

#### **Windows**

Download the ST-Link Utility from the ST-LINK [website](https://www.st.com/en/development-tools/st-link-v2.html#tools-software).

Open the GUI and follow the [ST Documentation](https://www.st.com/en/development-tools/stsw-link007.html#documentation) to program the MCU.

#### **Ubuntu**

Follow the instructions on the official ST-LINK[ github page](https://github.com/stlink-org/stlink) to install the stlink tools.

**Test the Connection**

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

If you see an error, check your wiring.

**Erase Flash Memory**

Before flashing the bootloader, erase the flash:

```bash
st-flash erase
```

**Flash the Bootloader**

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
