# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| IMU | [Murata SCH16T](https://www.murata.com/en-us/products/sensor/gyro/overview/lineup/sch16t): SCH16T-K01 (ARK SCH16T), SCH16T-K10 (ARK SCH16T-K10) |
| Gyroscope range | ±300 °/s (K01), ±2000 °/s (K10) |
| Accelerometer range | ±8 g (K01), ±16 g (K10); redundant digital accelerometer channel up to ±26 g |
| Gyro bias instability | Down to 0.3 °/h (K01), 2 °/h (K10) |
| Gyro noise density | Down to 0.3 m°/s/√Hz (K01), 6 m°/s/√Hz (K10) |
| Operating temperature | −40 °C to +110 °C |
| Interface | SPI, 11-pin JST-GH |
| Power | 5 V, 46 mA average |
| Dimensions | 2.5 × 2.25 × 0.59 cm |
| Weight | 2.5 g |

## Pinout

### SPI — 11-pin JST-GH

The pinout matches the [ARK PAB and Jetson carrier SPI connector](https://docs.px4.io/main/en/flight_controller/arkpab.html#spi6); nCS2 and DRDY2 are not connected.

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

* [ARK SCH16T](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_SCH16T/datasheet/ARK_SCH16T_Datasheet.pdf)
* [Murata SCH16T-K01](https://www.murata.com/-/media/webrenewal/products/sensor/pdf/datasheet/datasheet-sch16t-k01-short.ashx?la=en)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_SCH16T\_Rev\_01.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_SCH16T/model/ARK_SCH16T_Rev_01.step) | Board, rev 01, both variants |

All files: [ARK\_SCH16T in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_SCH16T)
