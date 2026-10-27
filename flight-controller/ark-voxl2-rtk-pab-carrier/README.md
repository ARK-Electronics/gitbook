---
cover: ../../.gitbook/assets/IMG_1998_edited.JPG
coverY: 8
---

# ARK VOXL2 RTK PAB Carrier

A carrier board for a ModalAI VOXL2 and a Pixhawk Autopilot Bus flight controller module, with an onboard RTK GPS. It takes any PAB flight controller, such as the [ARKV6X](../arkv6x/README.md).

<a href="https://arkelectron.com/product/ark-voxl2-rtk-pab-carrier/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_VOXL2_RTK_PAB_Carrier/model" class="button secondary" data-icon="cube">3D model</a>

* **GNSS:** u-blox ZED-F9P, L1/L2 RTK; heading needs a second ZED-F9P GPS as the moving base or rover
* **Flight controller I/O:** eight PWM, two CAN, three UARTs and two I2C on a 40-pin Molex Pico-Clasp; SPI and debug on JST
* **Payload I/O:** battery output, autopilot and VOXL2 UARTs and USB 2.0 on a 40-pin Molex Pico-Clasp; VOXL2 USB-C and USB 2.0 ports
* **Power:** dual 5 V 6 A power module inputs with I2C; a battery input, up to 12S and 3 A, feeds only the payload battery output
* **Compliance:** USA built, NDAA, Blue Framework listed

## Documentation

* [Hardware Reference](hardware.md)
* [Autopilot Connections](autopilot-connections.md)
