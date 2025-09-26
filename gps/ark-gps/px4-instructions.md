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

You need to set necessary [DroneCAN](https://docs.px4.io/main/en/dronecan/) parameters and define offsets if the sensor is not centered within the vehicle. The required settings are outlined below.

INFO

The ARK GPS will not boot if there is no SD card in the flight controller when powered on.

#### Enable DroneCAN <a href="#enable-dronecan" id="enable-dronecan"></a>

In order to use the ARK GPS board, connect it to the Pixhawk CAN bus and enable the DroneCAN driver by setting parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` for dynamic node allocation (or `3` if using [DroneCAN ESCs](https://docs.px4.io/main/en/dronecan/escs.html)).

The steps are:

* In _QGroundControl_ set the parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` or `3` and reboot (see [Finding/Updating Parameters](https://docs.px4.io/main/en/advanced_config/parameters.html)).
* Connect ARK GPS CAN to the Pixhawk CAN.

Once enabled, the module will be detected on boot. GPS data should arrive at 10Hz.

DroneCAN configuration in PX4 is explained in more detail in [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan).

#### Sensor Position Configuration <a href="#sensor-position-configuration" id="sensor-position-configuration"></a>

If the sensor is not centered within the vehicle you will also need to define sensor offsets:

* Enable GPS yaw fusion by setting bit 3 of [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) to true.
* Enable [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS), [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG), and [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO).
* Set [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) to `1` if this is that last node on the CAN bus.
* The parameters [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X), [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) and [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) can be set to account for the offset of the ARK GPS from the vehicles centre of gravity.
