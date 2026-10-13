# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Distance sensor | SR: [Broadcom AFBR-S50LV85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lv85d). MR: [Broadcom AFBR-S50LX85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lx85d). LR: Broadcom AFBR-S50EX85D. All time-of-flight |
| Range | See [Range](#range) |
| Reported distance | SR: 0 to 30 m. MR: 0.1 to 50 m. LR: 0.6 to 100 m |
| Rate | SR: 20 Hz. MR: 15 Hz. LR: 10 Hz |
| Laser | 850 nm, Class 1 eye safe (IEC 60825-1) |
| Beam | 2° × 2°, 3.5 cm spot at 1 m. SR and MR: 32-pixel receiver, 12.4° × 6.2° field of view, reference pixel for system health monitoring |
| MCU | STM32F412VG |
| CAN | DroneCAN range, 2× Pixhawk-standard 4-pin JST-GH |
| UART | MAVLink 2 `DISTANCE_SENSOR`, Pixhawk-standard 6-pin JST-GH |
| Debug | NSH console and SWD, Pixhawk-standard 6-pin JST-SH |
| Power | 5 V, 78–86 mA |
| Dimensions | 2.0 × 2.8 × 1.4 cm |
| Weight | 4 g |

## Range

Range depends on the ambient light on the ground and on how well the surface reflects 850 nm light. With default settings, range is the greatest height at which at least half the readings are valid and within 5 m of the true height:

| Variant | Asphalt, bright sun | Asphalt, dusk | Grass, bright sun | Grass, dusk |
|---------|---------------------|---------------|-------------------|-------------|
| SR | 18 m | 30 m | 18 m | 30 m\* |
| MR | 18 m | 40 m | 18 m | 50 m\* |
| LR | 18 m | 40 m | 40 m | 82 m |

Bright sun: sun 49–61° above the horizon; a lower sun gives more range. Dusk: sun below 6°. \* Limited by the maximum reported distance; the sensor was still measuring at the flight ceiling (SR 38 m, MR 54 m). Wet surfaces reduce range. Over open water, readings are short and intermittent.

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

## Datasheets

* [ARK DIST](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_DIST/datasheet/ARK_DIST_Datasheet.pdf)

## 3D Model and Case

All three variants use the same board and case.

| File | Contents |
|------|----------|
| [ARK\_DIST\_Rev\_1\_0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/model/ARK_DIST_Rev_1_0.step) | Board, rev 1.0 |
| [ARK\_DIST\_Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/case/ARK_DIST_Top_Case.stl) | Case top |
| [ARK\_DIST\_Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DIST/case/ARK_DIST_Bottom_Case.stl) | Case bottom |

All files: [ARK\_DIST in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_DIST)
