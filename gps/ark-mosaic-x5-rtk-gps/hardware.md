# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [Septentrio mosaic-X5](https://www.septentrio.com/en/products/gps/gnss-receiver-modules/mosaic-x5), triple-band L1/L2/L5 |
| Update rate | 100 Hz |
| Interference protection | [AIM+ jamming protection](https://www.septentrio.com/en/learn-more/advanced-positioning-technology/aim-jamming-protection) |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Barometer | [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/pressure-sensors-bmp390.html) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412VGH6 |
| Safety button | Yes |
| Buzzer | Yes |
| Interfaces | Two CAN (5 V input), receiver UART2 with timepulse and GP1, Pixhawk-standard basic GPS port (USART3 and I2C2 from the MCU) for external sensors such as airspeed or distance, receiver USB-C (USB 2.0, 5 V input), debug |
| Logging | Micro-SD slot for mosaic-X5 logging |
| Power | 5 V; 260 mA average, 340 mA peak |
| Weight | 21 g |

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

### GPS UART2 and Timepulse — 5-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | TXD2 | 3.3 V |
| 2 | RXD2 | 3.3 V |
| 3 | TIMEPULSE | 1.8 V |
| 4 | GP1 | 3.3 V |
| 5 | GND | GND |

### USART3 and I2C2 — 6-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V out (500 mA) | 5.0 V |
| 2 | USART3_TX | 3.3 V |
| 3 | USART3_RX | 3.3 V |
| 4 | I2C2_SCL | 3.3 V |
| 5 | I2C2_SDA | 3.3 V |
| 6 | GND | GND |

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
| White, fast blink (10 Hz) | GPS passthrough, entered by holding the safety switch at power-up. The receiver's UART1 is bridged to the debug connector's UART. |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_MOSAIC-X5\_REV\_2.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MOSAIC-X5_RTK_GPS/model/ARK_MOSAIC-X5_REV_2.step) | Board, rev 2 |
| [ARK\_MOSAIC-X5\_Top\_Case\_REV\_2.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MOSAIC-X5_RTK_GPS/case/ARK_MOSAIC-X5_Top_Case_REV_2.stl) | Case top, rev 2 |
| [ARK\_MOSAIC-X5\_Bottom\_Case\_REV\_1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_MOSAIC-X5_RTK_GPS/case/ARK_MOSAIC-X5_Bottom_Case_REV_1.stl) | Case bottom, rev 1 |
| [BT-T076.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/Antennas/beitian/BT-T076.stl) | Beitian BT-T076 helical antenna |

All files: [ARK\_MOSAIC-X5\_RTK\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_MOSAIC-X5_RTK_GPS)
