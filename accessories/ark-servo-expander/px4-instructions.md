# PX4 Instructions

## PX4 Setup

Set [PCA9685\_EN\_BUS](https://docs.px4.io/main/en/advanced_config/parameter_reference#PCA9685_EN_BUS) to the I2C port number it is connected to. On the ARKV6X if it is connected to the 4 pin JST-GH I2C port, this would be set to 3.

After a reboot, the new outputs will be available in the [actuator page of QGroundcontrol](https://docs.px4.io/main/en/config/actuators).

The parameters can also be manually edited with the PCA9685\_ params.

The [pca9685 driver](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/fmu-v6x/default.px4board#L42) must be complied in the board firmware for the parameter to appear.
