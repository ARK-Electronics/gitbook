# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox NEO-M9N](https://www.u-blox.com/en/product/neo-m9n-module), meter-level, 4 concurrent GNSS |
| Interference | Spoofing and jamming detection, RF interference mitigation |
| Magnetometer | [Bosch BMM150](https://www.bosch-sensortec.com/products/motion-sensors/magnetometers-bmm150/) |
| Barometer | [Bosch BMP388](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp388/) |
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412CEU6 |
| Safety button | Yes |
| Buzzer | Yes |
| Interfaces | 2× DroneCAN (Pixhawk-standard 4-pin JST-GH), debug (Pixhawk-standard 6-pin JST-SH) |
| Power | 5 V, 110 mA average, 117 mA max |
| Dimensions | 5 × 5 × 1 cm |

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

The board has a safety LED, a GPS fix LED and an RGB status LED.

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

If the status LED blinks red, check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the ARK GPS has `ark_can-gps_canbootloader` installed prior to flashing `ark_can-gps_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_GPS\_Rev\_3\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_GPS/model/ARK_GPS_Rev_3_3D_Model.step) | Board, rev 3 |
| [Top\_Case\_Rev\_1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_GPS/case/Top_Case_Rev_1.stl) | Case top, rev 1 |
| [Bottom\_Case\_Rev\_1.1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_GPS/case/Bottom_Case_Rev_1.1.stl) | Case bottom, rev 1.1 |

All files: [ARK\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_GPS)

## Schematic and BOM

| File | Contents |
|------|----------|
| [ARK\_GPS\_Rev\_3\_Schematic.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_GPS/schematic/ARK_GPS_Rev_3_Schematic.pdf) | Schematic, rev 3 |
| [ARK\_GPS\_Rev\_3\_BOM.xlsx](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_GPS/bom/ARK_GPS_Rev_3_BOM.xlsx) | Bill of materials, rev 3 |
