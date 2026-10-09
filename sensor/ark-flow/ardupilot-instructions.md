# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-arkflow.html" %}
Most up to date ArduPilot documentation
{% endembed %}

Connect and mount the ARK Flow as described in [Wiring](hardware.md#wiring) and [Mounting](hardware.md#mounting).

## Flight Controller Parameters

Connect the ARK Flow to the flight controller's CAN port and set the following in _Mission Planner_, then reboot the flight controller.

### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver) | 1 | Enable CAN port 1 driver |
| [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol) | 1 | Set protocol to DroneCAN |
| [FLOW\_TYPE](https://ardupilot.org/copter/docs/parameters.html#flow-type) | 6 | DroneCAN optical flow |
| [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) | 24 | DroneCAN range finder |
| [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) | 3000 | Range finder maximum range (cm) — set to 30 m |
| [RNGFND1\_ADDR](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-addr) | _sensor ID_ | Sensor ID of the rangefinder |
| [RNGFND1\_RECV\_ID](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-recv-id) | _node ID_ | CAN node ID of the ARK Flow |

### Optional

| Parameter | Description |
|-----------|-------------|
| [FLOW\_POS\_X](https://ardupilot.org/copter/docs/parameters.html#flow-pos-x) / [FLOW\_POS\_Y](https://ardupilot.org/copter/docs/parameters.html#flow-pos-y) / [FLOW\_POS\_Z](https://ardupilot.org/copter/docs/parameters.html#flow-pos-z) | ARK Flow offset from the vehicle center of gravity (meters). For example, if the sensor is mounted 2 cm forward and 5 cm below the frame's center of rotation, set `FLOW_POS_X` to `0.02` and `FLOW_POS_Z` to `0.05` |

{% hint style="info" %}
[FlowHold](https://ardupilot.org/copter/docs/flowhold-mode.html#flowhold-mode) does not require the use of a rangefinder.
{% endhint %}

## CAN Node Parameters

The node publishes optical flow and range finder data with its default parameters. To terminate the bus, publish IMU data or change the distance sensor mode and rate, see [Node Parameters](firmware.md#node-parameters).

## ArduPilot Setup Instructions

{% embed url="https://ardupilot.org/copter/docs/common-optical-flow-sensor-setup.html" %}
Sensor Setup Instructions
{% endembed %}
