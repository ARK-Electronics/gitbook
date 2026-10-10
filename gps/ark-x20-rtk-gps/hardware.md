# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox ZED-X20P](https://www.u-blox.com/en/product/zed-x20p-module), all-band (L1/L2/L5). The node firmware uses GPS, QZSS, SBAS, Galileo, BeiDou and NavIC, not GLONASS: see [Constellations](firmware.md#constellations) |
| Positioning | RTK, PPP-RTK and PPP |
| Update rate | 25 Hz |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Barometer | [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp390/) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412VGH6 |
| Safety button | Yes |
| Buzzer | Yes |
| Interfaces | Two CAN, receiver UART2 with PPS, I2C expansion, debug |
| Power | 4.7–5.4 V; 144 mA average, 157 mA max |
| Dimensions | 48.0 × 40.0 × 15.4 mm without antenna, 55.2 × 43.5 × 51.2 mm with antenna |
| Weight | 13.0 g without antenna, 43.5 g with antenna |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### GPS UART2 and Timepulse — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | TXD2 | 3.3 V |
| 2 | RXD2 | 3.3 V |
| 3 | TIMEPULSE | 3.3 V |
| 4 | GND | GND |

### I2C2 — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V out (500 mA) | 5.0 V |
| 2 | I2C2_SCL | 3.3 V |
| 3 | I2C2_SDA | 3.3 V |
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
| Green, one flash per second | Receiver time pulse. Starts once the receiver has a fix. |
| Blue, blinking | Corrections received and in use, RTK Float |
| Blue, solid | RTK Fixed |

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |
| White, fast blink (10 Hz) | GPS passthrough, entered by holding the safety switch at power-up. See [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md). |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_X20\_GPS\_Rev\_2.1.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_X20_RTK_GPS/model/ARK_X20_GPS_Rev_2.1.step) | Board, rev 2.1 |
| [Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_X20_RTK_GPS/case/Top_Case.stl) | Case top |
| [Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_X20_RTK_GPS/case/Bottom_Case.stl) | Case bottom |
| [BT-T076.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/Antennas/beitian/BT-T076.stl) | Beitian BT-T076 helical antenna |

All files: [ARK\_X20\_RTK\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_X20_RTK_GPS)
