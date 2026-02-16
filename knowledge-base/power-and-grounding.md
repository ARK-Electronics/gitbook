---
description: >-
  Voltage levels, power distribution, ground loops, signal integrity, and noise
  avoidance on drones.
---

# Power and Grounding

## What is Power Distribution?

Every component on a drone — flight controller, sensors, GPS, companion computer, radio — needs clean, stable power at the correct voltage. Power distribution is how you get the right voltage to the right place while keeping electrical noise from corrupting sensor readings and communication buses.

Getting this right is the difference between a drone that flies reliably and one that suffers mysterious glitches.

## How It Works

### Voltage Levels

Drones deal with multiple voltage levels simultaneously:

| Voltage | Source | Powers |
|---------|--------|--------|
| **Battery voltage** (3S–6S, 11.1–25.2V) | LiPo battery | ESCs, motors |
| **5V** | BEC or power module | Flight controller, CAN peripherals, GPS, radios |
| **3.3V** | On-board regulator (from 5V) | MCU logic, sensors, communication interfaces |

The flight controller and all Pixhawk standard peripherals run on **5V** supplied through their connectors. The 5V rail is typically provided by a power module or a BEC (Battery Eliminator Circuit) that steps down the battery voltage.

The **3.3V** level is internal to each board — the MCU and sensors operate at 3.3V, but this is regulated on-board from the 5V input. You generally don't need to supply 3.3V externally.

### Power Module Role

ARK power modules ([ARK PAB Power Module](../power/ark-pab-power-module/README.md), [ARK 12S PAB Power Module](../power/ark-12s-pab-power-module/README.md)) do two things:

1. **Regulate** battery voltage down to clean 5V for the flight controller and peripherals
2. **Measure** battery voltage and current, reporting it to the flight controller over I2C.

### 5V Power Through CAN

On ARK systems, the [CAN bus](can-bus.md) carries both data and power on the same cable. Pin 1 of every 4-pin JST-GH CAN connector is 5V. This means DroneCAN peripherals are powered through their CAN cable — no separate power wiring needed.

{% hint style="warning" %}
**Power budget matters.** Every device in the CAN daisy chain draws current through the same cables and connectors. If the total current draw exceeds what the source can provide, voltage will drop and devices will behave erratically. Check the current draw of each peripheral and ensure the power module or BEC can handle the total.
{% endhint %}

### Ground Loops

A **ground loop** occurs when two or more devices are connected to the same ground reference through multiple paths, creating a loop that acts as an antenna for electromagnetic interference.

```
❌ Ground loop:
Battery GND ──→ Flight Controller GND ──→ Sensor GND
    └────────────────────────────────────────┘
    (second ground path through metal frame)

✅ Star ground (preferred):
Battery GND ──→ Power Module GND ──→ Flight Controller GND ──→ Sensor GND
                                      (single ground path, no loops)
```

Ground loops inject noise into analog sensor readings (barometer, current sensor) and can cause communication errors on buses like [UART](serial-communication-uart.md) and [I2C](communication-buses.md).

**Mitigation:**

* Use a star grounding topology — all grounds return to a single point
* Avoid mounting electronics directly to a conductive (carbon fiber) frame without insulation
* Keep signal wires away from high-current motor wires

### Signal Integrity and Noise

Digital communication buses ([CAN](can-bus.md), [UART](serial-communication-uart.md), [I2C, SPI](communication-buses.md)) all depend on clean signal transitions. Electrical noise can corrupt these signals, causing:

* Intermittent sensor dropouts
* CAN bus errors or node disconnects
* Garbled serial console output
* I2C bus lockups

**Major noise sources on a drone:**

| Source | Frequency | Affects |
|--------|-----------|---------|
| Motor commutation | kHz–MHz | All buses, especially I2C and analog |
| ESC switching | 10–100 kHz | Power rail ripple, sensor noise |
| USB | 480 MHz (harmonics into GHz) | GPS reception — USB is a major source of RF interference in the L-band |
| Radio transmitter | GHz | Possible digital bus upset at close range |
| High-current wires | DC–kHz | Magnetometer — motor wires and battery leads create strong magnetic fields |
| PWM servo signals | 50–400 Hz | Ground bounce on shared connectors |

**Noise reduction strategies:**

* Keep sensor cables short and routed away from motor/ESC/power wires
* Use shielded cables for long runs (>15 cm) on sensitive interfaces
* Ensure all connectors are fully seated — intermittent contacts cause noise
* Twist signal pairs to reduce pickup

### GPS Placement

GPS modules are particularly sensitive to both RF interference (which degrades satellite reception) and magnetic interference (which corrupts the built-in compass). Proper placement is critical for reliable position and heading data.

For detailed guidance on interference sources, mounting best practices, and common mistakes, see the dedicated [GPS Placement](gps-placement.md) page.

### Servo and Actuator Power Isolation

Servos and other actuators with motors are among the worst power consumers on a drone. A stalled servo can draw several amps, and even normal operation causes large current spikes that collapse the voltage rail it shares with other devices.

{% hint style="warning" %}
**Never power servos from the same regulator as the flight controller.** A servo stall or jam can brown out the entire 5V rail, causing the flight controller and all CAN peripherals to reboot mid-flight. Always use a dedicated BEC for servos and actuators.
{% endhint %}

This applies to any high-current load: gimbal motors, LED arrays, radio amplifiers, or payload actuators. If it can draw more than a few hundred milliamps, give it its own power supply with only a shared ground to the flight controller.

## Common Pitfalls

* **Under-rated power supply** — a BEC that can handle bench testing may brown out under load when motors spin up. Size your power supply for worst-case current draw plus margin.
* **Ground loops through the frame** — carbon fiber frames are conductive. If two boards are bolted to the frame and also connected by a cable, you have a ground loop. Use nylon standoffs or insulating tape.
* **Long I2C runs** — I2C/Serial is highly susceptible to noise and capacitance. Runs longer than 10–15 cm are unreliable on a drone. Use [CAN bus](can-bus.md) for any peripheral that isn't directly next to the flight controller.
* **Servos on the flight controller BEC** — see [Servo and Actuator Power Isolation](#servo-and-actuator-power-isolation) above. A stalled servo will take down your entire avionics power rail.
* **GPS mounted near USB or motor wires** — see [GPS Placement](gps-placement.md). USB interference and magnetic fields from high-current wires are the two most common causes of poor GPS and compass performance.
* **Ignoring decoupling** — if you're building custom hardware, every IC needs 100 nF decoupling capacitors on its power pins. ARK products include these, but custom carrier boards sometimes omit them.
* **Assuming USB power is sufficient** — USB provides 5V but limited current (500 mA from USB 2.0). A flight controller may boot on USB power but behave erratically because peripherals are under-powered.

## Further Reading

* [PX4 Power Module Setup](https://docs.px4.io/main/en/power_module/)
* [CAN Bus](can-bus.md) — CAN wiring and 5V power delivery
* [Connectors and Wiring](connectors-and-wiring.md) — connector types and pinouts
* [Communication Buses (I2C, SPI)](communication-buses.md) — bus noise susceptibility comparison
