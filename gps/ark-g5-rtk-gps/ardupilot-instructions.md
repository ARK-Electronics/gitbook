# ArduPilot Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters on the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data.

{% hint style="warning" %}
Do not set `GPS_AUTO_CONFIG` to 2. The `GPS_AUTO_CONFIG=2` setting only works with GPS modules running AP\_Periph firmware (e.g., the ARK RTK GPS). The G5 runs PX4-based cannode firmware and handles its own GPS configuration internally via the `SEP_*` parameters. Setting this to 2 causes ArduPilot to attempt a parameter handshake with the CAN node that fails silently, blocking all GPS data from being processed.
{% endhint %}

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

### CAN Node Parameter

The `SEP_DUAL_ANT` parameter must be set on the G5H CAN node to enable dual antenna heading. This can be configured using [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SEP_DUAL_ANT` | 3 | Enable Fixed + Float ambiguities (default, recommended) |

The parameter is a bitmask with the following options:

| Bit | Value | Mode |
|-----|-------|------|
| 0 | 1 | Fixed — highest accuracy |
| 1 | 2 | Float — less accurate but more robust |
| Both | 3 | Fixed + Float — receiver uses best available |

{% hint style="info" %}
A reboot of the CAN node is required after changing `SEP_DUAL_ANT`.
{% endhint %}

### Autopilot Parameters

#### GPS Configuration

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

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

## Troubleshooting

* **GPS NO FIX with 0 satellites** — if Mission Planner shows "GPS NO FIX" with 0 sats and no position data, but the DroneCAN GUI Tool shows the GPS is publishing valid fix data on the CAN bus, check `GPS_AUTO_CONFIG`. If it is set to 2, change it to 1 and reboot. Setting it to 2 causes ArduPilot to try to auto-configure the CAN node by requesting parameters that the G5 firmware does not expose under the expected names. This handshake never completes, which blocks all GPS data from being used by the autopilot even though the CAN node is broadcasting valid fixes.
* **Verify RDist** — check the `GPYW.RDist` log field. It should closely match your measured antenna separation. A large discrepancy indicates a problem with the antenna connection or multipath.
* **Heading rejected (OK=0)** — common causes include:
  * Insufficient antenna separation
  * Poor sky view or multipath (e.g., reflections from nearby structures)
  * Incorrect `GPS1_MB_OFS_X/Y/Z` values
  * `EK3_SRC1_YAW` not set to 2 or 3
* **SEP\_OFFS\_YAW parameter** — if the antennas are not aligned along the vehicle's forward axis, set the `SEP_OFFS_YAW` parameter on the G5H node to the clockwise rotation angle (see the [Parameter Reference](./)).
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
