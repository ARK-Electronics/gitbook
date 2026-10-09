# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/ark_v6xrt" %}
PX4 user guide for the ARKV6X-RT
{% endembed %}

To build, flash or recover the firmware, see [Firmware](firmware.md).

## Hardware Type

Rev 1.0 reports hardware type `ARKV6XRT000`. `init/rc.board_sensors` starts the internal IMUs only for that type:

```sh
icm45686 -R 6 -b 1 -s start
lsm6dsv -R 1 -b 3 -s -T 80 start
iim20670 -R 2 -b 2 -s start
```

The IIS2MDC starts on I2C3, and the BMP390 starts on I2C2 (`bmp388 -I -b 2 start`), for every hardware type.

Rev 2.0 has different IMUs: three LSM6DSV32X parts, on SPI1, SPI2, and SPI3, in place of the ICM-45686, IIM-20670, and LSM6DSV80X. It also sets the FMUM hardware revision to 1 and moves the BMP390 to I2C3. A firmware build that only matches `ARKV6XRT000` prints `unsupported FMU hwtype, internal IMUs not started` on that board, and it still looks for the barometer on I2C2. The `lsm6dsv` driver recognizes the LSM6DSV32X, and the board's SPI table declares an LSM6DSV on SPI3, so the SPI3 part can be started by hand. SPI1 and SPI2 are declared as the ICM-45686 and IIM-20670, so those two LSM6DSV32X parts can't start until the board configuration changes.

## IMUs

These rates are for Rev 1.0. Rev 2.0 fits three LSM6DSV32X IMUs instead, and the startup script above does not start them.

On Rev 1.0, each IMU runs at the widest full scale of the channel it publishes, with light on-chip filtering. PX4 filters downstream. The LSM6DSV80X accelerometer keeps its LPF2 at ODR/10 (768 Hz) as an anti-alias filter, and the IIM-20670 gyro low-pass can't be set wider than 60 Hz (see below).

| IMU        | Bus  | Full scale          | Publish rate |
| ---------- | ---- | ------------------- | ------------ |
| ICM-45686  | SPI1 | ±32 g / ±4000 dps   | 800 Hz       |
| LSM6DSV80X | SPI3 | ±16 g / ±4000 dps   | 768 Hz       |
| IIM-20670  | SPI2 | ±65.5 g / ±1966 dps | 1000 Hz      |

The ICM-45686 and LSM6DSV80X rates follow `IMU_GYRO_RATEMAX`. The table shows multicopter rates, because multicopter airframes raise `IMU_GYRO_RATEMAX` from 400 to 800. Fixed-wing, VTOL, and rover airframes keep 400, so those two IMUs publish at about 400 Hz. The IIM-20670 publishes at 1000 Hz on every airframe.

Startup order is ICM-45686, then LSM6DSV80X, then IIM-20670. At equal calibration priority the voter keeps the lowest instance, and `CAL_ACC0_PRIO` / `CAL_GYRO0_PRIO` are seeded on the ICM-45686, so that part is the primary.

The IIM-20670 starts last on purpose. Its gyro low-pass cannot be set wider than 60 Hz, which is too much group delay for the rate loop, so it is the navigation and fallback IMU. Its gyro trace looks smoother and later than the other two.

The LSM6DSV80X publishes its ±16 g accelerometer. The ±80 g element stays powered down.

## Heater

On Rev 1.0 (`ARKV6XRT000`), the heater is closed-loop on the ICM-45686 die temperature: the board defaults set `HEATER1_SENS_ID` to that sensor (`3407882`). Other hardware types keep the driver default, 0. The pad warms the whole board. The parameter only selects which die is the feedback.

Run the accelerometer calibration after the heater reaches its setpoint. `heater status` prints the sensor temperature and the set temperature. Wait until they are within 2.5 °C, or until `listener heater_status` shows `temperature_target_met` as true.

## PWM Outputs

The module provides 12 FMU PWM outputs, and 8 more from PX4IO on a carrier that has one. How many of those reach a connector depends on the carrier.

FMU outputs 1–8 support DShot and bidirectional DShot. Outputs 9–12 are PWM only.

Each FMU output has its own FlexPWM submodule, so protocol and rate are set per output.

## RC Input

The RC port (LPUART6, the carrier **RC/SBUS** connector) runs CRSF by default: `RC_CRSF_PRT_CFG` is set to Radio Controller. SBUS is off. For an SBUS receiver, set `RC_CRSF_PRT_CFG` to Disabled and `RC_SBUS_PRT_CFG` to Radio Controller, then reboot.

## Power

The module is powered at 5 V from the carrier. Two digital power bricks are supported. `SENS_EN_INA226` is enabled by default. The INA228 and INA238 drivers are built in for carriers that use those parts. Set `ADC_ADS1115_EN` to use an ADS1115 instead of the onboard ADC for analog monitoring.

## GPS and Compass

* GPS1 (LPUART3) is the full GPS port on a PAB carrier: safety switch, buzzer, LED, and compass I2C.
* GPS2 (LPUART5) is the basic GPS port.

The onboard IIS2MDC is a backup. Yaw normally comes from an external compass in the GPS module.

## Debug Console

The PX4 system console is LPUART1, on the carrier FMU Debug connector, at 57600 baud. SWD is on the same connector. An NXP MCU-Link's virtual COM port is this console.

