# PX4 Instructions

## Single GPS Configuration

Connect the ARK MOSAIC-X5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters in _QGroundControl_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |

Reboot the autopilot. The GPS should be detected automatically and begin reporting position data.

### Sensor Position Configuration

If the sensor is not centered within the vehicle you will also need to define sensor offsets:

* The parameters [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X), [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) and [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) can be set to account for the offset of the ARK MOSAIC-X5 RTK GPS from the vehicle center of gravity.

### CAN Node Configuration

On the ARK MOSAIC-X5 RTK GPS, you may need to configure the following parameter via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md):

| Parameter                                                                                          | Value | Description                                                                |
| -------------------------------------------------------------------------------------------------- | ----- | -------------------------------------------------------------------------- |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | 1     | Enable the built-in CAN bus termination resistor. Set to `1` only if this device is the last node on the CAN bus. |

***

## Troubleshooting

* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
