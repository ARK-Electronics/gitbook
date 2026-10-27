# ArduPilot Instructions

## Firmware Setup

Set [SERIALx\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#serial-parameters) to `5` (GPS) on the port the ARK DAN GPS connects to. The ARK FPV GPS port defaults to GPS.

ArduPilot 4.7.2 and later detect the IIS2MDC magnetometer on that port's I2C bus in standard firmware. On the ARK FPV, every release since 4.6.3, the first for that board, detects it. Targets that don't probe external I2C compasses never detect it, among them `fmuv2`, `fmuv3`, `revo-mini` and `mRoX21`.

On other boards, standard firmware from 4.6.0 to 4.7.1 leaves the IIS2MDC driver out. For those versions, build firmware with the [ArduPilot Custom Firmware Builder](https://custom.ardupilot.org/) and select `IIS2MDC compasses` under `Compass` (`LIS2MDL/IIS2MDC compasses` on 4.7.x).

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
