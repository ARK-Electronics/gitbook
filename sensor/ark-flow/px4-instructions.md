# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/dronecan/ark_flow.html" %}
Most up to date PX4 Documentation
{% endembed %}

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK Flow is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

This corresponds to the default value (`0`) of the parameter [SENS\_FLOW\_ROT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_ROT). Change the parameter appropriately if using a different orientation.

The sensor can be mounted anywhere on the frame, but you will need to specify the focal point position, relative to vehicle centre of gravity, during [PX4 configuration](https://docs.px4.io/main/en/dronecan/ark_flow.html#px4-configuration).

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK Flow runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

ARK Flow boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

* Firmware target: `ark_can-flow_default`
* Bootloader target: `ark_can-flow_canbootloader`

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

INFO

The Ark Flow will not boot if there is no SD card in the flight controller when powered on.

#### Enable DroneCAN <a href="#enable-dronecan" id="enable-dronecan"></a>

In order to use the ARK Flow board, connect it to the Pixhawk CAN bus and enable the UAVCAN driver by setting parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` for dynamic node allocation (or `3` if using [DroneCAN ESCs](https://docs.px4.io/main/en/dronecan/escs.html)).

The steps are:

* In _QGroundControl_ set the parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` or `3` and reboot (see [Finding/Updating Parameters](https://docs.px4.io/main/en/advanced_config/parameters.html)).
* Connect ARK Flow CAN to the Pixhawk CAN.

Once enabled, the module will be detected on boot.

DroneCAN configuration in PX4 is explained in more detail in [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan).

#### PX4 Configuration <a href="#px4-configuration" id="px4-configuration"></a>

You need to set the EKF optical flow parameters to enable fusing optical flow measurements for velocity calculation, set necessary [DroneCAN](https://docs.px4.io/main/en/dronecan/) parameters, and define offsets if the sensor is not centred within the vehicle.

Set the following parameters in _QGroundControl_:

* Enable optical flow fusion by setting [EKF2\_OF\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_CTRL).
* To optionally disable GPS aiding, set [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) to `0`.
* Enable [UAVCAN\_SUB\_FLOW](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_FLOW).
* Enable [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG).
* Set [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) to `10`.
* Set [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) to `0.2`.
* Set [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) to `0.08`.
* Set [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) to `30`.
* Set [SENS\_FLOW\_MINHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MINHGT) to `0.08`.
* Set [SENS\_FLOW\_MAXHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXHGT) to `25`.
* Set [SENS\_FLOW\_MAXR](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXR) to `7.4` to match the PAW3902 maximum angular flow rate.
* The parameters [EKF2\_OF\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_X), [EKF2\_OF\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Y) and [EKF2\_OF\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Z) can be set to account for the offset of the Ark Flow from the vehicle centre of gravity.

### Ark Flow Configuration <a href="#ark-flow-configuration" id="ark-flow-configuration"></a>

On the ARK Flow, you may need to configure the following parameters:

| Parameter                                                                                          | Description                   |
| -------------------------------------------------------------------------------------------------- | ----------------------------- |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | CAN built-in bus termination. |
