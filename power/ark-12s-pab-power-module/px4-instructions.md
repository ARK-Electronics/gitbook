# PX4 Instructions

## PX4 Setup

1. Disable the [SENS\_EN\_INA226](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_EN_INA226) parameter if it is enabled
2. Enable the [SENS\_EN\_INA238 ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_EN_INA238)parameter
3. Reboot the flight controller
4. Set the [INA238\_SHUNT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#INA238_SHUNT) parameter to 0.0001
5. Reboot the flight controller
