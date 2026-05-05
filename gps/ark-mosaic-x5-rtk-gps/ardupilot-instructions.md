# ArduPilot Instructions

## Single GPS Configuration

Connect the ARK MOSAIC-X5 RTK GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters on the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data.

***

## Troubleshooting

* **GPS NO FIX with 0 satellites** — if Mission Planner shows "GPS NO FIX" with 0 sats and no position data, but the DroneCAN GUI Tool shows the GPS is publishing valid fix data on the CAN bus, check `GPS_AUTO_CONFIG`. If it is set to 2, change it to 1 and reboot. Setting it to 2 causes ArduPilot to try to auto-configure the CAN node by requesting parameters that the Mosaic-X5 firmware does not expose under the expected names. This handshake never completes, which blocks all GPS data from being used by the autopilot even though the CAN node is broadcasting valid fixes.
* **Compass calibration or configuration issues** — if you are having trouble calibrating or configuring the compasses, reset all `COMPASS_*` parameters back to their defaults and reboot the autopilot. Perform the compass calibration only after the GPS is connected.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
