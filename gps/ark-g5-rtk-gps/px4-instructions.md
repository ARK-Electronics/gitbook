# PX4 Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable.

### Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 7 | Enable GPS fusion (lon/lat + alt + 3D velocity) |

### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X) / [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) / [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) | GPS offset from the vehicle center of gravity (meters) |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | Set to `1` on the GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) to publish the `RawIMU` messages on the CAN bus |
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` on the autopilot to subscribe to DroneCAN `RawIMU` messages. Requires `CANNODE_PUB_IMU` to also be set on the GPS |

***

## Dual Antenna Heading Configuration (G5H Only)

{% hint style="warning" %}
Dual antenna heading requires the **ARK G5H RTK GPS** (with the Septentrio mosaic-G5 P3H module). The standard ARK G5 RTK GPS (P3 module) only supports a single antenna and cannot provide heading.
{% endhint %}

The G5H provides compass-free yaw estimation using two GNSS antennas on a single DroneCAN node. The mosaic-G5 module handles the moving baseline calculation internally and reports the heading over DroneCAN.

### Hardware Setup

* Connect the ARK G5H RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable
* Connect antennas to both the MAIN and ANT2 SMA connectors
* Mount the antennas with a minimum of **30 cm separation** (more is better for heading accuracy)

### Required Parameters

The `SEP_DUAL_ANT` parameter must be set on the G5H CAN node via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md). The remaining parameters are set on the autopilot in _QGroundControl_. Reboot both the CAN node and the autopilot after changes.

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SEP_DUAL_ANT` | 3 | Enable Fixed + Float ambiguities on the G5H (default, recommended). Bitmask: `1`=Fixed, `2`=Float, `3`=both |
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_GPS\_R](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS_R) | 1 | Subscribe to DroneCAN GPS relative (heading) messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 15 | Enable GPS fusion + GPS yaw (lon/lat + alt + 3D velocity + yaw) |

### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [EKF2\_GPS\_YAW\_OFFSET](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_YAW_OFFSET) | Clockwise rotation in degrees from the vehicle forward axis to the MAIN→ANT2 baseline (e.g. `0` if ANT2 is directly ahead of MAIN, `90` if ANT2 is to the right). Equivalent to the `SEP_OFFS_YAW` node parameter — use one or the other, not both |

***

## Troubleshooting

* **Heading not appearing** — verify `UAVCAN_SUB_GPS_R` is set to 1 and reboot the flight controller.
* **Verify antenna separation** — ensure a minimum of 30 cm between antennas. Greater separation improves heading accuracy.
* **SEP\_OFFS\_YAW parameter** — if the antennas are not aligned along the vehicle's forward axis, set the `SEP_OFFS_YAW` parameter on the G5H node to the clockwise rotation angle, or set `EKF2_GPS_YAW_OFFSET` on the flight controller.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
