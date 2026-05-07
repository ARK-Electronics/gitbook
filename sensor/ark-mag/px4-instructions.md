# PX4 Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK MAG runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |

### CAN Node Parameters

Set the following on the magnetometer and reboot the node. CAN node parameters can be configured using either:

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
