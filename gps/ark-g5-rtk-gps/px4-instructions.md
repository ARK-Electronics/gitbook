# PX4 Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters in _QGroundControl_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |

Reboot the autopilot. The GPS should be detected automatically and begin reporting position data.

### Sensor Position Configuration

If the sensor is not centered within the vehicle you will also need to define sensor offsets:

* The parameters [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X), [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) and [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) can be set to account for the offset of the ARK G5 RTK GPS from the vehicle center of gravity.

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

### CAN Node Parameter

The `SEP_DUAL_ANT` parameter must be set on the G5H CAN node to enable dual antenna heading. This can be configured using [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SEP_DUAL_ANT` | 3 | Enable Fixed + Float ambiguities (default, recommended) |

The parameter is a bitmask with the following options:

| Bit | Value | Mode |
|-----|-------|------|
| 0 | 1 | Fixed — highest accuracy |
| 1 | 2 | Float — less accurate but more robust |
| Both | 3 | Fixed + Float — receiver uses best available |

{% hint style="info" %}
A reboot of the CAN node is required after changing `SEP_DUAL_ANT`.
{% endhint %}

### Flight Controller Parameters

Set the following parameters in _QGroundControl_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_GPS\_R](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS_R) | 1 | Subscribe to DroneCAN GPS relative (heading) messages |
| [EKF2\_GPS\_YAW\_OFFSET](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_YAW_OFFSET) | 0 | Heading offset in degrees between antenna baseline and vehicle forward axis |

{% hint style="info" %}
`EKF2_GPS_YAW_OFFSET` defines the clockwise rotation from the vehicle forward axis to the baseline from MAIN to ANT2. Set to `0` if ANT2 is directly ahead of MAIN, `90` if ANT2 is to the right, etc. This is equivalent to the `SEP_OFFS_YAW` node parameter — use one or the other, not both.
{% endhint %}

Reboot the autopilot after setting these parameters.

***

## Troubleshooting

* **Heading not appearing** — verify `UAVCAN_SUB_GPS_R` is set to 1 and reboot the flight controller.
* **Verify antenna separation** — ensure a minimum of 30 cm between antennas. Greater separation improves heading accuracy.
* **SEP\_OFFS\_YAW parameter** — if the antennas are not aligned along the vehicle's forward axis, set the `SEP_OFFS_YAW` parameter on the G5H node to the clockwise rotation angle, or set `EKF2_GPS_YAW_OFFSET` on the flight controller.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
