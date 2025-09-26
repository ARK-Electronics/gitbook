---
cover: ../../.gitbook/assets/ark_rtk_gps_1.jpg
coverY: 0
---

# ARK RTK GPS

Find most up to date documentation in the PX4 Documentation [https://docs.px4.io/main/en/dronecan/ark\_rtk\_gps.html](https://docs.px4.io/main/en/dronecan/ark_rtk_gps.html)

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_RTK\_GPS](https://github.com/ARK-Electronics/ARK_RTK_GPS)

## Firmware

Follow the steps for updating the firmware through the flight controller.&#x20;

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../../.gitbook/assets/82-1.16.e68afe1e.uavcan.bin" %}
ARK RTK GPS Firmware
{% endfile %}

## Release Notes

* 82-1.16.e68afe1e - 2025-2-12
  * Disable mag bias estimator by default

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### F9P UART2 - 3 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>F9P_TXD2</td><td>3.3V</td></tr><tr><td>2</td><td>F9P_RXD2</td><td>3.3V</td></tr><tr><td>3</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
