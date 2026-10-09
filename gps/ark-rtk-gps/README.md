---
cover: ../../.gitbook/assets/ark_rtk_gps_1.jpg
coverY: 0
---

# ARK RTK GPS

The ARK RTK GPS is an open source [DroneCAN](https://dronecan.github.io/) RTK GNSS module built around the [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module) multi-band receiver, with a magnetometer, barometer, IMU, buzzer and safety switch. It works with PX4 and ArduPilot. The ARK RTK GPS L1L5 variant uses the u-blox ZED-F9P-15B, which receives the L1/L5 bands instead of L1/L2; the L5 band improves resilience to interference and multipath. Aside from the receiver, the L1L5 variant is identical to the standard ARK RTK GPS: it uses the same DroneCAN interface, onboard sensors, pinout, and firmware. USA built and FCC compliant; the L1/L2 ARK RTK GPS is [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).

Buy: [ARK RTK GPS](https://arkelectron.com/product/ark-rtk-gps/) · [ARK RTK GPS L1L5](https://arkelectron.com/product/ark-rtk-gps-l1-l5/)

| Variant | Receiver | Bands | Moving baseline heading |
|---------|----------|-------|-------------------------|
| ARK RTK GPS | u-blox ZED-F9P | L1/L2 | Yes |
| ARK RTK GPS L1L5 | u-blox ZED-F9P-15B | L1/L5 | No |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Updating, AP\_Periph, node parameters, downloads and release notes |
| [Hardware Reference](hardware.md) | Specifications, pinout, LEDs, 3D model and case, schematic and BOM |
| [PX4 Instructions](px4-instructions.md) | Single GPS, RTK corrections and moving baseline heading with PX4 |
| [ArduPilot Instructions](ardupilot-instructions.md) | Single GPS and dual GPS heading with ArduPilot |
