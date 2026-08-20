# PX4 Instructions

## Single GPS Configuration

Connect the ARK TESEO GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable.

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
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` to subscribe to DroneCAN `RawIMU` messages |
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
| `CANNODE_PUB_IMU` | Set to `1` to publish `RawIMU` messages on the CAN bus |
| `TESEO_FWUPD` | Set to `1` to force the cannode to re-flash the embedded LIV4F firmware on the next boot. The cannode auto-updates the LIV4F whenever the embedded version differs from what is on the GPS chip — this parameter is only needed to force a re-flash without a version change. Auto-cleared back to `0` after a successful update |

***

## Constellation Selection

The Teseo-LIV4F can track up to **four GNSS constellations simultaneously**. Enabling more than four has no effect — pick the four that match your operating region. SBAS does not count toward this limit. Configure these on the GPS using the same method as the [CAN Node Parameters](#can-node-parameters) above.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TESEO_GPS` | 1 | Enable the GPS (USA) constellation |
| `TESEO_GLONASS` | 1 | Enable the GLONASS (Russia) constellation |
| `TESEO_GALILEO` | 1 | Enable the Galileo (EU) constellation |
| `TESEO_BEIDOU` | 1 | Enable the BeiDou (China) constellation |
| `TESEO_QZSS` | 0 | Enable the QZSS (Japan) constellation |
| `TESEO_IRNSS` | 0 | Enable the IRNSS / NavIC (India) constellation |
| `TESEO_SBAS` | 1 | Enable SBAS (Satellite-Based Augmentation System) |

***

## Tuning EKF2_REQ_SACC

The Teseo-LIV4F can report higher speed-accuracy values than the default [EKF2\_REQ\_SACC](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_REQ_SACC) threshold (0.5 m/s), causing PX4 to reject GPS fusion. Increasing `EKF2_REQ_SACC` to **1.5–2.0 m/s** is recommended for this module.

***

## Troubleshooting

* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
