---
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/flashing-guide.md
---

# Flashing Guide

Bundles ship pre-flashed with the ARK Jetson image and ARK-OS. Follow this guide to update to a newer release or to flash a Jetson for the first time.

The image is built from the [ark\_jetson\_kernel](https://github.com/ARK-Electronics/ark_jetson_kernel) repository, which adds the carrier's device tree to NVIDIA's JetPack. One image covers every Orin Nano/NX module variant.

{% hint style="info" %}
A stock NVIDIA JetPack image will not enable all carrier hardware — use the ARK image, or build from source with the ARK device tree.
{% endhint %}

## Enter Recovery Mode

Connect the **USB-C** port to your host PC, then power on the Jetson while holding the **Force Recovery** button.

## Flash a Prebuilt Release (recommended)

On a Debian/Ubuntu host, download the flasher script and flash the latest PAB V3 release to the NVMe SSD:

```bash
curl -LO https://raw.githubusercontent.com/ARK-Electronics/ark_jetson_kernel/main/packaging/flash_from_package.sh
chmod +x flash_from_package.sh
./flash_from_package.sh pab-v3
```

The script downloads the release package from the [releases page](https://github.com/ARK-Electronics/ark_jetson_kernel/releases) (tags starting with `pab-v3-`), waits for the Jetson in recovery mode, and flashes the bootloader and root filesystem. No build tools needed. Pass a specific tag instead of `pab-v3` to flash a specific version.

{% hint style="warning" %}
`pab-v3` images are for this product only. The original ARK Jetson PAB Carrier — including its hardware revision 3 (PAB Rev 3) — uses `pab` images.
{% endhint %}

## Build From Source

To customize the kernel, device tree, or preinstalled software, build and flash from source — see the [ark\_jetson\_kernel README](https://github.com/ARK-Electronics/ark_jetson_kernel#build--flash):

```bash
./setup.sh            # one-time download of BSP + rootfs + sources
./build.sh PAB_V3     # build and provision the image (installs ARK-OS)
./flash.sh PAB_V3     # flash to NVMe (--sdcard and --usb also available)
```

You can bake a WiFi profile into the image before flashing with `./scripts/add_wifi_network.sh PAB_V3 <ssid> <password>`.
