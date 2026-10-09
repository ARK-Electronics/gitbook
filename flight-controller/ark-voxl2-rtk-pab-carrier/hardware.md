# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Form factor | [Pixhawk Autopilot Bus (PAB)](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-010%20Pixhawk%20Autopilot%20Bus%20Standard.pdf) and [ModalAI VOXL2](https://www.modalai.com/products/voxl-2) |
| GNSS receiver | [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module), L1/L2 multi-band RTK with centimeter-level accuracy. Concurrent GPS, GLONASS, Galileo and BeiDou. Moving base for heading. MMCX antenna connector |
| VOXL2 connectors | MicroSD. USB-C: USB 3.0 host, 5 V 1.5 A. USB: USB 2.0 host, 4-pin JST-GH, 5 V 0.75 A |
| PAB board-to-board interface | 100-pin Hirose DF40, 50-pin Hirose DF40 |
| Flight Controller IO | 40-pin Molex Pico-Clasp: dual 5 V 1.5 A (shared with Payload IO), 5 V 0.25 A out for an RC receiver, dual CAN, dual UART (TX/RX), UART with RTS/CTS, dual I2C, 8 PWM |
| SPI | 11-pin JST-GH |
| Debug | Pixhawk Debug, 10-pin JST-SH: SWD, UART |
| Payload IO | 40-pin Molex Pico-Clasp: battery output, dual 5 V 1.5 A (shared with Flight Controller IO), autopilot UART with RTS/CTS, autopilot UART (TX/RX), dual VOXL2 UARTs (TX/RX), USB 2.0 |
| Power | 14-pin Molex CLIK-Mate: 12S 3 A battery input, dual 5 V 6 A inputs, dual I2C power module inputs |
| Dimensions | 94.25 × 36.00 × 18 mm, without VOXL2 and flight controller module |
| Weight | 25 g |

This product is not intended for military use. See the [u-blox code of conduct](https://www.u-blox.com/en/code-of-conduct).

## Pinout

<figure><img src="../../.gitbook/assets/Pinout Guide 1 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Pinout Guide 2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Pinout Guide 3.png" alt=""><figcaption></figcaption></figure>

{% file src="../../.gitbook/assets/Pinout Guide.pdf" %}

### Flight Controller IO — 40-pin Molex [Pico-Clasp 501571](https://www.molex.com/en-us/part-list/501571)

Mating plug [5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524)

Pre-crimped wires [0797581019](https://www.digikey.com/en/products/detail/molex/0797581019/6564344)

| Pin | Signal | Voltage | Pin | Signal | Voltage |
|-----|--------|---------|-----|--------|---------|
| 1 | CAN1_P | 5.0V | 2 | UART8_TX_GPS2_EXT | 3.3V |
| 3 | CAN1_N | 5.0V | 4 | UART8_RX_GPS2_EXT | 3.3V |
| 5 | GND | GND | 6 | I2C2_SCL_BASE_GPS2_EXT | 3.3V |
| 7 | VDD_5V_HIPOWER | 5.0V | 8 | I2C2_SDA_BASE_GPS2_EXT | 3.3V |
| 9 | VDD_5V_HIPOWER | 5.0V | 10 | GND | GND |
| 11 | GND | GND | 12 | FMU_CH1_EXT | 3.3V |
| 13 | GND | GND | 14 | FMU_CH2_EXT | 3.3V |
| 15 | VDD_5V_SBUS_RC | 5.0V | 16 | FMU_CH3_EXT | 3.3V |
| 17 | GND | GND | 18 | FMU_CH4_EXT | 3.3V |
| 19 | RX_SBUS_IN_EXT | 3.3V | 20 | GND | GND |
| 21 | USART6_TX_EXT | 3.3V | 22 | FMU_CH5_EXT | 3.3V |
| 23 | I2C1_SDA_BASE_GPS1_EXT | 3.3V | 24 | FMU_CH6_EXT | 3.3V |
| 25 | I2C1_SCL_BASE_GPS1_EXT | 3.3V | 26 | FMU_CH7_EXT | 3.3V |
| 27 | GND | GND | 28 | FMU_CH8_EXT | 3.3V |
| 29 | GND | GND | 30 | GND | GND |
| 31 | VDD_5V_PERIPH | 5.0V | 32 | UART7_TX_TELEM1_EXT | 3.3V |
| 33 | VDD_5V_PERIPH | 5.0V | 34 | UART7_RX_TELEM1_EXT | 3.3V |
| 35 | GND | GND | 36 | UART7_CTS_TELEM1_EXT | 3.3V |
| 37 | CAN2_P | 5.0V | 38 | UART7_RTS_TELEM1_EXT | 3.3V |
| 39 | CAN2_N | 5.0V | 40 | GND | GND |

### Payload IO — 40-pin Molex [Pico-Clasp 501571](https://www.molex.com/en-us/part-list/501571)

Mating plug [5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524)

Pre-crimped wires [0797581019](https://www.digikey.com/en/products/detail/molex/0797581019/6564344)

| Pin | Signal | Voltage | Pin | Signal | Voltage |
|-----|--------|---------|-----|--------|---------|
| 1 | VDD_5V_PERIPH | 5.0V | 2 | VIN | BAT |
| 3 | VDD_5V_PERIPH | 5.0V | 4 | VIN | BAT |
| 5 | GND | GND | 6 | VIN | BAT |
| 7 | GND | GND | 8 | VIN | BAT |
| 9 | USART2_TX_TELEM3_EXT | 3.3V | 10 | VIN | BAT |
| 11 | USART2_RX_TELEM3_EXT | 3.3V | 12 | GND | GND |
| 13 | USART2_CTS_TELEM3_EXT | 3.3V | 14 | GND | GND |
| 15 | USART2_RTS_TELEM3_EXT | 3.3V | 16 | GND | GND |
| 17 | GND | GND | 18 | GND | GND |
| 19 | VDD_5V_HIPOWER | 5.0V | 20 | GND | GND |
| 21 | VDD_5V_HIPOWER | 5.0V | 22 | UART4_TX_EXT | 3.3V |
| 23 | GND | GND | 24 | UART4_RX_EXT | 3.3V |
| 25 | GND | GND | 26 | GND | GND |
| 27 | GPIO_23_UART7_RXD_EXT | 3.3V | 28 | PAYLOAD_5V | 5.0V |
| 29 | GPIO_22_UART7_TXD_EXT | 3.3V | 30 | PAYLOAD_5V | 5.0V |
| 31 | GND | GND | 32 | GND | GND |
| 33 | ttyHS2_RX_EXT | 3.3V | 34 | GND | GND |
| 35 | ttyHS2_TX_EXT | 3.3V | 36 | USB_PAYLOAD_EXT_P | 3.3V |
| 37 | GND | GND | 38 | USB_PAYLOAD_EXT_N | 3.3V |
| 39 | GND | GND | 40 | GND | GND |

### Flight Controller Debug — 10-pin JST-SH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3V3_FMU | 3.3V |
| 2 | USART3_TX_DEBUG | 3.3V |
| 3 | USART3_RX_DEBUG | 3.3V |
| 4 | FMU_SWDIO | 3.3V |
| 5 | FMU_SWCLK | 3.3V |
| 6 | SPI6_SCK_EXTERNAL1 | 3.3V |
| 7 | NFC_GPIO | 3.3V |
| 8 | PD15 | 3.3V |
| 9 | FMU_NRST | 3.3V |
| 10 | GND | GND |

### USB — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | USB_JST_5V | 5.0V |
| 2 | USB_JST_EXT_N | 3.3V |
| 3 | USB_JST_EXT_P | 3.3V |
| 4 | GND | GND |

### POWER — 14-pin 2.00mm Molex [CLIK-Mate 502494](https://www.molex.com/en-us/part-list/502494)

Mating plug [5024391400](https://www.digikey.com/en/products/detail/molex/5024391400/2380427)

Pre-crimped wires [0797581014](https://www.digikey.com/en/products/detail/molex/0797581014/6346648)

`VBRICK1` and `VBRICK2` are ideal-diode ORed; see [Carrier Power Inputs](../../knowledge-base/carrier-power-inputs.md) for load sharing.

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | VIN | BAT |
| 2 | VBRICK1 | 5.0V |
| 3 | VBRICK1 | 5.0V |
| 4 | I2C1_SCL_PWR_EXT | 3.3V |
| 5 | I2C1_SDA_PWR_EXT | 3.3V |
| 6 | VBRICK2 | 5.0V |
| 7 | VBRICK2 | 5.0V |
| 8 | I2C2_SCL_BASE_PWR_EXT | 3.3V |
| 9 | I2C2_SDA_BASE_PWR_EXT | 3.3V |
| 10 | GND | GND |
| 11 | GND | GND |
| 12 | GND | GND |
| 13 | GND | GND |
| 14 | GND | GND |

### SPI — 11-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | VDD_5V_PERIPH | 5.0V |
| 2 | SPI6_SCK_EXT | 3.3V |
| 3 | SPI6_MISO_EXT | 3.3V |
| 4 | SPI6_MOSI_EXT | 3.3V |
| 5 | SPI6_nCS1_EXT | 3.3V |
| 6 | SPI6_nCS2_EXT | 3.3V |
| 7 | SPIX_nSYNC_EXT | 3.3V |
| 8 | SPI6_DRDY1_EXT | 3.3V |
| 9 | SPI6_DRDY2_EXT | 3.3V |
| 10 | SPI6_nRESET_EXT | 3.3V |
| 11 | GND | GND |

## Connectors and Cables

### Flight Controller IO and Payload IO — 40-pin Molex Pico-Clasp

Pico-Clasp 501189

[Connector - 5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524)

[Pre-crimped Wires 6"](https://www.digikey.com/en/products/detail/molex/0797581018/6564343)

[Pre-crimped Wires 12"](https://www.digikey.com/en/products/detail/molex/0797581019/6564344)

[Crimps](https://www.molex.com/en-us/part-list/501193)

### Power — 14-pin Molex CLIK-Mate

CLIK-Mate 502439

[Connector - 5024391400](https://www.digikey.com/en/products/detail/molex/5024391400/2380427)

[Pre-crimped Wires 6"](https://www.digikey.com/en/products/detail/molex/0797581014/6346648)

[Pre-crimped Wires 12"](https://www.digikey.com/en/products/detail/molex/0797581015/6592311)

[Crimps](https://www.digikey.com/en/products/detail/molex/5024380000/2421358)

## 3D Model and Case

| File | Contents |
|------|----------|
| [VOXL2\_RTK\_PAB\_CARRIER\_Rev\_2.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_VOXL2_RTK_PAB_Carrier/model/VOXL2_RTK_PAB_CARRIER_Rev_2.step) | Board, rev 2 |

All files: [ARK\_VOXL2\_RTK\_PAB\_Carrier in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_VOXL2_RTK_PAB_Carrier)
