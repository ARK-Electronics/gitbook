# Firmware

The ARK X20 RTK GPS runs the [PX4 DroneCAN firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html), so it supports firmware update over the CAN bus and dynamic node allocation.

* Firmware target: `ark_x20-gps_default`
* Bootloader target: `ark_x20-gps_canbootloader`
* Board ID: `89`

## Updating from the Flight Controller

PX4 flashes DroneCAN nodes automatically at boot. This is the recommended method — it needs no hardware beyond the flight controller.

1. Download the firmware from [Downloads](#downloads), or build `ark_x20-gps_default` yourself.
2. Copy the `.uavcan.bin` file to the root of the flight controller's SD card.
3. Set [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` (or `3`) and power cycle the vehicle.
4. Wait for the update to finish. The node's status LED flashes red, green and blue together during the update, then returns to fast blinking green.

On boot PX4 reads the board ID from the metadata block embedded in the binary, moves the file to `/fs/microsd/ufw/89.bin`, and deletes it from the SD card root. The file name does not matter — only the embedded metadata is used to match the file to the node.

{% hint style="info" %}
The firmware stays in `/fs/microsd/ufw/` and PX4 re-flashes any ARK X20 RTK GPS on the bus whose firmware does not match it. This keeps a replacement node in sync automatically, but it also means you must delete `/fs/microsd/ufw/89.bin` before flashing a different version by any other method.
{% endhint %}

{% hint style="info" %}
For remote or scripted updates, upload the file to `/fs/microsd/ufw_staging/` instead. PX4 moves it into `/fs/microsd/ufw/` on the next boot, which avoids write conflicts if the file is uploaded while the vehicle is running.
{% endhint %}

## Updating with the DroneCAN GUI Tool

Use this when the node is not connected to a PX4 flight controller, or when you want to flash a single node directly. You need:

* A USB-to-CAN adapter that supports SLCAN, such as the Zubax Babel, connected to the same CAN bus. PX4 cannot expose its own CAN bus to the tool — see the _ArduPilot - Flight Controller as CAN Interface_ section of the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for the ArduPilot alternative.
* A dynamic node ID allocation server on the bus to assign the node an ID. Either a flight controller with `UAVCAN_ENABLE` set to `2` or `3`, or the DroneCAN GUI Tool's own allocation server, started with the rocket icon in the tool's main window.

Upload the `.uavcan.bin` file to the node — see the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for connection and firmware upload steps.

{% hint style="warning" %}
If the flight controller still has firmware in `/fs/microsd/ufw/`, it will re-flash the node on the next boot and undo the update. Delete `/fs/microsd/ufw/89.bin` from the SD card first.
{% endhint %}

## Recovering over SWD

If the node does not appear on the CAN bus — for example after a bad flash that erased the bootloader — recover it over SWD with an ST-LINK. See [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).

## Downloads

* [ARK X20 GPS Firmware](https://downloads.arkelectron.com/firmware/ark_x20-gps/latest/application.uavcan.bin)
* [ARK X20 GPS Bootloader](https://downloads.arkelectron.com/firmware/ark_x20-gps/latest/bootloader.bin)
* [All releases and SHA-256 checksums](https://downloads.arkelectron.com/firmware/ark_x20-gps/)

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Receiver Firmware

The X20P receiver's own firmware is updated separately with u-center 2 — see [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).

## ArduPilot Firmware

To run the node with ArduPilot, flash [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) instead. AP\_Periph support for the ARK X20 RTK GPS is in review — [ArduPilot PR #33941](https://github.com/ArduPilot/ardupilot/pull/33941) adds the `ARK_X20_GPS` target (board ID 89). Until it merges there are no prebuilt binaries on the ArduPilot firmware server.

Build AP\_Periph from the PR branch:

```bash
./waf configure --board ARK_X20_GPS
./waf AP_Periph
```

Flash it using either method:

* **Over CAN** — upload `AP_Periph.apj` with the DroneCAN GUI Tool, see our [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md). Then set `FLASH_BOOTLOADER` to `1` in the node's parameters so future updates use the AP\_Periph bootloader.
* **Over SWD** — flash the combined `AP_Periph_with_bl.hex` with an ST-LINK on the 6-pin debug connector, see the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md).

## Node Parameters

These apply to the PX4 DroneCAN firmware. Set them on the GPS node, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

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
| `GPS_UBX_MODE` | 0 | `0` default. Moving baseline over CAN: `3` rover, `4` moving base. Moving baseline over UART2: `1` rover, `2` moving base. `7` makes the `UART2` connector a UBX diagnostic port for [u-center](https://docs.px4.io/main/en/gps_compass/u-center.html), at the `GPS_UBX_BAUD2` baudrate. `8` uses Galileo HAS from E6 (receiver firmware 2.10 or later) and ignores RTCM and SPARTN from the flight controller |
| `GPS_UBX_BAUD1` | 921600 | X20P UART1 baudrate |
| `GPS_UBX_BAUD2` | 230400 | X20P UART2 baudrate |
| `GPS_UBX_RATE` | 0 | Navigation rate in Hz, up to 25. `0` selects it automatically: 5 Hz in the moving baseline modes on node firmware 1.18 and later |
| `GPS_1_GNSS` | 47 | Constellations, see [Constellations](#constellations) |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

{% hint style="warning" %}
UART2 cannot be used for u-blox firmware update. Use the debug passthrough method in [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).
{% endhint %}

### Constellations

`GPS_1_GNSS` is the sum of the constellations to use. The default, `47`, enables all of them. The firmware does not configure GLONASS on the X20P, so `16` has no effect. `0` keeps the receiver's own configuration.

| Value | Constellation |
|-------|---------------|
| 1 | GPS and QZSS |
| 2 | SBAS |
| 4 | Galileo |
| 8 | BeiDou |
| 32 | NavIC |

## Release Notes

* 89-1.18.73506671 - 2026-10-9
  * Moving baseline: an invalid heading goes out with a zero baseline, so ArduPilot ignores it instead of taking a NaN yaw that blocks arming (`PreArm: Internal errors 0x400`)
* 89-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * The antenna mounting for moving baseline heading is set on the flight controller (`GPS_YAW_OFFSET` removed), see [PX4 Instructions](px4-instructions.md#moving-baseline-gps-heading-configuration)
  * Moving base and rover run at 5 Hz
  * Fix timestamps from the receiver's time pulse
  * A moving baseline rover uses only its moving base's corrections
  * Receiver UART1 at 921600 baud
  * Magnetometer scale corrected to the IIS2MDC datasheet
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 89-1.16.47e04790 - 2025-11-17
  * Initial release
