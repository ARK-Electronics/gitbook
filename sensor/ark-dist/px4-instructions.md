# PX4 Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK DIST is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK DIST’s second CAN connector.

The ARK DIST can also be connected with UART and communicates over MAVLink sending the [DISTANCE\_SENSOR](https://mavlink.io/en/messages/common.html#DISTANCE_SENSOR) message.&#x20;

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK DIST runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

#### CAN Configuration <a href="#px4-configuration" id="px4-configuration"></a>

Set the following parameters in _QGroundControl_:

* [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` for dynamic node allocation
* Enable [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG).
* Set [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) to the max sensor range
* Set [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) to 0.2
* Set [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) to 0
* Set [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) to the max sensor range

#### UART/MAVLink Configuration <a href="#px4-configuration" id="px4-configuration"></a>

* Set [MAV\_X\_CONFIG ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_CONFIG)to the port the sensor is connected to
* Set [MAV\_X\_FORWARD ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_FORWARD)to 0 (off)
* Set [MAV\_X\_MODE ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_MODE)to 7 or 13 (Minimal or Low Bandwidth) to reduce memory usage
* Set [SER\_X\_BAUD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SER_TEL1_BAUD) to 115200
* Set [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) to the max sensor range
* Set [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) to 0.2
