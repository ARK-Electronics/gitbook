# Ardupilot Instructions

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

The IIS2MDC magnetometer driver was added in January 2025 and requires Ardupilot version 4.6 or newer.

Use the [Ardupilot Custom Firmware Builder](https://custom.ardupilot.org/) to compile firmware for your autopilot with the IIS2MDC driver. Select `IIS2MDC Compasses` under `Compass` for your board.

<figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

This PR can be backported into previous releases of Ardupilot.

[https://github.com/ArduPilot/ardupilot/pull/28602](https://github.com/ArduPilot/ardupilot/pull/28602)

Configure [SERIALX ](https://ardupilot.org/copter/docs/parameters.html#serial-parameters)to GPS on the port the GPS is connected to. On the ARK FPV GPS port, this is set by default and is plug and play.

Ensure [COMPASS\_EXTERNAL ](https://ardupilot.org/copter/docs/parameters.html#compass-external-compass-is-attached-via-an-external-cable)is set to 1 to auto detect the magnetometer on I2C.&#x20;
