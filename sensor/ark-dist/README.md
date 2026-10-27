---
cover: ../../.gitbook/assets/IMG_5260_edited.JPG
coverY: 38.38586956521739
---

# ARK DIST

A time-of-flight distance sensor that reports to the flight controller over DroneCAN or MAVLink.

<a href="https://arkelectron.com/product-category/sensors/rangefinders/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_DIST/model" class="button secondary" data-icon="cube">3D model</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_DIST/case" class="button secondary" data-icon="box">Case</a> <a href="https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_DIST/datasheet/ARK_DIST_Datasheet.pdf" class="button secondary" data-icon="file-pdf">Datasheet</a>

* **Sensor:** Broadcom time-of-flight, 850 nm Class 1 eye-safe laser
* **Interfaces:** 2× CAN (DroneCAN), UART (MAVLink 2)
* **Works with:** PX4, ArduPilot, ROS 2 through ros2\_dronecan
* **Compliance:** USA built, NDAA

## Variants

| Variant | Sensor | Typical range | Rate | Buy |
|---------|--------|-----------------------|------|-----|
| **ARK DIST SR** | AFBR-S50LV85D | Up to 30 m | 20 Hz | [Buy](https://arkelectron.com/product/ark-dist-sr/) |
| **ARK DIST MR** | AFBR-S50LX85D | Up to 50 m | 15 Hz | [Buy](https://arkelectron.com/product/ark-dist-mr/) |
| **ARK DIST LR** | AFBR-S50EX85D | Up to 80 m | 10 Hz | [Buy](https://arkelectron.com/product/ark-dist-lr/) |

Maximum range depends on the surface's texture and reflectivity and on ambient light; see [Range](hardware.md#range).

## Documentation

* [Firmware](firmware.md)
* [Hardware Reference](hardware.md)
* [PX4 Instructions](px4-instructions.md)
* [ArduPilot Instructions](ardupilot-instructions.md)
* [UART / MAVLink](uart-mavlink.md)
