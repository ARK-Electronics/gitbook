# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Camera module | Teledyne FLIR Hadron 640R / 640R+, on the 50-pin board-to-board connector underneath |
| EO camera | OmniVision OV64B40, 4-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC |
| IR camera | FLIR Boson, USB 2.0 on a 4-pin JST-GH, UVC device `09cb:4007` |
| Control | Hadron I2C on a 6-pin JST-GH, level-translated to 3.3 V |
| IMU | TDK InvenSense ICM-45686 6-axis, I2C address `0x68`, on the control I2C |
| Frame sync | Hadron `EXT_VSYNC` to the camera port's MCLK pin and the IMU's FSYNC pin |
| Power | 5 V from the USB connector, which powers the Hadron and the adapter |
| ESD protection | On every MIPI, USB and I2C line |
| Mounting | 4× 1.8 mm holes |
| Dimensions | 33 × 47 × 6 mm |
| Weight | 8 g |

## Connectors

<figure><img src="../../.gitbook/assets/ARK Hadron Adapter Top.jpg" alt="ARK Hadron Adapter, top"><figcaption><p>Top: EO Camera FFC (J4), IR Camera USB (J2) and I2C (J3)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/ARK Hadron Adapter Bottom.jpg" alt="ARK Hadron Adapter, bottom"><figcaption><p>Bottom: Hadron connector (J1)</p></figcaption></figure>

| Connector | Label | Part |
|-----------|-------|------|
| J1 (bottom) | Hadron | Hirose DF40HC(4.0)-50DS-0.4V, 50-pin, 0.4 mm pitch, 4.0 mm stack height |
| J4 | EO Camera | Molex 52559-2253, 22-pin 0.5 mm FFC |
| J2 | IR Camera / USB | JST BM04B-GHS, 4-pin JST-GH |
| J3 | I2C | JST BM06B-GHS, 6-pin JST-GH |

Each host's cabling is on its setup page: [Jetson](jetson-setup.md#cabling), [Just A Pi](just-a-pi-setup.md#cabling).

## What's Included

| Item | Use |
|------|-----|
| ARK Hadron Adapter | |
| 22-to-22-pin 0.5 mm FFC | EO camera to a 22-pin CSI port (Just A Jetson, Jetson PAB Carrier V3, Just A Pi) |
| 22-to-15-pin 0.5 mm FFC | EO camera to a 15-pin CSI port (Jetson PAB Carrier) |
| 4-pin JST-GH cable | IR camera / USB |
| 6-pin JST-GH cable | I2C |

The Hadron camera module is not included.

## Pinout

### EO Camera (J4) — 22-pin 0.5 mm FFC

The connector uses the 22-pin Raspberry Pi and Jetson camera pinout, numbered the way the carriers number their CSI ports.

| Pin | Signal | Voltage | Note |
| --- | ------ | ------- | ---- |
| 1 | GND | GND | |
| 2 | EO\_D0\_N | 1.2V | MIPI data lane 0 |
| 3 | EO\_D0\_P | 1.2V | |
| 4 | GND | GND | |
| 5 | EO\_D1\_N | 1.2V | MIPI data lane 1 |
| 6 | EO\_D1\_P | 1.2V | |
| 7 | GND | GND | |
| 8 | EO\_CLK\_N | 1.2V | MIPI clock lane |
| 9 | EO\_CLK\_P | 1.2V | |
| 10 | GND | GND | |
| 11 | EO\_D2\_N | 1.2V | MIPI data lane 2 |
| 12 | EO\_D2\_P | 1.2V | |
| 13 | GND | GND | |
| 14 | EO\_D3\_N | 1.2V | MIPI data lane 3 |
| 15 | EO\_D3\_P | 1.2V | |
| 16 | GND | GND | |
| 17 | CAM\_RESET\_N | +3.3V | Carrier `CAMn_PWDN` pin. Hadron reset, translated to 1.8 V; high releases it |
| 18 | CAM\_FS | +1.8V | Carrier `CAMn_MCLK` pin. Frame-sync line, see below |
| 19 | GND | GND | |
| 20 | CAM\_SCL | +3.3V | EO camera I2C, translated to the Hadron's 1.8 V |
| 21 | CAM\_SDA | +3.3V | EO camera I2C, translated to the Hadron's 1.8 V |
| 22 | 3V3\_CON | +3.3V | From the carrier; powers the carrier side of the level translators |

On a 2-lane port only lanes 0 and 1 are used.

The EO sensor and the Boson share the reset on pin 17. ARK's drivers release it once and never pull it low again, so powering down the EO camera does not reset the Boson.

### IR Camera / USB (J2) — 4-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1 | USB\_VBUS | +5.0V |
| 2 | USB\_N | +3.3V |
| 3 | USB\_P | +3.3V |
| 4 | GND | GND |

`USB_VBUS` powers the Hadron and the adapter.

### I2C (J3) — 6-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1 | NC | — |
| 2 | NC | — |
| 3 | NC | — |
| 4 | I2C\_SCL | +3.3V |
| 5 | I2C\_SDA | +3.3V |
| 6 | GND | GND |

Pins 4 to 6 match the I2C pins of a Pixhawk-standard 6-pin UART/I2C connector, so a straight cable works. The bus carries the ICM-45686 at `0x68` and the Hadron's own I2C devices. A TXS0104E translates the Hadron's 1.8 V I2C to 3.3 V and supplies the pull-ups.

### Hadron (J1) — 50-pin board-to-board

The adapter connects these Hadron pins: USB 2.0 and 5 V in, the four EO MIPI data lanes and clock, the EO camera I2C, the Hadron I2C, the shared reset and `EXT_VSYNC` on pin 43. The rest are not connected.

## Frame Sync

The Hadron's frame-sync line is `EXT_VSYNC` on pin 43. R11 joins it to pin 18 of the EO camera connector, the carrier's MCLK pin. R12 joins it to the IMU's FSYNC pin. Both are 0 Ω and fitted.

| Device | Role on the sync line |
| ------ | --------------------- |
| Boson | Once made sync master over its serial port, sends a short 1.8 V pulse for each 60 Hz core frame |
| Host | Can timestamp the pulses on the camera port's MCLK pin, which ARK's overlays set as an input |
| ICM-45686 | Once its pin 9 is switched from INT2 to FSYNC, tags the first sample after each pulse with the pulse-to-sample delay at 1 µs resolution |
| EO sensor | Neither drives nor follows the line with the current driver. It free-runs on its own oscillator |

## 3D Model

| File | Contents |
|------|----------|
| [ARK\_Hadron\_Adapter\_Rev\_1.1.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Hadron_Adapter/model/ARK_Hadron_Adapter_Rev_1.1.step) | Board |
| [ARK\_Hadron\_Adapter\_Rev\_1.1\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Hadron_Adapter/model/ARK_Hadron_Adapter_Rev_1.1_PDF3D.pdf) | 3D PDF |

All files: [ARK\_Hadron\_Adapter in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Hadron_Adapter)
