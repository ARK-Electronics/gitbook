---
cover: ../../.gitbook/assets/IMG_5857_edited.JPG
coverY: 0
---

# ARK G5 RTK Heading GPS

The ARK G5 RTK Heading GPS is a [DroneCAN](https://dronecan.github.io/) RTK GNSS module built around a Septentrio [mosaic-G5 P3H](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3H), [P6](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P6) or [P8](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-g5-p8) module, with a magnetometer, barometer, IMU and buzzer. It takes two antennas on MAIN and ANT2 and provides compass-free yaw estimation, computing the heading in the module and reporting it over DroneCAN as a single GPS node. It works with PX4 and ArduPilot. USA built and NDAA compliant. For the single-antenna P3, see the [ARK G5 RTK GPS](../ark-g5-rtk-gps/README.md).

Buy: [ARK G5 P3H RTK Heading GPS](https://arkelectron.com/product/ark-g5-rtk-heading-gps/) · [ARK G5 P6 RTK GPS](https://arkelectron.com/product/ark-g5-p6-rtk-gps/) · [ARK G5 P8 RTK GPS](https://arkelectron.com/product/ark-g5-p8-rtk-gps/)

CAD: [3D model](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_G5_RTK_GPS/model) · [case](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_G5_RTK_GPS/case)

| Variant | Antenna mode as shipped |
|---------|-------------------------|
| P3H | Dual antenna |
| P6, P8 | Single antenna. `SEP_ANT_MODE` `2` turns on dual antenna |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Updating node and receiver firmware, node parameters, downloads and release notes |
| [Hardware Reference](hardware.md) | Specifications, pinout, LEDs, 3D model and case |
| [PX4 Instructions](px4-instructions.md) | Connecting and configuring with PX4, including dual antenna heading |
| [ArduPilot Instructions](ardupilot-instructions.md) | Connecting and configuring with ArduPilot, including dual antenna heading and checking it in logs |
| [Web GUI Login](web-gui-login.md) | Receiver web interface over USB-C, login and spectrum analyzer |
