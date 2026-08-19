---
cover: ../../.gitbook/assets/IMG_5983_edited.JPG
coverY: 0
---

# ARK Jetson PAB V3 Modalix Bundle

ARK Jetson PAB Carrier V3, SiMa.ai Modalix SOM, heatsink and fan. Optional NDAA 480GB M.2 NVMe SSD.

The carrier is the same hardware as [ARK Jetson PAB Carrier V3](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/) — ARKV6X flight controller, Pixhawk Autopilot Bus, I/O co-processor, avionics connectors, and Payload Bus. This page covers SOM differences only.

{% hint style="info" %}
The ARK carrier is NDAA. The SOM is SiMa.ai.
{% endhint %}

## Carrier Hardware

{% content-ref url="../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/" %}
[ark-jetson-pab-carrier-v3](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/)
{% endcontent-ref %}

Use the PAB V3 [Hardware Reference](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/hardware.md) for pinout, power, and 3D models. Do not use the PAB V3 [Flashing Guide](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/flashing-guide.md) or [USB-C Console](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/micro-usb-console.md) gadget login.

## Where to Start

Do not use NVIDIA SDK Manager or L4T. The SOM boots from built-in eMMC; an NVMe SSD is not required.

1. Flash SiMa Modalix eLxr and the ARK PAB V3 carrier overlay — [meta-ark-simaai](https://github.com/ARK-Electronics/meta-ark-simaai).
2. Install the ARK-OS `modalix` package — see [ARK-OS](#ark-os).
3. ML tooling — [SiMa.ai Palette](https://developer.sima.ai/) and [SiMa.ai hardware docs](https://developer.sima.ai/hardware).

SiMa eLxr default login: user `sima`, password `edgeai`, hostname `modalix`. ARK-OS services run as `sima`.

## Interface Differences

| Interface | Modalix |
| --------- | ------- |
| UART2 | Works as a console (UART2 debug header) |
| CAN | No SOM CAN. Flight-controller CAN on the avionics connectors is unchanged. |
| HDMI | Works only if the Modalix SOM was ordered with the HDMI option. ARK units will not have HDMI. The V3 Micro HDMI connector is unused. |
| PCIE2 | Only works when HDMI is not used. On ARK units (no HDMI), PCIE2 is available |
| M.2 Key E | No PCIE |
| USB-C | USB 3.0 works as a host. USB 2.0 on that connector goes to an FTDI console on the SOM (not Jetson gadget device mode) |
| UART0 | Works without flow control (no RTS/CTS) |
| UART1 | Does not work. On this carrier UART1 is the SOM-to-flight-controller serial (Telem2). |

Do not install the Jetson Wi-Fi 6E / Remote ID M.2 option — M.2 Key E has no PCIE on Modalix.

The PAB V3 [Autopilot Connections](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/autopilot-connections/) UART map (`/dev/ttyTHS1` → Telem2) is for NVIDIA Jetson modules.

## Flight Controller

USB and Ethernet between the Modalix SOM and the ARKV6X are functional. UART1 / Telem2 is not.

Use USB or Ethernet for MAVLink (and for DDS, if you need it). Do not use the Jetson serial path.

Flight-controller CAN, PWM, GPS, and the rest of the avionics connectors are on the ARKV6X and are unchanged.

## Console

UART2 is the console. USB-C USB 2.0 is an FTDI console on the SOM. USB-C USB 3.0 is host only.

Do not use the Jetson USB-C gadget login (`jetson` / `192.168.55.1`).

## Storage

Boots from on-module eMMC. M.2 Key M NVMe is optional extra storage.

## Display / PCIe

ARK-sold Modalix SOMs do not include HDMI. The V3 Micro HDMI connector is unused. Because HDMI is unused, PCIE2 is available.

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
* mavlink-router can use the USB flight-controller path
* Do not use XRCE-DDS on UART1 / Telem2 — that serial link does not work

{% content-ref url="../../ark-os/" %}
[ark-os](../../ark-os/)
{% endcontent-ref %}

## Performance

Vendor peak ratings, not a lab benchmark:

| Module | Peak TOPS | Rated power |
| ------ | --------- | ----------- |
| SiMa.ai Modalix | 50 TOPS (BF16/INT8/INT16) | sub-10W |
| NVIDIA Jetson Orin Nano 8GB | 40 TOPS; Super 67 TOPS | 25W |
| NVIDIA Jetson Orin NX 16GB | 100 TOPS; Super 157 TOPS | 40W |

Modalix has higher TOPS per watt than Orin Nano Super and Orin NX Super at those rated points. Peak TOPS on Super NX is higher.

## External

* [SiMa.ai MLSoC Family](https://sima.ai/mlsoc-family/)
* [SiMa.ai Developer Center (Palette)](https://developer.sima.ai/)
* [SiMa.ai Hardware Docs](https://developer.sima.ai/hardware)
* [meta-ark-simaai](https://github.com/ARK-Electronics/meta-ark-simaai) — ARK carrier device tree and flash tooling
* [ARK-OS](https://github.com/ARK-Electronics/ARK-OS) — `modalix` platform package
