# PX4 Instructions

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

Configure [GPS\_1\_CONFIG ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#GPS_1_CONFIG)to match the port the ARK DAN GPS is connected to on the flight controller. On the ARK FPV Flight Controller, this is already GPS 1 by default. On the ARK PAB Carrier or ARK Jetson Carrier, this is likely GPS 2 or TELEM/SERIAL 4 depending on which port it is connected to.

Older versions of PX4 will require [this PR](https://github.com/PX4/PX4-Autopilot/pull/24254) backported to start the IIS2MDL magnetometer and [this PR](https://github.com/PX4/PX4-GPSDrivers/pull/181) backported to enable using the L5 band.&#x20;

#### Sensor Position Configuration <a href="#sensor-position-configuration" id="sensor-position-configuration"></a>

If the sensor is not centered within the vehicle you will also need to define sensor offsets:

* The parameters [EKF2\_GPS\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_X), [EKF2\_GPS\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Y) and [EKF2\_GPS\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_POS_Z) can be set to account for the offset of the ARK DAN GPS from the vehicles center of gravity.
