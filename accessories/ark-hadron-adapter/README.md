---
cover: ../../.gitbook/assets/ARK Hadron Adapter on Hadron 640R.jpg
coverY: 0
---

# ARK Hadron Adapter

A breakout for the Teledyne FLIR Hadron 640R and 640R+ camera module. The Hadron plugs into the 50-pin connector on the underside, and the adapter brings its visible (EO) camera out on a 22-pin MIPI CSI-2 FFC, its thermal (IR) camera out on a USB JST-GH, and its control I2C out on a 6-pin JST-GH. An onboard ICM-45686 IMU shares the control I2C and tags the Hadron's frame-sync pulses, for camera and IMU synchronization.

<a href="https://arkelectron.com/product/ark-hadron-adapter/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Hadron_Adapter/model" class="button secondary" data-icon="cube">3D model</a>

* **Camera module:** Teledyne FLIR Hadron 640R / 640R+ (not included)
* **In the box:** the adapter, a 22-to-22-pin and a 22-to-15-pin 0.5 mm FFC camera cable, a 4-pin and a 6-pin JST-GH cable
* **EO camera:** 4-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC
* **IR camera:** USB 2.0 on a 4-pin JST-GH
* **Control:** Hadron I2C and the adapter's ICM-45686 IMU on a 6-pin JST-GH
* **Hosts:** [ARK Just A Jetson](../../embedded-computers/ark-just-a-jetson/README.md), [ARK Jetson PAB Carrier V3](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/README.md), [ARK Jetson PAB Carrier](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier/README.md), [ARK Just A Pi](../../embedded-computers/ark-just-a-pi/README.md)
* **Compliance:** USA built, NDAA

## Documentation

* [Hardware Reference](hardware.md)
* [Jetson Setup](jetson-setup.md)
* [Just A Pi Setup](just-a-pi-setup.md)
