# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Avionics connector | 40-pin Molex Pico-Clasp secondary avionics port |
| Breakout connectors | Pixhawk-standard JST-GH: PWM (10-pin), TELEM3 (6-pin), GPS2 (6-pin), JCAN (4-pin), SPI (11-pin), SBUS out (3-pin) |
| Weight | 5 g |

## Pinout

### Secondary Avionics Port (J3) — 40-pin Molex Pico-Clasp

Molex [Pico-Clasp 501571](https://www.molex.com/en-us/part-list/501571). Mating plug [5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524), pre-crimped wires [0797581019](https://www.digikey.com/en/products/detail/molex/0797581019/6564344).

| Pin | Signal                     | Voltage  |
| --- | -------------------------- | -------- |
| 1   | VDD\_5V\_PERIPH            | 5V       |
| 2   | SPI6\_DRDY1\_EXT           | 3.3V     |
| 3   | SPIX\_nSYNC\_EXT           | 3.3V     |
| 4   | GND                        | GND      |
| 5   | SPI6\_SCK\_EXT             | 3.3V     |
| 6   | SPI6\_MOSI\_EXT            | 3.3V     |
| 7   | GND                        | GND      |
| 8   | SPI6\_nCS1\_EXT            | 3.3V     |
| 9   | USART2\_TX\_TELEM3\_EXT    | 3.3V     |
| 10  | SPI6\_nRESET\_EXT          | 3.3V     |
| 11  | USART2\_RX\_TELEM3\_EXT    | 3.3V     |
| 12  | SPI6\_MISO\_EXT            | 3.3V     |
| 13  | VDD\_5V\_PERIPH            | 5V       |
| 14  | GND                        | GND      |
| 15  | VDD\_5V\_SBUS\_RC          | 5V       |
| 16  | IO\_SBUS\_OUTPUT\_EXT      | 3.3V     |
| 17  | GND                        | GND      |
| 18  | UART8\_TX\_GPS2\_EXT       | 3.3V     |
| 19  | I2C2\_SCL\_BASE\_GPS2\_EXT | 3.3V     |
| 20  | UART8\_RX\_GPS2\_EXT       | 3.3V     |
| 21  | I2C2\_SDA\_BASE\_GPS2\_EXT | 3.3V     |
| 22  | VDD\_5V\_PERIPH            | 5V       |
| 23  | GND                        | GND      |
| 24  | GND                        | GND      |
| 25  | IO\_CH1\_EXT               | 3.3V     |
| 26  | IO\_CH5\_EXT               | 3.3V     |
| 27  | IO\_CH2\_EXT               | 3.3V     |
| 28  | IO\_CH6\_EXT               | 3.3V     |
| 29  | IO\_CH3\_EXT               | 3.3V     |
| 30  | IO\_CH7\_EXT               | 3.3V     |
| 31  | IO\_CH4\_EXT               | 3.3V     |
| 32  | IO\_CH8\_EXT               | 3.3V     |
| 33  | GND                        | GND      |
| 34  | VDD\_SERVO\_SENSE          | 9.9V Max |
| 35  | JCAN\_P                    | 5V       |
| 36  | GND                        | GND      |
| 37  | JCAN\_N                    | 5V       |
| 38  | GND                        | GND      |
| 39  | GND                        | GND      |
| 40  | VDD\_5V\_PERIPH            | 5V       |

### SPI (J1) — 11-pin JST-GH

| Pin | Signal            | Voltage |
| --- | ----------------- | ------- |
| 1   | VDD\_5V\_PERIPH   | 5V      |
| 2   | SPI6\_SCK\_EXT    | 3.3V    |
| 3   | SPI6\_MISO\_EXT   | 3.3V    |
| 4   | SPI6\_MOSI\_EXT   | 3.3V    |
| 5   | SPI6\_nCS1\_EXT   | 3.3V    |
| 6   | Not connected     | —       |
| 7   | SPIX\_nSYNC\_EXT  | 3.3V    |
| 8   | SPI6\_DRDY1\_EXT  | 3.3V    |
| 9   | Not connected     | —       |
| 10  | SPI6\_nRESET\_EXT | 3.3V    |
| 11  | GND               | GND     |

### GPS2 (J2) — 6-pin JST-GH

| Pin | Signal                     | Voltage |
| --- | -------------------------- | ------- |
| 1   | VDD\_5V\_PERIPH            | 5V      |
| 2   | UART8\_TX\_GPS2\_EXT       | 3.3V    |
| 3   | UART8\_RX\_GPS2\_EXT       | 3.3V    |
| 4   | I2C2\_SCL\_BASE\_GPS2\_EXT | 3.3V    |
| 5   | I2C2\_SDA\_BASE\_GPS2\_EXT | 3.3V    |
| 6   | GND                        | GND     |

### JCAN (J4) — 4-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | JCAN\_P         | 5V      |
| 3   | JCAN\_N         | 5V      |
| 4   | GND             | GND     |

### SBUS Out (J5) — 3-pin JST-GH

| Pin | Signal                | Voltage |
| --- | --------------------- | ------- |
| 1   | VDD\_5V\_SBUS\_RC     | 5V      |
| 2   | IO\_SBUS\_OUTPUT\_EXT | 3.3V    |
| 3   | GND                   | GND     |

### PWM (J6) — 10-pin JST-GH

| Pin | Signal            | Voltage  |
| --- | ----------------- | -------- |
| 1   | VDD\_SERVO\_SENSE | 9.9V Max |
| 2   | IO\_CH1\_EXT      | 3.3V     |
| 3   | IO\_CH2\_EXT      | 3.3V     |
| 4   | IO\_CH3\_EXT      | 3.3V     |
| 5   | IO\_CH4\_EXT      | 3.3V     |
| 6   | IO\_CH5\_EXT      | 3.3V     |
| 7   | IO\_CH6\_EXT      | 3.3V     |
| 8   | IO\_CH7\_EXT      | 3.3V     |
| 9   | IO\_CH8\_EXT      | 3.3V     |
| 10  | GND               | GND      |

### TELEM3 (J7) — 6-pin JST-GH

| Pin | Signal                  | Voltage |
| --- | ----------------------- | ------- |
| 1   | VDD\_5V\_PERIPH         | 5V      |
| 2   | USART2\_TX\_TELEM3\_EXT | 3.3V    |
| 3   | USART2\_RX\_TELEM3\_EXT | 3.3V    |
| 4   | Not connected           | —       |
| 5   | Not connected           | —       |
| 6   | GND                     | GND     |

## 3D Model and Case

| File | Contents |
|------|----------|
| [Secondary\_Avionics\_Breakout.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Secondary_Avionics_Breakout/model/Secondary_Avionics_Breakout.step) | Board |

All files: [ARK\_Secondary\_Avionics\_Breakout in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Secondary_Avionics_Breakout)
