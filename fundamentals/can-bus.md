---
description: >-
  CAN bus fundamentals, differential signaling, termination, DroneCAN protocol,
  and 4-pin JST-GH wiring.
---

# CAN Bus

## What is CAN Bus?

CAN (Controller Area Network) is a robust communication bus designed for noisy environments. Originally developed for automobiles, it is the standard for connecting sensors, GPS modules, and other peripherals in the Pixhawk drone ecosystem.

CAN uses **differential signaling** over a twisted pair, which makes it highly resistant to electromagnetic interference — critical on a drone where motors, ESCs, and radios generate significant noise.

## How It Works

### Differential Signaling

CAN uses two wires, **CAN\_H** (high) and **CAN\_L** (low), that carry the same signal in opposite polarities. The receiver reads the _difference_ between the two, which cancels out any noise that affects both wires equally.

| Bus State | CAN\_H | CAN\_L | Difference |
|-----------|--------|--------|------------|
| Recessive (1) | 2.5V | 2.5V | 0V |
| Dominant (0) | 3.5V | 1.5V | 2V |

This is why CAN is so much more reliable than [UART](serial-communication-uart.md) or [I2C](communication-buses.md) in electrically noisy environments.

### Bus Topology

CAN is a true **multi-drop bus** — all devices share the same two wires. Any device can transmit, and all devices receive every message. Message priority is handled by arbitration built into the protocol.

```
[Flight Controller] ──── CAN_H/CAN_L ──── [GPS] ──── [Flow Sensor] ──── [Mag]
       120Ω                                                               120Ω
```

Devices are daisy-chained, with two 120-ohm termination resistors at each end of the bus.

### Termination

A CAN bus requires a **120-ohm termination resistor** at each physical end of the bus. Without proper termination, signal reflections corrupt data and cause intermittent communication failures.

Most ARK DroneCAN products have a software-configurable built-in termination resistor controlled by the `CANNODE_TERM` parameter. Only the two devices at the physical ends of the bus should have termination enabled.

{% hint style="info" %}
**Rule of thumb:** if you measure the resistance between CAN\_H and CAN\_L with everything powered off, you should see approximately 60 ohms (two 120-ohm resistors in parallel).
{% endhint %}

### Bit Rate

The Pixhawk standard CAN bit rate is **1 Mbps** (1000000 bps). This is the default for PX4, ArduPilot, and all ARK DroneCAN devices. Unlike UART, you almost never need to change the CAN bit rate.

### 4-Pin JST-GH Connector (Pixhawk Standard CAN)

All ARK DroneCAN products use the Pixhawk Standard CAN connector:

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0V |
| 2 | CAN\_H | — |
| 3 | CAN\_L | — |
| 4 | GND | GND |

Devices are connected in a daisy chain using these 4-pin JST-GH cables. Most ARK DroneCAN products have **two CAN connectors** so you can chain one into the next without a splitter.

### DroneCAN Protocol

DroneCAN (formerly UAVCAN v0) is the application-layer protocol that runs on top of CAN bus. It defines standard message types for sensor data, firmware updates, parameter configuration, and node management.

Key DroneCAN concepts:

* **Node ID** — each device on the bus has a unique ID (1–127). PX4 and ArduPilot assign these automatically by default.
* **Message types** — [standardized data structures](https://dronecan.github.io/Specification/7._List_of_standard_data_types/) (e.g., `uavcan.equipment.ahrs.RawIMU`, `uavcan.equipment.gnss.Fix2`) that all compliant devices understand.
* **Dynamic node allocation** — devices can obtain a node ID automatically from the flight controller on first boot.
* **Firmware update** — the flight controller or a tool like the [DroneCAN GUI Tool](../resources/dronecan-gui-tool-guide.md) can push firmware updates to any node on the bus.

## Common Pitfalls

* **Missing termination** — the most common CAN issue. If devices appear and disappear intermittently, check that exactly two nodes have termination enabled (one at each end of the bus).
* **All nodes terminated** — enabling termination on every device drops the bus resistance too low, causing signal distortion. Only the two end nodes should be terminated.
* **Wrong bit rate** — all devices must use the same bit rate (1 Mbps). A device configured for a different rate will be invisible on the bus.
* **Node ID conflicts** — two devices with the same node ID will interfere with each other. Dynamic node allocation usually prevents this, but manually assigned IDs can collide.
* **Cable length** — CAN is robust but not unlimited. For runs over 1 meter, use quality twisted-pair cable and ensure proper termination.
* **5V power through CAN** — the CAN connector provides 5V power. If a device draws too much current through the cable, the voltage can drop below the minimum for reliable operation. Check the power budget for your bus.

## Further Reading

* [DroneCAN GUI Tool Guide](../resources/dronecan-gui-tool-guide.md) — how to inspect, configure, and update firmware on DroneCAN devices
* [PX4 DroneCAN Documentation](https://docs.px4.io/main/en/dronecan/)
* [PX4 CAN Wiring Guide](https://docs.px4.io/main/en/can/#wiring)
* [DroneCAN Specification](https://dronecan.github.io/Specification/)
* [Connectors and Wiring](connectors-and-wiring.md) — details on the JST-GH connectors used for CAN
