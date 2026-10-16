# Firmware

ARK Flow LR runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html) (`ark_can-flow-lr_default`). Supports CAN firmware update and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation). Only ARK's builds (below) drive the AFBR-S50EX85D; upstream PX4's build of this target cannot identify it.

The flight controller flashes the node firmware over CAN.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

The node firmware can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Downloads

* [ARK Flow LR Firmware](https://downloads.arkelectron.com/firmware/ark_can-flow-lr/latest/application.uavcan.bin)
* [ARK Flow LR Bootloader](https://downloads.arkelectron.com/firmware/ark_can-flow-lr/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_can-flow-lr/)

## Node Parameters

Set these on the ARK Flow LR, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `CANNODE_PUB_IMU` | 0 | Set to `1` to publish `RawIMU` messages on the CAN bus. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `SENS_AFBR_MODE` | -1 | Measurement mode. `-1` the sensor's default, Extended Long Range. `0` short range, `1` long range, `2` high speed short range, `3` high speed long range, `4` high precision short range, `5` background suppression short range, `6` extended long range |
| `SENS_AFBR_RATE` | 0 | Measurement rate in Hz. `0` uses 10 Hz. Lower rates give more range. Values below 5 Hz are clamped to 5 Hz |
| `SENS_AFBR_SNM` | 3 | Shot noise monitor. `0` static indoor, `1` static outdoor, `2` dynamic, `3` dynamic plus |
| `SENS_AFBR_QMIN` | 0 | Minimum signal quality (0–100). Readings below it are sent as invalid. `0` sends every reading |
| `SENS_AFBR_OFS_LO` | 0 | Range offset in m for the low laser power stage, added to the factory calibration. Written by `afbrs50 cal` |
| `SENS_AFBR_OFS_HI` | 0 | Range offset in m for the high laser power stage, added to the factory calibration. Written by `afbrs50 cal` |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

## Release Notes

* 95-1.18.46d8238c - 2026-10-16
  * Initial release: PX4 v1.18 base, AFBR-S50EX85D in Extended Long Range mode at 10 Hz
