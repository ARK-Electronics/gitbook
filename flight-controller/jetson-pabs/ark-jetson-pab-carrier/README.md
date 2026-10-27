---
cover: ../../../.gitbook/assets/Jetson_PAB-3.jpg
coverY: -16
---

# ARK Jetson PAB Carrier

A carrier board for an NVIDIA Jetson Orin Nano or NX module and a Pixhawk Autopilot Bus flight controller, such as the [ARKV6X](../../arkv6x/README.md). The [comparison table](../README.md) lists what changed in the ARK Jetson PAB Carrier V3.

<a href="https://arkelectron.com/product/ark-jetson-pab-carrier/" class="button primary" data-icon="cart-shopping">Buy carrier</a> <a href="https://arkelectron.com/product/ark-jetson-pab-ndaa-bundle/" class="button primary" data-icon="cart-shopping">Buy NDAA bundle</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Jetson_PAB_Carrier/model" class="button secondary" data-icon="cube">3D model</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Jetson_PAB_Carrier/case" class="button secondary" data-icon="box">Case</a>

* **Flight controller I/O:** eight PWM, two CAN, two TELEM, two GPS, RC, SPI, I2C on JST-GH
* **Jetson interfaces:** gigabit Ethernet (RJ45), three USB 3.0 and one USB 2.0 Type-A, four CSI cameras, Mini DisplayPort, CAN, M.2 Key E
* **Power:** three 5 V, 6 A inputs (Molex CLIK-Mate)
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
