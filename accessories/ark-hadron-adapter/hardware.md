# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Camera module | Teledyne FLIR Hadron 640R / 640R+, on a Hirose DF40 50-pin board-to-board connector (underside) |
| EO camera | OmniVision OV64B40, 4-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC (Molex 52559-2253) |
| IR camera | FLIR Boson, USB 2.0 on a 4-pin JST-GH (UVC device `09cb:4007`) |
| Control | Hadron I2C on a 6-pin JST-GH, level-translated to 3.3 V |
| IMU | TDK InvenSense ICM-45686 6-axis, I2C address `0x68`, on the control I2C |
| Frame sync | Hadron `EXT_VSYNC` joined to the camera port's MCLK pin and to the IMU's FSYNC pin |
| Power | 5 V from the USB connector; the Hadron and the adapter's 1.8 V regulator run from it |
| ESD protection | On every MIPI, USB and I2C line |
| PCB | 6-layer, impedance controlled |
| Mounting | 4× 1.8 mm holes |
| Dimensions | 33 × 47 × 6 mm |

The Hadron's reset is one line shared by the EO sensor and the Boson. The adapter level-translates it from the camera port's `CAMn_PWDN` pin, and the host drivers release it once and never pull it low again, so a camera driver powering down cannot reset the Boson.

## Connectors

| Connector | Label | Part |
|-----------|-------|------|
| J1 (bottom) | Hadron | Hirose DF40HC(4.0)-50DS-0.4V, 50-pin, 0.4 mm pitch, 4.0 mm stack height |
| J4 | EO Camera | Molex 52559-2253, 22-pin 0.5 mm FFC |
| J2 | IR Camera / USB | JST BM04B-GHS, 4-pin JST-GH |
| J3 | I2C | JST BM06B-GHS, 6-pin JST-GH |

The EO camera FFC goes to a CSI port on the carrier, the USB cable to a USB 2.0 JST-GH, and the I2C cable to a 6-pin JST-GH with I2C on pins 4 and 5, such as the Jetson carriers' UART2/I2C0 connector. All three are straight cables.

## What's included

| Item | Use |
|------|-----|
| ARK Hadron Adapter | |
| 22-to-22-pin 0.5 mm FFC | EO camera to a 22-pin CSI port (Just A Jetson, Jetson PAB Carrier V3, Just A Pi) |
| 22-to-15-pin 0.5 mm FFC | EO camera to a 15-pin CSI port (Jetson PAB Carrier) |
| 4-pin JST-GH cable | IR camera / USB |
| 6-pin JST-GH cable | I2C |

The Hadron camera module is not included.

## Pinout

### EO Camera — 22-pin 0.5 mm FFC

The connector carries the 22-pin Raspberry Pi / Jetson camera pinout. The pins are listed as the adapter numbers them.

| Pin | Signal | Voltage | Note |
| --- | ------ | ------- | ---- |
| 1 | 3V3\_CON | +3.3V | From the carrier; powers the carrier side of the level translators |
| 2 | CAM\_SDA | +3.3V | EO camera I2C, translated to the Hadron's 1.8 V |
| 3 | CAM\_SCL | +3.3V | EO camera I2C, translated to the Hadron's 1.8 V |
| 4 | GND | GND | |
| 5 | CAM\_FS | +1.8V | Carrier `CAMn_MCLK` pin. Frame-sync line, see below |
| 6 | CAM\_RESET\_N | +3.3V | Carrier `CAMn_PWDN` pin. Hadron reset, translated to 1.8 V; high releases it |
| 7 | GND | GND | |
| 8 | EO\_D3\_P | 1.2V | MIPI data lane 3 |
| 9 | EO\_D3\_N | 1.2V | |
| 10 | GND | GND | |
| 11 | EO\_D2\_P | 1.2V | MIPI data lane 2 |
| 12 | EO\_D2\_N | 1.2V | |
| 13 | GND | GND | |
| 14 | EO\_CLK\_P | 1.2V | MIPI clock lane |
| 15 | EO\_CLK\_N | 1.2V | |
| 16 | GND | GND | |
| 17 | EO\_D1\_P | 1.2V | MIPI data lane 1 |
| 18 | EO\_D1\_N | 1.2V | |
| 19 | GND | GND | |
| 20 | EO\_D0\_P | 1.2V | MIPI data lane 0 |
| 21 | EO\_D0\_N | 1.2V | |
| 22 | GND | GND | |

On a 2-lane port only lanes 0 and 1 are used.

### IR Camera / USB — 4-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1 | USB\_VBUS | +5.0V |
| 2 | USB\_N | +3.3V |
| 3 | USB\_P | +3.3V |
| 4 | GND | GND |

`USB_VBUS` powers the Hadron and the adapter. The Boson enumerates as a UVC camera.

### I2C — 6-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1 | NC | — |
| 2 | NC | — |
| 3 | NC | — |
| 4 | I2C\_SCL | +3.3V |
| 5 | I2C\_SDA | +3.3V |
| 6 | GND | GND |

Pins 4 to 6 match the I2C pins of a Pixhawk-standard UART/I2C 6-pin connector, so a straight cable works. The bus carries the ICM-45686 at `0x68` and the Hadron's own I2C devices, translated from 1.8 V to 3.3 V by a TXS0104E, which also supplies the 3.3 V pull-ups.

### Hadron connector

The adapter connects these Hadron pins: USB 2.0 and 5 V in, the four EO MIPI data lanes and clock, the EO camera I2C, the Hadron I2C, the shared reset and `EXT_VSYNC` (pin 43). The rest are not connected.

## Frame sync

Hadron pin 43 `EXT_VSYNC` is the module's frame-sync line. On the adapter, R11 joins it to the EO camera connector's MCLK pin (pin 5), and R12 joins it to the ICM-45686's FSYNC pin. Both are 0 Ω and fitted from Rev 1.1 on (Rev 1.0 shipped without R12).

* The Boson can be made the sync master over its serial port. It then sends a short 1.8 V pulse for each of its 60 Hz core frames, and the host can timestamp those pulses on its MCLK pad, which the host overlays turn into an input.
* The ICM-45686 tags the first sample after each pulse with the pulse-to-sample delay, at 1 µs resolution, once its pin 9 is switched from INT2 to FSYNC.
* The EO sensor neither drives nor follows the line with the current driver tables; it free-runs on its own oscillator.

## 3D Model

| File | Contents |
|------|----------|
| [ARK\_Hadron\_Adapter\_Rev\_1.1.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Hadron_Adapter/model/ARK_Hadron_Adapter_Rev_1.1.step) | Board |
| [ARK\_Hadron\_Adapter\_Rev\_1.1\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Hadron_Adapter/model/ARK_Hadron_Adapter_Rev_1.1_PDF3D.pdf) | 3D PDF |

All files: [ARK\_Hadron\_Adapter in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Hadron_Adapter)
