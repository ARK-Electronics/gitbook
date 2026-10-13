# PX4 Instructions

Connect the ARK MAG to the flight controller's CAN port as described in [Wiring](hardware.md#wiring).

## Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |

## CAN Node Parameters

The node publishes magnetometer data with its default parameters (`CANNODE_PUB_MAG` is `1`). To terminate the bus or fix the node ID, see [Node Parameters](firmware.md#node-parameters).
