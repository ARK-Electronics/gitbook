# Firmware

ARK MAG runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

The flight controller flashes the node firmware over CAN.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

* Firmware target: `ark_mag_default`
* Bootloader target: `ark_mag_canbootloader`

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Downloads

* [ARK MAG Firmware](https://downloads.arkelectron.com/firmware/ark_mag/latest/application.uavcan.bin)
* [ARK MAG Bootloader](https://downloads.arkelectron.com/firmware/ark_mag/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_mag/)

## Node Parameters

Set these on the ARK MAG, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware. Firmware before 1.18 lacks this parameter |

## Release Notes

### v1.18.0.1 - 59dac08e - 2026-11-03

- PX4 v1.18 base
- `CANNODE_PUB_MAG` turns the magnetometer publication off
- Bootloader update from the running firmware (`SYS_BL_UPDATE`)

### v1.17 - 482683d1 - 2025-10-29

- Initial Release
