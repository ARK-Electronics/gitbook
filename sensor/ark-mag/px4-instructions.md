# PX4 Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK MAG runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

#### CAN Configuration <a href="#px4-configuration" id="px4-configuration"></a>

Set the following parameters in _QGroundControl_:

* [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` for dynamic node allocation
* Enable [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference#UAVCAN_SUB_MAG)
