# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | Septentrio [mosaic-G5 P3H](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3H), P6 or P8, multi-constellation, quad-band |
| Positioning | cm-level RTK |
| Dual antenna heading | MAIN and ANT2, triple-band, set to dual antenna in production |
| Update rate | 20 Hz (P3H), 100 Hz (P8) |
| Interference protection | [AIM+](https://www.septentrio.com/en/learn-more/advanced-positioning-technology/aim-jamming-protection) (P3H), [AIM+ Premium](https://www.septentrio.com/en/learn-more/advanced-positioning-technology/gps-gnss-interference#paragraph-id-21060) (P6), [AIM+ ultimate](https://www.septentrio.com/en/learn-more/advanced-positioning-technology/gps-gnss-interference#paragraph-id-21060) (P8): jamming and spoofing detection and mitigation |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Barometer | [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp390/) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412VGH6 |
| Buzzer | Yes |
| Interfaces | Two CAN, receiver UART2 with PPS, receiver USB-C, debug |
| Power | 4.6–5.4 V, 360 mA |
| Dimensions | 48.0 × 40.0 × 15.4 mm without antenna, 48.0 × 40.0 × 51.0 mm with main antenna, 91.5 × 40.0 × 51.0 mm with dual antennas |
| Weight | 13.0 g without antenna, 43.5 g with main antenna, 91.0 g with dual antennas |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### USB — USB-C

| Pin | Signal | Voltage |
|-----|--------|---------|
| 2, 11 | VBUS | 5.0 V |
| 5, 8 | USB_N | 3.3 V |
| 6, 7 | USB_P | 3.3 V |
| 1, 12 | GND | GND |

### GPS UART2 and Timepulse — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | TXD2 | 3.3 V |
| 2 | RXD2 | 3.3 V |
| 3 | TIMEPULSE | 3.3 V |
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

With the connectors at the bottom edge, the GNSS LEDs are on the right edge and the status LED (red, green and blue) is on the left edge. The GNSS LEDs are driven by the receiver; the status LED by the node firmware.

| GNSS LED | Meaning |
|-----|---------|
| Green, one short flash per second | Receiver PPS. Starts once the receiver has a position fix. |
| Blue, blinking | RTK Float |
| Blue, solid | RTK Fixed |

The receiver configuration ARK saves at the factory sets both LEDs; resetting the receiver to its defaults changes them.

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## 3D Model and Case

The G5H shares these files with the ARK G5 RTK GPS.

| File | Contents |
|------|----------|
| [ARK\_G5\_RTK\_GPS\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_G5_RTK_GPS/model/ARK_G5_RTK_GPS_Rev_1.0.step) | Board, rev 1.0 |
| [ARK\_G5\_RTK\_GPS\_Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_G5_RTK_GPS/case/ARK_G5_RTK_GPS_Top_Case.stl) | Case top |
| [ARK\_G5\_RTK\_GPS\_Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_G5_RTK_GPS/case/ARK_G5_RTK_GPS_Bottom_Case.stl) | Case bottom |
| [BT-T076.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/Antennas/beitian/BT-T076.stl) | Beitian BT-T076 helical antenna |

All files: [ARK\_G5\_RTK\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_G5_RTK_GPS)
