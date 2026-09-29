---
cover: ../../.gitbook/assets/IMU_Compressed_1-1-scaled.jpg
coverY: 0
---

# ARK ADIS16507

## Datasheet

* [Analog Devices ADIS16507-3](https://www.analog.com/media/en/technical-documentation/data-sheets/ADIS16507.pdf)

## Wiring

11 pin JST-GH&#x20;

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

