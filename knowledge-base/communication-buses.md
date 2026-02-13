---
description: >-
  I2C and SPI basics, a comparison of UART vs I2C vs SPI vs CAN, and why CAN
  wins for drones.
---

# Communication Buses

## What Are Communication Buses?

A communication bus is a set of shared wires and protocols that allow multiple chips or devices to exchange data. Drones use several different buses, each with different trade-offs in speed, distance, noise immunity, and wiring complexity.

This page covers **I2C** and **SPI** — two buses commonly found inside or very near the flight controller. For the other major buses, see [UART](serial-communication-uart.md) and [CAN Bus](can-bus.md).

## How They Work

### I2C (Inter-Integrated Circuit)

I2C is a two-wire bus that supports multiple devices on the same pair of wires. Each device has a unique 7-bit address, and the controller (flight controller) selects which device to talk to by address.

| Signal | Purpose |
|--------|---------|
| SCL | Clock — driven by the controller |
| SDA | Data — bidirectional, shared by all devices |

**Key characteristics:**

* **Multi-device** — many devices share two wires (plus power and ground)
* **Addressable** — each device has a hardware address (e.g., 0x76 for a barometer, 0x1E for a magnetometer)
* **Speed** — typically 100 kHz (standard) or 400 kHz (fast mode)
* **Distance** — very short, typically on-board or a few centimeters. Unreliable beyond 10–15 cm on a drone due to capacitance and noise.
* **Pull-up resistors** — SDA and SCL require pull-up resistors to 3.3V. These are usually included on the flight controller board.

I2C is used for on-board sensors (barometers, magnetometers, IMUs) and short-range external connections via the [Pixhawk Standard I2C connector](connectors-and-wiring.md) (4-pin JST-GH).

### SPI (Serial Peripheral Interface)

SPI is a high-speed bus that uses separate wires for data in each direction plus a chip-select line for each device.

| Signal | Purpose |
|--------|---------|
| SCLK | Clock — driven by the controller |
| MOSI | Master Out, Slave In — data from controller to device |
| MISO | Master In, Slave Out — data from device to controller |
| CS | Chip Select — one per device, active low |

**Key characteristics:**

* **Fast** — typically 1–10 MHz, some devices support 20+ MHz
* **Full duplex** — data flows in both directions simultaneously
* **No addressing** — each device needs its own CS line, so wiring grows with each added device
* **Short range** — on-board only, not designed for inter-board connections
* **No bus contention** — only the selected device responds, making it very reliable on a PCB

SPI is used for the primary IMU, high-speed flash memory, and other on-board sensors that need fast data transfer.

## Comparison: UART vs I2C vs SPI vs CAN

| Feature | UART | I2C | SPI | CAN |
|---------|------|-----|-----|-----|
| **Wires (data)** | 2 (TX, RX) | 2 (SCL, SDA) | 3 + 1/device (SCLK, MOSI, MISO, CS) | 2 (CAN\_H, CAN\_L) |
| **Topology** | Point-to-point | Multi-drop bus | Multi-drop (with CS lines) | Multi-drop bus |
| **Speed** | Up to 921600 bps typical | 100–400 kHz | 1–20 MHz | 1 Mbps |
| **Distance** | Meters (with proper levels) | Centimeters | On-board only | Tens of meters |
| **Noise immunity** | Low (single-ended) | Low (single-ended) | Low (single-ended) | **High (differential)** |
| **Devices per bus** | 2 (point-to-point) | Up to 127 (by address) | Limited by CS lines | Up to 127 (by node ID) |
| **Connector** | 6-pin JST-GH | 4-pin JST-GH | 7-pin JST-GH | 4-pin JST-GH |
| **Hot-pluggable** | Yes | No (can lock bus) | No | Yes |
| **Drone use case** | Debug console, telemetry, GPS | On-board sensors, short-range external | Primary IMU, flash | **Peripheral sensors, GPS, power** |

### Why CAN Wins for Drone Peripherals

For any sensor or module that is not on the flight controller PCB itself, [CAN bus](can-bus.md) is the clear choice:

1. **Noise immunity** — differential signaling rejects the electromagnetic noise from motors and ESCs that plagues I2C
2. **Distance** — works reliably over the cable lengths found on real drones (10 cm to 1+ meter), where I2C fails
3. **Hot-pluggable** — devices can be connected and disconnected without locking the bus or requiring a reboot
4. **Power delivery** — 5V power and data on the same 4-pin cable
5. **Firmware updates** — DroneCAN supports over-the-bus firmware updates, no debug adapter needed

I2C and SPI remain critical for on-board sensors where their speed advantages and tight PCB integration make them the right choice. The pattern is:

* **On the board** → SPI (fastest) or I2C (fewer pins)
* **Off the board** → CAN (robust and long-distance)

## How ARK Products Use It

### I2C

* [ARK CANnode](../sensor/ark-cannode/README.md) provides a Pixhawk Standard I2C connector to bridge non-CAN I2C sensors onto the [CAN bus](can-bus.md)
* Flight controllers use I2C internally for barometers and secondary magnetometers
* External I2C is available on ARK flight controllers but not recommended for long cable runs

### SPI

* All ARK flight controllers use SPI for the primary IMU (e.g., Bosch BMI088, Invensense ICM-42688-P)
* [ARK CANnode](../sensor/ark-cannode/README.md) provides a Pixhawk Standard SPI connector for bridging SPI sensors onto CAN
* SPI connections are on-board only — there are no long SPI cables in a typical ARK build

### CAN

* Most external ARK sensors use [DroneCAN](can-bus.md) as their primary interface
* This is by design — CAN's noise immunity and robustness make it the right bus for inter-board communication on a drone

## Common Pitfalls

* **Using I2C for external sensors on a drone** — I2C works perfectly on a bench but fails intermittently in flight due to motor noise and cable capacitance. Use CAN for any sensor that isn't on the flight controller board.
* **I2C bus lockup** — if an I2C device holds SDA low (due to noise, interrupted transfer, or a bug), the entire bus locks up. The only recovery is usually a power cycle. CAN does not have this failure mode.
* **Address conflicts on I2C** — two devices with the same I2C address cannot share a bus. Some sensors have configurable addresses, but many do not.
* **Missing I2C pull-ups** — if you connect an external I2C device to a port that doesn't have pull-up resistors, communication will fail. The Pixhawk Standard I2C port on ARK boards includes pull-ups.
* **SPI chip-select wiring** — each SPI device needs its own CS line wired correctly. A floating or mis-routed CS line will cause data corruption or no communication.

## Further Reading

* [CAN Bus](can-bus.md) — detailed CAN bus reference
* [Serial Communication (UART)](serial-communication-uart.md) — UART protocol details
* [Connectors and Wiring](connectors-and-wiring.md) — Pixhawk standard connector pinouts
* [I2C Specification (NXP)](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)
* [SPI Overview (Analog Devices)](https://www.analog.com/en/analog-dialogue/articles/introduction-to-spi-interface.html)
