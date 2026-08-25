---
description: >-
  This page details flashing the bootloader firmware using SWD, or letting
  ARK32 firmware update it.
---

# Flash Bootloader

Get the ARK 4IN1 bootloader **`AM32_F051_BOOTLOADER_ARK4IN1`** from **[ARK32-bootloader](https://github.com/ARK-Electronics/ARK32-bootloader)** ([releases](https://github.com/ARK-Electronics/ARK32-bootloader/releases)). The filename includes a version suffix (for example `_V18`).

The [ARK32 Configurator](https://ark32.arkelectron.com/) does not flash the bootloader. Use a factory image, an app flash that embeds a newer bootloader, or SWD as below.

## App-side bootloader update

Flashing current [ARK32](https://github.com/ARK-Electronics/ARK32/releases) app firmware can rewrite the on-chip bootloader if it differs. After a successful rewrite the ESC resets and plays two rising beeps, then the normal startup tune. See [Bootloader](https://github.com/ARK-Electronics/ARK32#bootloader) in the ARK32 README.

## Factory image (blank chip)

For a **blank chip**, flash the full-chip factory image from [ARK32 releases](https://github.com/ARK-Electronics/ARK32/releases). Use **`ARK32_ARK_4IN1_F051_<version>.factory.bin`**. That one file writes the bootloader, app, and EEPROM defaults.

Setup, probe, and `st-flash` usage: [ST-LINK Flashing Guide](../../../knowledge-base/st-link-flashing-guide.md). Then:

```bash
st-flash write ARK32_ARK_4IN1_F051_<version>.factory.bin 0x08000000
```

You can also build the same image with `make factory-image` in [ARK32](https://github.com/ARK-Electronics/ARK32).

***

## Flashing Bootloader via SWD

If you're flashing an ESC without firmware or the firmware has become corrupted, you can reflash the ESC with SWD to bring it back to a fresh state.

For detailed instructions on ST-LINK setup, software installation, and usage, see the [ST-LINK Flashing Guide](../../../knowledge-base/st-link-flashing-guide.md).

#### What You'll Need

* ARK 4IN1 ESC
* ST-LINK V3 Mini (recommended) or ST-LINK V2
* Computer running Windows or Ubuntu
* `AM32_F051_BOOTLOADER_ARK4IN1` from [ARK32-bootloader releases](https://github.com/ARK-Electronics/ARK32-bootloader/releases)

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

Releases publish Intel HEX, which carries its own load address — there is no offset to pass:

```bash
st-flash --format ihex write AM32_F051_BOOTLOADER_ARK4IN1_V18.hex
```
