# ArduPilot Instructions

## Firmware Setup

ArduPilot supports the IIS2MDC magnetometer since 4.7.2, and on the ARK FPV since 4.6.3. For 4.6.0 to 4.7.1 on other boards, build firmware with the [ArduPilot Custom Firmware Builder](https://custom.ardupilot.org/) and select `IIS2MDC compasses` under `Compass`.

Set [SERIALx\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#serial-parameters) to `5` (GPS) on the port the ARK SAM GPS connects to. The ARK FPV GPS port defaults to GPS.

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
