# Firmware

The flight controller flashes the node firmware over CAN.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

On boot, the node also updates the Teseo receiver's own firmware when the version embedded in the node firmware differs from the one on the chip. While it updates, the status LED blinks blue.

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Downloads

{% file src="../../.gitbook/assets/86-1.18.0d10f176.uavcan.bin" %}
ARK Teseo GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_teseo-gps_canbootloader.bin" %}
ARK Teseo GPS Bootloader
{% endfile %}

## Node Parameters

Set these on the GPS node, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer data |
| `CANNODE_PUB_BAR` | 1 | Publish barometer data |
| `CANNODE_PUB_IMU` | 0 | Publish `RawIMU` data. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `TESEO_RATE` | 5 | Output rate in Hz, 1–10. Above 5 Hz with many satellites in use, the Teseo repeats its previous solution in the epochs it cannot compute, and the flight controller fuses each repeat as a new measurement |
| `TESEO_FWUPD` | 0 | Set to `1` to re-flash the Teseo receiver firmware on the next boot without a version change. Returns to `0` after a successful update |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

### Constellations

The Teseo-LIV4F tracks at most four constellations at once; enabling more has no effect. SBAS does not count toward the four.

| Parameter | Default | Constellation |
|-----------|---------|---------------|
| `TESEO_GPS` | 1 | GPS (USA) |
| `TESEO_GLONASS` | 1 | GLONASS (Russia) |
| `TESEO_GALILEO` | 1 | Galileo (EU) |
| `TESEO_BEIDOU` | 1 | BeiDou (China) |
| `TESEO_QZSS` | 0 | QZSS (Japan) |
| `TESEO_IRNSS` | 0 | IRNSS / NavIC (India) |
| `TESEO_SBAS` | 1 | SBAS |

## Release Notes

* 86-1.18.0d10f176 - 2026-10-5
  * PX4 v1.18 base
  * Output at 5 Hz by default, set with `TESEO_RATE`. Above 5 Hz with many satellites in use, the Teseo repeats its previous solution in the epochs it cannot compute, and the flight controller fuses each repeat as a new measurement
  * Check the Teseo's saved configuration on every boot and rewrite it only when it differs: a module that lost its configuration is repaired automatically, and the Teseo's flash is no longer rewritten on every boot
  * If the Teseo's configuration cannot be saved, keep publishing a fix from its standard NMEA output, with accuracy estimated from DOP, and log a warning every 30 s
  * Fix the position accuracy sent to the flight controller, which received the square root of the true value
  * Magnetometer scale corrected to the IIS2MDC datasheet
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
