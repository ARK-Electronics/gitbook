# Firmware

Follow the steps for updating the firmware through the flight controller.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

## Downloads

* [ARK Mosaic-X5 GPS Firmware](https://downloads.arkelectron.com/firmware/ark_mosaic-x5-gps/latest/application.uavcan.bin)
* [ARK Mosaic-X5 GPS Bootloader](https://downloads.arkelectron.com/firmware/ark_mosaic-x5-gps/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_mosaic-x5-gps/)

Node firmware 84-1.18.73506671 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Node Parameters

Set these on the GPS node, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` on the last node of the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer data |
| `CANNODE_PUB_BAR` | 1 | Publish barometer data |
| `CANNODE_PUB_IMU` | 0 | Publish `RawIMU` data. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `CANNODE_SUB_RTCM` | 1 | Receive RTCM corrections from the flight controller |
| `CANNODE_PUB_MBD` | 0 | Publish `MovingBaselineData`. Set to `1` on a moving base |
| `CANNODE_SUB_MBD` | 1 | Receive `MovingBaselineData` from a moving base |
| `SEP_MODE` | 0 | `0` rover, `1` moving base, `2` moving-base rover |
| `SEP_PVT_MODE` | 15 | Bitmask of allowed PVT modes for Rover operation. Bits: `1` = StandAlone, `2` = DGNSS, `4` = RTKFloat, `8` = RTKFixed, `16` = SBAS, `32` = PPP (Galileo HAS, ignored on the mosaic-X5). The receiver uses the most accurate mode available |
| `SEP_RCV_DYN` | 6 | Receiver dynamics model: `0` = Static, `1` = Quasistatic, `2` = Pedestrian, `3` = Automotive, `4` = RaceCar, `5` = HeavyMachinery, `6` = UAV, `7` = Unlimited |
| `SEP_OUT_RATE` | 50 | Output rate for GNSS data messages: `-1` = OnChange, or `10` / `20` / `40` / `50` / `100` / `200` / `500` ms. Do not use OnChange on a moving base or its rover |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

## Release Notes

* 84-1.18.73506671 - 2026-10-6
  * ArduPilot no longer takes a heading the node marks invalid as its GPS yaw: the node sends it with a zero baseline, which ArduPilot rejects. With 84-1.18.a784eb57, ArduPilot could block arming with `Internal errors 0x400` while the heading solution was not fixed
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 84-1.18.a784eb57 - 2026-10-1
  * PX4 v1.18 base
  * Moving base and moving-base rover (`SEP_MODE`)
  * SBAS available in `SEP_PVT_MODE`, off by default
  * Jamming, spoofing, OSNMA and receiver error reporting
  * Receiver reconfigured after it restarts
  * Bootloader file renamed to `ark_mosaic-x5-gps_canbootloader.bin`
* 84-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 84-1.15.6dea2ce5 - 2025-2-12
  * Disable mag bias estimator by default
