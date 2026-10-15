# Flashing Guide

Bundles that include a CM4 ship pre-imaged with ARK-OS. Follow this guide if you bought the carrier alone and are installing your own compute module.

## Option 1: ARK Golden Image

The golden image is Raspberry Pi OS with the carrier's `config.txt` baked in and ARK-OS installed, the same image that ships on bundles. Download the one for your compute module from [downloads.arkelectron.com/pi/pi6x/latest](https://downloads.arkelectron.com/pi/pi6x/latest/): `pi6x-cm4-trixie-ark-os.img.xz` or `pi6x-cm5-trixie-ark-os.img.xz`. Write it to the SD card with [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (**Use custom**), without OS customization. Log in as `pi` / `raspberry`. The image configures the cameras for the Raspberry Pi Camera Module 3 (IMX708); for another camera, change the `dtoverlay=imx708` lines in `/boot/firmware/config.txt`.

For a module with eMMC, short the **BOOT** header next to the micro USB, connect the micro USB to the host, and run [rpiboot](https://www.raspberrypi.com/documentation/computers/compute-module.html#flashing-the-compute-module-emmc) so the eMMC appears as a drive. Write the image to it, then remove the jumper.

To build the image yourself, see [ark\_pi\_image](https://github.com/ARK-Electronics/ark_pi_image) (`--target pi6x-cm4` or `pi6x-cm5`).

## Option 2: Raspberry Pi Imager (manual)

Flash stock Raspberry Pi OS, then configure the carrier by hand:

{% content-ref url="pi-cm4-lite-with-micro-sd.md" %}
[pi-cm4-lite-with-micro-sd.md](pi-cm4-lite-with-micro-sd.md)
{% endcontent-ref %}

{% content-ref url="pi-cm4-with-emmc.md" %}
[pi-cm4-with-emmc.md](pi-cm4-with-emmc.md)
{% endcontent-ref %}

Then edit `config.txt` for the carrier ([After Flashing, Before Installing](after-flashing-before-installing.md)), boot, and [install ARK-OS](../../../ark-os/README.md#installing-and-updating-ark-os).
