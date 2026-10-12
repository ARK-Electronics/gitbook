# Firmware

ARK DIST runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html) (`ark_dist_default`). Supports CAN firmware update and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation). The ARK DIST LR needs firmware 92-1.18.f8ebe52d or later; earlier firmware cannot identify its sensor.

The flight controller flashes the node firmware over CAN. An older ARK DIST image left in the flight controller's `ufw` directory is flashed back onto the node at its next boot.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Downloads

* [ARK DIST Firmware](https://downloads.arkelectron.com/firmware/ark_dist/latest/application.uavcan.bin)
* [ARK DIST Bootloader](https://downloads.arkelectron.com/firmware/ark_dist/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_dist/)

## Node Parameters

Set these on the ARK DIST, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md). The defaults suit each variant; the driver picks the mode and rate for the sensor it finds.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `SENS_AFBR_MODE` | -1 | Measurement mode. `-1` the sensor's default: Long Range on the SR and MR, Extended Long Range on the LR. `0` short range, `1` long range, `2` high speed short range, `3` high speed long range, `4` high precision short range, `5` background suppression short range, `6` extended long range |
| `SENS_AFBR_PROF` | 0 | SR and MR only. `0` Range: 20 Hz on the SR, 15 Hz on the MR. `1` Fast: 50 Hz on the SR, 25 Hz on the MR, for optical flow and terrain following near the ground; costs a few metres of range in bright light |
| `SENS_AFBR_RATE` | 0 | Measurement rate in Hz. `0` uses the profile's rate (SR, MR) or 10 Hz (LR). Lower rates give more range. Values below 5 Hz are clamped to 5 Hz |
| `SENS_AFBR_DFM` | -1 | Dual frequency mode. `-1` 4X on the SR and MR; the LR's mode has none. `0` off, `1` 4X, `2` 8X |
| `SENS_AFBR_SNM` | 3 | Shot noise monitor. `0` static indoor, `1` static outdoor, `2` dynamic, `3` dynamic plus |
| `SENS_AFBR_QMIN` | 0 | Minimum signal quality (0–100). Readings below it are sent as invalid. `0` sends every reading |
| `SENS_AFBR_ROT` | 25 | Mounting orientation. `25` pitch 270° (facing down) |
| `SENS_AFBR_OFS_LO` | 0 | Range offset in m for the low laser power stage, added to the factory calibration. Written by `afbrs50 cal` |
| `SENS_AFBR_OFS_HI` | 0 | Range offset in m for the high laser power stage, added to the factory calibration. Written by `afbrs50 cal` |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |
| `MAV_SYS_ID` | 158 | MAVLink system ID on the UART |
| `MAV_COMP_ID` | 158 | MAVLink component ID on the UART |
| `MAV_0_MODE` | 14 | MAVLink mode on the UART. `14` streams `DISTANCE_SENSOR` |
| `MAV_0_FLOW_CTRL` | 2 | UART flow control. `0` off, `1` on, `2` auto-detect |
| `SER_TEL1_BAUD` | 115200 | UART baud rate |

## Release Notes

* 92-1.18.f8ebe52d - 2026-10-12
  * PX4 v1.18 base
  * Supports the ARK DIST LR (AFBR-S50EX85D) in Extended Long Range mode at 10 Hz
  * Broadcom AFBR-S50 API 1.7.6
  * Mode, rate and dual frequency mode default per sensor: SR 20 Hz and MR 15 Hz, both with DFM 4X; `SENS_AFBR_PROF` Fast selects 50 and 25 Hz
  * `SENS_AFBR_RATE` and `SENS_AFBR_PROF` replace `SENS_AFBR_S_RATE`, `SENS_AFBR_L_RATE`, `SENS_AFBR_THRESH` and `SENS_AFBR_HYSTER`; settings made with those are not carried over
  * Range offset calibration (`afbrs50 cal`), minimum signal quality (`SENS_AFBR_QMIN`) and mounting orientation (`SENS_AFBR_ROT`)
  * Recovers on its own when the sensor stalls
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`) and static node ID (`CANNODE_NODE_ID`)
* 92-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 92-1.16.e448eba4 - 2025-8-8
  * Initial Release
