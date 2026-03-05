# ArduPilot Instructions

## Firmware Setup

The ARK G5 RTK GPS ships with PX4 CANnode firmware by default. For use with ArduPilot, we recommend flashing [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) (ArduPilot Peripheral) firmware. AP\_Periph is the well-tested configuration for DroneCAN GPS modules with ArduPilot.

### Flashing AP\_Periph

1. Download `AP_Periph.apj` for the ARK G5 RTK GPS from the [ArduPilot firmware server](https://firmware.ardupilot.org/AP_Periph/stable/ARK_G5_GPS/)
2. Connect to the ARK G5 RTK GPS using the DroneCAN GUI Tool — see our [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for connection and firmware upload instructions
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

Connect the ARK G5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters on the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 2 | Auto-configure DroneCAN GPS |

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data.

***

## Dual Antenna Heading Configuration (G5H Only)

{% hint style="warning" %}
Dual antenna heading requires the **ARK G5H RTK GPS** (with the Septentrio mosaic-G5 P3H module). The standard ARK G5 RTK GPS (P3 module) only supports a single antenna and cannot provide heading.
{% endhint %}

The G5H provides compass-free yaw estimation using two GNSS antennas on a single DroneCAN node. Unlike the ARK RTK GPS dual-GPS heading setup (which uses two separate u-blox F9P nodes with `GPS1_TYPE=22` and `GPS2_TYPE=23`), the G5H handles the moving baseline calculation internally within the Septentrio mosaic-G5 module and reports the heading over DroneCAN as a single GPS.

### Hardware Setup

* Connect the ARK G5H RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable
* Connect antennas to both the MAIN and ANT2 SMA connectors
* Mount the antennas with a minimum of **30 cm separation** (more is better for heading accuracy)

### Autopilot Parameters

#### GPS Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 2 | Auto-configure DroneCAN GPS |

{% hint style="info" %}
Use `GPS1_TYPE = 9` (standard DroneCAN), **not** type 22/23 (moving baseline base/rover). The G5H is a single DroneCAN node that computes the heading internally — it is not a two-node moving baseline setup.
{% endhint %}

#### Moving Baseline Offsets

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS1_MB_TYPE` | 1 | RelativeToCustomBase — tells ArduPilot to use the antenna offsets below |
| `GPS1_MB_OFS_X` | _(meters)_ | Antenna offset from MAIN to ANT2, forward |
| `GPS1_MB_OFS_Y` | _(meters)_ | Antenna offset from MAIN to ANT2, right |
| `GPS1_MB_OFS_Z` | _(meters)_ | Antenna offset from MAIN to ANT2, down |

{% hint style="info" %}
The offsets describe the position of ANT2 relative to MAIN in the vehicle body frame (forward/right/down). Measure the physical separation between the two antenna phase centers and enter the values in meters.
{% endhint %}

#### EKF Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `AHRS_EKF_TYPE` | 3 | Use EKF3 |
| `EK2_ENABLE` | 0 | Disable EKF2 |
| `EK3_ENABLE` | 1 | Enable EKF3 |
| `EK3_SRC1_YAW` | 2 | GPS yaw (or 3 for GPS with compass fallback) |

Reboot the autopilot after setting these parameters.

***

## Verifying Heading in Logs

Once the G5H is reporting heading, you can verify it in the flight logs by examining the **GPYW** (GPS Yaw) log message:

| Field | Description |
|-------|-------------|
| `RHD` | Reported heading in degrees |
| `RDist` | Reported baseline distance between antennas (meters) — should match your physical antenna separation |
| `RDown` | Reported vertical offset between antennas (meters) |
| `OK` | 1 if the heading is valid and being used by the EKF, 0 if rejected |

If `OK` is 0, the EKF is rejecting the GPS yaw. See the troubleshooting section below for common causes.

***

## Tips and Troubleshooting

* **Antenna separation** — ensure a minimum of 30 cm between the MAIN and ANT2 antennas. Greater separation improves heading accuracy and reduces susceptibility to multipath errors.
* **Clear sky view** — both antennas need an unobstructed view of the sky. Heading estimation requires RTK-level carrier phase measurements, which are more sensitive to signal quality than standard positioning.
* **Verify RDist** — check the `GPYW.RDist` log field. It should closely match your measured antenna separation. A large discrepancy indicates a problem with the antenna connection or multipath.
* **Heading rejected (OK=0)** — common causes include:
  * Insufficient antenna separation
  * Poor sky view or multipath (e.g., reflections from nearby structures)
  * Incorrect `GPS1_MB_OFS_X/Y/Z` values
  * `EK3_SRC1_YAW` not set to 2 or 3
* **SEP\_OFFS\_YAW parameter** — if the antennas are not aligned along the vehicle's forward axis, set the `SEP_OFFS_YAW` parameter on the G5H node to the clockwise rotation angle (see the [Parameter Reference](./)).
* **Test outside** — GPS heading requires a clear sky view. Indoor testing will not produce reliable results.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
