# Ardupilot Instructions

### Connection to Autopilot

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK DIST is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK DIST’s second CAN connector.

The ARK DIST can also be connected with UART and communicates over MAVLINK sending the [DISTANCE\_SENSOR](https://mavlink.io/en/messages/common.html#DISTANCE_SENSOR) message.&#x20;

#### Connection to Autopilot with CAN <a href="#mounting" id="mounting"></a>

* Set [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) = 24 (DroneCAN)
* Set [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) = to set range finder’s maximum range

#### Connection to Autopilot with UART/MAVLink <a href="#mounting" id="mounting"></a>

* Set [RNGFND1\_TYPE](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-type) = 10 (MAVLink)
* Set [RNGFND1\_MAX](https://ardupilot.org/copter/docs/parameters.html#rngfnd1-max) = to set range finder’s maximum range
* Set [SERIALX parameter](https://ardupilot.org/copter/docs/parameters.html#serial-parameters) for the port it is connected to
* Set [SERIALX\_BAUD ](https://ardupilot.org/copter/docs/parameters.html#serial0-baud-serial0-baud-rate)= 115 (115200)
* Set [SERIALX\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#serial0-protocol-console-protocol-selection) = 2  (MAVLink2)

#### ArduPilot Setup Instructions

[https://ardupilot.org/copter/docs/common-rangefinder-setup.html](https://ardupilot.org/copter/docs/common-rangefinder-setup.html)





