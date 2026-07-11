---
description: Pin assignments for the ARK Primary Avionics Adapter connectors.
---

# Pinout

### Primary avionics port

**J3** — 40-pin Pico-Clasp primary avionics port

| Pin | Signal                         | Voltage          |
| --- | ------------------------------ | ---------------- |
| 1   | VDD\_5V\_SBUS\_RC              | 5V               |
| 2   | IO\_SBUS\_INPUT\_EXT           | 3.3V             |
| 3   | GND                            | GND              |
| 4   | GND                            | GND              |
| 5   | nSAFETY\_SWITCH\_IN\_EXT       | 3.3V             |
| 6   | nSAFETY\_SWITCH\_LED\_OUT\_EXT | 3.3V             |
| 7   | 3V3\_FMU                       | 3.3V             |
| 8   | BUZZER\_EXT                    | 24V (Open Drain) |
| 9   | UART7\_TX\_TELEM1\_EXT         | 3.3V             |
| 10  | UART7\_CTS\_TELEM1\_EXT        | 3.3V             |
| 11  | UART7\_RX\_TELEM1\_EXT         | 3.3V             |
| 12  | UART7\_RTS\_TELEM1\_EXT        | 3.3V             |
| 13  | VDD\_5V\_HIPOWER               | 5V               |
| 14  | GND                            | GND              |
| 15  | GND                            | GND              |
| 16  | GND                            | GND              |
| 17  | GND                            | GND              |
| 18  | GND                            | GND              |
| 19  | I2C1\_SCL\_GPS1\_EXT           | 3.3V             |
| 20  | USART1\_RX\_GPS1\_EXT          | 3.3V             |
| 21  | I2C1\_SDA\_GPS1\_EXT           | 3.3V             |
| 22  | VDD\_5V\_PERIPH                | 5V               |
| 23  | GND                            | GND              |
| 24  | GND                            | GND              |
| 25  | FMU\_CH1\_EXT                  | 3.3V             |
| 26  | FMU\_CH5\_EXT                  | 3.3V             |
| 27  | FMU\_CH2\_EXT                  | 3.3V             |
| 28  | FMU\_CH6\_EXT                  | 3.3V             |
| 29  | FMU\_CH3\_EXT                  | 3.3V             |
| 30  | FMU\_CH7\_EXT                  | 3.3V             |
| 31  | FMU\_CH4\_EXT                  | 3.3V             |
| 32  | FMU\_CH8\_EXT                  | 3.3V             |
| 33  | GND                            | GND              |
| 34  | VDD\_SERVO\_SENSE              | 9.9V Max         |
| 35  | CAN1\_P                        | 5V               |
| 36  | GND                            | GND              |
| 37  | CAN1\_N                        | 5V               |
| 38  | GND                            | GND              |
| 39  | GND                            | GND              |
| 40  | GND                            | GND              |

### RC input

**J1** — 3-pin JST-GH

| Pin | Signal               | Voltage |
| --- | -------------------- | ------- |
| 1   | VDD\_5V\_SBUS\_RC    | 5V      |
| 2   | IO\_SBUS\_INPUT\_EXT | 3.3V    |
| 3   | GND                  | GND     |

### TELEM1

**J2** — 6-pin JST-GH

| Pin | Signal                  | Voltage |
| --- | ----------------------- | ------- |
| 1   | VDD\_5V\_HIPOWER        | 5V      |
| 2   | UART7\_TX\_TELEM1\_EXT  | 3.3V    |
| 3   | UART7\_RX\_TELEM1\_EXT  | 3.3V    |
| 4   | UART7\_CTS\_TELEM1\_EXT | 3.3V    |
| 5   | UART7\_RTS\_TELEM1\_EXT | 3.3V    |
| 6   | GND                     | GND     |

### GPS1

**J4** — 10-pin JST-GH

| Pin | Signal                         | Voltage          |
| --- | ------------------------------ | ---------------- |
| 1   | VDD\_5V\_PERIPH                | 5V               |
| 2   | USART1\_TX\_GPS1\_EXT          | 3.3V             |
| 3   | USART1\_RX\_GPS1\_EXT          | 3.3V             |
| 4   | I2C1\_SCL\_GPS1\_EXT           | 3.3V             |
| 5   | I2C1\_SDA\_GPS1\_EXT           | 3.3V             |
| 6   | nSAFETY\_SWITCH\_IN\_EXT       | 3.3V             |
| 7   | nSAFETY\_SWITCH\_LED\_OUT\_EXT | 3.3V             |
| 8   | BUZZER\_EXT                    | 24V (Open Drain) |
| 9   | 3V3\_FMU                       | 3.3V             |
| 10  | GND                            | GND              |

### PWM

**J5** — 10-pin JST-GH

| Pin | Signal            | Voltage  |
| --- | ----------------- | -------- |
| 1   | VDD\_SERVO\_SENSE | 9.9V Max |
| 2   | FMU\_CH1\_EXT     | 3.3V     |
| 3   | FMU\_CH2\_EXT     | 3.3V     |
| 4   | FMU\_CH3\_EXT     | 3.3V     |
| 5   | FMU\_CH4\_EXT     | 3.3V     |
| 6   | FMU\_CH5\_EXT     | 3.3V     |
| 7   | FMU\_CH6\_EXT     | 3.3V     |
| 8   | FMU\_CH7\_EXT     | 3.3V     |
| 9   | FMU\_CH8\_EXT     | 3.3V     |
| 10  | GND               | GND      |

### CAN1

**J6** — 4-pin JST-GH

| Pin | Signal           | Voltage |
| --- | ---------------- | ------- |
| 1   | VDD\_5V\_HIPOWER | 5V      |
| 2   | CAN1\_P          | 5V      |
| 3   | CAN1\_N          | 5V      |
| 4   | GND              | GND     |
