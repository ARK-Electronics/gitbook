# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Camera module | Teledyne FLIR Boson+ with the MIPI interface, on the 80-pin board-to-board connector underneath. The USB versions do not work with the adapter |
| Video | 2-lane MIPI CSI-2 on a 22-pin 0.5 mm FFC, 640x512 at 60 fps |
| Camera control | Boson I2C on the camera connector, level-translated to 3.3 V, address `0x6a` |
| Serial port | Boson UART on a 6-pin JST-GH, level-translated to 3.3 V, 921600 8N1 |
| IMU | TDK InvenSense ICM-45686 6-axis, I2C address `0x68`, on the 6-pin JST-GH |
| Frame sync | Boson `EXT_SYNC`, 1.8 V, to the camera connector's MCLK pin and the IMU's FSYNC pin |
| Power | 3.3 V from the camera connector, which powers the Boson and the adapter |
| ESD protection | On every MIPI, I2C and UART line |
| Mounting | 4× 1.8 mm holes |
| Dimensions | 21 × 21 × 6 mm |
| Weight | 2.5 g |

The adapter wires no reset, power-down or clock to the Boson. The Boson runs from the camera connector's 3.3 V and its own oscillator.

## Connectors

<figure><img src="../../.gitbook/assets/ARK Boson Adapter Top.jpg" alt="ARK Boson Adapter, top"><figcaption><p>Top: Camera FFC (J2) and I2C/UART (J3)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/ARK Boson Adapter Bottom.jpg" alt="ARK Boson Adapter, bottom"><figcaption><p>Bottom: Boson connector (J1)</p></figcaption></figure>

| Connector | Label | Part |
|-----------|-------|------|
| J1 (bottom) | Boson | Hirose DF40HC(4.0)-80DS-0.4V, 80-pin, 0.4 mm pitch, 4.0 mm stack height |
| J2 | Camera | Molex 52559-2253, 22-pin 0.5 mm FFC |
| J3 | I2C/UART | JST BM06B-GHS, 6-pin JST-GH |

Video needs only the camera cable. The camera connector powers the Boson and carries the I2C that ARK's drivers configure it over. The I2C/UART cable is for the Boson's serial port and the IMU.

Each host's cabling is on its setup page: [Jetson](jetson-setup.md#cabling), [Just A Pi](just-a-pi-setup.md#cabling).

## What's Included

| Item | Use |
|------|-----|
| ARK Boson Adapter | |
| 22-to-22-pin 0.5 mm FFC | Camera to a 22-pin CSI port (Just A Jetson, Just A Pi) |
| 22-to-15-pin 0.5 mm FFC | Camera to a 15-pin CSI port (Jetson PAB Carrier) |
| 6-pin JST-GH cable | Serial port and IMU. Straight, see the [I2C/UART pinout](#pinout) |

The Boson+ camera module is not included.

## Pinout

### Camera (J2) — 22-pin 0.5 mm FFC

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

The Boson answers on this I2C at `0x6a`.

### I2C/UART (J3) — 6-pin JST-GH

This is the pinout of Rev 1.0, the shipping revision.

| Pin | Signal | Voltage | Note |
| --- | ------ | ------- | ---- |
| 1 | NC | — | |
| 2 | BOSON\_TX | +3.3V | Boson serial output |
| 3 | BOSON\_RX | +3.3V | Boson serial input |
| 4 | I2C\_SCL | +3.3V | IMU |
| 5 | I2C\_SDA | +3.3V | IMU |
| 6 | GND | GND | |

{% hint style="warning" %}
Cross pins 2 and 3 of the 6-pin cable before connecting this connector to a host UART. On a Pixhawk-standard UART/I2C connector pin 2 is the host's output, and on Rev 1.0 pin 2 is the Boson's output too. The included cable is straight. The crossed cable was bench-tested on the Just A Jetson and the Just A Pi. Video and the IMU do not use these pins.
{% endhint %}

Pins 4 to 6 match the I2C pins of a Pixhawk-standard 6-pin UART/I2C connector. An LSF0102 translates the UART between the Boson's 1.8 V and 3.3 V. A TXS0104E translates the I2C and supplies its pull-ups. This I2C carries only the ICM-45686 at `0x68`. The Boson's own I2C is on the camera connector.

### Boson (J1) — 80-pin board-to-board

The adapter connects these Boson pins: 3.3 V in, the two MIPI data lanes and clock, the Boson I2C, the UART, `EXT_SYNC` on pin 72 and the pull-up FLIR asks for on pin 58. The rest are not connected.

## Frame Sync

The Boson's frame-sync line is `EXT_SYNC` on pin 72. It connects to pin 18 of the camera connector, the carrier's MCLK pin, and to the IMU's FSYNC pin.

The line is the Boson's own 1.8 V I/O, with no buffer on the adapter. FLIR's absolute limit for it is −0.25 to 1.92 V.

| Device | Role on the sync line |
| ------ | --------------------- |
| Boson | Holds the line low from power-on. As sync master, sends one pulse per 60 Hz frame while it streams |
| Host | Reads the pulses on the camera port's MCLK pin, which ARK's overlays set as an input |
| ICM-45686 | Tags the first sample after each pulse with the pulse-to-sample delay at 1 µs resolution |

Set the Boson's sync mode over its serial port with FLIR function `0x00050098`: 0 off, 1 master, 2 slave. The Boson powers on with sync off and forgets the setting at power-off. Switch the IMU's pin 9 from INT2, its power-on function, to FSYNC before it can tag the pulses.

On the bench, with the Boson as sync master, the Just A Jetson counted 59.9–60.2 pulses per second and the Just A Pi 60.25. The IMU tagged 59.4–59.8 pulses per second, counted on its own clock.

## 3D Model

| File | Contents |
|------|----------|
| [ARK\_Boson\_Adapter\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Boson_Adapter/model/ARK_Boson_Adapter_Rev_1.0.step) | Board |
| [ARK\_Boson\_Adapter\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Boson_Adapter/model/ARK_Boson_Adapter_Rev_1.0_PDF3D.pdf) | 3D PDF |

All files: [ARK\_Boson\_Adapter in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Boson_Adapter)
