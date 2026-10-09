# Firmware

The ARK RTK GPS runs the [PX4 DroneCAN firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html), so it supports firmware update over the CAN bus and dynamic node allocation.

* Firmware target: `ark_can-rtk-gps_default`
* Bootloader target: `ark_can-rtk-gps_canbootloader`
* Board ID: `82`

If the node does not appear on the CAN bus — for example after a bad flash that erased the bootloader — recover it over SWD with an ST-LINK. See [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).

The F9P receiver's own firmware is updated separately with u-center — see [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).

## Updating from the Flight Controller

PX4 flashes DroneCAN nodes automatically at boot. This is the recommended method — it needs no hardware beyond the flight controller.

1. Download the firmware from [Downloads](#downloads), or build `ark_can-rtk-gps_default` yourself.
2. Copy the `.uavcan.bin` file to the root of the flight controller's SD card.
3. Set [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` (or `3`) and power cycle the vehicle.
4. Wait for the update to finish. The node's status LED flashes red, green and blue together during the update, then returns to fast blinking green.

On boot PX4 reads the board ID from the metadata block embedded in the binary, moves the file to `/fs/microsd/ufw/82.bin`, and deletes it from the SD card root. The file name does not matter — only the embedded metadata is used to match the file to the node.

{% hint style="info" %}
The firmware stays in `/fs/microsd/ufw/` and PX4 re-flashes any ARK RTK GPS on the bus whose firmware does not match it. This keeps a replacement node in sync automatically, but it also means you must delete `/fs/microsd/ufw/82.bin` before flashing a different version by any other method.
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
If the flight controller still has firmware in `/fs/microsd/ufw/`, it will re-flash the node on the next boot and undo the update. Delete `/fs/microsd/ufw/82.bin` from the SD card first.
{% endhint %}

## Updating to AP\_Periph

To run the node with ArduPilot, flash [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) (ArduPilot Peripheral) instead. An ArduPilot flight controller can act as the CAN adapter for this, so no USB-to-CAN adapter is needed.

### Flashing AP\_Periph over CAN

1. Download `AP_Periph.apj` for the ARK RTK GPS from the [ArduPilot firmware server](https://firmware.ardupilot.org/AP_Periph/stable/ARK_RTK_GPS/)
2. Connect to the ARK RTK GPS using the DroneCAN GUI Tool — see our [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for connection and firmware upload instructions
3. Flash the `AP_Periph.apj` file to the node

### Flashing the Bootloader

After flashing AP\_Periph, you should also flash the AP\_Periph bootloader onto the node:

1. Open the node's parameters in the DroneCAN GUI Tool
2. Set `FLASH_BOOTLOADER` to 1
3. Send the parameter and wait for the bootloader flash to complete
4. Reboot the node

This ensures future firmware updates use the AP\_Periph bootloader.

### Flashing AP\_Periph with an ST-LINK

If the node has no bootloader, or you want to replace both images at once, flash over SWD with an ST-LINK. Use the combined bootloader + application image — `AP_Periph_with_bl.hex` — rather than `AP_Periph.bin`:

1. Download `AP_Periph_with_bl.hex` from the [ArduPilot firmware server](https://firmware.ardupilot.org/AP_Periph/stable/ARK_RTK_GPS/)
2. Connect an ST-LINK to the 6-pin debug connector — see the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md) for wiring and tool setup
3. Flash the combined image, then power-cycle the node

```bash
st-flash --format ihex write AP_Periph_with_bl.hex
```

{% hint style="warning" %}
Do not flash `AP_Periph.bin` to `0x08000000`. On the ARK RTK GPS the bootloader occupies the first 64 KB of flash and the application starts at `0x08010000`, so writing the application to the start of flash erases the bootloader. The flash appears to succeed, but the node flashes its LED once at boot and never appears as a CAN node. The combined HEX file carries its own addresses and avoids the problem — see [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).
{% endhint %}

## Downloads

{% file src="../../.gitbook/assets/82-1.18.76e683ea.uavcan.bin" %}
ARK RTK GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-rtk-gps_canbootloader.bin" %}
ARK RTK GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Node Parameters

These apply to the PX4 DroneCAN firmware. Set them on the GPS node, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CANNODE_TERM` | 0 | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_NODE_ID` | 0 | Static node ID, `1`-`125`. `0` uses dynamic node allocation |
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |
| `CANNODE_PUB_BAR` | 1 | Publish barometer messages on the CAN bus |
| `CANNODE_PUB_IMU` | 0 | Set to `1` to publish `RawIMU` messages on the CAN bus. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `CANNODE_SUB_RTCM` | 1 | Subscribe to `RTCMStream` messages (RTK corrections) on the CAN bus |
| `CANNODE_PUB_MBD` | 0 | Publish `MovingBaselineData` messages on the CAN bus. Set to `1` on a moving base |
| `CANNODE_SUB_MBD` | 1 | Subscribe to `MovingBaselineData` messages on the CAN bus. Used by a moving baseline rover |
| `GPS_UBX_MODE` | 0 | u-blox configuration. `3` / `4`: moving baseline rover / moving base over CAN. `1` / `2`: rover / moving base linked over `UART2`. `7`: makes the `UART2` connector a UBX diagnostic port for [u-center](https://docs.px4.io/main/en/gps_compass/u-center.html), at the `GPS_UBX_BAUD2` baudrate |
| `GPS_UBX_RATE` | 0 | Navigation rate in Hz. `0` selects it automatically: 5 Hz on the F9P |
| `GPS_UBX_BAUD1` | 921600 | F9P UART1 baudrate |
| `GPS_UBX_BAUD2` | 230400 | F9P UART2 baudrate |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware |

{% hint style="warning" %}
UART2 cannot be used for u-blox firmware update. Use the debug passthrough method in [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).
{% endhint %}

## Release Notes

* 82-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * Fix the IMU not starting after some resets until the next power cycle
  * The antenna mounting for moving baseline heading is set on the flight controller (`GPS_YAW_OFFSET` removed), see [PX4 Instructions](px4-instructions.md#moving-baseline-gps-heading-configuration)
  * Moving base and rover run at 5 Hz
  * Fix timestamps from the receiver's time pulse
  * A moving baseline rover uses only its moving base's corrections
  * Receiver UART1 at 921600 baud
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 82-1.16.e68afe1e - 2025-2-12
  * Disable mag bias estimator by default
