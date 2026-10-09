# ArduPilot Instructions

Connect and mount the ARK Flow MR as described in [Wiring](hardware.md#wiring) and [Mounting](hardware.md#mounting).

## Flight Controller Parameters

Connect the ARK Flow MR to the flight controller's CAN port and set the following parameters. Reboot the flight controller after setting them.

### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver) | 1 | Enable CAN port 1 driver |
| [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol) | 1 | Set protocol to DroneCAN |
| [FLOW\_TYPE](https://ardupilot.org/copter/docs/parameters.html#flow-type) | 6 | DroneCAN optical flow |

### Optional

To use the onboard lidar:

| Parameter | Value | Description |
|-----------|-------|-------------|
| [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) | 24 | DroneCAN rangefinder |
| [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) | 5000 | Maximum range in cm (50 m) |
| [RNGFND1\_ADDR](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-addr) | _sensor ID_ | Sensor ID of the rangefinder |
| [RNGFND1\_RECV\_ID](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-recv-id) | _node ID_ | CAN node ID of the sensor |

To compensate for sensor placement (see [sensor offset compensation](https://ardupilot.org/copter/docs/common-sensor-offset-compensation.html#common-sensor-offset-compensation)):

| Parameter | Description |
|-----------|-------------|
| [FLOW\_POS\_X](https://ardupilot.org/copter/docs/parameters.html#flow-pos-x) / [FLOW\_POS\_Y](https://ardupilot.org/copter/docs/parameters.html#flow-pos-y) / [FLOW\_POS\_Z](https://ardupilot.org/copter/docs/parameters.html#flow-pos-z) | ARK Flow MR offset from the vehicle center of gravity (meters) |

## CAN Node Parameters

The node publishes optical flow and range finder data with its default parameters. To terminate the bus, publish IMU data or change the distance sensor mode and rate, see [Node Parameters](firmware.md#node-parameters).

## Additional Notes

* [FlowHold](https://ardupilot.org/copter/docs/flowhold-mode.html#flowhold-mode) does not require the use of a rangefinder.

## ArduPilot Setup Instructions

{% embed url="https://ardupilot.org/copter/docs/common-optical-flow-sensor-setup.html" fullWidth="false" %}
Sensor Setup Instructions
{% endembed %}
