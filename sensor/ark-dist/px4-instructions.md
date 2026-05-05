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

##### Required Parameters

Set the following in _QGroundControl_ and reboot the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation |
| [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG) | 1 | Subscribe to DroneCAN range finder messages |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | _max sensor range_ | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |
| [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) | 0 | Min reported range |
| [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) | _max sensor range_ | Max reported range |

##### Optional Parameters

| Parameter | Description |
|-----------|-------------|
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` on the ARK DIST via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) if this is the last node on the CAN bus |

#### UART/MAVLink Configuration <a href="#px4-configuration" id="px4-configuration"></a>

##### Required Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| [MAV\_X\_CONFIG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_CONFIG) | _port_ | Port the sensor is connected to |
| [MAV\_X\_FORWARD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_FORWARD) | 0 | Disable MAVLink forwarding on this port |
| [MAV\_X\_MODE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_MODE) | 7 or 13 | Minimal or Low Bandwidth — reduces memory usage |
| [SER\_X\_BAUD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SER_TEL1_BAUD) | 115200 | Baud rate for the MAVLink port |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | _max sensor range_ | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |
