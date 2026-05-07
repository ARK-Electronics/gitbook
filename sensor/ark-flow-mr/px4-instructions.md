# PX4 Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK Flow MR is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

This corresponds to the default value (`0`) of the parameter [SENS\_FLOW\_ROT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_ROT). Change the parameter appropriately if using a different orientation.

The sensor can be mounted anywhere on the frame, but you will need to specify the focal point position, relative to vehicle center of gravity, during [PX4 configuration](https://docs.px4.io/main/en/dronecan/ark_flow.html#px4-configuration).

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK Flow MR runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

INFO

The Ark Flow MR will not boot if there is no SD card in the flight controller when powered on.

Connect the ARK Flow MR CAN to the Pixhawk CAN. Once parameters are set the module will be detected on boot. See [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan) for more detail.

#### Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation (use `3` if also driving DroneCAN ESCs) |
| [EKF2\_OF\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_CTRL) | 1 | Enable optical flow fusion in the EKF |
| [UAVCAN\_SUB\_FLOW](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_FLOW) | 1 | Subscribe to DroneCAN optical flow messages |
| [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG) | 1 | Subscribe to DroneCAN range finder messages |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | 10 | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |
| [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) | 0.08 | Min reported range |
| [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) | 50 | Max reported range |
| [SENS\_FLOW\_MINHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MINHGT) | 0.08 | Min height for optical flow fusion |
| [SENS\_FLOW\_MAXHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXHGT) | 25 | Max height for optical flow fusion |
| [SENS\_FLOW\_MAXR](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXR) | 7.4 | Max angular flow rate (PAW3902 limit) |

#### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | Set to `0` to disable GPS aiding (e.g. indoor flight) |
| [EKF2\_OF\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_X) / [EKF2\_OF\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Y) / [EKF2\_OF\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Z) | ARK Flow MR offset from the vehicle center of gravity (meters) |
| [SENS\_FLOW\_ROT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_ROT) | Sensor rotation if mounted in a non-default orientation (default `0`) |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the ARK Flow MR via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | Set to `1` on the ARK Flow MR via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) to publish the `RawIMU` messages on the CAN bus |
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` on the autopilot to subscribe to DroneCAN `RawIMU` messages. Requires `CANNODE_PUB_IMU` to also be set on the ARK Flow MR |
