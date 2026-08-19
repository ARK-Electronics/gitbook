---
cover: ../../.gitbook/assets/IMG_6613_edited.JPG
coverY: 333.37784522003034
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

1. Flash SiMa Modalix eLxr and the ARK carrier overlay — [meta-ark-simaai](https://github.com/ARK-Electronics/meta-ark-simaai).
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

Do not install the Jetson Wi-Fi 6E / Remote ID M.2 option — M.2 Key E has no PCIE on Modalix.

The JAJ [Ports and Serial](../ark-just-a-jetson/connections.md) UART map (`/dev/ttyTHS*`) is for NVIDIA Jetson modules.

## Console

UART2 is the console. USB-C USB 2.0 is an FTDI console on the SOM. USB-C USB 3.0 is host only.

Do not use the Jetson USB-C gadget login (`jetson` / `192.168.55.1`).

## Storage

Boots from on-module eMMC. M.2 Key M NVMe is optional extra storage.

## Display / PCIe

ARK-sold Modalix SOMs do not include HDMI. Because HDMI is unused, PCIE2 is available.

M.2 Key M is still NVMe. M.2 Key E has no PCIE.

## ARK-OS

ARK-OS is a Debian package, not a full OS image. Flash eLxr first, then install the `modalix` platform on the board (user `sima` must exist):

```bash
git clone https://github.com/ARK-Electronics/ARK-OS.git
cd ARK-OS
sudo ./packaging/install_ark_os.sh --platform=modalix --ark-os-version=X.Y.Z
```

Build the package on arm64 (eLxr 12 or Debian 12). Do not install the `jetson` package.

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
* [meta-ark-simaai](https://github.com/ARK-Electronics/meta-ark-simaai) — ARK carrier device tree and flash tooling
* [ARK-OS](https://github.com/ARK-Electronics/ARK-OS) — `modalix` platform package
