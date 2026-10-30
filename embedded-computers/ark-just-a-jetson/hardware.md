# Hardware Reference

* [Pinout](pinout.md)
* [Ports and Serial](connections.md) — USB-C modes and the UART map
* [Block Diagram](block-diagram.md)
* [3D Model](3d-model.md)
* [GPIO Control](gpio-control.md)
* [Camera Overlays](camera-overlays.md)
* [IMU ICM-42688P Guide](imu-icm-42688p-guide.md) — the onboard IMU on SPI1
* [INA238 Power Monitor Guide](ina238-power-monitor-guide.md) — carrier rail monitoring over I2C
* [Power Cycling USB Ports](power-cycling-usb-ports.md)

## Power

| Input or rail | Limit | Connectors |
|---------------|-------|------------|
| `5V IN` | 6 A input | 5V IN |
| `VDD_5V_JPERIPH` | 1.5 A typical, shared | CAN, UART0/GPIO, SPI/GPIO, Fan |
| Fan 5 V | 500 mA fuse, inside `VDD_5V_JPERIPH` | Fan |
| `VDD_5V_JPERIPH_2` | 1.5 A typical, shared | UART1/GPIO, UART2/I2C0, I2S/GPIO |
| USB VBUS | 750 mA minimum, 1 A typical each | Both USB JST-GH |
| USB VBUS | 1.5 A typical each | Both USB-A, USB-C (host mode only) |
| `5V_PCIE_FFC` | 1.5 A typical | PCIE |
| HDMI 5 V | 500 mA fuse | HDMI |
| Camera 3.3 V | 1 A each | CAM0/CSI0, CAM1/CSI2 |

The Jetson module and every rail above draw from the same 5 V supply. `VDD_5V_JPERIPH`, `VDD_5V_JPERIPH_2` and the camera 3.3 V stay off while the Jetson is in reset.

## Temperature

| Specification | Value |
|---------------|-------|
| Operating temperature | −10 °C to +60 °C, carrier only |
| Storage temperature | −10 °C to +60 °C, carrier only |

Jetson Orin NX and Orin Nano modules are rated −25 °C to +105 °C junction.
