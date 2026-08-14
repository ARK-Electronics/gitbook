---
description: What each ARK-OS service does.
---

# Services

ARK-OS services are system-level [systemd services](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) running as the device user — `jetson` on Jetson carriers, `pi` on Pi carriers. Manage them, including configuration editing, from the ARK-UI **Services** page or with `systemctl`. Configuration files live under `/etc/ark-os/`.

## Enabled by Default

**mavlink-router** routes MAVLink between the flight controller (USB, `/dev/ttyACM0`) and user-defined UDP/TCP endpoints such as QGroundControl. Default config: [main.conf](https://github.com/ARK-Electronics/ARK-OS/blob/main/services/mavlink-router/main.conf).

**rtsp-server** streams the first CSI camera over RTSP at `rtsp://<hostname>.local:5600/camera1` using gstreamer.

**go2rtc** restreams the RTSP feed to the browser over WebRTC for the ARK-UI **Video** page.

**ark-ui-backend**, **system-manager**, **service-manager**, **connection-manager**, **autopilot-manager** are the REST APIs behind the ARK-UI (hidden from the Services page).

**jetson-can** brings up the Jetson CAN interface (`can0`). Jetson carriers only.

## Optional (installed, disabled by default)

Enable from the ARK-UI Services page or with `systemctl enable --now <service>`.

**dds-agent** bridges PX4 uORB topics to ROS 2 by running the [Micro XRCE-DDS Agent](https://github.com/eProsima/Micro-XRCE-DDS-Agent) on the high-speed serial connection to the flight controller — `/dev/ttyTHS1` on Jetson carriers, `/dev/ttyAMA4` on the Pi6X Flow, both wired to TELEM2 at 3 Mbps. The bridged topics are defined in [PX4's dds\_topics.yaml](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/uxrce_dds_client/dds_topics.yaml). Set these PX4 parameters:

| Parameter       | Value   | Description  |
| --------------- | ------- | ------------ |
| UXRCE\_DDS\_CFG | 102     | TELEM 2      |
| SER\_TEL2\_BAUD | 3000000 | 3 Mbps 8N1   |

**logloader** downloads PX4 `.ulg` flight logs from the flight controller's SD card over MAVLink FTP and optionally uploads them to [Flight Review](https://review.px4.io/). Driven from the ARK-UI **Logs** page.

**flight-review** hosts a local [PX4 Flight Review](https://github.com/PX4/flight_review) server at `http://<hostname>.local/flight-review` for the logs downloaded by logloader.

**polaris** receives network RTK corrections from the [Point One Polaris](https://pointonenav.com/polaris) service (subscription required) and publishes them to the flight controller over MAVLink.

**pointperfect** receives GNSS corrections from the [u-blox PointPerfect](https://www.u-blox.com/en/product/pointperfect) NTRIP service and publishes them to the flight controller over MAVLink. For u-blox receivers it can also request AssistNow start-up assistance for a faster first fix.

**rid-transmitter** broadcasts Remote ID over Bluetooth per ASTM F3411 (requires a Bluetooth 5.x capable radio).
