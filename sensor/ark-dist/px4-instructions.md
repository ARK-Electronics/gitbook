# PX4 Instructions

## Hardware Setup

### Wiring

**CAN:** connect with a Pixhawk standard 4-pin JST-GH cable. See [CAN Wiring](https://docs.px4.io/main/en/can/#wiring). Chain additional nodes from the second CAN connector.

**UART:** connect the 6-pin UART JST-GH to a free FC serial port. Protocol details: [UART / MAVLink](uart-mavlink.md).

### Firmware

ARK DIST runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html) (`ark_dist_default`). Supports CAN firmware update and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation). See [Firmware](firmware.md).

## CAN Configuration

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG) | 1 | Subscribe to DroneCAN range finder messages |
| [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) | 0 | Min reported range |
| [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) | _max sensor range_ | Max reported range |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | _max sensor range_ | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |

### CAN Node Parameters

No node parameters are required for range publishing.

Configure optional node params via [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) (_Component X_ under **Vehicle Settings > Parameters**) or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |

## UART/MAVLink Configuration

No parameters need to be set on the ARK DIST. Stock firmware streams MAVLink on the UART port at 115200. See [UART / MAVLink](uart-mavlink.md).

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [MAV\_X\_CONFIG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_CONFIG) | _port_ | Port the sensor is connected to |
| [MAV\_X\_FORWARD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_FORWARD) | 0 | Disable MAVLink forwarding on this port |
| [MAV\_X\_MODE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_MODE) | 7 or 13 | Minimal or Low Bandwidth — reduces memory usage |
| [SER\_X\_BAUD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SER_TEL1_BAUD) | 115200 | Baud rate for the MAVLink port |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | _max sensor range_ | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |
