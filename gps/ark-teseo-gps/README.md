---
cover: ../../.gitbook/assets/IMG_2267_edited (Large).JPG
coverY: -10
---

# ARK TESEO GPS

The ARK TESEO GPS is a [DroneCAN](https://docs.px4.io/main/en/dronecan/) GNSS module built around the [ST Teseo-LIV4F](https://www.st.com/en/positioning/teseo-liv4f.html) L1/L5 multi-constellation receiver. It also carries an IIS2MDC magnetometer, BMP390 barometer, and ICM-42688-P IMU.

{% embed url="https://docs.px4.io/main/en/dronecan/#gps" %}

## Firmware

Follow the steps for updating the firmware through the flight controller. The firmware will automatically update the LIV4F GPS module firmware on first boot if the embedded version differs from what is on the chip.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../../.gitbook/assets/86-1.18.0d10f176.uavcan.bin" %}
ARK Teseo GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_teseo-gps_canbootloader.bin" %}
ARK Teseo GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Release Notes

* 86-1.18.0d10f176 - 2026-10-5
  * PX4 v1.18 base
  * Output at 5 Hz by default, set with `TESEO_RATE`. Above 5 Hz with many satellites in use, the Teseo repeats its previous solution in the epochs it cannot compute, and the flight controller fuses each repeat as a new measurement
  * Check the Teseo's saved configuration on every boot and rewrite it only when it differs: a module that lost its configuration is repaired automatically, and the Teseo's flash is no longer rewritten on every boot
  * If the Teseo's configuration cannot be saved, keep publishing a fix from its standard NMEA output, with accuracy estimated from DOP, and log a warning every 30 s
  * Fix the position accuracy sent to the flight controller, which received the square root of the true value
  * Magnetometer scale corrected to the IIS2MDC datasheet: readings are 1.7% lower, recalibrate the compass
  * Fix the IMU not starting after some resets until the next power cycle
  * Barometer at 25 Hz, and recovers on its own after repeated read errors
  * Optional `RawIMU` output (`CANNODE_PUB_IMU`) and static node ID (`CANNODE_NODE_ID`)
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
  * Embedded Teseo firmware is ST's STA8041\_LIV4F\_PVT\_STD 4.6.8.5.11 EB5 build. It reports the same version as 4.6.8.5.11, so a module already on 4.6.8.5.11 keeps its firmware unless `TESEO_FWUPD` is set
  * Node parameters are kept on update; installing an older firmware afterwards resets all node parameters to defaults
* 86-1.16.c93582f2 - 2026-5-5
  * Fix NMEA parsers eating first char of each first field. Observable on the RMC timestamp (hhmmss.sss): UTC hours 10-19 appear as 00-09 and 20-23 as 00-03.
* 86-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
  * Improve NMEA decoder
  * platforms: Serial new dedicated writeBlocking method [#25537](https://github.com/PX4/PX4-Autopilot/pull/25537)
  * Update to STA8041\_LIV4F\_PVT\_STD\_4\_6\_8\_5\_11\_UPG [Teseo Firmware](https://www.st.com/en/embedded-software/teseo-liv4fsw.html)
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

## LED Meanings

The green LED on the left edge flashes once per second with the receiver's time pulse (PPS). The status LED (red, green and blue in a row) is on the right edge and is driven by the node firmware.

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |
| Blue, blinking (2 Hz) after the firmware has started | Updating the Teseo receiver firmware |
| Red, blinking (1 Hz) after the firmware has started | Teseo receiver firmware update failed |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## 3D Model

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_TESEO\_GPS](https://github.com/ARK-Electronics/ARK_TESEO_GPS)

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### I2C + Timepulse - 5 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>I2C2_SCL</td><td>3.3V</td></tr><tr><td>3</td><td>I2C2_SDA</td><td>3.3V</td></tr><tr><td>4</td><td>TIMEPULSE</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr></tbody></table>

{% hint style="info" %}
The **I2C2 SCL/SDA lines on this connector are currently unused** by the firmware.

The TIMEPULSE pin outputs a PPS signal that the flight controller can use to accurately timestamp incoming PVT solutions.
{% endhint %}

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
