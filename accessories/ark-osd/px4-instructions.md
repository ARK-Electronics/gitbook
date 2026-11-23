# PX4 Instructions

The ARK OSD connects to the ARK FPV's SPI port or its TELEM port, as in [Wiring](hardware.md#wiring). Set the parameters for one link in _QGroundControl_ and reboot the flight controller. PX4's [ARK FPV page](https://docs.px4.io/main/en/flight_controller/ark_fpv.html#analog-osd) covers the same setup.

## SPI

PX4 main builds the [atxxxx](https://docs.px4.io/main/en/peripherals/osd.html#atxxxx-analog-osd) driver for the ARK FPV and starts it on the SPI port. Until [PX4#29916](https://github.com/PX4/PX4-Autopilot/pull/29916) is in a release, flash a build of PX4 main.

| Parameter | Value | Description |
|-----------|-------|-------------|
| [OSD\_ATXXXX\_CFG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#OSD_ATXXXX_CFG) | `1` or `2` | `1` for an NTSC camera, `2` for PAL. The default, `0`, leaves the driver off |

`atxxxx` draws battery voltage and consumed charge, altitude, the flight mode while disarmed and the flight time while armed, at fixed positions. It doesn't upload a font, so the ARK OSD draws with the font it holds.

## MSP DisplayPort

PX4 v1.16 and later build the [msp\_osd](https://docs.px4.io/main/en/peripherals/osd.html#msp-osd) driver for the ARK FPV.

| Parameter | Value | Description |
|-----------|-------|-------------|
| [MSP\_OSD\_CONFIG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MSP_OSD_CONFIG) | `TELEM 1` (101) | Runs `msp_osd` on the TELEM port |
| [MAV\_0\_CONFIG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_0_CONFIG) | `Disabled` (0) or another port | Moves MAVLink off TELEM 1, which it uses by default |

`msp_osd` places its items on a 60 × 22 grid for digital goggles. The ARK OSD shows 30 columns and 13 or 16 rows, and an item placed outside them doesn't show.
