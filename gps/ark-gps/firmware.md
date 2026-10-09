# Firmware

ARK GPS runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

ARK GPS boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

* Firmware target: `ark_can-gps_default`
* Bootloader target: `ark_can-gps_canbootloader`

Follow the steps for updating the firmware through the flight controller.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

## Downloads

{% file src="../../.gitbook/assets/81-1.18.76e683ea.uavcan.bin" %}
ARK GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-gps_canbootloader.bin" %}
ARK GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Node Parameters

Set these on the GPS node, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | 0 | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer data |
| `CANNODE_PUB_BAR` | 1 | Publish barometer data |
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | 0 | Set to `1` to publish the `RawIMU` messages on the CAN bus. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

## Release Notes

* 81-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * Fix the IMU not starting after some resets until the next power cycle
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 81-1.17.67ace351 - 2025-11-14
  * [Fix M9N output rate](https://github.com/PX4/PX4-GPSDrivers/pull/191)
* 81-1.16.e68afe1e - 2025-2-12
  * Disable mag bias estimator by default
