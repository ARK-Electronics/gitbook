# Firmware

Follow the steps for updating the firmware through the flight controller.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

## Downloads

* [ARK G5 RTK GPS Firmware](https://downloads.arkelectron.com/firmware/ark_g5-gps/latest/application.uavcan.bin)
* [ARK G5 RTK GPS Bootloader](https://downloads.arkelectron.com/firmware/ark_g5-gps/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_g5-gps/)

Node firmware 91-1.18.73506671 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Receiver Firmware

The Septentrio G5 module firmware can be updated using the [Septentrio RxTools](https://www.septentrio.com/en/products/gps-gnss-receiver-software/rxtools) application.

1. Install [RxTools](https://www.septentrio.com/en/products/gps-gnss-receiver-software/rxtools)
2. Launch RxControl
3. Connect to the module on the USB serial connection\
   ![](<../../.gitbook/assets/image (70).png>)
4. Under File, select "Upgrade Receiver using Current Connection"\
   ![](<../../.gitbook/assets/image (71).png>)
5. Select the SUF firmware file downloaded from [Septentrio's website](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3#resources)\
   ![](<../../.gitbook/assets/image (72).png>)
6. Run the upgrade

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
| `SEP_MODE` | 0 | `0` rover, `1` moving base, `2` moving-base rover. See [Moving Base Heading Configuration](px4-instructions.md#moving-base-heading-configuration) |
| `SEP_ANT_MODE` | 0 | P6 and P8 only. `0` keeps the antenna mode saved in the receiver (single antenna unless changed in the web GUI), `1` single antenna, `2` dual antenna. `1` and `2` are applied without saving them in the receiver, which restarts once (about 10 s) at each power-up where its saved mode differs |
| `SEP_DUAL_ANT` | 3 | Ambiguity types allowed for dual antenna heading: `1` fixed, `2` float, `3` both. `0` disables heading |
| `SEP_PVT_MODE` | 15 | Bitmask of allowed PVT modes for Rover operation. Bits: `1` = StandAlone, `2` = DGNSS, `4` = RTKFloat, `8` = RTKFixed, `16` = SBAS, `32` = PPP (Galileo HAS). The receiver uses the most accurate mode available |
| `SEP_RCV_DYN` | 6 | Receiver dynamics model: `0` = Static, `1` = Quasistatic, `2` = Pedestrian, `3` = Automotive, `4` = RaceCar, `5` = HeavyMachinery, `6` = UAV, `7` = Unlimited |
| `SEP_OUT_RATE` | 50 | Output rate for GNSS data messages: `-1` = OnChange, or `10` / `20` / `40` / `50` / `100` / `200` / `500` ms. Do not use OnChange on a moving base or its rover |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

## Release Notes

* 91-1.18.73506671 - 2026-10-6
  * ArduPilot no longer takes a heading the node marks invalid as its GPS yaw: the node sends it with a zero baseline, which ArduPilot rejects. With 91-1.18.a784eb57, ArduPilot could block arming with `Internal errors 0x400` while the heading solution was not fixed
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 91-1.18.a784eb57 - 2026-10-1
  * PX4 v1.18 base
  * Moving base and moving-base rover (`SEP_MODE`)
  * Single or dual antenna on the P6 and P8 (`SEP_ANT_MODE`)
  * Heading reported only with fixed ambiguities; the antenna mounting is set on the flight controller (`SEP_OFFS_YAW` and `SEP_OFFS_PITCH` removed)
  * SBAS and Galileo HAS available in `SEP_PVT_MODE`, off by default
  * Jamming, spoofing, OSNMA and receiver error reporting
  * Receiver reconfigured after it restarts
* 91-1.16.c8403786 - 2026-2-12
  * Septentrio sensor\_gnss\_relative
  * General heading improvement
* 91-1.16.c53f8d8e - 2025-12-18
  * Initial release
