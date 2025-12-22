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

For detailed instructions on ST-LINK setup, software installation, and usage, see the [ST-LINK Flashing Guide](../../../resources/st-link-flashing-guide.md).

#### What You'll Need

* ARK 4IN1 ESC
* ST-LINK V3 Mini (recommended) or ST-LINK V2
* Computer running Windows or Ubuntu
* [AM32 bootloader file](./#am32-bootloader-firmware)

#### Hardware Setup

The ARK 4IN1 ESC uses a 10-pin debug connector with separate SWD pins for each of the 4 ESC MCUs. See the [pinout](../pinout.md) for pin assignments.

Connect and program each MCU individually. If your ESC is powered with a power supply or battery **do not** connect the 3.3V.

#### Flash the Bootloader

Flash each ESC MCU with the bootloader binary:

```bash
st-flash write AM32_F051_BOOTLOADER_PB4.bin 0x08000000
```
