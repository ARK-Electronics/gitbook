# PX4 Instructions

Find additional documentation at [https://docs.px4.io/main/en/dronecan/ark\_rtk\_gps.html](https://docs.px4.io/main/en/dronecan/ark_rtk_gps.html)

{% hint style="warning" %}
The flight controller must have an SD card installed. PX4 uses it for dynamic node allocation and for CAN firmware update — without one the ARK RTK GPS is never assigned a node ID and will not appear on the bus.
{% endhint %}

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

The node publishes GPS, magnetometer and barometer data and subscribes to RTK corrections with its default parameters. To terminate the bus, fix the node ID, publish IMU data, change the F9P baudrates or make `UART2` a u-center diagnostic port, see [Node Parameters](firmware.md#node-parameters).

***

## RTK Corrections from a Fixed Base

Centimeter-level absolute position requires RTCM corrections from a fixed base station on the ground. For the base station setup and the flight controller and CAN node parameters that carry the corrections onto the CAN bus, see [ARK RTK Base > PX4 Instructions](../ark-rtk-base/px4-instructions.md).

The F9P also accepts [u-blox PointPerfect](https://www.u-blox.com/en/product/pointperfect) PPP-RTK corrections (SPARTN), which need no base station. On vehicles running ARK-OS, the [pointperfect service](../../ark-os/services.md) streams them to the flight controller over MAVLink — see [pointperfect-client-mavlink](https://github.com/ARK-Electronics/pointperfect-client-mavlink). They reach the node the same way as base-station corrections: `UAVCAN_PUB_RTCM` on the flight controller, `CANNODE_SUB_RTCM` on the node.

***

## Moving Baseline GPS Heading Configuration

Two ARK RTK GPS modules can provide compass-free yaw estimation using the GPS moving baseline technique. The relative position between the two antennas determines heading, so no magnetometer is required.

{% hint style="info" %}
The L1L5 variant does **not** support moving baseline heading. For dual-GPS heading use the standard L1/L2 ARK RTK GPS, or see the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/README.md) for a dual-antenna solution.
{% endhint %}

### Hardware Setup

* Connect both modules to the same CAN bus. Each module has two CAN connectors, so the second can be daisy-chained from the first.
* Mount the antennas with a minimum of **30 cm separation** — more is better for heading accuracy.
* Choose one module to be the _Rover_ and the other to be the _Moving Base_.

{% hint style="info" %}
Heading is only output when the _Rover_ has an RTK **Fixed** solution. No heading is output in RTK Float. RTK Fixed here means the baseline between the two antennas is resolved, which is what produces the heading — the vehicle's absolute position is no more accurate than a normal 3D fix unless you also feed in [corrections from a fixed base](#rtk-corrections-from-a-fixed-base).
{% endhint %}

{% hint style="info" %}
A moving base and its rover must run at the same navigation rate, and u-blox limits a moving base to 5 Hz. Node firmware 1.18 and later sets 5 Hz on both modules in the moving baseline modes, so leave `GPS_UBX_RATE` at `0`. On earlier node firmware set `GPS_UBX_RATE` to `5` on both modules: a rover running faster than its base has no time-matched observations for the extra epochs and outputs no heading for them.
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

#### Antenna Mounting

| PX4 version | Parameters |
|-------------|------------|
| v1.18 and earlier | `EKF2_GPS_YAW_OFF`: clockwise angle in degrees from the vehicle forward axis to the _Moving Base_ → _Rover_ baseline: `0` if the _Rover_ is in front of the _Moving Base_, `90` if right, `180` if behind, `270` if left |
| `main` | `SENS_GNSSn_ID` and `SENS_GNSSn_OFFX/Y/Z` (antenna position, meters in the body frame) for both modules, and `SENS_GNSSn_HDG` `1` (Moving base rover) in the _Rover_'s slot |

### CAN Node Parameters

Set the following on each node and reboot it.

On the _Rover_:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS_UBX_MODE` | 3 | Heading — rover with moving base, F9P UART1 connected to the CAN node |
| `CANNODE_SUB_MBD` | 1 | Subscribe to `MovingBaselineData` messages on the CAN bus |

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

Then set `GPS_UBX_MODE` to `1` on the _Rover_ and `2` on the _Moving Base_. `CANNODE_PUB_MBD` and `CANNODE_SUB_MBD` are not used in this configuration.

***

## Troubleshooting

* **Node does not appear on the bus** — run `uavcan status` in the _QGroundControl_ MAVLink Console to list the nodes PX4 has detected. Check that `UAVCAN_ENABLE` is set to `2` or `3` and that the flight controller has a working SD card installed.
* **Blinking red status LED** — see [LEDs](hardware.md#leds), then confirm the flight controller has an SD card, that `ark_can-rtk-gps_canbootloader` was installed on the node before `ark_can-rtk-gps_default`, and that there are no stale binaries left in the SD card root or in `/fs/microsd/ufw/`.
* **Node is not detected at all, even by the DroneCAN GUI Tool** — for example after a bad flash that erased the bootloader. Recover it over SWD with an ST-LINK, see [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).
* **No heading in a moving baseline setup** — heading is only output at RTK Fixed. Confirm the _Rover_ shows a solid blue GPS LED, and that the antennas are at least 30 cm apart.
* **Test outside** — GPS modules need a clear sky view to get a good fix. Indoor testing will not produce reliable results.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
