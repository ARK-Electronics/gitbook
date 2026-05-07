# ArduPilot Instructions

## Firmware Setup

The ARK RTK GPS ships with PX4 CANnode firmware by default. For use with ArduPilot, we recommend flashing [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) (ArduPilot Peripheral) firmware. AP\_Periph is the well-tested configuration for DroneCAN GPS modules with ArduPilot.

### Flashing AP\_Periph

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

***

## Single GPS Configuration

Connect the ARK RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters on the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 2 | Auto-configure DroneCAN GPS |

{% hint style="info" %}
`GPS_AUTO_CONFIG=2` is correct here because the ARK RTK GPS runs AP\_Periph firmware, which supports ArduPilot's DroneCAN parameter auto-configuration. If your GPS module is not running AP\_Periph firmware, leave `GPS_AUTO_CONFIG` at its default value of 1 — setting it to 2 on non-AP\_Periph firmware will block GPS data.
{% endhint %}

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data.

***

## Dual GPS Heading Configuration

Two ARK RTK GPS modules can provide compass-free yaw estimation using the GPS moving baseline technique. This uses the relative position between two GPS antennas to determine heading, eliminating the need for a magnetometer.

### Hardware Setup

* Connect both ARK RTK GPS modules to the same CAN bus using a CAN splitter
* Mount the antennas with a minimum of **30 cm separation** (more is better for heading accuracy)
* The antenna connected to GPS1 (base) should be positioned ahead of or to the side of GPS2 (rover) — the offset between them is configured in the parameters below

### Autopilot Parameters

#### EKF Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `AHRS_EKF_TYPE` | 3 | Use EKF3 |
| `EK2_ENABLE` | 0 | Disable EKF2 |
| `EK3_ENABLE` | 1 | Enable EKF3 |
| `EK3_SRC1_YAW` | 2 | GPS yaw (or 3 for GPS with compass fallback) |

#### GPS Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS1_TYPE` | 22 | DroneCAN moving baseline base |
| `GPS2_TYPE` | 23 | DroneCAN moving baseline rover |
| `GPS_AUTO_CONFIG` | 2 | Auto-configure DroneCAN GPS |
| `GPS_AUTO_SWITCH` | 1 | Use best GPS (do NOT set to 2/Blend) |

#### CAN Node Identification

| Parameter | Description |
|-----------|-------------|
| `GPS1_CAN_OVRIDE` | CAN node ID of the base GPS (auto-populated at boot from detected nodes, or set manually) |
| `GPS2_CAN_OVRIDE` | CAN node ID of the rover GPS (auto-populated at boot from detected nodes, or set manually) |

#### Moving Baseline Offsets

| Parameter | Description |
|-----------|-------------|
| `GPS1_MB_TYPE` | Set to 1 to enable moving baseline offsets |
| `GPS1_MB_OFS_X` | Antenna offset from base to rover, forward (meters) |
| `GPS1_MB_OFS_Y` | Antenna offset from base to rover, right (meters) |
| `GPS1_MB_OFS_Z` | Antenna offset from base to rover, down (meters) |

{% hint style="warning" %}
Do **not** set `GPS_AUTO_SWITCH` to 2 (Blend). Blending is not compatible with the moving baseline configuration.
{% endhint %}

For the full parameter reference, see the [ArduPilot GPS for Yaw documentation](https://ardupilot.org/copter/docs/common-gps-for-yaw.html#dual-dronecan-f9p-gps).

***

## Tips

* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning
* Mount GPS modules on a mast above the frame whenever possible — even 5-10 cm of vertical separation significantly reduces RF and magnetic interference
* Keep GPS antennas away from USB 3.0 cables, ESCs, and radio antennas
* Ensure the GPS antenna has a clear view of the sky — avoid placing batteries, carbon fiber, or other conductive materials above or beside it

***

## Troubleshooting

* **Antenna spacing** — for dual GPS heading setups, ensure a minimum of 30 cm between antennas. Greater separation improves heading accuracy.
* **Test outside** — GPS modules need a clear sky view to get a good fix. Indoor testing will not produce reliable results.
* **Enable logging before arming** — set `LOG_DISARMED` to 1 so GPS data is captured in logs before arming. This helps debug fix quality and satellite count issues.
* **Verify Fix2 messages** — use the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) Bus Monitor to confirm that [`Fix2`](../../knowledge-base/dronecan-messages.md#fix2) messages are being sent by the GPS node(s). If Fix2 messages are absent, check firmware version and CAN wiring.
