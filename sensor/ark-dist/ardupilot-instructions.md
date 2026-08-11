# ArduPilot Instructions

## Hardware Setup

### Wiring

**CAN:** connect with a Pixhawk standard 4-pin JST-GH cable. See [CAN Wiring](https://docs.px4.io/main/en/can/#wiring). Chain additional nodes from the second CAN connector.

**UART:** connect the 6-pin UART JST-GH to a free FC serial port. Protocol details: [UART / MAVLink](uart-mavlink.md).

See the [ArduPilot rangefinder setup guide](https://ardupilot.org/copter/docs/common-rangefinder-setup.html) for additional configuration guidance.

## CAN Configuration

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) | 24 | DroneCAN |
| [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) | _max sensor range_ | Range finder maximum range |
| [RNGFND1\_ADDR](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-addr) | _sensor ID_ | Sensor ID of the rangefinder |
| [RNGFND1\_RECV\_ID](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-recv-id) | _node ID_ | CAN node ID of the sensor |

{% hint style="info" %}
If you intend to use multiple distance sensors, you will need [this ArduPilot PR](https://github.com/ArduPilot/ardupilot/pull/31931).
{% endhint %}

### CAN Node Parameters

No node parameters are required for range publishing.

Configure optional node params via [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |

## UART/MAVLink Configuration

No parameters need to be set on the ARK DIST. Stock firmware streams MAVLink on the UART port at 115200. See [UART / MAVLink](uart-mavlink.md).

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) | 10 | MAVLink |
| [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) | _max sensor range_ | Range finder maximum range |
| [SERIALX\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#serial0-protocol-console-protocol-selection) | 2 | MAVLink2 |
| [SERIALX\_BAUD](https://ardupilot.org/copter/docs/parameters.html#serial0-baud-serial0-baud-rate) | 115 | 115200 baud |
