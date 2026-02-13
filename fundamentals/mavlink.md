---
description: >-
  What MAVLink is, how ground stations and companion computers communicate with
  the flight controller, and MAVLink vs XRCE-DDS.
---

# MAVLink

## What is MAVLink?

MAVLink (Micro Air Vehicle Link) is a lightweight messaging protocol for communicating with and between drones. It is the standard protocol used by ground control stations (like QGroundControl and Mission Planner) to talk to flight controllers running PX4 or ArduPilot.

MAVLink handles everything from live telemetry and parameter configuration to mission uploads and command execution.

## How It Works

### Messages and Packets

MAVLink defines hundreds of standardized message types. Each message has a numeric ID and a fixed set of fields. Messages are wrapped in packets that include source and destination addresses, sequence numbers, and checksums.

Common message categories:

| Category | Examples | Purpose |
|----------|----------|---------|
| Telemetry | `HEARTBEAT`, `ATTITUDE`, `GPS_RAW_INT` | Live vehicle state |
| Commands | `COMMAND_LONG`, `COMMAND_INT` | Arm, takeoff, set mode, reboot |
| Parameters | `PARAM_REQUEST_LIST`, `PARAM_SET` | Read and write configuration |
| Missions | `MISSION_ITEM_INT`, `MISSION_COUNT` | Upload and download waypoints |
| File Transfer | `FILE_TRANSFER_PROTOCOL` | Log download, firmware update |

### System and Component IDs

Every device on a MAVLink network has a **system ID** (identifies the vehicle) and a **component ID** (identifies a specific part of that vehicle, like the autopilot, gimbal, or companion computer).

* The flight controller is typically system ID 1, component ID 1
* A ground station is usually system ID 255
* A companion computer might be system ID 1, component ID 191

### Transport Layers

MAVLink is transport-agnostic — it doesn't care how the bytes get from A to B. Common transports:

| Transport | Use Case |
|-----------|----------|
| [UART](serial-communication-uart.md) serial | Telemetry radios, direct FC-to-companion links |
| UDP | Ethernet/Wi-Fi connections (QGC default: port 14550) |
| TCP | Stable connections over network links |
| USB | Direct QGC connection to flight controller |

### MAVLink Versions

* **MAVLink v1** — original protocol, 8 bytes overhead per message
* **MAVLink v2** — current standard, supports message signing, extensible fields, and 16-bit message IDs. PX4 and ArduPilot both default to v2.

## MAVLink vs XRCE-DDS

PX4 supports two protocols for companion computer communication:

| | MAVLink | XRCE-DDS (uORB over DDS) |
|---|---------|--------------------------|
| **Maturity** | Battle-tested, supported everywhere | Newer, actively evolving |
| **Ecosystem** | QGC, Mission Planner, pymavlink, MAVSDK | ROS 2 native integration |
| **Data model** | Fixed message definitions | PX4 uORB topics published as ROS 2 topics |
| **Best for** | GCS communication, telemetry radios, simple companion scripts | ROS 2 applications, high-bandwidth sensor data |
| **Transport** | Serial, UDP, TCP | Serial (Micro XRCE-DDS Agent) |

{% hint style="info" %}
**Which should I use?** If you're building a ROS 2 application on a companion computer, use XRCE-DDS — it gives you direct access to PX4's internal topics as ROS 2 messages. For everything else (GCS, telemetry, simple offboard control), MAVLink is the standard choice.
{% endhint %}

## How ARK Products Use It

### Ground Station Communication

Flight controllers like the [ARKV6X](../flight-controller/arkv6x/README.md) and [ARK FPV](../flight-controller/ark-fpv/README.md) use MAVLink to communicate with QGroundControl or Mission Planner over USB, telemetry radio, or network connections.

### Companion Computer Links

The [ARK Jetson PAB Carrier](../flight-controller/ark-jetson-pab-carrier/README.md) and [ARK Pi6X Flow](../flight-controller/ark-pi6x-flow/README.md) use both MAVLink and XRCE-DDS for communication between the companion computer (Jetson or Pi) and the integrated flight controller:

* **MAVLink** — used by the [QGroundControl connection](../flight-controller/ark-jetson-pab-carrier/autopilot-connections/qgroundcontrol-connection.md) and [MissionPlanner connection](../flight-controller/ark-jetson-pab-carrier/autopilot-connections/missionplanner-ardupilot-connection.md) forwarded from the companion computer
* **XRCE-DDS** — used by [ROS 2 applications](../ros2-and-px4/ros2-and-px4-teleop-example.md) running on the companion computer

### MAVCAN

Ardupilot supports MAVLink can tunnel [CAN bus](can-bus.md) traffic over any MAVLink link using the MAVCAN protocol. This lets you use the [DroneCAN GUI Tool](../resources/dronecan-gui-tool-guide.md) to manage CAN devices remotely — even over a telemetry radio link. PX4 does not yet support this.

## Common Pitfalls

* **Baud rate mismatch** — MAVLink over serial requires matching baud rates on both ends. PX4 TELEM ports default to 57600 baud. If QGC shows "Communication Lost," check the baud rate first.
* **Same port, multiple connections** — only one application can open a serial port at a time. If MAVProxy is already connected, QGC cannot connect to the same port.
* **Firewall blocking UDP** — QGC listens on UDP port 14550 by default. Firewalls or VPNs can block these packets silently.
* **System ID conflicts** — if two vehicles share the same system ID on the same network, the GCS will merge their telemetry into a confusing mess. Each vehicle needs a unique system ID.
* **MAVLink vs XRCE-DDS confusion** — these are separate protocols on separate interfaces. You cannot connect QGC to an XRCE-DDS port or subscribe to ROS 2 topics over MAVLink.
* **Baudrate and throughput** — Ensure the baudrate is high enough for the configured mavlink throughput. Baudrates at or above 921600 tend to only work with very short wires, otherwise hardware flow control must be used.

## Further Reading

* [MAVLink Developer Guide](https://mavlink.io/en/)
* [PX4 MAVLink Documentation](https://docs.px4.io/main/en/middleware/mavlink.html)
* [PX4 XRCE-DDS (ROS 2)](https://docs.px4.io/main/en/middleware/uxrce_dds.html)
* [QGroundControl User Guide](http://qgroundcontrol.com/getting_started/)
* [MAVSDK — MAVLink SDK](https://mavsdk.mavlink.io/main/en/)
