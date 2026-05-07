# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-arkflow.html" %}
Most up to date ArduPilot documentation
{% endembed %}

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK Flow is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK Flow's second CAN connector.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

### Flight Controller Parameters

Connect the ARK Flow to the flight controller's CAN port and set the following in _Mission Planner_, then reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver) | 1 | Enable CAN port 1 driver |
| [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol) | 1 | Set protocol to DroneCAN |
| [FLOW\_TYPE](https://ardupilot.org/copter/docs/parameters.html#flow-type) | 6 | DroneCAN optical flow |
| [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) | 24 | DroneCAN range finder |
| [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) | 3000 | Range finder maximum range (cm) — set to 30 m |
| [RNGFND1\_ADDR](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-addr) | _sensor ID_ | Sensor ID of the rangefinder |
| [RNGFND1\_RECV\_ID](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-recv-id) | _node ID_ | CAN node ID of the ARK Flow |

#### Optional

| Parameter | Description |
|-----------|-------------|
| [FLOW\_POS\_X](https://ardupilot.org/copter/docs/parameters.html#flow-pos-x) / [FLOW\_POS\_Y](https://ardupilot.org/copter/docs/parameters.html#flow-pos-y) / [FLOW\_POS\_Z](https://ardupilot.org/copter/docs/parameters.html#flow-pos-z) | ARK Flow offset from the vehicle center of gravity (meters). For example, if the sensor is mounted 2 cm forward and 5 cm below the frame's center of rotation, set `FLOW_POS_X` to `0.02` and `FLOW_POS_Z` to `0.05` |

{% hint style="info" %}
[FlowHold](https://ardupilot.org/copter/docs/flowhold-mode.html#flowhold-mode) does not require the use of a rangefinder.
{% endhint %}

### CAN Node Parameters

Optical flow and range finder messages are published by the ARK Flow by default — no CAN node parameters are required for those streams.

Set the following on the sensor and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_PUB_IMU` | Set to `1` to publish [`RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) messages on the CAN bus |

#### ArduPilot Setup Instructions

{% embed url="https://ardupilot.org/copter/docs/common-optical-flow-sensor-setup.html" %}
Sensor Setup Instructions
{% endembed %}
