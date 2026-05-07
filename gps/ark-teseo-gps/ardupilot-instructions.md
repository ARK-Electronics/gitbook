# ArduPilot Instructions

## Single GPS Configuration

Connect the ARK TESEO GPS to the flight controller's CAN port using a standard 4-pin JST-GH cable.

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Enable auto-config for serial GPSes only |

{% hint style="warning" %}
Do not set `GPS_AUTO_CONFIG` to 2. The `GPS_AUTO_CONFIG=2` setting only works with GPS modules running AP\_Periph firmware (e.g., the ARK RTK GPS). The TESEO runs PX4-based cannode firmware and handles its own GPS configuration internally via the `TESEO_*` parameters. Setting this to 2 causes ArduPilot to attempt a parameter handshake with the CAN node that fails silently, blocking all GPS data from being processed.
{% endhint %}

Reboot the flight controller. The GPS should appear as a DroneCAN node and begin reporting position data. The on-board IIS2MDC magnetometer will appear as an additional DroneCAN compass and can be enabled via the standard `COMPASS_*` parameters.

### CAN Node Parameters

Set the following on the GPS and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_PUB_BARO` | Set to `1` to publish barometer messages on the CAN bus |
| `CANNODE_PUB_IMU` | Set to `1` to publish [`RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) messages on the CAN bus |
| `TESEO_FWUPD` | Set to `1` to force the cannode to re-flash the embedded LIV4F firmware on the next boot. The cannode auto-updates the LIV4F whenever the embedded version differs from what is on the GPS chip — this parameter is only needed to force a re-flash without a version change. Auto-cleared back to `0` after a successful update |

***

## Constellation Selection

The Teseo-LIV4F can track up to **four GNSS constellations simultaneously**. Enabling more than four has no effect — pick the four that match your operating region. SBAS does not count toward this limit. Configure these on the GPS using the same method as the [CAN Node Parameters](#can-node-parameters) above.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `TESEO_GPS` | 1 | Enable the GPS (USA) constellation |
| `TESEO_GLONASS` | 1 | Enable the GLONASS (Russia) constellation |
| `TESEO_GALILEO` | 1 | Enable the Galileo (EU) constellation |
| `TESEO_BEIDOU` | 1 | Enable the BeiDou (China) constellation |
| `TESEO_QZSS` | 0 | Enable the QZSS (Japan) constellation |
| `TESEO_IRNSS` | 0 | Enable the IRNSS / NavIC (India) constellation |
| `TESEO_SBAS` | 1 | Enable SBAS (Satellite-Based Augmentation System) |

***

## Troubleshooting

* **GPS NO FIX with 0 satellites** — if Mission Planner shows "GPS NO FIX" with 0 sats and no position data, but the DroneCAN GUI Tool shows the GPS is publishing valid fix data on the CAN bus, check `GPS_AUTO_CONFIG`. If it is set to 2, change it to 1 and reboot. See the warning above for why.
* **Compass calibration or configuration issues** — if you are having trouble calibrating or configuring the compasses, reset all `COMPASS_*` parameters back to their defaults and reboot the flight controller. Perform the compass calibration only after the GPS is connected.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
