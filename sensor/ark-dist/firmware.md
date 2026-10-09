# Firmware

ARK DIST runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html) (`ark_dist_default`). Supports CAN firmware update and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

The flight controller flashes the node firmware over CAN.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

## Downloads

{% file src="../../.gitbook/assets/92-1.16.3c45b562.uavcan.bin" %}
ARK DIST Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_dist_canbootloader (1).bin" %}
ARK DIST Bootloader
{% endfile %}

## Node Parameters

Set these on the ARK DIST, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md). Defaults are those of the firmware above.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `SENS_AFBR_MODE` | 1 | Measurement mode. `0` short range, `1` long range, `2` high speed short range, `3` high speed long range |
| `SENS_AFBR_S_RATE` | 25 | Measurement rate in Hz below the switching distance |
| `SENS_AFBR_L_RATE` | 5 | Measurement rate in Hz above the switching distance |
| `SENS_AFBR_THRESH` | 2 | Switching distance in m. The rate changes to `SENS_AFBR_L_RATE` above `SENS_AFBR_THRESH` + `SENS_AFBR_HYSTER` and back to `SENS_AFBR_S_RATE` below `SENS_AFBR_THRESH` − `SENS_AFBR_HYSTER` |
| `SENS_AFBR_HYSTER` | 1 | Hysteresis in m around `SENS_AFBR_THRESH` |
| `MAV_SYS_ID` | 158 | MAVLink system ID on the UART |
| `MAV_COMP_ID` | 158 | MAVLink component ID on the UART |
| `MAV_0_MODE` | 14 | MAVLink mode on the UART. `14` streams `DISTANCE_SENSOR` |
| `MAV_0_FLOW_CTRL` | 2 | UART flow control. `0` off, `1` on, `2` auto-detect |
| `SER_TEL1_BAUD` | 115200 | UART baud rate |

## Release Notes

* 92-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 92-1.16.e448eba4 - 2025-8-8
  * Initial Release
