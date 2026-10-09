# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| IMU | [Analog Devices ADIS16507-2](https://www.analog.com/media/en/technical-documentation/data-sheets/ADIS16507.pdf), 6-axis precision MEMS |
| Gyroscope | ±500 °/s; in-run bias stability 2.2 °/h (X), 2.7 °/h (Y), 1.6 °/h (Z) |
| Accelerometer | ±392 m/s²; in-run bias stability 125 µm/s² |
| Calibration | Factory calibrated sensitivity, bias and axial alignment, −40 °C to +85 °C |
| Interface | SPI, 11-pin JST-GH |
| Power | 5 V, 41 mA average |
| Dimensions | 2.5 × 2.25 × 0.71 cm |
| Weight | 4 g |

## Pinout

### SPI — 11-pin JST-GH

The pinout matches the [ARK PAB carrier SPI connector](https://docs.px4.io/main/en/flight_controller/arkpab.html#spi6); nCS2 and DRDY2 are not connected.

| Pin      | Signal                            | Voltage |
| -------- | --------------------------------- | ------- |
| 1 (red)  | `VDD_5V_IN`                       | +5.0V   |
| 2        | SPI6\_SCK                         | +3.3V   |
| 3        | SPI6\_MISO                        | +3.3V   |
| 4        | SPI6\_MOSI                        | +3.3V   |
| 5        | SPI6\_nCS1                        | +3.3V   |
| 6        | NC                                | +3.3V   |
| 7        | SPIX\_nSYNC                       | +3.3V   |
| 8        | SPI6\_DRDY1                       | +3.3V   |
| 9        | NC                                | +3.3V   |
| 10       | SPI6\_nRESET (10k pullup to 3.3V) | +3.3V   |
| 11 (blk) | GND                               | GND     |

## Datasheets

* [ARK ADIS16507](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_ADIS16507/datasheet/ARK_ADIS16507_Datasheet.pdf)
* [Analog Devices ADIS16507-2](https://www.analog.com/media/en/technical-documentation/data-sheets/ADIS16507.pdf)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_ADIS16507\_REV\_1\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_ADIS16507/model/ARK_ADIS16507_REV_1_3D_Model.step) | Board, rev 1 |
| [Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_ADIS16507/case/Top_Case.stl) | Case top |
| [Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_ADIS16507/case/Bottom_Case.stl) | Case bottom |

All files: [ARK\_ADIS16507 in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_ADIS16507)
