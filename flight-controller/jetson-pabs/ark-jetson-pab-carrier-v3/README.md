---
cover: ../../../.gitbook/assets/IMG_5983_edited.JPG
coverY: 0
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/
---

# ARK Jetson PAB Carrier V3

A carrier board for an NVIDIA Jetson Orin Nano or NX module and a Pixhawk Autopilot Bus flight controller, such as the ARKV6X. The [comparison table](../README.md) lists what changed from the original ARK Jetson PAB Carrier.

<a href="https://arkelectron.com/product/ark-jetson-pab-v3/" class="button primary" data-icon="cart-shopping">Buy carrier</a> <a href="https://arkelectron.com/product/ark-jetson-pab-v3-ndaa-bundle/" class="button primary" data-icon="cart-shopping">Buy NDAA bundle</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Jetson_PAB_V3/model" class="button secondary" data-icon="cube">3D model</a>

* **Flight controller I/O:** STM32F103 I/O co-processor, 16 PWM, two CAN, two 40-pin avionics connectors, 30-pin Pixhawk Payload Bus
* **Jetson interfaces:** 10/100 Ethernet switch, USB 3.0 on USB-C, two USB 2.0 on JST-GH, two CSI camera connectors, Micro HDMI, CAN, M.2 Key E
* **Power:** three 5 V, 4 A inputs (Molex Micro-Lock PLUS)
* **Software:** ARK-OS on the Jetson (preinstalled on the bundles), PX4 or ArduPilot on the flight controller
* **Compliance:** USA built, NDAA

## Where to Start

**Your bundle arrived preflashed.** The Jetson already runs ARK-OS and the flight controller already has PX4. Go to [Set Up Your Carrier](setup/), then manage it from the ARK-UI web interface.

**You have a bare board, or you want to flash it yourself.** Install a Jetson module and NVMe SSD, then start at the [Flashing Guide](flashing-guide.md).

## Documentation

* [Set Up Your Carrier](setup/README.md)
* [Using ARK-OS](using-ark-os.md)
* [Hardware Reference](hardware.md)
* [Developer Guide](developer.md)
