# PX4 Instructions

The ARK RTK Base is a ground-side base station. It connects to _QGroundControl_ over USB-C, and _QGroundControl_ forwards its RTCM corrections to the vehicle over MAVLink. An RTK rover on the vehicle — such as the [ARK RTK GPS](../ark-rtk-gps/README.md) — uses those corrections to reach centimeter-level absolute position.

This requires _QGroundControl_ running on a laptop or PC, and a Wi-Fi or telemetry radio link between it and the vehicle. The Android and iOS builds of _QGroundControl_ do not support RTK.

***

## Setting Up the Base Station

1. Place the base station where it will not be moved, with a clear view of the sky and well away from buildings. Elevating it on a tripod or a roof mount helps.
2. Connect the ARK RTK Base to the _QGroundControl_ laptop over USB-C. It is detected automatically, and an RTK status icon appears in the toolbar alongside the normal GPS icon.
3. Power the vehicle and confirm it is connected to _QGroundControl_.
4. _QGroundControl_ starts Survey-In, the procedure that establishes an accurate position for the base station. This typically takes several minutes. Click the RTK status icon to watch the progress.
5. Survey-In is complete when the RTK status icon turns from red to white and corrections begin streaming. The vehicle's GPS status then reads `3D RTK GPS Lock`.

The minimum Survey-In duration and accuracy are set in the _QGroundControl_ [RTK GPS settings](https://docs.qgroundcontrol.com/master/en/qgc-user-guide/settings_view/general.html#rtk_gps), under **Settings > General > RTK GPS**. After a survey completes you can select _Use Specified Base Position_ and press **Save Current Base Position** to reuse that position and skip Survey-In on later flights.

{% hint style="warning" %}
The base station must not be moved while it is in use. Moving it invalidates the surveyed position, and the corrections it sends will pull the vehicle's position with it.
{% endhint %}

***

## Vehicle Configuration

### Serial GPS

No configuration is needed. PX4 forwards the RTCM corrections it receives over MAVLink directly to the GPS on the serial port.

### DroneCAN GPS

PX4 has to republish the corrections on the CAN bus, and the GPS node has to subscribe to them.

#### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_PUB\_RTCM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_PUB_RTCM) | 1 | Publish `RTCMStream` messages on the CAN bus |

#### CAN Node Parameters

Set the following on the GPS and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNODE_SUB_RTCM` | 1 | Subscribe to `RTCMStream` messages on the CAN bus. Enabled by default on the ARK RTK GPS |

***

## Tuning

The default EKF2 GPS noise parameters assume meter-level accuracy. With RTK, lower [EKF2\_GPS\_P\_NOISE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_P_NOISE) and [EKF2\_GPS\_V\_NOISE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_V_NOISE) to `0.2`.

RTCM streaming needs MAVLink 2, which is the default on recent builds. If corrections do not reach the vehicle over a telemetry radio, confirm [MAV\_PROTO\_VER](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_PROTO_VER) is set to `2` and that the radio firmware is up to date.

***

## Troubleshooting

* **RTK status icon stays red** — Survey-In has not converged. Check that the base station has a clear sky view and has not been moved, and consider relaxing the accuracy target in the _QGroundControl_ RTK GPS settings.
* **Vehicle never reaches RTK Fixed** — confirm corrections are streaming (white RTK status icon) and that the telemetry link has enough bandwidth. When using a DroneCAN GPS on the aircraft, ensure the flight controller sets `UAVCAN_PUB_RTCM` to `1` and the GPS node sets `CANNODE_SUB_RTCM` to `1`.
* See our [GPS Placement](../../knowledge-base/gps-placement.md) guide for mounting best practices, interference sources, and antenna positioning.
