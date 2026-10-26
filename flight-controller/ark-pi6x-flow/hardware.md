# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Flight controller | ARKV6X: [STM32H743](https://www.st.com/en/microcontrollers-microprocessors/stm32h743ii.html), 480 MHz, 2 MB flash, 1 MB RAM |
| IMUs | Dual [Invensense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), heated |
| Barometer | [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp390/) |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Power monitor | [TI INA226](https://www.ti.com/product/INA226) voltage and current monitor |
| Optical flow (Pi6X Flow only) | [PixArt PAW3902](https://www.pixart.com/products-detail/93/PAW3902JF-TXQT) |
| Distance sensor (Pi6X Flow only) | [Broadcom AFBR-S50LV85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lv85d), 30 m. Not supported in ArduPilot |
| Compute module | Raspberry Pi Compute Module 4; CM4 Lite boots from the microSD slot. Compute Module 5 with the [differences below](#compute-module-5) |
| Flight controller interfaces | TELEM1, RC input, 8 PWM outputs (DShot capable), UART4, GPS (UART, I2C), CAN, buzzer, debug (SWD, UART console), microSD |
| Pi interfaces | Micro HDMI, Ethernet, USB-C host, 2× USB JST-GH, 2× MIPI CSI (22-pin FFC), programming micro USB, I2C, UART, LED strip GPIO, GPIO, console, CPU fan |
| Power | 5.5–25.2 V (2S–6S) battery input |
| ESC mounting | 4-in-1 ESC, 30 × 30 mm |
| Dimensions | 91.5 × 56 mm, without compute module and ESC |
| Weight | 41 g without compute module, SD card and ESC; 53 g with CM4 and SD card |
| Compliance | USA built, NDAA compliant, [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list) |

## Compute Module 5

The board was designed for the CM4. With a CM5:

| | CM4 | CM5 |
|---|---|---|
| Telem2 to the flight controller | UART4, `/dev/ttyAMA4` | UART3, `/dev/ttyAMA3` |
| Pi UART3 connector | UART3, `/dev/ttyAMA3` | UART2, `/dev/ttyAMA2` |
| Cameras | CAM0 and CAM1 | CAM1 only, as `cam0` in `config.txt`. The CM5 uses the CM4's CAM0 pins for USB 3.0 |
| USB 3.0 | None | Not wired to any connector |

The `config.txt` for each module is in [After Flashing, Before Installing](flashing-guide/after-flashing-before-installing.md).

## USB

The compute module's USB 2.0 port goes through a mux to either the programming micro USB or an onboard USB hub. The hub feeds the flight controller, the USB-C port and both USB JST-GH ports.

{% hint style="warning" %}
The hub is full speed only (12 Mbps, USB 1.1) with either compute module, so every device behind it is limited to 12 Mbps.
{% endhint %}

While a cable is plugged into the micro USB, the compute module switches to that port and the hub is disconnected. Reboot after unplugging it.

## Pinout

<figure><img src="../../.gitbook/assets/Pi6X Flow Wireframe.png" alt=""><figcaption><p>ARK Pi6X Flow connector locations</p></figcaption></figure>

{% file src="../../.gitbook/assets/Pi6X Flow Wireframe.png" %}

### PWM + UART4 — 11-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | FMU_CH1_EXT | 3.3V |
| 2 | FMU_CH2_EXT | 3.3V |
| 3 | FMU_CH3_EXT | 3.3V |
| 4 | FMU_CH4_EXT | 3.3V |
| 5 | FMU_CH5_EXT | 3.3V |
| 6 | FMU_CH6_EXT | 3.3V |
| 7 | FMU_CH7_EXT | 3.3V |
| 8 | FMU_CH8_EXT | 3.3V |
| 9 | UART4_TX_EXT | 3.3V |
| 10 | UART4_RX_EXT | 3.3V |
| 11 | GND | GND |

### RC — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VDD_5V_SBUS_RC | 5.0V |
| 2 | USART6_RX_IN_EXT | 3.3V |
| 3 | USART6_TX_OUTPUT_EXT | 3.3V |
| 4 | GND | GND |

### CAN — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VDD_5V_HIPOWER | 5.0V |
| 2 | CAN1_P | 5.0V |
| 3 | CAN1_N | 5.0V |
| 4 | GND | GND |

### GPS — 6-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VDD_5V_HIPOWER | 5.0V |
| 2 | USART1_TX_GPS1_EXT | 3.3V |
| 3 | USART1_RX_GPS1_EXT | 3.3V |
| 4 | I2C1_SCL_GPS1_EXT | 3.3V |
| 5 | I2C1_SDA_GPS1_EXT | 3.3V |
| 6 | GND | GND |

### TELEM1 — 6-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VDD_5V_HIPOWER | 5.0V |
| 2 | UART7_TX_TELEM1_EXT | 3.3V |
| 3 | UART7_RX_TELEM1_EXT | 3.3V |
| 4 | UART7_CTS_TELEM1_EXT | 3.3V |
| 5 | UART7_RTS_TELEM1_EXT | 3.3V |
| 6 | GND | GND |

### Flight Controller Debug — 10-pin JST-SH

| Pin | Signal | Voltage |
|---|---|---|
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

### Pi I2C1 — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | 5.0V | 5.0V |
| 2 | I2C1_SCL_EXT | 3.3V |
| 3 | I2C1_SDA_EXT | 3.3V |
| 4 | GND | GND |

### Pi UART3 — 6-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | 5.0V | 5.0V |
| 2 | UART3_TX_EXT | 3.3V |
| 3 | UART3_RX_EXT | 3.3V |
| 4 | UART3_CTS_EXT | 3.3V |
| 5 | UART3_RTS_EXT | 3.3V |
| 6 | GND | GND |

### Pi ETH — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | ETH_RD_N | 3.3V |
| 2 | ETH_RD_P | 3.3V |
| 3 | ETH_TD_N | 3.3V |
| 4 | ETH_TD_P | 3.3V |

### Pi LED Strip — 8-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | 5.0V | 5.0V |
| 2 | 5.0V | 5.0V |
| 3 | GPIO12_EXT | 3.3V |
| 4 | GPIO16_EXT | 3.3V |
| 5 | GPIO17_EXT | 3.3V |
| 6 | GPIO20_EXT | 3.3V |
| 7 | GND | GND |
| 8 | GND | GND |

### Pi GPIO — 6-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | 5.0V | 5.0V |
| 2 | GPIO21_EXT | 3.3V |
| 3 | GPIO22_EXT | 3.3V |
| 4 | GPIO23_EXT | 3.3V |
| 5 | GPIO24_EXT | 3.3V |
| 6 | GND | GND |

### Pi Fan — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | GND | GND |
| 2 | 5.0V | 5.0V |
| 3 | FAN_TACH_CON | 5.0V |
| 4 | FAN_PWM_Q* | 5.0V |

### Pi Console — 6-pin JST-SH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | 3.3V_RPI | 3.3V |
| 2 | CONSOLE_TXD0 | 3.3V |
| 3 | CONSOLE_RXD0 | 3.3V |
| 4 | NC | NC |
| 5 | NC | NC |
| 6 | GND | GND |

### Pi USB (hub port 2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VBUS2_FLT | 5.0V |
| 2 | USB2_EXT_N | 3.3V |
| 3 | USB2_EXT_P | 3.3V |
| 4 | GND | GND |

### Pi USB (hub port 4) — 4-pin JST-GH

| Pin | Signal | Voltage |
|---|---|---|
| 1 | VBUS4_FLT | 5.0V |
| 2 | USB4_EXT_N | 3.3V |
| 3 | USB4_EXT_P | 3.3V |
| 4 | GND | GND |

### CAM0 — 22-pin 0.5 mm FFC (Molex 0545482271)

| Pin | Signal | Voltage |
|---|---|---|
| 1 | GND | GND |
| 2 | CAM0_D0_N | 1.2V |
| 3 | CAM0_D0_P | 1.2V |
| 4 | GND | GND |
| 5 | CAM0_D1_N | 1.2V |
| 6 | CAM0_D1_P | 1.2V |
| 7 | GND | GND |
| 8 | CAM0_C_N | 1.2V |
| 9 | CAM0_C_P | 1.2V |
| 10 | GND | GND |
| 11 | NC | NC |
| 12 | NC | NC |
| 13 | GND | GND |
| 14 | NC | NC |
| 15 | NC | NC |
| 16 | GND | GND |
| 17 | CAM_GPIO | 3.3V |
| 18 | NC | NC |
| 19 | GND | GND |
| 20 | ID_SC | 3.3V |
| 21 | ID_SD | 3.3V |
| 22 | 3.3V_RPI | 3.3V |

### CAM1 — 22-pin 0.5 mm FFC (Molex 0545482271)

| Pin | Signal | Voltage |
|---|---|---|
| 1 | GND | GND |
| 2 | CAM1_D0_N | 1.2V |
| 3 | CAM1_D0_P | 1.2V |
| 4 | GND | GND |
| 5 | CAM1_D1_N | 1.2V |
| 6 | CAM1_D1_P | 1.2V |
| 7 | GND | GND |
| 8 | CAM1_C_N | 1.2V |
| 9 | CAM1_C_P | 1.2V |
| 10 | GND | GND |
| 11 | CAM1_D2_N | 1.2V |
| 12 | CAM1_D2_P | 1.2V |
| 13 | GND | GND |
| 14 | CAM1_D3_N | 1.2V |
| 15 | CAM1_D3_P | 1.2V |
| 16 | GND | GND |
| 17 | CAM_GPIO | 3.3V |
| 18 | NC | NC |
| 19 | GND | GND |
| 20 | SCL0 | 3.3V |
| 21 | SDA0 | 3.3V |
| 22 | 3.3V_RPI | 3.3V |

## Serial Port Mapping

| UART | Connector | PX4 | NuttX device | ArduPilot |
|------|-----------|-----|--------------|-----------|
| USART1 | GPS | GPS1 | `/dev/ttyS0` | SERIAL3 |
| USART3 | Debug | Debug console | `/dev/ttyS1` | — |
| UART4 | PWM + UART4 | TELEM4 | `/dev/ttyS2` | SERIAL4 |
| UART5 | None, wired to the Pi | TELEM2 | `/dev/ttyS3` | SERIAL2 |
| USART6 | RC | RC | `/dev/ttyS4` | SERIAL5 |
| UART7 | TELEM1 | TELEM1 | `/dev/ttyS5` | SERIAL1 |

ArduPilot's SERIAL0 is the USB connection to the Pi.

## Block Diagram

<figure><img src="../../.gitbook/assets/ARK Pi6X Flow Block Diagram.png" alt=""><figcaption><p>Block diagram</p></figcaption></figure>

{% file src="../../.gitbook/assets/ARK Pi6X Flow Block Diagram.pdf" %}

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK-Pi6X-Flow-Rev-2.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Pi6X/model/ARK-Pi6X-Flow-Rev-2.0.step) | Board model |
| [ARK-Pi6X-Flow-Rev-2.0-with-Sensor-FOV.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Pi6X/model/ARK-Pi6X-Flow-Rev-2.0-with-Sensor-FOV.step) | Board model with the flow and distance sensor fields of view |

All files: [ARK\_Pi6X in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Pi6X)
