# Hardware Reference

## Specifications

| Specification         | Value                                |
| --------------------- | ------------------------------------ |
| Supply voltage        | 5 V (J3)                             |
| Peripheral rail       | `VDD_5V_PERIPH`, 1.5 A current limit |
| Rail enable           | `VDD_5V_PERIPH_nEN` (active low)     |
| Protection            | [TI BQ24315](https://www.ti.com/product/BQ24315) switch: overvoltage, overcurrent, fault flag |
| Signal logic level    | 3.3 V                                |
| Operating temperature | −25 °C to +85 °C                     |
| Dimensions            | 34.25 × 18.50 × 5.81 mm              |
| Weight                | 3.5 g                                |
| PCB                   | 2-layer FR-4, 1.61 mm, ENIG          |

Operating temperature is limited by the JST-GH connectors; all other components are rated wider.

## Pinout

### Payload Bus (J4) — 30-pin 0.5 mm pitch FFC

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

### 5V Input and I2C3 (J3) — 6-pin Molex Pico-Clasp

| Pin | Signal         | Voltage |
| --- | -------------- | ------- |
| 1   | 5V             | 5V      |
| 2   | 5V             | 5V      |
| 3   | I2C3\_SCL\_EXT | 3.3V    |
| 4   | I2C3\_SDA\_EXT | 3.3V    |
| 5   | GND            | GND     |
| 6   | GND            | GND     |

### UART4 / I2C3 (J1) — 6-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | UART4\_TX\_EXT  | 3.3V    |
| 3   | UART4\_RX\_EXT  | 3.3V    |
| 4   | I2C3\_SCL\_EXT  | 3.3V    |
| 5   | I2C3\_SDA\_EXT  | 3.3V    |
| 6   | GND             | GND     |

### CAN (J2) — 4-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | CAN\_P          | 5V      |
| 3   | CAN\_N          | 5V      |
| 4   | GND             | GND     |

### Ethernet (J5) — 4-pin JST-GH

| Pin | Signal           | Voltage      |
| --- | ---------------- | ------------ |
| 1   | PYLD\_ETH\_RX\_N | Differential |
| 2   | PYLD\_ETH\_RX\_P | Differential |
| 3   | PYLD\_ETH\_TX\_N | Differential |
| 4   | PYLD\_ETH\_TX\_P | Differential |

The connector shell is intentionally left unconnected.

### USB (J6) — 4-pin JST-GH

| Pin | Signal | Voltage |
| --- | ------ | ------- |
| 1   | VBUS   | 5V      |
| 2   | USB\_N | 3.3V    |
| 3   | USB\_P | 3.3V    |
| 4   | GND    | GND     |

### GPIO (J7) — 7-pin JST-GH

| Pin | Signal          | Voltage |
| --- | --------------- | ------- |
| 1   | VDD\_5V\_PERIPH | 5V      |
| 2   | FMU\_CH7\_EXT   | 3.3V    |
| 3   | FMU\_CH8\_EXT   | 3.3V    |
| 4   | FMU\_CAP\_EXT   | 3.3V    |
| 5   | GPIO01          | 3.3V    |
| 6   | GPIO12\_EXT     | 3.3V    |
| 7   | GND             | GND     |

## Power

A 5 V supply enters on a 6-pin Molex Pico-Clasp using the Pixhawk power-module pinout. An onboard TI BQ24315 protection switch derives the `VDD_5V_PERIPH` rail with a 1.5 A current limit, overvoltage protection, and a fault flag, and is gated by the autopilot over `VDD_5V_PERIPH_nEN`.

`VDD_5V_PERIPH` is shared by J1, J2, and J7 and is limited to 1.5 A in total. J5 and J6 carry no supply rail — `VBUS` on J6 is passed through directly from Payload Bus pin 24 and is not switched or protected on this board.

Test points: TP1 = `VDD_5V_HIGHPOWER_nEN`, TP2 = `VDD_5V_PERIPH`, TP3 = `FAULT` (open drain).

## Datasheet

* [ARK Pixhawk Payload Bus Breakout](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_Pixhawk_Payload_Bus_Breakout/datasheet/ARK_Pixhawk_Payload_Bus_Breakout_Datasheet.pdf)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_Pixhawk\_Payload\_Bus\_Breakout.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Pixhawk_Payload_Bus_Breakout/model/ARK_Pixhawk_Payload_Bus_Breakout.step) | Board |

All files: [ARK\_Pixhawk\_Payload\_Bus\_Breakout in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Pixhawk_Payload_Bus_Breakout)
