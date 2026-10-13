# Flashing Guide

Bundles that include a CM4 ship pre-imaged with ARK-OS. Follow this guide if you bought the carrier alone and are installing your own compute module.

## Option 1: ARK Golden Image (CM4)

The [ark\_pi\_image](https://github.com/ARK-Electronics/ark_pi_image) repository builds the image that ships on bundles: Raspberry Pi OS with the carrier's `config.txt` baked in and ARK-OS installed. On a Linux host:

```bash
git clone https://github.com/ARK-Electronics/ark_pi_image.git
cd ark_pi_image
./build.sh --target pi6x-cm4 --provision
./flash.sh --target pi6x-cm4
```

`flash.sh` finds the SD card and asks for confirmation before writing. For a CM4 with eMMC, short the **BOOT** header next to the micro USB, connect the micro USB to the host, and run [rpiboot](https://www.raspberrypi.com/documentation/computers/compute-module.html#flashing-the-compute-module-emmc) so the eMMC appears as a block device. Then run `./flash.sh --target pi6x-cm4 /dev/sdX` and remove the jumper.

## Option 2: Raspberry Pi Imager (CM4 or CM5)

There is no golden image for the CM5 on this carrier. Flash stock Raspberry Pi OS, then configure the carrier by hand:

{% content-ref url="pi-cm4-lite-with-micro-sd.md" %}
[pi-cm4-lite-with-micro-sd.md](pi-cm4-lite-with-micro-sd.md)
{% endcontent-ref %}

{% content-ref url="pi-cm4-with-emmc.md" %}
[pi-cm4-with-emmc.md](pi-cm4-with-emmc.md)
{% endcontent-ref %}

Then edit `config.txt` for the carrier ([After Flashing, Before Installing](after-flashing-before-installing.md)), boot, and [install ARK-OS](../using-ark-os.md).
