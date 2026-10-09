# Firmware

ARK Flow MR runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

The flight controller flashes the node firmware over CAN.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

* Firmware target: `ark_can-flow-mr_default`
* Bootloader target: `ark_can-flow-mr_canbootloader`

## Downloads

{% file src="../../.gitbook/assets/88-1.16.3c45b562.uavcan.bin" %}
ARK Flow MR Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-flow-mr_canbootloader (1).bin" %}
ARK Flow MR Bootloader
{% endfile %}

## Node Parameters

Set these on the ARK Flow MR, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md). Defaults are those of the firmware above.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_PUB_IMU` | 0 | Set to `1` to publish `RawIMU` messages on the CAN bus. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `SENS_AFBR_MODE` | 1 | Distance sensor measurement mode. `0` short range, `1` long range, `2` high speed short range, `3` high speed long range |
| `SENS_AFBR_S_RATE` | 25 | Distance sensor measurement rate in Hz below the switching distance |
| `SENS_AFBR_L_RATE` | 5 | Distance sensor measurement rate in Hz above the switching distance |
| `SENS_AFBR_THRESH` | 4 | Switching distance in m. The rate changes to `SENS_AFBR_L_RATE` above `SENS_AFBR_THRESH` + `SENS_AFBR_HYSTER` and back to `SENS_AFBR_S_RATE` below `SENS_AFBR_THRESH` − `SENS_AFBR_HYSTER` |
| `SENS_AFBR_HYSTER` | 1 | Hysteresis in m around `SENS_AFBR_THRESH` |

## Release Notes

* 88-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 88-1.16.afb2c08b - 2025-8-6
  * AFBRS50: Fix long range measurement publishing
* 88-1.16.2248a40e - 2025-7-10
  * [AFBRS40: fix Range Mode switching](https://github.com/PX4/PX4-Autopilot/pull/25185)
* 88-1.16.d0bfa548 - 2025-6-12
  * [AFBRS50 fix scheduling and refactor](https://github.com/PX4/PX4-Autopilot/pull/24837)
* 88-1.15.82ff8744- 2025-6-11
  * Add DroneCAN RawIMU publisher
* 88-1.16.c8bed86b - 2025-2-26
  * Default to Long Range Mode (SENS\_AFBR\_MODE = 1)
  * Default to 5Hz output rate over 4m (SENS\_AFBR\_L\_RATE = 5)
* 88-1.16.61036f77 - 2025-2-7
  * Update to [AFBR 1.6.5 API](https://github.com/Broadcom/AFBR-S50-API/releases/tag/v1.6.5)
    * Improved distance sensor performance
  * Fix PAA3905 challenging surface detected spam
    * Only notify once every second
