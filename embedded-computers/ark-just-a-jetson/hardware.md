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

## Temperature

| Specification | Value |
|---------------|-------|
| Operating temperature | −10 °C to +60 °C, carrier only |
| Storage temperature | −10 °C to +60 °C, carrier only |

The RTC backup supercapacitor sets both ranges. The next limit is the USB hub's crystal, −20 °C to +80 °C. Jetson Orin NX and Orin Nano modules are rated −25 °C to +105 °C junction.
