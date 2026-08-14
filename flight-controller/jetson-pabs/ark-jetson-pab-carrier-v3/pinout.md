---
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/pinout.md
---

# Pinout

<figure><img src="../../../.gitbook/assets/Jetson PAB V3 Pinout Drawing Top.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Jetson PAB V3 Pinout Drawing Bottom.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Jetson PAB V3 Pintout Drawing Front.png" alt=""><figcaption></figcaption></figure>

### **Primary Avionics- 40 Pin** Pico-Clasp 501571

Mating plug [5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524)

Pre-crimped wires [0797581019](https://www.digikey.com/en/products/detail/molex/0797581019/6564344)

| Pin Number | Signal Name                    | Voltage          |
| ---------- | ------------------------------ | ---------------- |
| 1          | VDD\_5V\_SBUS\_RC              | 5.0V             |
| 2          | IO\_SBUS\_INPUT\_EXT           | 3.3V             |
| 3          | nSAFETY\_SWITCH\_IN\_EXT       | 3.3V             |
| 4          | GND                            | GND              |
| 5          | nSAFETY\_SWITCH\_LED\_OUT\_EXT | 3.3V             |
| 6          | TIM14\_CH1\_BUZZER\_1          | 24V (Open Drain) |
| 7          | GND                            | GND              |
| 8          | 3V3\_FMU                       | 3.3V (250mA)     |
| 9          | UART7\_TX\_TELEM1\_EXT         | 3.3V             |
| 10         | UART7\_CTS\_TELEM1\_EXT        | 3.3V             |
| 11         | UART7\_RX\_TELEM1\_EXT         | 3.3V             |
| 12         | UART7\_RTS\_TELEM1\_EXT        | 3.3V             |
| 13         | VDD\_5V\_HIPOWER               | 5.0V (1.5A)      |
| 14         | GND                            | GND              |
| 15         | VDD\_5V\_HIPOWER               | 5.0V (1.5A)      |
| 16         | GND                            | GND              |
| 17         | GND                            | GND              |
| 18         | USART1\_TX\_GPS1\_EXT          | 3.3V             |
| 19         | I2C1\_SCL\_GPS1\_EXT           | 3.3V             |
| 20         | USART1\_RX\_GPS1\_EXT          | 3.3V             |
| 21         | I2C1\_SDA\_GPS1\_EXT           | 3.3V             |
| 22         | VDD\_5V\_PERIPH                | 5.0V (1.5A)      |
| 23         | GND                            | GND              |
| 24         | GND                            | GND              |
| 25         | FMU\_CH1\_EXT                  | 3.3V             |
| 26         | FMU\_CH5\_EXT                  | 3.3V             |
| 27         | FMU\_CH2\_EXT                  | 3.3V             |
| 28         | FMU\_CH6\_EXT                  | 3.3V             |
| 29         | FMU\_CH3\_EXT                  | 3.3V             |
| 30         | FMU\_CH7\_EXT                  | 3.3V             |
| 31         | FMU\_CH4\_EXT                  | 3.3V             |
| 32         | FMU\_CH8\_EXT                  | 3.3V             |
| 33         | GND                            | GND              |
| 34         | VDD\_SERVO\_SENSE              | 9.9V Max         |
| 35         | CAN1\_P                        | 5.0V             |
| 36         | GND                            | GND              |
| 37         | CAN1\_N                        | 5.0V             |
| 38         | GND                            | GND              |
| 39         | GND                            | GND              |
| 40         | VDD\_5V\_PERIPH                | 5.0V (1.5A)      |

### **Secondary Avionics- 40 Pin** Pico-Clasp 501571

Mating plug [5011894010](https://www.digikey.com/en/products/detail/molex/5011894010/1531524)

Pre-crimped wires [0797581019](https://www.digikey.com/en/products/detail/molex/0797581019/6564344)

| Pin Number | Signal Name                | Voltage     |
| ---------- | -------------------------- | ----------- |
| 1          | VDD\_5V\_PERIPH            | 5.0V (1.5A) |
| 2          | SPI6\_DRDY1\_EXT           | 3.3V        |
| 3          | SPIX\_nSYNC\_EXT           | 3.3V        |
| 4          | GND                        | GND         |
| 5          | SPI6\_SCK\_EXT             | 3.3V        |
| 6          | SPI6\_MOSI\_EXT            | 3.3V        |
| 7          | GND                        | GND         |
| 8          | SPI6\_nCS1\_EXT            | 3.3V        |
| 9          | USART2\_TX\_TELEM3\_EXT    | 3.3V        |
| 10         | SPI6\_nRESET\_EXT          | 3.3V        |
| 11         | USART2\_RX\_TELEM3\_EXT    | 3.3V        |
| 12         | SPI6\_MISO\_EXT            | 3.3V        |
| 13         | VDD\_5V\_PERIPH            | 5.0V (1.5A) |
| 14         | GND                        | GND         |
| 15         | VDD\_5V\_SBUS\_RC          | 5.0V        |
| 16         | GND                        | GND         |
| 17         | GND                        | GND         |
| 18         | UART8\_TX\_GPS2\_EXT       | 3.3V        |
| 19         | I2C2\_SCL\_BASE\_GPS2\_EXT | 3.3V        |
| 20         | UART8\_RX\_GPS2\_EXT       | 3.3V        |
| 21         | I2C2\_SDA\_BASE\_GPS2\_EXT | 3.3V        |
| 22         | VDD\_5V\_PERIPH            | 5.0V (1.5A) |
| 23         | GND                        | GND         |
| 24         | GND                        | GND         |
| 25         | IO\_CH1\_EXT               | 3.3V        |
| 26         | IO\_CH5\_EXT               | 3.3V        |
| 27         | IO\_CH2\_EXT               | 3.3V        |
| 28         | IO\_CH6\_EXT               | 3.3V        |
| 29         | IO\_CH3\_EXT               | 3.3V        |
| 30         | IO\_CH7\_EXT               | 3.3V        |
| 31         | IO\_CH4\_EXT               | 3.3V        |
| 32         | IO\_CH8\_EXT               | 3.3V        |
| 33         | GND                        | GND         |
| 34         | NC                         | NC          |
| 35         | JCAN\_P                    | 5.0V        |
| 36         | GND                        | GND         |
| 37         | JCAN\_N                    | 5.0V        |
| 38         | GND                        | GND         |
| 39         | GND                        | GND         |
| 40         | VDD\_5V\_PERIPH            | 5.0V (1.5A) |

### **Pixhawk Payload Bus - 30 Pin 0.5mm Pitch** FFC

Mating cable [05-30-D-0304-A-4-06-4-T](https://www.digikey.com/en/products/detail/gct/05-30-D-0304-A-4-06-4-T/21266656)

| Pin Number | Signal Name             | Voltage     |
| ---------- | ----------------------- | ----------- |
| 1          | GND                     | GND         |
| 2          | UART4\_TX\_EXT          | 3.3V        |
| 3          | UART4\_RX\_EXT          | 3.3V        |
| 4          | GND                     | GND         |
| 5          | I2C3\_SDA\_EXT          | 3.3V        |
| 6          | I2C3\_SCL\_EXT          | 3.3V        |
| 7          | GND                     | GND         |
| 8          | CAN2\_P                 | 5.0V        |
| 9          | CAN2\_N                 | 5.0V        |
| 10         | GND                     | GND         |
| 11         | FMU\_CH7\_EXT           | 3.3V        |
| 12         | GPIO12\_EXT             | 1.8V        |
| 13         | FMU\_CH8\_EXT           | 3.3V        |
| 14         | GND                     | GND         |
| 15         | FMU\_CAP\_EXT           | 3.3V        |
| 16         | GND                     | GND         |
| 17         | ETH\_TX\_P              | 3.3V        |
| 18         | ETH\_TX\_N              | 3.3V        |
| 19         | GND                     | GND         |
| 20         | ETH\_RX\_P              | 3.3V        |
| 21         | ETH\_RX\_N              | 3.3V        |
| 22         | GND                     | GND         |
| 23         | GPIO01                  | 1.8V        |
| 24         | HUB\_USB3\_VBUS         | 5.0V (1.0A) |
| 25         | HUB\_USB3\_N            | 5.0V        |
| 26         | HUB\_USB3\_P            | 5.0V        |
| 27         | GND                     | GND         |
| 28         | VDD\_5V\_HIGHPOWER\_nEN | 3.3V        |
| 29         | VDD\_5V\_PERIPH\_nEN    | 3.3V        |
| 30         | GND                     | GND         |

### **Fan - 4 Pin PicoBlade**

| Pin Number | Signal Name     | Voltage |
| ---------- | --------------- | ------- |
| 1          | GND             | GND     |
| 2          | VDD\_5V\_PERIPH | 5.0V    |
| 3          | FAN\_TACH\_CON  | 5.0V    |
| 4          | FAN\_PWM\_Q\*   | 5.0V    |

### **Power 1 - 6 Pin** Micro-Lock PLUS 505567

Mating plug [5055650601](https://www.digikey.com/en/products/detail/molex/5055650601/7807030)

Pre-crimped wires [0797581149](https://www.digikey.com/en/products/detail/molex/0797581149/10483011)

| Pin Number | Signal Name         | Voltage |
| ---------- | ------------------- | ------- |
| 1          | VBRICK1             | 5.0V    |
| 2          | VBRICK1             | 5.0V    |
| 3          | I2C1\_SCL\_PWR\_EXT | 3.3V    |
| 4          | I2C1\_SDA\_PWR\_EXT | 3.3V    |
| 5          | GND                 | GND     |
| 6          | GND                 | GND     |

### **Power 2 - 6 Pin** Micro-Lock PLUS 505567

Mating plug [5055650601](https://www.digikey.com/en/products/detail/molex/5055650601/7807030)

Pre-crimped wires [0797581149](https://www.digikey.com/en/products/detail/molex/0797581149/10483011)

| Pin Number | Signal Name               | Voltage |
| ---------- | ------------------------- | ------- |
| 1          | VBRICK2                   | 5.0V    |
| 2          | VBRICK2                   | 5.0V    |
| 3          | I2C2\_SCL\_BASE\_PWR\_EXT | 3.3V    |
| 4          | I2C2\_SDA\_BASE\_PWR\_EXT | 3.3V    |
| 5          | GND                       | GND     |
| 6          | GND                       | GND     |

### **Power 3 - 6 Pin** Micro-Lock PLUS 505567

Mating plug [5055650601](https://www.digikey.com/en/products/detail/molex/5055650601/7807030)

Pre-crimped wires [0797581149](https://www.digikey.com/en/products/detail/molex/0797581149/10483011)

| Pin Number | Signal Name         | Voltage |
| ---------- | ------------------- | ------- |
| 1          | VBRICK3             | 5.0V    |
| 2          | VBRICK3             | 5.0V    |
| 3          | I2C3\_SCL\_PWR\_EXT | 3.3V    |
| 4          | I2C3\_SDA\_PWR\_EXT | 3.3V    |
| 5          | GND                 | GND     |
| 6          | GND                 | GND     |

#### CAM0/CSI0- 22 Pin 0.5mm FFC

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CSI0_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CSI0_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CSI0_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CSI0_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CSI0_CLK_N</td><td>1.2V</td></tr><tr><td>9</td><td>CSI0_CLK_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>CSI1_D0_N</td><td>1.2V</td></tr><tr><td>12</td><td>CSI1_D0_P</td><td>1.2V</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>CSI1_D1_N</td><td>1.2V</td></tr><tr><td>15</td><td>CSI1_D1_P</td><td>1.2V</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM0_PWDN_3V3</td><td>3.3V</td></tr><tr><td>18</td><td>CAM0_MCLK</td><td>1.8V</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>CAM0_SCL</td><td>3.3V</td></tr><tr><td>21</td><td>CAM0_SDA</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V</td><td>3.3V (1A)</td></tr></tbody></table>

#### CAM1/CSI2- 22 Pin 0.5mm FFC

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CSI2_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CSI2_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CSI2_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CSI2_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CSI2_CLK_N</td><td>1.2V</td></tr><tr><td>9</td><td>CSI2_CLK_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>CSI3_D0_N</td><td>1.2V</td></tr><tr><td>12</td><td>CSI3_D0_P</td><td>1.2V</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>CSI3_D1_N</td><td>1.2V</td></tr><tr><td>15</td><td>CSI3_D1_P</td><td>1.2V</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM1_PWDN_3V3</td><td>3.3V</td></tr><tr><td>18</td><td>CAM1_MCLK</td><td>1.8V</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>CAM1_SCL</td><td>3.3V</td></tr><tr><td>21</td><td>CAM1_SDA</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V</td><td>3.3V (1A)</td></tr></tbody></table>

#### USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>USBSS1_VBUS</td><td>5.0V</td></tr><tr><td>2</td><td>HUB_USB1_N</td><td>3.3V</td></tr><tr><td>3</td><td>HUB_USB1_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>USBSS2_VBUS</td><td>5.0V</td></tr><tr><td>2</td><td>HUB_USB2_N</td><td>3.3V</td></tr><tr><td>3</td><td>HUB_USB2_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### UART2 - 6 Pin JST-SH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3V3</td><td>3.3V</td></tr><tr><td>2</td><td>UART2_TXD_3V3</td><td>3.3V</td></tr><tr><td>3</td><td>UART2_RXD_3V3</td><td>3.3V</td></tr><tr><td>4</td><td>NC</td><td>NC</td></tr><tr><td>5</td><td>NC</td><td>NC</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### ETH - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>EXT_ETH_RX_N</td><td>3.3V</td></tr><tr><td>2</td><td>EXT_ETH_RX_P</td><td>3.3V</td></tr><tr><td>3</td><td>EXT_ETH_TX_N</td><td>3.3V</td></tr><tr><td>4</td><td>EXT_ETH_TX_P</td><td>3.3V</td></tr></tbody></table>

#### Flight Controller Debug - 10 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3V3_FMU</td><td>3.3V</td></tr><tr><td>2</td><td>USART3_TX_DEBUG</td><td>3.3V</td></tr><tr><td>3</td><td>USART3_RX_DEBUG</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>SPI6_SCK_EXTERNAL1</td><td>3.3V</td></tr><tr><td>7</td><td>NFC_GPIO</td><td>3.3V</td></tr><tr><td>8</td><td>PD15</td><td>3.3V</td></tr><tr><td>9</td><td>FMU_NRST</td><td>3.3V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr></tbody></table>

#### IO MCU Debug - 10 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3V3_IO_MCU</td><td>3.3V</td></tr><tr><td>2</td><td>IO_USART1_TX_DEBUG</td><td>3.3V</td></tr><tr><td>3</td><td>NC</td><td>NC</td></tr><tr><td>4</td><td>IO_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>IO_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>IO_SWO</td><td>3.3V</td></tr><tr><td>7</td><td>IO_SPARE_GPIO1</td><td>3.3V</td></tr><tr><td>8</td><td>IO_SPARE_GPIO2</td><td>3.3V</td></tr><tr><td>9</td><td>IO_nRST</td><td>3.3V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr></tbody></table>
