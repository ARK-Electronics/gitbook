---
cover: ../../.gitbook/assets/IMG_5857_edited.JPG
coverY: 0
---

# ARK G5 RTK GPS

The ARK G5 RTK GPS is a [DroneCAN](https://dronecan.github.io/) RTK GNSS module built around a Septentrio [mosaic-G5 P3](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3), [P6](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P6) or [P8](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-g5-p8) module, with a magnetometer, barometer, IMU and buzzer. It works with PX4 and ArduPilot. USA built and NDAA compliant.

Buy: [ARK G5 P3 RTK GPS](https://arkelectron.com/product/ark-g5-rtk-gps/) · [ARK G5 P6 RTK GPS](https://arkelectron.com/product/ark-g5-p6-rtk-gps/) · [ARK G5 P8 RTK GPS](https://arkelectron.com/product/ark-g5-p8-rtk-gps/)

| Variant | ANT2 |
|---------|------|
| P3 | Not active |
| P6, P8 | `SEP_ANT_MODE` `2` turns on dual antenna heading, configured as on the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/README.md) |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Updating node and receiver firmware, node parameters, downloads and release notes |
| [Hardware Reference](hardware.md) | Specifications, pinout, LEDs, 3D model and case |
| [PX4 Instructions](px4-instructions.md) | Connecting and configuring with PX4, and heading from two units as moving base and rover |
| [ArduPilot Instructions](ardupilot-instructions.md) | Connecting and configuring with ArduPilot |
| [Web GUI Login](web-gui-login.md) | Receiver web interface over USB-C, login and spectrum analyzer |
