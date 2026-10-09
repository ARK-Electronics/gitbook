# ArduPilot Instructions

## Single GPS Configuration

Connect the ARK G5 RTK GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable.

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

Reboot the flight controller. The GPS should appear as a DroneCAN node and begin reporting position data. The on-board magnetometer will appear as an additional DroneCAN compass and can be enabled via the standard `COMPASS_*` parameters.

### CAN Node Parameters

The node publishes GPS, magnetometer and barometer data with its default parameters. To terminate the bus, fix the node ID, publish IMU data or change the receiver's output rate, PVT modes or dynamics model, see [Node Parameters](firmware.md#node-parameters).

{% hint style="info" %}
On the P3 the ANT2 connector is not active. On the P6 and P8, `SEP_ANT_MODE` `2` turns on dual antenna heading, configured as on the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/ardupilot-instructions.md#dual-antenna-heading-configuration).
{% endhint %}

***

## Troubleshooting

* **GPS NO FIX with 0 satellites** — if Mission Planner shows "GPS NO FIX" with 0 sats and no position data, but the DroneCAN GUI Tool shows the GPS is publishing valid fix data on the CAN bus, check `GPS_AUTO_CONFIG`. If it is set to 2, change it to 1 and reboot. Setting it to 2 causes ArduPilot to try to auto-configure the CAN node by requesting parameters that the G5 firmware does not expose under the expected names. This handshake never completes, which blocks all GPS data from being used by the flight controller even though the CAN node is broadcasting valid fixes.
* **Compass calibration or configuration issues** — if you are having trouble calibrating or configuring the compasses, reset all `COMPASS_*` parameters back to their defaults and reboot the flight controller. Perform the compass calibration only after the GPS is connected.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
