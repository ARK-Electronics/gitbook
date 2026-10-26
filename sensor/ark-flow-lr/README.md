---
cover: ../../.gitbook/assets/IMG_4086_Edited.JPG
coverY: 0
---

# ARK Flow LR

The ARK Flow LR is a [DroneCAN](https://dronecan.github.io/) optical flow and long-range distance sensor module, with a [PixArt PAA3905](https://www.pixart.com/products-detail/108/PAA3905E1-Q_) optical flow sensor, a Broadcom AFBR-S50EX85D time-of-flight distance sensor and an [InvenSense IIM-42653](https://invensense.tdk.com/products/smartindustrial/iim-42653/) IMU. It is the [ARK Flow MR](../ark-flow-mr/README.md) with a longer-range distance sensor, and runs its own firmware. It works with PX4, ArduPilot and ROS 2 through [ros2\_dronecan](https://github.com/ARK-Electronics/ros2_dronecan). USA built and NDAA compliant.

[Buy the ARK Flow LR](https://arkelectron.com/product/ark-flow-lr/)

CAD: [3D model](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Flow_MR/model) · [case](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Flow_MR/case)

The distance sensor reports 0.6 to 100 m at 10 Hz. Range depends on the light on the ground and on the surface. See [Range](hardware.md#range).

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Updating, node parameters, downloads and release notes |
| [Hardware Reference](hardware.md) | Specifications, range, pinout, LEDs, wiring, mounting, 3D model and case |
| [PX4 Instructions](px4-instructions.md) | Connecting and configuring with PX4 |
| [ArduPilot Instructions](ardupilot-instructions.md) | Connecting and configuring with ArduPilot |
| [DroneCAN Messages](dronecan-messages.md) | Messages the ARK Flow LR publishes |
