# Ardupilot Instructions

### Connection to Autopilot

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

#### Connection to Autopilot with CAN <a href="#mounting" id="mounting"></a>

* Set [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver-index-of-virtual-driver-to-be-used-with-physical-can-interface) = 1 (First Driver)
* Set [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol-enable-use-of-specific-protocol-over-virtual-driver) = 1  (Dronecan)
* Set [COMPASS\_ENABLE](https://ardupilot.org/copter/docs/parameters.html#compass-enable-enable-compass) = 1 (Enabled)

#### ArduPilot Setup Instructions

[https://ardupilot.org/copter/docs/common-compass-setup-advanced.html](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html)





