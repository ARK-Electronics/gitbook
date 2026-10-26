---
cover: ../../.gitbook/assets/ark_rtk_gps_1.jpg
coverY: 0
---

# ARK RTK GPS

An open source DroneCAN RTK GNSS module that connects to a flight controller's CAN port.

<a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_RTK_GPS/model" class="button secondary" data-icon="cube">3D model</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_RTK_GPS/case" class="button secondary" data-icon="box">Case</a>

* **Receiver:** u-blox ZED-F9P, centimeter-level RTK
* **Sensors:** Bosch BMM150 magnetometer, Bosch BMP388 barometer, InvenSense ICM-42688-P IMU
* **Interface:** 2× CAN, F9P UART2, safety switch, buzzer
* **Autopilots:** PX4, ArduPilot (AP\_Periph recommended)
* **Compliance:** USA built, NDAA, Blue Framework listed (L1/L2 model)

## Variants

| Variant | Receiver | Moving baseline heading | Buy |
|---------|----------|-------------------------|-----|
| **ARK RTK GPS** | u-blox ZED-F9P, L1/L2 | Yes | [Buy](https://arkelectron.com/product/ark-rtk-gps/) |
| **ARK RTK GPS L1L5** | u-blox ZED-F9P-15B, L1/L5 | No | [Buy](https://arkelectron.com/product/ark-rtk-gps-l1-l5/) |

## Documentation

* [Firmware](firmware.md)
* [Hardware Reference](hardware.md)
* [PX4 Instructions](px4-instructions.md)
* [ArduPilot Instructions](ardupilot-instructions.md)
