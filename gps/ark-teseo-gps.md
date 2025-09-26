---
cover: ../.gitbook/assets/IMG_2267_edited (Large).JPG
coverY: -10
---

# ARK TESEO GPS

## PX4 EKF Parameters

The ST Teseo-LIV4F can report slightly higher speed accuracy values than the default [EKF2\_REQ\_SACC](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_REQ_SACC) parameter, causing PX4 to reject GPS fusion. The default is 0.5m/s. Increasing this to 1.5-2.0m/s is recommended.

## Firmware

Follow the steps for updating the firmware through the flight controller. The firmware will now automatically update the LIV4F GPS module firmware.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../.gitbook/assets/86-1.16.3c45b562.uavcan.bin" %}
ARK Teseo GPS Firmware
{% endfile %}

{% file src="../.gitbook/assets/ark_teseo-gps_canbootloader.bin" %}
ARK Teseo GPS Bootloader
{% endfile %}

## Release Notes

* 86-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 86-1.15.b4c24e95 - 2025-6-13
  * Update to STA8041\_LIV4F\_PVT\_STD\_4\_6\_8\_5\_10\_UPG [Teseo Firmware](https://www.st.com/en/embedded-software/teseo-liv4fsw.html)
* 86-1.15.6616d230 - 2025-2-26
  * Update to STA8041\_LIV4F\_PVT\_STD\_4\_6\_8\_5\_9\_UPG [Teseo Firmware](https://www.st.com/en/embedded-software/teseo-liv4fsw.html)
  * Add TESEO\_\* parameters to configure constellations
  * Default to GPS + GLONASS + BeiDou + Galileo
    * Note that only 4 constellations can be enabled at a time
* 86-1.15.1895b31a - 2025-2-12
  * Disable mag bias estimator by default
* 86-1.15.14443827 - 2025-2-5
  * Update to STA8041\_LIV4F\_PVT\_STD\_4\_6\_8\_5\_8\_UPG [Teseo Firmware](https://www.st.com/en/embedded-software/teseo-liv4fsw.html)
  * Fix speed accuracy reporting
  * Fix EPH reporting
* 86-1.15.37fb6452 - 2024-11-11
  * Update to STA8041\_LIV4F\_PVT\_STD\_4\_6\_7\_5\_7\_UPG [Teseo Firmware](https://www.st.com/en/embedded-software/teseo-liv4fsw.html)
  * Implement automatic LIV4F updating within the driver
  * Fix speed accuracy reporting

## 3D Model

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_TESEO\_GPS](https://github.com/ARK-Electronics/ARK_TESEO_GPS)

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### I2C + Timepulse - 5 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>I2C2_SCL</td><td>3.3V</td></tr><tr><td>3</td><td>I2C2_SDA</td><td>3.3V</td></tr><tr><td>4</td><td>TIMEPULSE</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
