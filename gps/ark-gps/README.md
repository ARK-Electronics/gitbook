---
cover: ../../.gitbook/assets/ark_gps_7.jpg
coverY: 0
---

# ARK GPS

## Firmware

Follow the steps for updating the firmware through the flight controller.&#x20;

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../../.gitbook/assets/81-1.18.76e683ea.uavcan.bin" %}
ARK GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-gps_canbootloader.bin" %}
ARK GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Release Notes

* 81-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * Fix the IMU not starting after some resets until the next power cycle
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 81-1.17.67ace351 - 2025-11-14
  * [Fix M9N output rate](https://github.com/PX4/PX4-GPSDrivers/pull/191)
* 81-1.16.e68afe1e - 2025-2-12
  * Disable mag bias estimator by default

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK GPS is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

### LED Meanings <a href="#led-meanings" id="led-meanings"></a>

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

If the status LED blinks red, check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the ARK GPS has `ark_can-gps_canbootloader` installed prior to flashing `ark_can-gps_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
