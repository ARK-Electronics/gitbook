---
description: What each ARK-OS service does.
---

# Services

ARK-OS services are system-level [systemd services](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) running as the `pi` user. Manage them — including configuration editing — from the [ARK-UI](http://just-a-pi.local) **Services** page, or with `systemctl`. Configuration files live under `/etc/ark-os/`. Services that talk to a flight controller expect one connected over USB.

## Enabled by Default

**mavlink-router** routes MAVLink between a USB-connected flight controller (`/dev/ttyACM0`) and user-defined UDP/TCP endpoints such as QGroundControl. Default config: [main.conf](https://github.com/ARK-Electronics/ARK-OS/blob/main/services/mavlink-router/main.conf).

**rtsp-server** streams the first CSI camera over RTSP at `rtsp://just-a-pi.local:5600/camera1` using gstreamer.

**go2rtc** restreams the RTSP feed to the browser over WebRTC for the ARK-UI **Video** page.

**ark-ui-backend**, **system-manager**, **service-manager**, **connection-manager**, **autopilot-manager** are the REST APIs behind the ARK-UI (hidden from the Services page).

## Optional (installed, disabled by default)

Enable from the ARK-UI Services page or with `systemctl enable --now <service>`.

**dds-agent** bridges PX4 uORB topics to ROS 2 by running the [Micro XRCE-DDS Agent](https://github.com/eProsima/Micro-XRCE-DDS-Agent) on a serial connection to a flight controller. The bridged topics are defined in [PX4's dds\_topics.yaml](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/uxrce_dds_client/dds_topics.yaml).

**logloader** downloads PX4 `.ulg` flight logs from the flight controller's SD card over MAVLink FTP and optionally uploads them to [Flight Review](https://review.px4.io/). Driven from the ARK-UI **Logs** page.

**flight-review** hosts a local [PX4 Flight Review](https://github.com/PX4/flight_review) server at [http://just-a-pi.local/flight-review](http://just-a-pi.local/flight-review) for the logs downloaded by logloader.

**polaris** receives network RTK corrections from the [Point One Polaris](https://pointonenav.com/polaris) service (subscription required) and publishes them to the flight controller over MAVLink.

**pointperfect** receives GNSS corrections from the [u-blox PointPerfect](https://www.u-blox.com/en/product/pointperfect) NTRIP service and publishes them to the flight controller over MAVLink. For u-blox receivers it can also request AssistNow start-up assistance for a faster first fix.
