---
description: Pin assignments for the ARK Pixhawk Payload Bus Breakout connectors.
---

# Pinout

### Payload bus

**J4** — 30-pin, 0.5 mm pitch FFC

| Pin   | Signal                  | Voltage      |
| ----- | ----------------------- | ------------ |
| 1     | GND                     | GND          |
| 2     | UART4\_TX\_EXT          | 3.3V         |
| 3     | UART4\_RX\_EXT          | 3.3V         |
| 4     | GND                     | GND          |
| 5     | I2C3\_SDA\_EXT          | 3.3V         |
| 6     | I2C3\_SCL\_EXT          | 3.3V         |
| 7     | GND                     | GND          |
| 8     | CAN\_P                  | 5V           |
| 9     | CAN\_N                  | 5V           |
| 10    | GND                     | GND          |
| 11    | FMU\_CH7\_EXT           | 3.3V         |
| 12    | GPIO12\_EXT             | 3.3V         |
| 13    | FMU\_CH8\_EXT           | 3.3V         |
| 14    | GND                     | GND          |
| 15    | FMU\_CAP\_EXT           | 3.3V         |
| 16    | GND                     | GND          |
| 17    | PYLD\_ETH\_TX\_P        | Differential |
| 18    | PYLD\_ETH\_TX\_N        | Differential |
| 19    | GND                     | GND          |
| 20    | PYLD\_ETH\_RX\_P        | Differential |
| 21    | PYLD\_ETH\_RX\_N        | Differential |
| 22    | GND                     | GND          |
| 23    | GPIO01                  | 3.3V         |
| 24    | VBUS                    | 5V           |
| 25    | USB\_N                  | 3.3V         |
| 26    | USB\_P                  | 3.3V         |
| 27    | GND                     | GND          |
| 28    | VDD\_5V\_HIGHPOWER\_nEN | 3.3V         |
| 29    | VDD\_5V\_PERIPH\_nEN    | 3.3V         |
| 30    | GND                     | GND          |
| G1–G6 | GND                     | GND          |

Pin 28 is brought out to test point TP1 only and is not otherwise connected on this board. Pin 29 drives the enable input of the onboard protection switch through a 47 kΩ series resistor; pulling it low enables the `VDD_5V_PERIPH` rail.

### 5V input

**J3** — 6-pin Molex Pico-Clasp

| Pin | Signal         | Voltage |
| --- | -------------- | ------- |
| 1   | 5V             | 5V      |
| 2   | 5V             | 5V      |
| 3   | I2C3\_SCL\_EXT | 3.3V    |
| 4   | I2C3\_SDA\_EXT | 3.3V    |
| 5   | GND            | GND     |
| 6   | GND            | GND     |

### UART4 / I2C3

**J1** — 6-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | UART4\_TX\_EXT  | 3.3V    |
| 3   | UART4\_RX\_EXT  | 3.3V    |
| 4   | I2C3\_SCL\_EXT  | 3.3V    |
| 5   | I2C3\_SDA\_EXT  | 3.3V    |
| 6   | GND             | GND     |

### CAN

**J2** — 4-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | CAN\_P          | 5V      |
| 3   | CAN\_N          | 5V      |
| 4   | GND             | GND     |

### Ethernet

**J5** — 4-pin JST-GH

| Pin | Signal           | Voltage      |
| --- | ---------------- | ------------ |
| 1   | PYLD\_ETH\_RX\_N | Differential |
| 2   | PYLD\_ETH\_RX\_P | Differential |
| 3   | PYLD\_ETH\_TX\_N | Differential |
| 4   | PYLD\_ETH\_TX\_P | Differential |

The connector shell is intentionally left unconnected.

### USB

**J6** — 4-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1   | VBUS   | 5V      |
| 2   | USB\_N | 3.3V    |
| 3   | USB\_P | 3.3V    |
| 4   | GND    | GND     |

### GPIO

**J7** — 7-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | FMU\_CH7\_EXT   | 3.3V    |
| 3   | FMU\_CH8\_EXT   | 3.3V    |
| 4   | FMU\_CAP\_EXT   | 3.3V    |
| 5   | GPIO01          | 3.3V    |
| 6   | GPIO12\_EXT     | 3.3V    |
| 7   | GND             | GND     |
