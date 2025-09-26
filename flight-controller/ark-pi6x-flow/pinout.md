# Pinout

<figure><img src="../../.gitbook/assets/Pi6X Flow Wireframe.png" alt=""><figcaption><p>ARK Pi6X Flow Connector Locations</p></figcaption></figure>

{% file src="../../.gitbook/assets/Pi6X Flow Wireframe.png" %}

#### UART Port Mapping

<table><thead><tr><th>UART</th><th width="187">Connector</th><th>PX4 name</th><th>Nuttx tty</th></tr></thead><tbody><tr><td>USART1</td><td>GPS</td><td>GPS1</td><td>/dev/ttyS0</td></tr><tr><td>USART3</td><td>Debug</td><td>Debug</td><td>/dev/ttyS1</td></tr><tr><td>UART4</td><td>UART4</td><td>Telem4</td><td>/dev/ttyS2</td></tr><tr><td>UART5</td><td>none (MCU to Pi)</td><td>Telem2</td><td>/dev/ttyS3</td></tr><tr><td>USART6</td><td>RC</td><td>USART6</td><td>/dev/ttyS4</td></tr><tr><td>UART7</td><td>Telem1</td><td>UART7</td><td>/dev/ttyS5</td></tr></tbody></table>

#### PWM + UART4 - 11 Pin JST-GH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>FMU_CH1_EXT</td><td>3.3V</td></tr><tr><td>2</td><td>FMU_CH2_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>FMU_CH3_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_CH4_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_CH5_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>FMU_CH6_EXT</td><td>3.3V</td></tr><tr><td>7</td><td>FMU_CH7_EXT</td><td>3.3V</td></tr><tr><td>8</td><td>FMU_CH8_EXT</td><td>3.3V</td></tr><tr><td>9</td><td>UART4_TX_EXT</td><td>3.3V</td></tr><tr><td>10</td><td>UART4_RX_EXT</td><td>3.3V</td></tr><tr><td>11</td><td>GND</td><td>GND</td></tr></tbody></table>

#### RC - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_SBUS_RC</td><td>5.0V</td></tr><tr><td>2</td><td>USART6_RX_IN_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>USART6_TX_OUTPUT_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_HIPOWER</td><td>5.0V</td></tr><tr><td>2</td><td>CAN1_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN1_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### GPS - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_HIPOWER</td><td>5.0V</td></tr><tr><td>2</td><td>USART1_TX_GPS1_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>USART1_RX_GPS1_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>I2C1_SCL_GPS1_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>I2C1_SDA_GPS1_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Telem1 - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_HIPOWER</td><td>5.0V</td></tr><tr><td>2</td><td>UART7_TX_TELEM1_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>UART7_RX_TELEM1_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>UART7_CTS_TELEM1_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>UART7_RTS_TELEM1_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Flight Controller Debug - 10 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3V3_FMU</td><td>3.3V</td></tr><tr><td>2</td><td>USART3_TX_DEBUG</td><td>3.3V</td></tr><tr><td>3</td><td>USART3_RX_DEBUG</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>SPI6_SCK_EXTERNAL1</td><td>3.3V</td></tr><tr><td>7</td><td>NFC_GPIO</td><td>3.3V</td></tr><tr><td>8</td><td>PD15</td><td>3.3V</td></tr><tr><td>9</td><td>FMU_NRST</td><td>3.3V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi I2C1 - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V</td><td>5.0V</td></tr><tr><td>2</td><td>I2C1_SCL_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>I2C1_SDA_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi UART3 - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V</td><td>5.0V</td></tr><tr><td>2</td><td>UART3_TX_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>UART3_RX_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>UART3_CTS_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>UART3_RTS_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi ETH - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>ETH_RD_N</td><td>3.3V</td></tr><tr><td>2</td><td>ETH_RD_P</td><td>3.3V</td></tr><tr><td>3</td><td>ETH_TD_N</td><td>3.3V</td></tr><tr><td>4</td><td>ETH_TD_P</td><td>3.3V</td></tr></tbody></table>

#### Pi LED Strip - 8 Pin JST-GH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V</td><td>5.0V</td></tr><tr><td>2</td><td>5.0V</td><td>5.0V</td></tr><tr><td>3</td><td>GPIO12_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>GPIO16_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>GPIO17_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GPIO20_EXT</td><td>3.3V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi GPIO - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V</td><td>5.0V</td></tr><tr><td>2</td><td>GPIO21_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>GPIO22_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>GPIO23_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>GPIO24_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi Fan - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>5.0V</td><td>5.0V</td></tr><tr><td>3</td><td>FAN_TACH_CON</td><td>5.0V</td></tr><tr><td>4</td><td>FAN_PWM_Q*</td><td>5.0V</td></tr></tbody></table>

#### Pi Console - 6 Pin JST-SH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V_RPI</td><td>3.3V</td></tr><tr><td>2</td><td>CONSOLE_TXD0</td><td>3.3V</td></tr><tr><td>3</td><td>CONSOLE_RXD0</td><td>3.3V</td></tr><tr><td>4</td><td>NC</td><td>NC</td></tr><tr><td>5</td><td>NC</td><td>NC</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VBUS2_FLT</td><td>5.0V</td></tr><tr><td>2</td><td>USB2_EXT_N</td><td>3.3V</td></tr><tr><td>3</td><td>USB2_EXT_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Pi USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VBUS4_FLT</td><td>5.0V</td></tr><tr><td>2</td><td>USB4_EXT_N</td><td>3.3V</td></tr><tr><td>3</td><td>USB4_EXT_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAM0 - 22 Pin 0.5mm FFC 0545482271

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CAM0_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CAM0_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CAM0_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CAM0_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CAM0_C_N</td><td>1.2V</td></tr><tr><td>9</td><td>CAM0_C_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>NC</td><td>NC</td></tr><tr><td>12</td><td>NC</td><td>NC</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>NC</td><td>NC</td></tr><tr><td>15</td><td>NC</td><td>NC</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM_GPIO</td><td>3.3V</td></tr><tr><td>18</td><td>NC</td><td>NC</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>ID_SC</td><td>3.3V</td></tr><tr><td>21</td><td>ID_SD</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V_RPI</td><td>3.3V</td></tr></tbody></table>

#### CAM1 - 22 Pin 0.5mm FFC 0545482271

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CAM1_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CAM1_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CAM1_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CAM1_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CAM1_C_N</td><td>1.2V</td></tr><tr><td>9</td><td>CAM1_C_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>CAM1_D2_N</td><td>1.2V</td></tr><tr><td>12</td><td>CAM1_D2_P</td><td>1.2V</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>CAM1_D3_N</td><td>1.2V</td></tr><tr><td>15</td><td>CAM1_D3_P</td><td>1.2V</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM_GPIO</td><td>3.3V</td></tr><tr><td>18</td><td>NC</td><td>NC</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>SCL0</td><td>3.3V</td></tr><tr><td>21</td><td>SDA0</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V_RPI</td><td>3.3V</td></tr></tbody></table>
