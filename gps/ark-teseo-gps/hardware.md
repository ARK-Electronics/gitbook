# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [ST Teseo-LIV4F](https://www.st.com/en/positioning/teseo-liv4f.html), L1/L5 |
| Constellations | GPS, GLONASS, Galileo, BeiDou, QZSS, IRNSS; four at a time, plus SBAS |
| Tracking sensitivity | −162 dBm |
| Position accuracy | Submeter |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Barometer | [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/pressure-sensors-bmp390.html) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412VGH6 |
| Buzzer | Yes |
| Power | 5 V, 137 mA |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### I2C and Timepulse — 5-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V out (500 mA) | 5.0 V |
| 2 | I2C2_SCL | 3.3 V |
| 3 | I2C2_SDA | 3.3 V |
| 4 | TIMEPULSE | 3.3 V |
| 5 | GND | GND |

The firmware does not use I2C2. TIMEPULSE outputs the receiver's PPS, which the flight controller can use to timestamp PVT solutions.

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

The green LED on the left edge flashes once per second with the receiver's time pulse (PPS). The status LED (red, green and blue in a row) is on the right edge and is driven by the node firmware.

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |
| Blue, blinking (2 Hz) after the firmware has started | Updating the Teseo receiver firmware |
| Red, blinking (1 Hz) after the firmware has started | Teseo receiver firmware update failed |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_TESEO\_GPS\_Rev\_2\_0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_TESEO_GPS/model/ARK_TESEO_GPS_Rev_2_0.step) | Board, rev 2.0 |
| [Teseo\_Top\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_TESEO_GPS/case/Teseo_Top_Case.stl) | Case top |
| [Teseo\_Bottom\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_TESEO_GPS/case/Teseo_Bottom_Case.stl) | Case bottom |

All files: [ARK\_TESEO\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_TESEO_GPS)
