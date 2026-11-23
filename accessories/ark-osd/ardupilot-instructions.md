# ArduPilot Instructions

The ARK OSD connects to the ARK FPV's SPI port or its TELEM port, as in [Wiring](hardware.md#wiring). Set the parameters for one link and reboot the flight controller. ArduPilot's [OSD](https://ardupilot.org/copter/docs/common-osd-overview.html) and [DisplayPort OSD](https://ardupilot.org/copter/docs/common-displayport.html) pages cover screens and items.

## SPI

[ArduPilot#35289](https://github.com/ArduPilot/ardupilot/pull/35289) adds the OSD on the ARK FPV's SPI port. Until it is in a release, use [MSP DisplayPort](#msp-displayport).

| Parameter | Value | Description |
|-----------|-------|-------------|
| [OSD\_TYPE](https://ardupilot.org/copter/docs/parameters.html#osd-type) | `1` | MAX7456 on the SPI port. The ARK FPV default, `5`, is MSP DisplayPort |
| [OSD\_TYPE2](https://ardupilot.org/copter/docs/parameters.html#osd-type2) | `5` | Optional. Keeps MSP DisplayPort on the VTX port as a second OSD |

ArduPilot checks the ARK OSD's font at boot and uploads the one [OSD\_FONT](https://ardupilot.org/copter/docs/parameters.html#osd-font) selects.

## MSP DisplayPort

| Parameter | Value | Description |
|-----------|-------|-------------|
| [SERIAL1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#serial1-protocol) | `42` | DisplayPort on the TELEM port |
| [SERIAL1\_BAUD](https://ardupilot.org/copter/docs/parameters.html#serial1-baud) | `115` | 115200 baud |
| [OSD\_TYPE](https://ardupilot.org/copter/docs/parameters.html#osd-type) | `5` | MSP DisplayPort, the ARK FPV default |

## NTSC Cameras

ArduPilot's default screen puts ground speed and GPS position on rows 13 and 14. On NTSC the ARK OSD shows rows 0 to 12, so move those items up with their `OSD1_*_Y` parameters.
