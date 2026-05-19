# ArduPilot Instructions

## Ardupilot Setup

1. Set the [BATTx\_MONITOR ](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html#other-types-of-power-modules-smart-batteries)parameter to INA2XX
2. Set the [BATTX\_SHUNT ](https://ardupilot.org/copter/docs/parameters.html#batt-shunt-battery-monitor-shunt-resistor)parameter to 0.0001
3. Set the [BATTn\_I2C\_BUS](https://ardupilot.org/copter/docs/parameters.html#batt2-i2c-bus-battery-monitor-i2c-bus-number) parameter to match the power connector the module is plugged into: `1` for Power 1, `2` for Power 2, `3` for Power 3
4. Reboot the flight controller
