# ArduPilot Instructions

## ArduPilot Setup

1. Set the [BATTx\_MONITOR](https://ardupilot.org/copter/docs/common-power-module-configuration-in-mission-planner.html#other-types-of-power-modules-smart-batteries) parameter to INA2XX
2. Set the [BATTX\_SHUNT](https://ardupilot.org/copter/docs/parameters.html#batt-shunt-battery-monitor-shunt-resistor) parameter to 0.0001
3. Set the [BATTx\_MAX\_AMPS](https://ardupilot.org/copter/docs/parameters.html#batt-max-amps-battery-monitor-max-current) parameter above the vehicle's peak current. Readings clip at this value, which defaults to 90 A
4. Set the [BATTn\_I2C\_BUS](https://ardupilot.org/copter/docs/parameters.html#batt2-i2c-bus-battery-monitor-i2c-bus-number) parameter to match the power connector the module is plugged into: `1` for Power 1, `2` for Power 2, `3` for Power 3
5. Reboot the flight controller

{% hint style="warning" %}
The bus numbers above apply to ARK flight controllers and the Pixhawk 6X. On other flight controllers, set `BATTn_I2C_BUS` to the ArduPilot bus number of the I2C port the module is wired to. Cube Orange power ports are analog and have no I2C.
{% endhint %}
