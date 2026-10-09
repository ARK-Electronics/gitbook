# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Distance sensor | MR: [Broadcom AFBR-S50LX85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lx85d) time-of-flight. SR: [Broadcom AFBR-S50LV85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lv85d) time-of-flight |
| Range | MR: typically up to 50 m. SR: typically up to 30 m |
| Beam | MR: laser opening angle of 2° × 2°. SR: integrated 850 nm laser, 2° × 2° transmitter beam illuminating 1 to 3 pixels, 12.4° × 6.2° field of view with 32 pixels, reference pixel for system health monitoring |
| Ambient light | Operates up to 200k lux |
| MCU | STM32F412VG |
| CAN | DroneCAN range, 2× Pixhawk-standard 4-pin JST-GH |
| UART | MAVLink 2 `DISTANCE_SENSOR`, Pixhawk-standard 6-pin JST-GH |
| Debug | NSH console and SWD, Pixhawk-standard 6-pin JST-SH |
| Power | 5 V. MR: 78 mA average, 84 mA max. SR: 84 mA average, 86 mA max |
| Dimensions | 2.0 × 2.8 × 1.4 cm |
| Weight | 4 g |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### UART — 6-pin JST-GH

MAVLink 2 distance output. See [UART / MAVLink](uart-mavlink.md).

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V_UART | 5.0 V |
| 2 | USART3_RX | 3.3 V |
| 3 | USART3_TX | 3.3 V |
| 4 | USART3_RTS | 3.3 V |
| 5 | USART3_CTS | 3.3 V |
| 6 | GND | GND |

### Debug — 6-pin JST-SH

NSH console and SWD.

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

**CAN:** connect with a Pixhawk standard 4-pin JST-GH cable. See [CAN Wiring](https://docs.px4.io/main/en/can/#wiring). Chain additional nodes from the second CAN connector.

**UART:** connect the 6-pin UART JST-GH to a free FC serial port. Protocol details: [UART / MAVLink](uart-mavlink.md).

## 3D Model and Case

Both variants use the same board and case.

| File | Contents |
|------|----------|
| [ARK\_DIST\_Rev\_1\_0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/model/ARK_DIST_Rev_1_0.step) | Board, rev 1.0 |
| [ARK\_DIST\_Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/case/ARK_DIST_Top_Case.stl) | Case top |
| [ARK\_DIST\_Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/case/ARK_DIST_Bottom_Case.stl) | Case bottom |

All files: [ARK\_DIST in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_DIST)
