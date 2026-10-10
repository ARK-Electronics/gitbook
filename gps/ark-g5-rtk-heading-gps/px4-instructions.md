# PX4 Instructions

The ARK G5H RTK Heading GPS can be operated as a single-antenna GPS or with two antennas to provide GNSS-derived heading. Start with the [Single GPS Configuration](#single-gps-configuration) below, then add the [Dual Antenna Heading Configuration](#dual-antenna-heading-configuration) if you want heading.

## Single GPS Configuration

Connect the ARK G5H RTK Heading GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable.

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

The node publishes GPS, magnetometer and barometer data with its default parameters. To terminate the bus, fix the node ID, publish IMU data or change the receiver's output rate, PVT modes or dynamics model, see [Node Parameters](firmware.md#node-parameters).

***

## Dual Antenna Heading Configuration

The G5H provides yaw estimation using two GNSS antennas on a single DroneCAN node. The mosaic-G5 module computes the heading and reports it over DroneCAN.

### Hardware Setup

* Connect the ARK G5H RTK Heading GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable
* Connect an antenna to MAIN (SMA) and one to ANT2 (U.FL), through an SMA-to-U.FL cable
* Mount the antennas with a minimum of **30 cm separation** (more is better for heading accuracy)

### Flight Controller Parameters

Apply the [Single GPS Configuration](#single-gps-configuration) flight controller parameters above, then change/add the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_SUB\_GPS\_R](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS_R) | 1 | Subscribe to DroneCAN GPS relative (heading) messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 15 | Enable GPS fusion + GPS yaw (lon/lat + alt + 3D velocity + yaw). Overrides the value of `7` from the single GPS configuration |

#### Antenna Mounting

The node reports the heading of the MAIN→ANT2 baseline. Set where the antennas are mounted on the flight controller:

| PX4 version | Parameters |
|-------------|------------|
| v1.18 and earlier | `EKF2_GPS_YAW_OFF`: clockwise angle in degrees from the vehicle forward axis to the MAIN→ANT2 baseline (`0` if ANT2 is directly ahead of MAIN, `90` if ANT2 is to the right) |
| `main` | `SENS_GNSSn_HDG` `2` (Dual antenna) in the G5H's slot (`SENS_GNSSn_ID`, `n` = `0` for a single receiver), `SENS_GNSSn_OFFX/Y/Z` the position of MAIN and `SENS_GNSSn_AUXX/Y/Z` the position of ANT2, in meters in the body frame |

PX4 v1.17 and earlier use the heading only while the position is RTK fixed.

### CAN Node Parameters

No change is needed on the node: the G5H ships with dual antenna saved in the receiver. The node reports a heading only with fixed ambiguities. To override the antenna mode (`SEP_ANT_MODE`) or disable heading (`SEP_DUAL_ANT` `0`), see [Node Parameters](firmware.md#node-parameters).

***

## Troubleshooting

* **Heading not appearing** — verify `UAVCAN_SUB_GPS_R` is set to 1 and reboot the flight controller.
* **Verify antenna separation** — ensure a minimum of 30 cm between antennas. Greater separation improves heading accuracy.
* **Yaw offset** — check the [Antenna Mounting](#antenna-mounting) parameters against the actual MAIN and ANT2 positions.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
