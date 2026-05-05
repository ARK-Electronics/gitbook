# PX4 Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK MAG runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

#### Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |

#### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the ARK MAG via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |
