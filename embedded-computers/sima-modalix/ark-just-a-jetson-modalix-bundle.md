---
cover: ../../.gitbook/assets/IMG_6613_edited.JPG
coverY: 0
---

# ARK Just A Jetson Modalix Bundle

ARK Just A Jetson carrier, SiMa.ai Modalix SOM, heatsink and fan. Optional NDAA 480GB M.2 NVMe SSD.

The carrier is the same hardware as [ARK Just A Jetson](../ark-just-a-jetson/). This page covers SOM differences only.

{% hint style="info" %}
The ARK carrier is NDAA. The SOM is SiMa.ai.
{% endhint %}

## Carrier Hardware

{% content-ref url="../ark-just-a-jetson/" %}
[ark-just-a-jetson](../ark-just-a-jetson/)
{% endcontent-ref %}

Use the JAJ [Hardware Reference](../ark-just-a-jetson/hardware.md) for pinout, power, and 3D models. Do not use the JAJ [Flashing Guide](../ark-just-a-jetson/flashing-guide.md) or [USB-C Console](../ark-just-a-jetson/usb-c-console.md) gadget login.

## Where to Start

Do not use NVIDIA SDK Manager or L4T. The SOM boots from built-in eMMC; an NVMe SSD is not required.

1. Apply the ARK carrier overlay to the running eLxr image — [ark-meta-simaai](https://github.com/ARK-Electronics/ark-meta-simaai). The overlay ships as a versioned release package:

   ```bash
   curl -LO https://raw.githubusercontent.com/ARK-Electronics/ark-meta-simaai/main/packaging/provision_from_package.sh
   chmod +x provision_from_package.sh
   BOARD=sima@<ip> ./provision_from_package.sh jaj
   ```

   `cat /etc/ark_modalix` afterwards reports which overlay release the board carries.
2. Install the ARK-OS `modalix` package — see [ARK-OS](ark-just-a-jetson-modalix-bundle.md#ark-os).
3. ML tooling — [SiMa.ai Palette](https://developer.sima.ai/) and [SiMa.ai hardware docs](https://developer.sima.ai/hardware).

SiMa eLxr default login: user `sima`, password `edgeai`, hostname `modalix`. ARK-OS services run as `sima`.

## Interface Differences

| Interface | Modalix                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| UART2     | Works as a console                                                                                                    |
| CAN       | No CAN interface                                                                                                      |
| HDMI      | Works only if the Modalix SOM was ordered with the HDMI option. ARK units will not have HDMI.                         |
| PCIE2     | Only works when HDMI is not used. On ARK units (no HDMI), PCIE2 is available                                          |
| M.2 Key E | No PCIE                                                                                                               |
| USB-C     | USB 3.0 works as a host. USB 2.0 on that connector goes to an FTDI console on the SOM (not Jetson gadget device mode) |
| UART0     | Works without flow control (no RTS/CTS)                                                                               |
| UART1     | Does not work                                                                                                         |
| Ethernet  | Carrier gigabit Ethernet works on stock eLxr, before the ARK overlay is applied                                        |

Do not install the Jetson Wi-Fi 6E / Remote ID M.2 option — M.2 Key E has no PCIE on Modalix.

The JAJ [Ports and Serial](../ark-just-a-jetson/connections.md) UART map (`/dev/ttyTHS*`) is for NVIDIA Jetson modules.

## Console

UART2 is the console. USB-C USB 2.0 is an FTDI console on the SOM. USB-C USB 3.0 is host only.

Do not use the Jetson USB-C gadget login (`jetson` / `192.168.55.1`). The SOM has no USB device controller at all (`/sys/class/udc` is empty), so no USB gadget networking of any kind is available — this is not just a different gadget address.

## Recovery

If the eMMC image is unbootable, reflash eLxr with SiMa's netboot path — `./flash.sh JAJ --netboot` in [ark-meta-simaai](https://github.com/ARK-Electronics/ark-meta-simaai), which drives `sima-cli` over TFTP. There is no NVIDIA Force Recovery mode on this SOM.

## Storage

Boots from on-module eMMC. M.2 Key M NVMe is optional extra storage.

## Display / PCIe

ARK-sold Modalix SOMs do not include HDMI. Because HDMI is unused, PCIE2 is available.

M.2 Key M is still NVMe. M.2 Key E has no PCIE.

## ARK-OS

ARK-OS is a Debian package, not a full OS image. Flash eLxr first, then install the `modalix` platform on the board (user `sima` must exist):

```bash
curl -fSLO https://github.com/ARK-Electronics/ARK-OS/releases/download/v1.3.0/ark-os-modalix-bookworm_1.3.0_arm64.deb
sudo apt-get install -y ./ark-os-modalix-bookworm_1.3.0_arm64.deb
```

Use `apt-get install`, not `dpkg -i` — the package has dependencies (nginx, gstreamer) that only apt resolves.

The package is named `bookworm` while eLxr 12 reports its own codename, `aria`. They are ABI-compatible; the bookworm build is the one to install. If you use `packaging/install_ark_os.sh` instead, pass `--codename=bookworm`, or it will look for an `aria` asset that is not published.

Do not install the `jetson` package.

ARK-UI is at [http://modalix.local](http://modalix.local) (or the board's IP). Do not use `jetson.local` or USB-C gadget networking.

Compared with [ARK-OS](../../ark-os/) on Jetson:

* No `jtop` / jetson-stats
* No `jetson-can` (no SOM CAN)
* No `rid-transmitter`
* FMU reset / VBUS GPIO helpers are no-ops until mapped
* mavlink-router still uses the USB flight-controller path when an FC is on USB

{% content-ref url="../../ark-os/" %}
[ark-os](../../ark-os/)
{% endcontent-ref %}

## Performance

Vendor peak ratings, not a lab benchmark:

| Module                      | Peak TOPS                 | Rated power |
| --------------------------- | ------------------------- | ----------- |
| SiMa.ai Modalix             | 50 TOPS (BF16/INT8/INT16) | sub-10W     |
| NVIDIA Jetson Orin Nano 8GB | 40 TOPS; Super 67 TOPS    | 25W         |
| NVIDIA Jetson Orin NX 16GB  | 100 TOPS; Super 157 TOPS  | 40W         |

Modalix has higher TOPS per watt than Orin Nano Super and Orin NX Super at those rated points. Peak TOPS on Super NX is higher.

## External

* [SiMa.ai MLSoC Family](https://sima.ai/mlsoc-family/)
* [SiMa.ai Developer Center (Palette)](https://developer.sima.ai/)
* [SiMa.ai Hardware Docs](https://developer.sima.ai/hardware)
* [ark-meta-simaai](https://github.com/ARK-Electronics/ark-meta-simaai) — ARK carrier device tree and flash tooling
* [ARK-OS](https://github.com/ARK-Electronics/ARK-OS) — `modalix` platform package
