# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module), L1/L2. L1L5 variant: u-blox ZED-F9P-15B, L1/L5 |
| Constellations | GPS, GLONASS, Galileo and BeiDou, concurrently |
| Position accuracy | Centimeter-level with RTK |
| Moving baseline heading | L1/L2 model only |
| Magnetometer | [Bosch BMM150](https://www.bosch-sensortec.com/products/motion-sensors/magnetometers-bmm150/) |
| Barometer | [Bosch BMP388](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp388/) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412CEU6 |
| Safety button | Yes |
| Buzzer | Yes |
| Interfaces | 2× DroneCAN (Pixhawk-standard 4-pin JST-GH), F9P UART2 (3-pin JST-GH), debug (Pixhawk-standard 6-pin JST-SH) |
| Power | 5 V, 170 mA average, 180 mA max |
| Alternate antennas (L1/L2) | [Tallysman 33-HC882-28](https://www.digikey.com/en/products/detail/tallysman-wireless-inc/33-HC882-28/10473741), [Taoglas AA.175.301111](https://www.digikey.com/en/products/detail/taoglas-limited/AA-175-301111/11196807), [Taoglas A.80.A.101111](https://www.digikey.com/en/products/detail/taoglas-limited/A-80-A-101111/9972792), [Linx ANT-GNRM-L12A-3](https://www.digikey.com/en/products/detail/linx-technologies-inc/ANT-GNRM-L12A-3/16740159), [u-blox ANN-MB-00-00](https://www.digikey.com/en/products/detail/u-blox/ANN-MB-00-00/9817928) |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### F9P UART2 — 3-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | F9P_TXD2 | 3.3 V |
| 2 | F9P_RXD2 | 3.3 V |
| 3 | GND | GND |

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
| [ARK\_RTK\_GPS\_Rev\_3\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_GPS/model/ARK_RTK_GPS_Rev_3_3D_Model.step) | Board, rev 3 |
| [Top\_Case\_0.5.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_GPS/case/Top_Case_0.5.stl) | Case top |
| [Bottom\_Case\_0.5.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_GPS/case/Bottom_Case_0.5.stl) | Case bottom |

All files: [ARK\_RTK\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_RTK_GPS)

## Schematic and BOM

| File | Contents |
|------|----------|
| [ARK\_RTK\_GPS\_Rev\_3\_Schematic.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_GPS/schematic/ARK_RTK_GPS_Rev_3_Schematic.pdf) | Schematic, rev 3 |
| [ARK\_RTK\_GPS\_Rev\_3\_BOM.xlsx](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_GPS/bom/ARK_RTK_GPS_Rev_3_BOM.xlsx) | Bill of materials, rev 3 |
