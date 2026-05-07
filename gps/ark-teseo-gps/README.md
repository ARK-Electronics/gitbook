---
cover: ../../.gitbook/assets/IMG_2267_edited (Large).JPG
coverY: -10
---

# ARK TESEO GPS

The ARK TESEO GPS is a [DroneCAN](https://docs.px4.io/main/en/dronecan/) GNSS module built around the [ST Teseo-LIV4F](https://www.st.com/en/positioning/teseo-liv4f.html) L1/L5 multi-constellation receiver. It also carries an IIS2MDC magnetometer, BMP390 barometer, and ICM-42688-P IMU.

## DroneCAN Messages

The ARK TESEO GPS publishes:

* GNSS solution: [`uavcan.equipment.gnss.Fix2`](../../knowledge-base/dronecan-messages.md#fix2) and [`uavcan.equipment.gnss.Auxiliary`](../../knowledge-base/dronecan-messages.md#gnss-auxiliary)
* Magnetometer: [`uavcan.equipment.ahrs.MagneticFieldStrength2`](../../knowledge-base/dronecan-messages.md#magneticfieldstrength2)
* Barometer: [`uavcan.equipment.air_data.StaticPressure`](../../knowledge-base/dronecan-messages.md#staticpressure) and [`uavcan.equipment.air_data.StaticTemperature`](../../knowledge-base/dronecan-messages.md#statictemperature)
* IMU: [`uavcan.equipment.ahrs.RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) (when `CANNODE_PUB_IMU=1`)

Like every DroneCAN node it also emits [`NodeStatus`](../../knowledge-base/dronecan-messages.md#nodestatus) and responds to [`GetNodeInfo`](../../knowledge-base/dronecan-messages.md#getnodeinfo).

See [DroneCAN Messages](../../knowledge-base/dronecan-messages.md) for full message definitions.

{% embed url="https://docs.px4.io/main/en/dronecan/#gps" %}

## Firmware

Follow the steps for updating the firmware through the flight controller. The firmware will automatically update the LIV4F GPS module firmware on first boot if the embedded version differs from what is on the chip.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../../.gitbook/assets/86-1.16.c93582f2.uavcan.bin" %}
ARK Teseo GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_teseo-gps_canbootloader (1).bin" %}
ARK Teseo GPS Bootloader
{% endfile %}

## Release Notes

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

## Parameter Reference

The following parameters are configured on the ARK TESEO GPS DroneCAN node (e.g. via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md)). Changes take effect on the next reboot of the node.

### Constellations

The Teseo-LIV4F can track up to **four GNSS constellations simultaneously**. Enabling more than four has no effect — pick the four that match your operating region. SBAS does not count toward this limit.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TESEO_GPS` | 1 | Enable the GPS (USA) constellation |
| `TESEO_GLONASS` | 1 | Enable the GLONASS (Russia) constellation |
| `TESEO_GALILEO` | 1 | Enable the Galileo (EU) constellation |
| `TESEO_BEIDOU` | 1 | Enable the BeiDou (China) constellation |
| `TESEO_QZSS` | 0 | Enable the QZSS (Japan) constellation |
| `TESEO_IRNSS` | 0 | Enable the IRNSS / NavIC (India) constellation |
| `TESEO_SBAS` | 1 | Enable SBAS (Satellite-Based Augmentation System) |

### Firmware Update

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TESEO_FWUPD` | 0 | Set to `1` to force the cannode to re-flash the embedded LIV4F firmware on the next boot. The cannode also auto-updates the LIV4F whenever the version embedded in the cannode firmware does not match what is on the GPS chip — this parameter is only needed to force a re-flash without a version change. The parameter is automatically cleared back to `0` after a successful update. |

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
