---
cover: ../../.gitbook/assets/IMG_5106_edited.JPG
coverY: 2.777482269503546
---

# ARK X20 RTK GPS

[ARK X20 RTK GPS](https://arkelectron.com/product/ark-x20-rtk-gps/)

The ARK X20 RTK GPS is built around the u-blox ZED-X20P all-band (L1/L2/L5) RTK GNSS module, with an onboard magnetometer, barometer, IMU, safety button, and buzzer.

Find additional documentation at [https://docs.px4.io/main/en/dronecan/ark\_x20\_rtk\_gps](https://docs.px4.io/main/en/dronecan/ark_x20_rtk_gps)

## Firmware

Follow the steps for updating the firmware through the flight controller — see [Firmware Update](px4-instructions.md#firmware-update) in the PX4 instructions.

If the node does not appear on the CAN bus — for example after a bad flash that erased the bootloader — recover it over SWD with an ST-LINK. See [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).

The X20P receiver's own firmware is updated separately with u-center 2 — see [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).

See the latest firmware below.

{% file src="../../.gitbook/assets/89-1.18.76e683ea.uavcan.bin" %}
ARK X20 GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_x20-gps_canbootloader.bin" %}
ARK X20 GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Release Notes

* 89-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * The antenna mounting for moving baseline heading is set on the flight controller (`GPS_YAW_OFFSET` removed), see [PX4 Instructions](px4-instructions.md#moving-baseline-gps-heading-configuration)
  * Moving base and rover run at 5 Hz
  * Fix timestamps from the receiver's time pulse
  * A moving baseline rover uses only its moving base's corrections
  * Receiver UART1 at 921600 baud
  * Magnetometer scale corrected by 1.7%: recalibrate the magnetometer after updating
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 89-1.16.47e04790 - 2025-11-17
  * Initial release

## LED Meanings

With the connectors at the bottom edge, the GNSS LEDs are on the right edge and the status LED (red, green and blue) is on the left edge. The GNSS LEDs are driven by the receiver; the status LED by the node firmware.

| GNSS LED | Meaning |
|-----|---------|
| Green, one flash per second | Receiver time pulse. Starts once the receiver has a fix. |
| Blue, blinking | Corrections received and in use, RTK Float |
| Blue, solid | RTK Fixed |

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |
| White, fast blink (10 Hz) | GPS passthrough, entered by holding the safety switch at power-up. See [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md). |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

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

Find 3D models at [https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK\_X20\_RTK\_GPS/model](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_X20_RTK_GPS/model)

Find case files at [https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK\_X20\_RTK\_GPS/case](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_X20_RTK_GPS/case)
