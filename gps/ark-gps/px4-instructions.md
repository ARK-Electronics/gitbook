# PX4 Instructions

Find most up to date documentation at [https://docs.px4.io/main/en/dronecan/ark\_gps.html](https://docs.px4.io/main/en/dronecan/ark_gps.html)

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK GPS is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards the **back of vehicle**.

The sensor can be mounted anywhere on the frame, but you will need to specify its position, relative to vehicle center of gravity, during [PX4 configuration](https://docs.px4.io/main/en/dronecan/ark_gps.html#px4-configuration).

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK GPS runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

ARK GPS boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

* Firmware target: `ark_can-gps_default`
* Bootloader target: `ark_can-gps_canbootloader`

### PX4 Configuration <a href="#px4-configuration" id="px4-configuration"></a>

INFO

The ARK GPS will not boot if there is no SD card in the flight controller when powered on.

Connect the ARK GPS CAN to the Pixhawk CAN. Once parameters are set the module will be detected on boot and GPS data should arrive at 10Hz. See [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan) for more detail.

#### Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation (use `3` if also driving DroneCAN ESCs) |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 7 | Enable GPS fusion (lon/lat + alt + 3D velocity) |

#### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO) | Set to `1` to subscribe to DroneCAN barometer messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | Set to `15` instead of `7` in a dual-GPS rover + moving-base setup to also fuse GPS yaw (lon/lat + alt + 3D velocity + yaw) |
| [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X) / [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) / [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) | ARK GPS offset from the vehicle center of gravity (meters) |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the ARK GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |
