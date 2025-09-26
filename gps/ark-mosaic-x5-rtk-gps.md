---
cover: ../.gitbook/assets/IMG_2391_edited (Large).JPG
coverY: 0
---

# ARK MOSAIC-X5 RTK GPS

## Firmware

Follow the steps for updating the firmware through the flight controller.&#x20;

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../.gitbook/assets/84-1.16.3c45b562.uavcan.bin" %}
ARK Mosaic-X5 GPS Firmware
{% endfile %}

{% file src="../.gitbook/assets/ark_septentrio-gps_canbootloader.bin" %}
ARK Mosaic-X5 GPS Bootloader
{% endfile %}

## Release Notes

* 84-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 84-1.15.6dea2ce5 - 2025-2-12
  * Disable mag bias estimator by default

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USB C

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>2, 11</td><td>VBUS</td><td>5.0V</td></tr><tr><td>5, 8</td><td>USB_N</td><td>3.3V</td></tr><tr><td>6,7</td><td>USB_P</td><td>3.3V</td></tr><tr><td>1,12</td><td>GND</td><td>GND</td></tr></tbody></table>

#### GPS UART2 + Timepulse - 5 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>TXD2</td><td>3.3V</td></tr><tr><td>2</td><td>RXD2</td><td>3.3V</td></tr><tr><td>3</td><td>TIMEPULSE</td><td>3.3V</td></tr><tr><td>4</td><td>GP1</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USART3/I2C2 - 6 Pin JST-GH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>USART3_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART3_RX</td><td>3.3V</td></tr><tr><td>4</td><td>I2C2_SCL</td><td>3.3V</td></tr><tr><td>5</td><td>I2C2_SDA</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

## 3D Model

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_MOSAIC-X5\_GPS](https://github.com/ARK-Electronics/ARK_MOSAIC-X5_GPS)
