# ArduPilot Instructions

Connect the ARK TESEO GPS to the autopilot's CAN port using a standard 4-pin JST-GH cable. Set the following parameters on the autopilot:

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

Reboot the autopilot. The GPS should appear as a DroneCAN node and begin reporting position data. The on-board IIS2MDC magnetometer will appear as an additional DroneCAN compass and can be enabled via the standard `COMPASS_*` parameters.

{% hint style="warning" %}
Do not set `GPS_AUTO_CONFIG` to 2. The `GPS_AUTO_CONFIG=2` setting only works with GPS modules running AP\_Periph firmware (e.g., the ARK RTK GPS). The TESEO runs PX4-based cannode firmware and handles its own GPS configuration internally via the `TESEO_*` parameters. Setting this to 2 causes ArduPilot to attempt a parameter handshake with the CAN node that fails silently, blocking all GPS data from being processed.
{% endhint %}

## Constellation Selection

Constellation selection is configured via the `TESEO_*` parameters on the GPS DroneCAN node, not on the autopilot. See the [Parameter Reference](./#parameter-reference) on the landing page for details.
***

## Troubleshooting

* **GPS NO FIX with 0 satellites** — if Mission Planner shows "GPS NO FIX" with 0 sats and no position data, but the DroneCAN GUI Tool shows the GPS is publishing valid fix data on the CAN bus, check `GPS_AUTO_CONFIG`. If it is set to 2, change it to 1 and reboot. See the warning above for why.
* **Compass calibration or configuration issues** — if you are having trouble calibrating or configuring the compasses, reset all `COMPASS_*` parameters back to their defaults and reboot the autopilot. Perform the compass calibration only after the GPS is connected.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
