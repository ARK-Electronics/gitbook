# Hardware Reference

![ARK CANnode](https://docs.px4.io/main/assets/ark_cannode.-X5QpRbg.jpg)

## Specifications

| Specification | Value |
|---------------|-------|
| IMU | [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/) or [Bosch BMI088](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/), 6-axis |
| MCU | STM32F412CGU6, 1 MB flash |
| CAN | 2× Pixhawk-standard 4-pin JST-GH |
| I2C | Pixhawk-standard 4-pin JST-GH |
| UART and I2C | Pixhawk-standard basic GPS port, 6-pin JST-GH |
| SPI | Pixhawk-standard 7-pin JST-GH |
| PWM | 8 outputs on a 10-pin JST-GH, matching the Pixhawk 4 PWM connector pinout |
| Debug | Pixhawk-standard 6-pin JST-SH |
| Power | 5 V, current depends on connected peripherals |
| Dimensions | 3 × 3 × 1.3 cm |
| Weight | 5 g |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### UART1/I2C1 — 6-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V out (500 mA) | 5.0 V |
| 2 | USART1_TX | 3.3 V |
| 3 | USART1_RX | 3.3 V |
| 4 | I2C1_SCL | 3.3 V |
| 5 | I2C1_SDA | 3.3 V |
| 6 | GND | GND |

### I2C1 — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V out (500 mA) | 5.0 V |
| 2 | I2C1_SCL | 3.3 V |
| 3 | I2C1_SDA | 3.3 V |
| 4 | GND | GND |

### SPI — 7-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V | 5.0 V |
| 2 | SPI2_SCK | 3.3 V |
| 3 | SPI2_MISO | 3.3 V |
| 4 | SPI2_MOSI | 3.3 V |
| 5 | SPI2_CS_1 | 3.3 V |
| 6 | SPI2_CS_2 | 3.3 V |
| 7 | GND | GND |

### PWM — 10-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | Pulled up to 3.3V through a 1.5 kΩ resistor | 3.3 V |
| 2 | TIM2_CH1_PWM1 | 3.3 V |
| 3 | TIM2_CH2_PWM2 | 3.3 V |
| 4 | TIM2_CH3_PWM3 | 3.3 V |
| 5 | TIM3_CH1_PWM4 | 3.3 V |
| 6 | TIM3_CH2_PWM5 | 3.3 V |
| 7 | TIM3_CH3_PWM6 | 3.3 V |
| 8 | TIM3_CH4_PWM7 | 3.3 V |
| 9 | TIM4_CH2_PWM8 | 3.3 V |
| 10 | GND | GND |

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

With the PX4 DroneCAN bootloader and firmware, the RGB status LED shows:

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

If the status LED blinks red, check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the ARK CANnode has `ark_cannode_canbootloader` installed prior to flashing `ark_cannode_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

## Wiring

The ARK CANnode is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_CANNODE\_Rev\_1\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_CANnode/model/ARK_CANNODE_Rev_1_3D_Model.step) | Board, rev 1 |
| [Top\_Case\_0.2.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_CANnode/case/Top_Case_0.2.stl) | Case top, rev 0.2 |
| [Bottom\_Case\_0.1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_CANnode/case/Bottom_Case_0.1.stl) | Case bottom, rev 0.1 |

All files: [ARK\_CANnode in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_CANnode)

## Schematic and BOM

| File | Contents |
|------|----------|
| [ARK\_CANNODE\_Rev\_1\_Schematic.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_CANnode/schematic/ARK_CANNODE_Rev_1_Schematic.pdf) | Schematic, rev 1 |
| [ARK\_CANNODE\_Rev\_1\_BOM.xlsx](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_CANnode/bom/ARK_CANNODE_Rev_1_BOM.xlsx) | Bill of materials, rev 1 |
