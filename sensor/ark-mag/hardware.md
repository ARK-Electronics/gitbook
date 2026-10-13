# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Magnetometer | [PNI RM3100](https://www.pnisensor.com/rm3100/), tri-axis |
| MCU | STM32F412VG |
| CAN | 2× Pixhawk-standard 4-pin JST-GH |
| Debug | Pixhawk-standard 6-pin JST-SH |
| Power | 5 V, 44 mA average, 50 mA max |
| Dimensions | 2.7 × 1.8 × 0.9 cm |
| Weight | 3 g |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### Debug — 6-pin JST-SH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3.3V | 3.3 V |
| 2 | USART2_TX | 3.3 V |
| 3 | USART2_RX | 3.3 V |
| 4 | FMU_SWDIO | 3.3 V |
| 5 | FMU_SWCLK | 3.3 V |
| 6 | GND | GND |

## LEDs

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## Wiring

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_MAG\_Rev\_1\_0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MAG/model/ARK_MAG_Rev_1_0.step) | Board, rev 1.0 |
| [Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MAG/case/Top_Case.stl) | Case top |
| [Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MAG/case/Bottom_Case.stl) | Case bottom |

All files: [ARK\_MAG in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_MAG)
