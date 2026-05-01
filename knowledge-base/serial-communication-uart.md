---
description: UART basics, RX/TX cross-wiring, baud rates, and using the debug console.
---

# Serial Communication (UART)

## What is UART?

UART (Universal Asynchronous Receiver/Transmitter) is a simple serial communication protocol used to send data between two devices over two wires. It is the most common way to access the debug console on a flight controller, connect GPS modules, and link telemetry radios.

Unlike [SPI or I2C](communication-buses.md), UART is point-to-point — it connects exactly two devices with no shared bus or addressing.

## How It Works

### Signals

A UART connection uses two data lines plus ground:

| Signal | Purpose                                |
| ------ | -------------------------------------- |
| TX     | Transmit — data output from the device |
| RX     | Receive — data input to the device     |
| GND    | Common ground reference                |

### RX/TX Cross-Wiring

This is the single most common wiring mistake in drone electronics: **TX on one device connects to RX on the other, and vice versa.**

```
Device A          Device B
  TX  ──────────→  RX
  RX  ←──────────  TX
  GND ────────────  GND
```

One device's transmit line must feed into the other device's receive line. If you connect TX to TX, neither device hears anything.

{% hint style="warning" %}
**The #1 UART debugging step:** if you get no data, swap TX and RX. This fixes the problem more often than not.
{% endhint %}

### Baud Rate

Both devices must agree on the same data speed, called the **baud rate** (bits per second). If the baud rates don't match, the receiving device sees garbage characters.

Common baud rates in the ARK/PX4 ecosystem:

| Baud Rate | Typical Use                                                   |
| --------- | ------------------------------------------------------------- |
| 9600      | Some GPS modules (default)                                    |
| 57600     | PX4 debug console (NuttX shell)                               |
| 115200    | MAVLink telemetry, some GPS modules                           |
| 921600    | High-speed MAVLink, companion computer links (see note below) |

{% hint style="warning" %}
**921600 baud and above requires hardware flow control** (CTS/RTS) unless the UART connection is very short (PCB-to-PCB, like the on-board link between the Jetson and flight controller on the [ARK Jetson PAB Carrier](../products/flight-controller/jetson-pabs/ark-jetson-pab-carrier/)). Over cables of any significant length, data will be lost at these speeds without flow control. If you must run high baud rates over a cable, use a TELEM port with CTS/RTS lines connected.
{% endhint %}

### Data Format

UART data is typically configured as **8N1**:

* **8** data bits
* **N**o parity
* **1** stop bit

This is the default on virtually all PX4 and ArduPilot peripherals. You almost never need to change it.

## How ARK Products Use It

### Debug Console

Every ARK board with a debug connector exposes a UART on pins 2 (TX) and 3 (RX) of the [Pixhawk Standard Debug Connector](connectors-and-wiring.md). Connecting to this UART at 57600 baud gives you the NuttX shell (PX4), where you can:

* View boot messages and error logs
* Run diagnostic commands (`sensors status`, `listener sensor_accel`)
* Set parameters directly

The easiest way to access the debug console is with an [ST-LINK V3 Mini and ARK Debug Adapter](st-link-flashing-guide.md), which provides both SWD and UART through a single USB connection.

### GPS Modules

ARK GPS modules ([ARK SAM GPS](../gps/ark-sam-gps/), [ARK DAN GPS](../gps/ark-dan-gps/)) that support non-CAN connections use UART to send position data to the flight controller. The flight controller's GPS port provides a UART with the Pixhawk Standard pinout.

### Telemetry

MAVLink telemetry between a flight controller and a ground station radio uses UART. The flight controller's TELEM ports are UART interfaces running MAVLink at 57600 or 115200 baud by default.

### Companion Computers

The [ARK Jetson PAB Carrier](../products/flight-controller/jetson-pabs/ark-jetson-pab-carrier/) and [ARK Pi6X Flow](../flight-controller/ark-pi6x-flow/) use UART connections between the companion computer and the flight controller MCU for MAVLink or XRCE-DDS communication.

## Common Pitfalls

* **TX and RX swapped** — see [RX/TX Cross-Wiring](serial-communication-uart.md#rxtx-cross-wiring) above. Always the first thing to check.
* **Baud rate mismatch** — if you see garbled characters instead of readable text, double-check that both ends are set to the same baud rate. The PX4 debug console is 57600, not 115200.
* **Missing common ground** — UART signals are referenced to ground. If two devices don't share a common ground, communication will be unreliable or fail entirely.
* **Voltage mismatch** — STM32 UART signals are 3.3V. Connecting directly to a 5V device (like some Arduino boards) can damage the MCU. Use a level shifter if needed.
* **Long or untwisted wires** — UART signals degrade over distance. Keep cables as short as possible and use twisted pairs (TX with GND, RX with GND) to reject noise. Runs over 15–20 cm at 115200 baud or above become unreliable without twisted wires, especially on a drone with motors running.
* **Port already in use** — on Linux, if `screen` or another terminal is already connected to a serial port, a second connection will fail silently. Kill existing sessions before reconnecting.
* **Not using an oscilloscope** — if UART isn't working and you've checked TX/RX wiring and baud rate, connect an oscilloscope to the TX and RX lines. This immediately tells you whether the signal is present, at the right voltage level, and clean. It also catches bad solder joints, broken traces, and damaged connectors that are invisible to the eye.

## Further Reading

* [ST-LINK Flashing Guide — UART Debug Console](st-link-flashing-guide.md#uart-debug-console) — step-by-step instructions for connecting to the debug console
* [PX4 System Console](https://docs.px4.io/main/en/debug/system_console.html)
* [Communication Buses (I2C, SPI)](communication-buses.md) — comparison of UART with other protocols
