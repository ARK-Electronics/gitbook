---
description: >-
  Pixhawk Payload Bus to Pixhawk-standard JST-GH, with a protected 5 V
  peripheral rail.
cover: ../../.gitbook/assets/IMG_6529 edited.JPG
coverY: 0
---

# ARK Pixhawk Payload Bus Breakout

The ARK Pixhawk Payload Bus Breakout fans the 30-pin Payload Bus out to individually keyed Pixhawk-standard JST-GH connectors. UART4/I2C3, CAN, Ethernet, USB, and GPIO each get their own connector, so a payload can be wired to an ARK carrier without a custom harness.

A 5 V supply enters on a 6-pin Molex Pico-Clasp using the Pixhawk power-module pinout. An onboard TI BQ24315 protection switch derives the `VDD_5V_PERIPH` rail with a 1.5 A current limit, overvoltage protection, and a fault flag, and is gated by the autopilot over `VDD_5V_PERIPH_nEN`.

### Connectors

| Ref | Connector                | Function           |
| --- | ------------------------ | ------------------ |
| J4  | 30-pin, 0.5 mm pitch FFC | Payload Bus        |
| J3  | 6-pin Molex Pico-Clasp   | 5 V input and I2C3 |
| J1  | 6-pin JST-GH             | UART4 / I2C3       |
| J2  | 4-pin JST-GH             | CAN                |
| J5  | 4-pin JST-GH             | Ethernet           |
| J6  | 4-pin JST-GH             | USB                |
| J7  | 7-pin JST-GH             | GPIO               |

### Specifications

| Parameter             | Value                                |
| --------------------- | ------------------------------------ |
| Supply voltage        | 5 V (J3)                             |
| Peripheral rail       | `VDD_5V_PERIPH`, 1.5 A current limit |
| Rail enable           | `VDD_5V_PERIPH_nEN` (active low)     |
| Protection            | Overvoltage, overcurrent, fault flag |
| Signal logic level    | 3.3 V                                |
| Operating temperature | −25 °C to +85 °C                     |
| Dimensions            | 34.25 × 18.50 × 5.81 mm              |
| Weight                | 3.5 g                                |
| PCB                   | 2-layer FR-4, 1.61 mm, ENIG          |

Operating temperature is limited by the JST-GH connectors; all other components are rated wider.

### Power

`VDD_5V_PERIPH` is shared by J1, J2, and J7 and is limited to 1.5 A in total. J5 and J6 carry no supply rail — `VBUS` on J6 is passed through directly from Payload Bus pin 24 and is not switched or protected on this board.

Test points: TP1 = `VDD_5V_HIGHPOWER_nEN`, TP2 = `VDD_5V_PERIPH`, TP3 = `FAULT` (open drain).

### Included

30-pin, 0.5 mm pitch, 150 mm FFC cable.
