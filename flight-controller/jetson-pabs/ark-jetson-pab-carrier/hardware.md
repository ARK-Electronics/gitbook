# Hardware Reference

* [Pinout](pinout.md)
* [Ports and Serial](ports-and-serial.md) — Micro USB modes and the UART map
* [Block Diagram](block-diagram.md)
* [3D Models and Case Files](3d-models-and-case-files.md)
* [GPIO Control](gpio-control.md)
* [Camera Overlays](camera-overlays.md)
* [Mini DisplayPort](mini-displayport.md) — display output and adapter requirements
* [Power Cycling USB Ports](power-cycling-usb-ports.md)

## Power

| Input or rail | Limit | Connectors |
|---------------|-------|------------|
| `POWER1`–`POWER3` | 6 A input each | POWER1, POWER2, POWER3 |
| `VDD_5V_HIPOWER` | 1.5 A typical, shared | TELEM1, TELEM3, GPS2, CAN1 |
| `VDD_5V_PERIPH` | 1.5 A typical, shared | GPS1, CAN2, UART4/I2C3, I2C3, SPI6, ADIO |
| `VDD_5V_JPERIPH` | 1.5 A typical, shared | Jetson CAN, Jetson I2C0, Jetson SPI0, Jetson SPI1, Jetson I2S0, Jetson Fan |
| Fan 5 V | 500 mA fuse, inside `VDD_5V_JPERIPH` | Jetson Fan |
| `VDD_5V_SBUS_RC` | 250 mA fuse | RC pin 1 |
| `VDD_3V3_SPEKTRUM` | 250 mA | RC pin 4 |
| `3V3_FMU` | Flight controller module's 3.3 V; 250 mA fuse on GPS1 | GPS1 pin 8, FC Debug pin 1 |
| Camera 3.3 V | 1 A each | Jetson CSI0–CSI3 |
| `3V3_DP` | 500 mA fuse | Mini DisplayPort |
| `3V3` | 12 A regulator, shared with the cameras, Mini DisplayPort and the USB hub | Jetson Debug, Jetson M.2 Key E, M.2 Key M (SSD) |
| USB VBUS | 1.5 A typical each | Standalone USB 3 port, both USB 3 ports on the combined connector |
| USB VBUS | 750 mA minimum, 1 A typical | USB 2.0 port |

The flight controller switches `VDD_5V_HIPOWER`, `VDD_5V_PERIPH` and `VDD_3V3_SPEKTRUM`. `VDD_5V_JPERIPH` and `3V3` stay off while the Jetson is in reset. The Jetson module, the flight controller module and every rail above draw from the combined power inputs.

## Temperature

| Specification | Value |
|---------------|-------|
| Operating temperature | −10 °C to +60 °C, carrier only |
| Storage temperature | −10 °C to +60 °C, carrier only |

Jetson Orin NX and Orin Nano modules are rated −25 °C to +105 °C junction.
