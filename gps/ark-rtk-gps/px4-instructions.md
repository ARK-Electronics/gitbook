# PX4 Instructions

The ARK RTK GPS runs the [PX4 DroneCAN firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html), so it supports firmware update over the CAN bus and dynamic node allocation.

* Firmware target: `ark_can-rtk-gps_default`
* Bootloader target: `ark_can-rtk-gps_canbootloader`
* Board ID: `82`

{% hint style="warning" %}
The flight controller must have an SD card installed. PX4 uses it for dynamic node allocation and for CAN firmware update — without one the ARK RTK GPS is never assigned a node ID and will not appear on the bus.
{% endhint %}

***

## Firmware Update

### Updating from the Flight Controller

PX4 flashes DroneCAN nodes automatically at boot. This is the recommended method — it needs no hardware beyond the flight controller.

1. Download the firmware from the [ARK RTK GPS](README.md) page, or build `ark_can-rtk-gps_default` yourself.
2. Copy the `.uavcan.bin` file to the root of the flight controller's SD card.
3. Set [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` (or `3`) and power cycle the vehicle.
4. Wait for the update to finish. The node's CAN LED blinks blue and red rapidly while flashing, then returns to fast blinking green.

On boot PX4 reads the board ID from the metadata block embedded in the binary, moves the file to `/fs/microsd/ufw/82.bin`, and deletes it from the SD card root. The file name does not matter — only the embedded metadata is used to match the file to the node.

{% hint style="info" %}
The firmware stays in `/fs/microsd/ufw/` and PX4 re-flashes any ARK RTK GPS on the bus whose firmware does not match it. This keeps a replacement node in sync automatically, but it also means you must delete `/fs/microsd/ufw/82.bin` before flashing a different version by any other method.
{% endhint %}

{% hint style="info" %}
For remote or scripted updates, upload the file to `/fs/microsd/ufw_staging/` instead. PX4 moves it into `/fs/microsd/ufw/` on the next boot, which avoids write conflicts if the file is uploaded while the vehicle is running.
{% endhint %}

### Updating with the DroneCAN GUI Tool

Use this when the node is not connected to a PX4 flight controller, or when you want to flash a single node directly. You need:

* A USB-to-CAN adapter that supports SLCAN, such as the Zubax Babel, connected to the same CAN bus. PX4 cannot expose its own CAN bus to the tool — see the _ArduPilot - Flight Controller as CAN Interface_ section of the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for the ArduPilot alternative.
* A dynamic node ID allocation server on the bus to assign the node an ID. Either a flight controller with `UAVCAN_ENABLE` set to `2` or `3`, or the DroneCAN GUI Tool's own allocation server, started with the rocket icon in the tool's main window.

Upload the `.uavcan.bin` file to the node — see the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for connection and firmware upload steps.

{% hint style="warning" %}
If the flight controller still has firmware in `/fs/microsd/ufw/`, it will re-flash the node on the next boot and undo the update. Delete `/fs/microsd/ufw/82.bin` from the SD card first.
{% endhint %}

### Updating to AP\_Periph

To run the node with ArduPilot, flash [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) instead. An ArduPilot flight controller can act as the CAN adapter for this, so no USB-to-CAN adapter is needed. See [ArduPilot Instructions](ardupilot-instructions.md).

***

## Single GPS Configuration

Connect the ARK RTK GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable. The recommended mounting orientation is with the connectors pointing towards the **back of the vehicle**.

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation (use `3` if also driving DroneCAN ESCs) |
| [UAVCAN\_SUB\_GPS](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS) | 1 | Subscribe to DroneCAN GPS messages |
| [UAVCAN\_SUB\_MAG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_MAG) | 1 | Subscribe to DroneCAN magnetometer messages |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 7 | Enable GPS fusion (lon/lat + alt + 3D velocity) |

#### Optional

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO) | Set to `1` to subscribe to DroneCAN barometer messages |
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` to subscribe to DroneCAN `RawIMU` messages. Requires `CANNODE_PUB_IMU` on the node |
| [UAVCAN\_SUB\_BTN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BTN) | Set to `1` to use the safety switch on the ARK RTK GPS |
| [SENS\_GPS0\_OFFX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS0_OFFX) / [SENS\_GPS0\_OFFY](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS0_OFFY) / [SENS\_GPS0\_OFFZ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS0_OFFZ) | GPS antenna offset from the vehicle center of gravity (meters). On PX4 v1.17 and earlier these are `EKF2_GPS_POS_X/Y/Z` |
| [SENS\_GPS0\_ID](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS0_ID) | Device ID of the receiver the `SENS_GPS0_*` offsets apply to. With two receivers, use `SENS_GPS0_ID` and `SENS_GPS1_ID` to match each set of offsets — matching by instance index is only reliable for serial GPS |

### CAN Node Parameters

Set the following on the GPS and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_NODE_ID` | Static node ID, `1`-`125`. Leave at `0` (default) to use dynamic node allocation |
| `CANNODE_PUB_MAG` | Publish magnetometer messages on the CAN bus. Enabled by default |
| `CANNODE_PUB_IMU` | Set to `1` to publish `RawIMU` messages on the CAN bus |
| `GPS_UBX_BAUD1` | F9P UART1 baudrate. Board default is `921600` |
| `GPS_UBX_BAUD2` | F9P UART2 baudrate. Default is `230400` |

***

## RTK Corrections from a Fixed Base

Centimeter-level absolute position requires RTCM corrections from a fixed base station on the ground. For the base station setup and the flight controller and CAN node parameters that carry the corrections onto the CAN bus, see [ARK RTK Base > PX4 Instructions](../ark-rtk-base/px4-instructions.md).

***

## Moving Baseline GPS Heading Configuration

Two ARK RTK GPS modules can provide compass-free yaw estimation using the GPS moving baseline technique. The relative position between the two antennas determines heading, so no magnetometer is required.

### Hardware Setup

* Connect both modules to the same CAN bus. Each module has two CAN connectors, so the second can be daisy-chained from the first.
* Mount the antennas with a minimum of **30 cm separation** — more is better for heading accuracy.
* Choose one module to be the _Rover_ and the other to be the _Moving Base_.

{% hint style="info" %}
Heading is only output when the _Rover_ has an RTK **Fixed** solution. No heading is output in RTK Float. RTK Fixed here means the baseline between the two antennas is resolved, which is what produces the heading — the vehicle's absolute position is no more accurate than a normal 3D fix unless you also feed in [corrections from a fixed base](#rtk-corrections-from-a-fixed-base).
{% endhint %}

### Flight Controller Parameters

Apply the [Single GPS Configuration](#single-gps-configuration) flight controller parameters above, then change/add the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | 15 | Enable GPS fusion + GPS yaw (lon/lat + alt + 3D velocity + yaw). Overrides the value of `7` from the single GPS configuration |
| [UAVCAN\_SUB\_GPS\_R](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_GPS_R) | 1 | Subscribe to DroneCAN `RelPosHeading` messages, which carry the heading computed by the _Rover_. Enabled by default |
| [SENS\_GPS\_PRIME](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS_PRIME) | node ID | CAN node ID of the _Moving Base_. It is preferred over the _Rover_, whose navigation rate and data latency can degrade when corrections are intermittent |
| [SENS\_GPS\_MASK](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_GPS_MASK) | 7 | Blend both receivers using speed, horizontal position, and vertical position accuracy. This is the default value |

### CAN Node Parameters

Set the following on each node and reboot it.

On the _Rover_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS_UBX_MODE` | 3 | Heading — rover with moving base, F9P UART1 connected to the CAN node |
| `CANNODE_SUB_MBD` | 1 | Subscribe to `MovingBaselineData` messages on the CAN bus |
| `GPS_YAW_OFFSET` | 0 / 90 / 180 / 270 | Clockwise angle in degrees from the vehicle forward axis to the _Moving Base_ → _Rover_ baseline: `0` if the _Rover_ is in front of the _Moving Base_, `90` if right, `180` if behind, `270` if left |

On the _Moving Base_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS_UBX_MODE` | 4 | Moving base — F9P UART1 connected to the CAN node |
| `CANNODE_PUB_MBD` | 1 | Publish `MovingBaselineData` messages on the CAN bus |

### Sending Corrections over UART

The moving baseline corrections can be sent directly between the two modules over the F9P `UART2` link instead of the CAN bus, which keeps that traffic off CAN. Both modules still connect to the flight controller over CAN.

Connect the two 3-pin JST-GH `UART2` connectors to each other — TX of one module to RX of the other, and GND to GND.

| Pin | Signal Name |
|-----|-------------|
| 1 | F9P\_TXD2 |
| 2 | F9P\_RXD2 |
| 3 | GND |

Then set `GPS_UBX_MODE` to `1` on the _Rover_ and `2` on the _Moving Base_. `GPS_YAW_OFFSET` is set on the _Rover_ as above. `CANNODE_PUB_MBD` and `CANNODE_SUB_MBD` are not used in this configuration.

***

## LED Meanings

The GPS status LEDs are to the right of the connectors:

| LED | Meaning |
|-----|---------|
| Blinking green | GPS fix |
| Blinking blue | Corrections received, RTK Float |
| Solid blue | RTK Fixed |

The CAN status LEDs are to the top left of the connectors:

| LED | Meaning |
|-----|---------|
| Slow blinking green | Waiting for CAN connection |
| Fast blinking green | Normal operation |
| Slow blinking green and blue | CAN enumeration |
| Fast blinking blue and red | Firmware update in progress |
| Blinking red | Error |

***

## Troubleshooting

* **Node does not appear on the bus** — run `uavcan status` in the _QGroundControl_ MAVLink Console to list the nodes PX4 has detected. Check that `UAVCAN_ENABLE` is set to `2` or `3` and that the flight controller has a working SD card installed.
* **Blinking red CAN LED** — confirm the flight controller has an SD card, that `ark_can-rtk-gps_canbootloader` was installed on the node before `ark_can-rtk-gps_default`, and that there are no stale binaries left in the SD card root or in `/fs/microsd/ufw/`.
* **Node is not detected at all, even by the DroneCAN GUI Tool** — for example after a bad flash that erased the bootloader. Recover it over SWD with an ST-LINK, see [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).
* **No heading in a moving baseline setup** — heading is only output at RTK Fixed. Confirm the _Rover_ shows a solid blue GPS LED, and that the antennas are at least 30 cm apart.
* **Test outside** — GPS modules need a clear sky view to get a good fix. Indoor testing will not produce reliable results.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
