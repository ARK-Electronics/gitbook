---
cover: ../.gitbook/assets/IMG_5106_edited.JPG
coverY: 2.777482269503546
---

# ARK X20 RTK GPS

Please read through the PX4 Documentation for DroneCAN GPS parameter configuration.

{% embed url="https://docs.px4.io/main/en/dronecan/#gps" %}

## Firmware

Follow the steps for updating the firmware through the flight controller.&#x20;

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../.gitbook/assets/89-1.16.47e04790.uavcan.bin" %}
ARK X20 GPS Firmware
{% endfile %}

{% file src="../.gitbook/assets/ark_x20-gps_canbootloader.bin" %}
ARK X20 GPS Bootloader
{% endfile %}

## Release Notes

* 89-1.16.47e04790 - 2025-11-17
  * Initial release

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### GPS UART2 + Timepulse - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>TXD2</td><td>3.3V</td></tr><tr><td>2</td><td>RXD2</td><td>3.3V</td></tr><tr><td>3</td><td>TIMEPULSE</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### I2C2 - 4 Pin JST-GH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>I2C2_SCL</td><td>3.3V</td></tr><tr><td>3</td><td>I2C2_SDA</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

## 3D Model

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_X20\_GPS](https://github.com/ARK-Electronics/ARK_X20_GPS)
