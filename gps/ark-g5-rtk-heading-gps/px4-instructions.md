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
| `CANNODE_PUB_BAR` | Publish barometer messages on the CAN bus. Enabled by default |
| `CANNODE_PUB_IMU` | Set to `1` to publish `RawIMU` messages on the CAN bus. |
| `SEP_OUT_RATE` | Output rate for GNSS data messages: `-1` = OnChange, or `50` / `100` / `200` / `500` ms |
| `SEP_PVT_MODE` | Bitmask of allowed PVT modes for Rover operation. Bits: `1` = StandAlone, `2` = DGNSS, `4` = RTKFloat, `8` = RTKFixed. Default `15` (all). The receiver uses the most accurate mode available |
| `SEP_RCV_DYN` | Receiver dynamics model: `0` = Static, `1` = Quasistatic, `2` = Pedestrian, `3` = Automotive, `4` = RaceCar, `5` = HeavyMachinery, `6` = UAV (default), `7` = Unlimited |

***

## Dual Antenna Heading Configuration

The G5H provides yaw estimation using two GNSS antennas on a single DroneCAN node. The mosaic-G5 module computes the heading and reports it over DroneCAN.

### Hardware Setup

* Connect the ARK G5H RTK Heading GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable
* Connect antennas to both the MAIN and ANT2 SMA connectors
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

No change is needed on the node: the G5H ships with dual antenna saved in the receiver. The node reports a heading only with fixed ambiguities.

#### Optional

| Parameter | Description |
|-----------|-------------|
| `SEP_ANT_MODE` | `0` (default) keeps the antenna mode saved in the receiver, `1` single antenna, `2` dual antenna. `1` and `2` are applied without saving them in the receiver, which restarts once (about 10 s) at each power-up where its saved mode differs |
| `SEP_DUAL_ANT` | `0` disables heading |

***

## Troubleshooting

* **Heading not appearing** — verify `UAVCAN_SUB_GPS_R` is set to 1 and reboot the flight controller.
* **Verify antenna separation** — ensure a minimum of 30 cm between antennas. Greater separation improves heading accuracy.
* **Yaw offset** — check the [Antenna Mounting](#antenna-mounting) parameters against the actual MAIN and ANT2 positions.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
