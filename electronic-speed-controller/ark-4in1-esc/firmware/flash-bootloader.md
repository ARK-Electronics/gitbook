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

For detailed instructions on ST-LINK setup, software installation, and usage, see the [ST-LINK Flashing Guide](../../../knowledge-base/st-link-flashing-guide.md).

#### What You'll Need

* ARK 4IN1 ESC
* ST-LINK V3 Mini (recommended) or ST-LINK V2
* Computer running Windows or Ubuntu
* [AM32 bootloader file](./#am32-bootloader-firmware)

#### Hardware Setup

The ARK 4IN1 ESC has 4 separate STM32F051 microcontrollers (one per motor channel), each with their own SWD interface on a single 10-pin debug connector. See the [pinout](../pinout.md) for the full connector diagram.

| Pin | Signal |
|-----|--------|
| 1 | 3.3V |
| 2 | SWDIO 1 (ESC 1) |
| 3 | SWCLK 1 (ESC 1) |
| 4 | SWDIO 2 (ESC 2) |
| 5 | SWCLK 2 (ESC 2) |
| 6 | SWDIO 3 (ESC 3) |
| 7 | SWCLK 3 (ESC 3) |
| 8 | SWDIO 4 (ESC 4) |
| 9 | SWCLK 4 (ESC 4) |
| 10 | GND |

To flash each ESC, connect your ST-LINK to the corresponding SWDIO/SWCLK pair. For example, to flash ESC 1:

| ST-LINK Pin | Debug Connector Pin | Signal |
|-------------|---------------------|--------|
| SWDIO | Pin 2 | SWDIO 1 |
| SWCLK | Pin 3 | SWCLK 1 |
| GND | Pin 10 | GND |
| 3.3V (optional) | Pin 1 | 3.3V |

{% hint style="warning" %}
If your ESC is powered from a battery or power supply, **do not** connect the 3.3V line from the ST-LINK.
{% endhint %}

Repeat the process for ESC 2-4 using their respective SWDIO/SWCLK pins (4/5, 6/7, 8/9).

#### Flash the Bootloader

Flash each ESC MCU with the bootloader binary:

```bash
st-flash write AM32_F051_BOOTLOADER_PB4.bin 0x08000000
```
