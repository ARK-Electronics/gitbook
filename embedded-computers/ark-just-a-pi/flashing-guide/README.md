# Flashing Guide

Bundles that include a CM5 ship pre-imaged with ARK-OS — no flashing required. Follow this guide if you purchased just the carrier and are installing your own Compute Module.

## Option 1: ARK Golden Image (recommended)

The [ark\_pi\_image](https://github.com/ARK-Electronics/ark_pi_image) repository builds the same turnkey image that ships on bundles: Raspberry Pi OS with the carrier's `config.txt` configuration baked in and ARK-OS pre-installed. On a Linux host:

```bash
git clone https://github.com/ARK-Electronics/ark_pi_image.git
cd ark_pi_image
./build.sh --provision        # build the Just A Pi CM5 image with ARK-OS
./flash.sh /dev/sdX           # write it to the SD card
```

No Raspberry Pi Imager and no manual `config.txt` edits. For a CM5 with onboard eMMC (no SD slot), short the `BOOT` jumper, connect USB-C, run [rpiboot](https://www.raspberrypi.com/documentation/computers/compute-module.html#flashing-the-compute-module-emmc) so the eMMC appears as a block device, then `./flash.sh` to it.

## Option 2: Raspberry Pi Imager (manual)

Flash stock Raspberry Pi OS, then configure the carrier by hand:

{% content-ref url="pi-cm5-lite-with-micro-sd.md" %}
[pi-cm5-lite-with-micro-sd.md](pi-cm5-lite-with-micro-sd.md)
{% endcontent-ref %}

{% content-ref url="pi-cm5-with-emmc.md" %}
[pi-cm5-with-emmc.md](pi-cm5-with-emmc.md)
{% endcontent-ref %}

Then edit `config.txt` for the carrier ([After Flashing, Before Installing](after-flashing-before-installing.md)), boot, and [install ARK-OS](../using-ark-os.md).
