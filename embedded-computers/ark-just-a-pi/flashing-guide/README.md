# Flashing Guide

Bundles that include a CM5 ship pre-imaged with ARK-OS — no flashing required. Follow this guide if you purchased just the carrier and are installing your own Compute Module.

## Option 1: ARK Golden Image (recommended)

The golden image is Raspberry Pi OS with the carrier's `config.txt` baked in and ARK-OS installed, the same image that ships on bundles. Download the one for your compute module from [downloads.arkelectron.com/pi/just-a-pi/latest](https://downloads.arkelectron.com/pi/just-a-pi/latest/): `justapi-cm5-trixie-ark-os.img.xz` or `justapi-cm4-trixie-ark-os.img.xz`. Write it to the SD card with [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (**Use custom**), without OS customisation. Log in as `pi` / `raspberry`. The image configures the cameras for the Raspberry Pi Camera Module 3 (IMX708); for another camera, change the `dtoverlay=imx708` lines in `/boot/firmware/config.txt`.

For a module with eMMC, hold the **BOOT** button while powering the board, connect the USB JST-GH port to the host, and run [rpiboot](https://www.raspberrypi.com/documentation/computers/compute-module.html#flashing-the-compute-module-emmc) so the eMMC appears as a drive. Write the image to it.

To build the image yourself, see [ark\_pi\_image](https://github.com/ARK-Electronics/ark_pi_image) (`--target justapi-cm5` or `justapi-cm4`).

## Option 2: Raspberry Pi Imager (manual)

Flash stock Raspberry Pi OS, then configure the carrier by hand:

{% content-ref url="pi-cm5-lite-with-micro-sd.md" %}
[pi-cm5-lite-with-micro-sd.md](pi-cm5-lite-with-micro-sd.md)
{% endcontent-ref %}

{% content-ref url="pi-cm5-with-emmc.md" %}
[pi-cm5-with-emmc.md](pi-cm5-with-emmc.md)
{% endcontent-ref %}

Then edit `config.txt` for the carrier ([After Flashing, Before Installing](after-flashing-before-installing.md)), boot, and [install ARK-OS](../using-ark-os.md).
