# Pinout

<figure><img src="../../.gitbook/assets/Pinout Top.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Pinout Bottom.png" alt=""><figcaption></figcaption></figure>

{% file src="../../.gitbook/assets/Pinout Drawing.pdf" %}

#### BAT IN - XT60

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>+</td><td>VBAT_IN</td><td>5.5V - 75V</td></tr><tr><td>-</td><td>GND</td><td>GND</td></tr></tbody></table>

#### BAT OUT - XT30

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>+</td><td>VBAT_OUT</td><td>VBAT_IN</td></tr><tr><td>-</td><td>GND</td><td>GND</td></tr></tbody></table>

#### 5V IN - 6 Pin Molex CLIK-Mate

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VBRICK1</td><td>5.0V</td></tr><tr><td>2</td><td>VBRICK1</td><td>5.0V</td></tr><tr><td>3</td><td>I2C0_SCL_PWR_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>I2C0_SDA_PWR_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Fan - 4 Pin PicoBlade

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>VDD_5V_JPERIPH</td><td>5.0V</td></tr><tr><td>3</td><td>FAN_TACH_CON</td><td>5.0V</td></tr><tr><td>4</td><td>FAN_PWM_Q*</td><td>5.0V</td></tr></tbody></table>

#### UART0/GPIO - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH</td><td>5.0V</td></tr><tr><td>2</td><td>UART0_TXD_3V3</td><td>3.3V</td></tr><tr><td>3</td><td>UART0_RXD_3V3</td><td>3.3V</td></tr><tr><td>4</td><td>UART0_CTS_3V3</td><td>3.3V</td></tr><tr><td>5</td><td>UART0_RTS_3V3</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### UART1/GPIO - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH_2</td><td>5.0V</td></tr><tr><td>2</td><td>UART1_TXD_3V3</td><td>3.3V</td></tr><tr><td>3</td><td>UART1_RXD_3V3</td><td>3.3V</td></tr><tr><td>4</td><td>UART1_CTS_3V3</td><td>3.3V</td></tr><tr><td>5</td><td>UART1_RTS_3V3</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### UART2/I2C0 - 6 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH_2</td><td>5.0V</td></tr><tr><td>2</td><td>UART2_TXD_EXT</td><td>3.3V</td></tr><tr><td>3</td><td>UART2_RXD_EXT</td><td>3.3V</td></tr><tr><td>4</td><td>I2C0_SCL_EXT</td><td>3.3V</td></tr><tr><td>5</td><td>I2C0_SDA_EXT</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAM1/CSI2- 22 Pin 0.5mm FFC

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CSI2_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CSI2_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CSI2_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CSI2_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CSI2_CLK_N</td><td>1.2V</td></tr><tr><td>9</td><td>CSI2_CLK_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>CSI3_D0_N</td><td>1.2V</td></tr><tr><td>12</td><td>CSI3_D0_P</td><td>1.2V</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>CSI3_D1_N</td><td>1.2V</td></tr><tr><td>15</td><td>CSI3_D1_P</td><td>1.2V</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM1_PWDN_3V3</td><td>3.3V</td></tr><tr><td>18</td><td>CAM1_MCLK</td><td>1.8V</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>CAM1_SCL</td><td>3.3V</td></tr><tr><td>21</td><td>CAM1_SDA</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V</td><td>3.3V (1A)</td></tr></tbody></table>

#### CAM0/CSI0- 22 Pin 0.5mm FFC

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>GND</td><td>GND</td></tr><tr><td>2</td><td>CSI1_D0_N</td><td>1.2V</td></tr><tr><td>3</td><td>CSI1_D0_P</td><td>1.2V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr><tr><td>5</td><td>CSI1_D1_N</td><td>1.2V</td></tr><tr><td>6</td><td>CSI1_D1_P</td><td>1.2V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr><tr><td>8</td><td>CSI1_CLK_N</td><td>1.2V</td></tr><tr><td>9</td><td>CSI1_CLK_P</td><td>1.2V</td></tr><tr><td>10</td><td>GND</td><td>GND</td></tr><tr><td>11</td><td>CSI0_D0_N</td><td>1.2V</td></tr><tr><td>12</td><td>CSI0_D0_P</td><td>1.2V</td></tr><tr><td>13</td><td>GND</td><td>GND</td></tr><tr><td>14</td><td>CSI0_D1_N</td><td>1.2V</td></tr><tr><td>15</td><td>CSI0_D1_P</td><td>1.2V</td></tr><tr><td>16</td><td>GND</td><td>GND</td></tr><tr><td>17</td><td>CAM0_PWDN_3V3</td><td>3.3V</td></tr><tr><td>18</td><td>CAM0_MCLK</td><td>1.8V</td></tr><tr><td>19</td><td>GND</td><td>GND</td></tr><tr><td>20</td><td>CAM0_SCL</td><td>3.3V</td></tr><tr><td>21</td><td>CAM0_SDA</td><td>3.3V</td></tr><tr><td>22</td><td>3.3V</td><td>3.3V (1A)</td></tr></tbody></table>

#### SPI/GPIO - 7 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH</td><td>5.0V</td></tr><tr><td>2</td><td>SPI0_MOSI_3V3</td><td>3.3V</td></tr><tr><td>3</td><td>SPI0_SCK_3V3</td><td>3.3V</td></tr><tr><td>4</td><td>SPI0_MISO_3V3</td><td>3.3V</td></tr><tr><td>5</td><td>SPI0_CS0n_3V3</td><td>3.3V</td></tr><tr><td>6</td><td>SPI0_CS1n_3V3</td><td>3.3V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr></tbody></table>

#### I2S/GPIO - 7 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH_2</td><td>5.0V</td></tr><tr><td>2</td><td>I2S0_DOUT_3V3</td><td>3.3V</td></tr><tr><td>3</td><td>I2S0_DIN_3V3</td><td>3.3V</td></tr><tr><td>4</td><td>I2S0_LRCLK_3V3</td><td>3.3V</td></tr><tr><td>5</td><td>I2S0_SCLK_3V3</td><td>3.3V</td></tr><tr><td>6</td><td>AUD_MCLK_3V3</td><td>3.3V</td></tr><tr><td>7</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VDD_5V_JPERIPH</td><td>5.0V</td></tr><tr><td>2</td><td>JCAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>JCAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>USB1_VBUS</td><td>5.0V</td></tr><tr><td>2</td><td>HUB_USB1_N</td><td>3.3V</td></tr><tr><td>3</td><td>HUB_USB1_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USB - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>USB3_VBUS</td><td>5.0V</td></tr><tr><td>2</td><td>HUB_USB3_N</td><td>3.3V</td></tr><tr><td>3</td><td>HUB_USB3_P</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### PCIE - 16 Pin FFC 5051101692

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V_PCIE_FFC</td><td>5.0V</td></tr><tr><td>2</td><td>5V_PCIE_FFC</td><td>5.0V</td></tr><tr><td>3</td><td>GND</td><td>GND</td></tr><tr><td>4</td><td>PCIE2_CLK_P</td><td>1.0V</td></tr><tr><td>5</td><td>PCIE2_CLK_N</td><td>1.0V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr><tr><td>7</td><td>PCIE2_RX0_P</td><td>1.0V</td></tr><tr><td>8</td><td>PCIE2_RX0_N</td><td>1.0V</td></tr><tr><td>9</td><td>GND</td><td>GND</td></tr><tr><td>10</td><td>PCIE2_TX0_P</td><td>1.0V</td></tr><tr><td>11</td><td>PCIE2_TX0_N</td><td>1.0V</td></tr><tr><td>12</td><td>GND</td><td>GND</td></tr><tr><td>13</td><td>PCIE2_PWR_EN_3V3</td><td>3.3V</td></tr><tr><td>14</td><td>PCIE_WAKE</td><td>3.3V</td></tr><tr><td>15</td><td>PCIE2_CLKREQ</td><td>3.3V</td></tr><tr><td>16</td><td>PCIE2_RST*</td><td>3.3V</td></tr></tbody></table>
