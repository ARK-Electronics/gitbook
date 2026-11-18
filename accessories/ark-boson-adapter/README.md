# ARK Boson Adapter

A breakout for the Teledyne FLIR Boson+ thermal camera module with the MIPI interface. It brings the Boson's video out on a 22-pin CSI-2 FFC, which also powers the Boson and carries the I2C the driver controls it over. The Boson's serial port and an onboard ICM-45686 IMU come out on a 6-pin JST-GH.

<a href="https://arkelectron.com/product/ark-boson-adapter/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Boson_Adapter/model" class="button secondary" data-icon="cube">3D model</a>

* **Camera module:** Teledyne FLIR Boson+ with the MIPI interface (not included)
* **In the box:** the adapter, a 22-to-22-pin and a 22-to-15-pin 0.5 mm FFC camera cable, and a 6-pin JST-GH cable
* **Video:** 2-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC, 640x512 at 60 fps
* **Control:** Boson serial port and the adapter's ICM-45686 IMU on a 6-pin JST-GH
* **Hosts:** [ARK Just A Jetson](../../embedded-computers/ark-just-a-jetson/README.md), [ARK Just A Pi](../../embedded-computers/ark-just-a-pi/README.md)
* **Compliance:** USA built, NDAA

{% hint style="warning" %}
Rev 1.0 swaps the Boson's TX and RX on the I2C/UART connector. Cross pins 2 and 3 in the cable to use the Boson's serial port. Video and the IMU are not affected.
{% endhint %}

## Documentation

* [Hardware Reference](hardware.md)
* [Jetson Setup](jetson-setup.md)
* [Just A Pi Setup](just-a-pi-setup.md)
