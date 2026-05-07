# ArduPilot Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable.

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

{% hint style="warning" %}
Do not set `GPS_AUTO_CONFIG` to 2. The `GPS_AUTO_CONFIG=2` setting only works with GPS modules running AP\_Periph firmware (e.g., the ARK RTK GPS). The G5 runs PX4-based cannode firmware and handles its own GPS configuration internally via the `SEP_*` parameters. Setting this to 2 causes ArduPilot to attempt a parameter handshake with the CAN node that fails silently, blocking all GPS data from being processed.
{% endhint %}

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data. The on-board magnetometer will appear as an additional DroneCAN compass and can be enabled via the standard `COMPASS_*` parameters.

### CAN Node Parameters

Set the following on the GPS via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) and reboot the node.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_PUB_BARO` | Set to `1` to publish barometer messages on the CAN bus |
| `CANNODE_PUB_IMU` | Set to `1` to publish `RawIMU` messages on the CAN bus |
| `SEP_OUT_RATE` | Output rate for GNSS data messages: `-1` = OnChange, or `50` / `100` / `200` / `500` ms |
| `SEP_PVT_MODE` | Bitmask of allowed PVT modes for Rover operation. Bits: `1` = StandAlone, `2` = DGNSS, `4` = RTKFloat, `8` = RTKFixed. Default `15` (all). The receiver uses the most accurate mode available |
| `SEP_RCV_DYN` | Receiver dynamics model: `0` = Static, `1` = Quasistatic, `2` = Pedestrian, `3` = Automotive, `4` = RaceCar, `5` = HeavyMachinery, `6` = UAV (default), `7` = Unlimited |

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

### Flight Controller Parameters

Apply the [Single GPS Configuration](#single-gps-configuration) flight controller parameters above, then add the following and reboot the autopilot.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `GPS1_MB_TYPE` | 1 | RelativeToCustomBase — tells ArduPilot to use the antenna offsets below |
| `GPS1_MB_OFS_X` | _(meters)_ | Antenna offset from ANT2 to MAIN, positive if MAIN is forward |
| `GPS1_MB_OFS_Y` | _(meters)_ | Antenna offset from ANT2 to MAIN, positive if MAIN is to the right |
| `GPS1_MB_OFS_Z` | _(meters)_ | Antenna offset from ANT2 to MAIN, positive if MAIN is below |
| `AHRS_EKF_TYPE` | 3 | Use EKF3 |
| `EK2_ENABLE` | 0 | Disable EKF2 |
| `EK3_ENABLE` | 1 | Enable EKF3 |
| `EK3_SRC1_YAW` | 2 | GPS yaw (or `3` for GPS with compass fallback) |

{% hint style="info" %}
The `GPS1_MB_OFS_*` offsets describe the position of MAIN relative to ANT2 in the vehicle body frame. Measure the physical separation between the two antenna phase centers and enter the values in meters.
{% endhint %}

### CAN Node Parameters

Apply the [Single GPS Configuration](#single-gps-configuration) CAN node parameters above, then add the following on the G5H via the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md) and reboot the node.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `SEP_DUAL_ANT` | 3 | Enable dual antenna heading. Bitmask: `1` = Fixed (highest accuracy), `2` = Float (more robust), `3` = Fixed + Float (default, recommended — receiver uses best available) |

#### Optional

| Parameter | Description |
|-----------|-------------|
| `SEP_OFFS_YAW` | Clockwise rotation in degrees from the vehicle forward axis to the MAIN→ANT2 baseline. Range: `-360` to `360`. Use this if the antennas are not aligned along the vehicle's forward axis |
| `SEP_OFFS_PITCH` | Pitch offset in degrees to compensate for vertical mounting differences between MAIN and ANT2. Range: `-90` to `90`. A positive pitch indicates the MAIN antenna is mounted lower than ANT2 |

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
* **Yaw alignment** — if the antennas are not aligned along the vehicle's forward axis, set the `SEP_OFFS_YAW` parameter on the G5H node to the clockwise rotation angle.
* **Compass calibration or configuration issues** — if you are having trouble calibrating or configuring the compasses, reset all `COMPASS_*` parameters back to their defaults and reboot the autopilot. Perform the compass calibration only after the GPS is connected.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
