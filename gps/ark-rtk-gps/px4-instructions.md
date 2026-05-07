# PX4 Instructions

See the official [PX4 Documentation](https://docs.px4.io/main/en/dronecan/ark_rtk_gps.html#setting-up-moving-baseline-gps-heading)

## Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | Set to `1` on the ARK RTK GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) to publish the `RawIMU` messages on the CAN bus |
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` on the autopilot to subscribe to DroneCAN `RawIMU` messages. Requires `CANNODE_PUB_IMU` to also be set on the ARK RTK GPS |
