# PX4 Instructions

Connect the ARK TESEO GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable.

## Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 7 | Enable GPS fusion (lon/lat + alt + 3D velocity) |

## Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO) | Set to `1` to subscribe to the barometer over DroneCAN |
| [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X) / [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) / [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) | GPS offset from the vehicle center of gravity (meters) |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |

## Tuning EKF2_REQ_SACC

The Teseo-LIV4F can report higher speed-accuracy values than the default [EKF2\_REQ\_SACC](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_REQ_SACC) threshold (0.5 m/s), causing PX4 to reject GPS fusion. Increasing `EKF2_REQ_SACC` to **1.5–2.0 m/s** is recommended for this module.

## Constellation Selection

Constellation selection is configured via the `TESEO_*` parameters on the GPS DroneCAN node, not on the autopilot. See the [Parameter Reference](./#parameter-reference) on the landing page for details.
***

## Troubleshooting

* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
