# Ardupilot Instructions



{% embed url="https://ardupilot.org/copter/docs/common-arkflow.html" %}
Most Up to date ArduPilot documentations
{% endembed %}

### Connection to Autopilot

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK Flow is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK Flow’s second CAN connector.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

#### Connection to Autopilot <a href="#mounting" id="mounting"></a>

* Connect the sensor to the autopilots’ CAN port
* Set [FLOW\_TYPE](https://ardupilot.org/copter/docs/parameters.html#flow-type) = 6 (DroneCAN)
* Set [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver) = 1 to enable DroneCAN
* Set [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol) = 1 (DroneCAN)

To use the onboard lidar:

* Set [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) = 24 (DroneCAN)
* Set [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) = 3000 to set range finder’s maximum range to 30m

#### Additional Notes <a href="#mounting" id="mounting"></a>

* [FlowHold](https://ardupilot.org/copter/docs/flowhold-mode.html#flowhold-mode) does not require the use of a rangefinder
* Performance can be improved by setting the [sensors position parameters](https://ardupilot.org/copter/docs/common-sensor-offset-compensation.html#common-sensor-offset-compensation). For example if the sensor is mounted 2cm forward and 5cm below the frame’s center of rotation set [FLOW\_POS\_X](https://ardupilot.org/copter/docs/parameters.html#flow-pos-x) to 0.02 and [FLOW\_POS\_Z](https://ardupilot.org/copter/docs/parameters.html#flow-pos-z) to 0.05.

#### ArduPilot Setup Instructions

{% embed url="https://ardupilot.org/copter/docs/common-optical-flow-sensor-setup.html" %}
Sensor Setup Instructions
{% endembed %}
