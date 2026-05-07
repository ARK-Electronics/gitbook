# PX4 Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable.

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 7 | Enable GPS fusion (lon/lat + alt + 3D velocity) |

#### Optional

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO) | Set to `1` to subscribe to DroneCAN barometer messages |
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` to subscribe to DroneCAN `RawIMU` messages. |
| [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X) / [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) / [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) | GPS offset from the vehicle center of gravity (meters) |

### CAN Node Parameters

Set the following on the GPS and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_PUB_BARO` | Set to `1` to publish barometer messages on the CAN bus |
| `CANNODE_PUB_IMU` | Set to `1` to publish `RawIMU` messages on the CAN bus. |
| `SEP_OUT_RATE` | Output rate for GNSS data messages: `-1` = OnChange, or `50` / `100` / `200` / `500` ms |
| `SEP_PVT_MODE` | Bitmask of allowed PVT modes for Rover operation. Bits: `1` = StandAlone, `2` = DGNSS, `4` = RTKFloat, `8` = RTKFixed. Default `15` (all). The receiver uses the most accurate mode available |
| `SEP_RCV_DYN` | Receiver dynamics model: `0` = Static, `1` = Quasistatic, `2` = Pedestrian, `3` = Automotive, `4` = RaceCar, `5` = HeavyMachinery, `6` = UAV (default), `7` = Unlimited |

{% hint style="info" %}
The ARK G5 RTK GPS uses the single-antenna mosaic-G5 P3 module. For dual antenna heading, see the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/README.md).
{% endhint %}

***

## Troubleshooting

* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
