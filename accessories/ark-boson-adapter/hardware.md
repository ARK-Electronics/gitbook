# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Camera module | Teledyne FLIR Boson+ with the MIPI interface, on the 80-pin board-to-board connector underneath. USB versions are not supported |
| Video | 2-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC, 640x512 at 60 fps |
| Camera control | Boson I2C on the camera connector, level-translated to 3.3 V, address `0x6a` |
| Serial port | Boson UART on a 6-pin JST-GH, level-translated to 3.3 V, 921600 8N1 |
| IMU | TDK InvenSense ICM-45686 6-axis, I2C address `0x68`, on the 6-pin JST-GH |
| Frame sync | Boson `EXT_SYNC` to the camera connector's MCLK pin. The jumper to the IMU's FSYNC pin is not fitted |
| Power | 3.3 V from the camera connector, which powers the Boson and the adapter |
| ESD protection | On every MIPI, I2C and UART line |
| PCB | 6-layer, impedance controlled |
| Mounting | 4× 1.8 mm holes |
| Dimensions | 21 × 21 × 6 mm |

The adapter wires no reset, power-down or clock to the Boson. The Boson runs from the camera connector's 3.3 V and its own oscillator.

## Connectors

| Connector | Label | Part |
|-----------|-------|------|
| J1 (bottom) | Boson | Hirose DF40HC(4.0)-80DS-0.4V, 80-pin, 0.4 mm pitch, 4.0 mm stack height |
| J2 | Camera | Molex 52559-2253, 22-pin 0.5 mm FFC |
| J3 | I2C/UART | JST BM06B-GHS, 6-pin JST-GH |

Each host's cabling is on its setup page: [Jetson](jetson-setup.md#cabling), [Just A Pi](just-a-pi-setup.md#cabling).

## What's included

| Item | Use |
|------|-----|
| ARK Boson Adapter | |
| 22-to-22-pin 0.5 mm FFC | Camera to a 22-pin CSI port (Just A Jetson, Just A Pi) |
| 22-to-15-pin 0.5 mm FFC | Camera to a 15-pin CSI port (Jetson PAB Carrier). The PAB carriers have no Boson+ overlay yet |
| 6-pin JST-GH cable | Serial port and IMU |

The Boson+ camera module is not included. Only the MIPI versions of the Boson+ work with the adapter. The USB versions do not.

## Pinout

### Camera — 22-pin 0.5 mm FFC

The connector uses the 22-pin Raspberry Pi and Jetson camera pinout, numbered the way the carriers number their CSI ports.

| Pin | Signal | Voltage | Note |
| --- | ------ | ------- | ---- |
| 1 | GND | GND | |
| 2 | CAM\_D0\_N | 1.2V | MIPI data lane 0 |
| 3 | CAM\_D0\_P | 1.2V | |
| 4 | GND | GND | |
| 5 | CAM\_D1\_N | 1.2V | MIPI data lane 1 |
| 6 | CAM\_D1\_P | 1.2V | |
| 7 | GND | GND | |
| 8 | CAM\_CLK\_N | 1.2V | MIPI clock lane |
| 9 | CAM\_CLK\_P | 1.2V | |
| 10 | GND | GND | |
| 11 | NC | — | The Boson has two lanes |
| 12 | NC | — | |
| 13 | GND | GND | |
| 14 | NC | — | |
| 15 | NC | — | |
| 16 | GND | GND | |
| 17 | NC | — | Carrier `CAMn_PWDN` pin, not connected |
| 18 | CAM\_FS | +1.8V | Carrier `CAMn_MCLK` pin. Frame-sync line, see below |
| 19 | GND | GND | |
| 20 | CAM\_SCL | +3.3V | Boson I2C, translated to the Boson's 1.8 V |
| 21 | CAM\_SDA | +3.3V | Boson I2C, translated to the Boson's 1.8 V |
| 22 | 3V3\_CON | +3.3V | From the carrier. Powers the Boson and the adapter |

The Boson answers on this I2C at `0x6a`. ARK's drivers configure it and start its MIPI output over this bus, so video needs no other cable.

### I2C/UART — 6-pin JST-GH

| Pin | Signal | Voltage | Note |
| --- | ------ | ------- | ---- |
| 1 | NC | — | |
| 2 | BOSON\_RX | +3.3V | Boson serial input. Goes to the host's TX |
| 3 | BOSON\_TX | +3.3V | Boson serial output. Goes to the host's RX |
| 4 | I2C\_SCL | +3.3V | IMU |
| 5 | I2C\_SDA | +3.3V | IMU |
| 6 | GND | GND | |

The UART is crossed against a Pixhawk-standard 6-pin UART/I2C connector, so a straight cable joins it to a host's UART. An LSF0102 translates the UART between the Boson's 1.8 V and 3.3 V. A TXS0104E translates the I2C and supplies its pull-ups. This I2C carries only the ICM-45686 at `0x68`. The Boson's own I2C is on the camera connector.

{% hint style="warning" %}
On Rev 1.0, pin 2 is the Boson's serial output and pin 3 its input. Cross pins 2 and 3 in the cable to a host UART. The board wires the Boson's `uart_apb_sin` on pin 33 and `uart_apb_sout` on pin 43 the other way round. With the crossed cable, the Boson's output has no 3.3 V pull-up of its own. It works with the Just A Jetson, which pulls up its RX line, and was bench-tested on the Just A Pi.
{% endhint %}

### Boson connector

The adapter connects these Boson pins: 3.3 V in, the two MIPI data lanes and clock, the Boson I2C, the UART on pins 33 and 43, `EXT_SYNC` on pin 72 and the pull-up FLIR asks for on pin 58. The rest are not connected.

## Frame sync

The Boson's frame-sync line is `EXT_SYNC` on pin 72. R12 joins it to pin 18 of the camera connector, the carrier's MCLK pin, and is fitted. R13 joins it to the IMU's FSYNC pin and is not fitted on Rev 1.0. Fit a 0 Ω resistor at R13 to let the IMU timestamp the pulses.

| Device | Role on the sync line |
| ------ | --------------------- |
| Boson | Powers on with sync off and holds the line low. Once made sync master over its serial port, with FLIR function `0x00050098` set to 1, it sends one pulse per 60 Hz frame while it streams |
| Host | Reads the pulses on the camera port's MCLK pin, which ARK's overlays set as an input. On the bench, 60.0–60.2 pulses per second on the Just A Jetson and 60.25 Hz on the Just A Pi |
| ICM-45686 | With R13 fitted and its pin 9 switched from INT2 to FSYNC, tags the first sample after each pulse with the pulse-to-sample delay at 1 µs resolution. On the bench, 59.4–59.8 tags per second, counted on the IMU's own clock |

## 3D Model

| File | Contents |
|------|----------|
| [ARK\_Boson\_Adapter\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Boson_Adapter/model/ARK_Boson_Adapter_Rev_1.0.step) | Board |
| [ARK\_Boson\_Adapter\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Boson_Adapter/model/ARK_Boson_Adapter_Rev_1.0_PDF3D.pdf) | 3D PDF |

All files: [ARK\_Boson\_Adapter in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Boson_Adapter)
