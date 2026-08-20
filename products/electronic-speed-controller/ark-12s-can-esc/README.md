---
description: >-
  NDAA compliant, made in the USA, single channel electronic speed controller
  with CAN FD, designed for 12S brushless propulsion.
cover: ../../../.gitbook/assets/IMG_6571_edited.JPG
coverY: 0
---

# ARK 12S CAN ESC

The ARK 12S CAN ESC is a single motor, three phase speed controller. It reports telemetry over CAN FD and accepts a conventional single wire signal input, so it can be used either as a CAN node or as a drop in replacement for a PWM/DShot ESC.

Power and phase connections are made through threaded SMT standoffs rather than wires, so the ESC bolts directly to a bus bar or motor mount.

{% hint style="warning" %}
When running over CAN, each ESC on the same bus must have a unique **ESC Index / Motor Index**. PX4 and ArduPilot use that index to identify which motor is which. A quadcopter is `0`, `1`, `2`, `3`. See [Firmware](firmware.md#esc-index-motor-index).
{% endhint %}

{% hint style="danger" %}
Pin 1 of the flight controller connector (J2) is **unregulated battery voltage**. It is not fused or current limited. Do not connect it to a 5V input on your flight controller. See [Pinout](pinout.md).
{% endhint %}

**Specifications:**

* Voltage
  * 4S – 12S Lithium Polymer Battery Input
  * 9V Minimum
  * 70V Absolute Maximum
* Current
  * Continuous: TBD
  * Burst: TBD
  * 0 – 300A measurement range, 10mV/A
* Motor Outputs
  * 1 motor, 3 phases
  * 6 × 120V 1.7mΩ MOSFETs
* Interfaces
  * CAN FD, up to 5Mbps, software switchable termination
  * Single wire signal input, 5V tolerant
  * Single wire serial telemetry output
  * Analog current output, 10mV/A
  * SWD and debug console
* Dimensions
  * 57.75mm x 36.20mm x 9.04mm
  * 31.20mm x 37.75mm mounting pattern
* Weight
  * 22g

{% hint style="info" %}
The board runs down to 9V input, but 4S remains the minimum recommended cell count. Below 4S there is very little margin between a sagging pack and the low voltage cutoff under load.
{% endhint %}

{% hint style="warning" %}
**Continuous and burst current ratings are TBD.**

These are thermal limits, not silicon limits. The current at which this ESC can run indefinitely depends on how it is mounted, how much airflow it gets, and whether it is heatsinked — the same board will hold very different numbers bolted to a cold plate versus sitting in still air inside a sealed enclosure.

Ratings will be published once thermal validation is complete. Until then, treat the hardware overcurrent trip below as a fault threshold, not as an operating target, and validate current limits in your own airframe.
{% endhint %}

**Board Maximum Design Specifications:**

These are the hardware limits the board is built to. They are not operating recommendations — the continuous rating will land well below the overcurrent trip.

| Parameter                        | Design limit   | Set by                                      |
| -------------------------------- | -------------- | ------------------------------------------- |
| MOSFET drain to source voltage   | 120V           | Power MOSFETs                               |
| Gate driver supply voltage       | 102V           | Gate driver                                 |
| Bulk capacitor voltage           | 100V           | Input bulk capacitors                       |
| Buck regulator input voltage     | 120V           | Primary step down regulator                 |
| Input TVS standoff voltage       | 70V            | Input transient suppressor, 77.8V breakdown |
| Voltage measurement range        | 102V           | 31V/V divider                               |
| Current measurement range        | 300A           | Shunt and current sense amplifier           |
| Overcurrent trip, 25°C junction  | 412A           | Gate driver VDS monitor at 700mV            |
| Overcurrent trip, 100°C junction | 292A           | Gate driver VDS monitor at 700mV            |
| Overcurrent trip, 150°C junction | 233A           | Gate driver VDS monitor at 700mV            |
| Overcurrent trip, 175°C junction | 206A           | Gate driver VDS monitor at 700mV            |
| Operating temperature            | -40°C to +85°C | MCU, oscillator, connectors                 |

The overcurrent trip falls as the MOSFETs heat up, because the VDS monitor measures voltage across a resistance that rises with temperature. A trip point set at 412A on a cold bench is a 233A trip point on a hot motor run.

Firmware applies its own protection well below these limits. See [Firmware](firmware.md) for the shipped current and temperature defaults.

**Capacitance:**

The ARK 12S CAN ESC has 380µF of 100V ceramic bulk capacitance on the battery input. There are no electrolytic capacitors on the board, so there is nothing to derate with age or temperature.

{% hint style="warning" %}
The input transient suppressor begins conducting at approximately 78V. Long battery leads increase loop inductance and make switching and inrush transients worse. On 12S, or with leads longer than a few inches, add an external bulk capacitor at the battery input.
{% endhint %}

**Sensing:**

| Measurement     | Method                                                         | Scaling | Range                  |
| --------------- | -------------------------------------------------------------- | ------- | ---------------------- |
| Battery current | 100µΩ shunt, low side, sense amplifier at 100V/V               | 10mV/A  | 0 – 300A               |
| Battery voltage | 30kΩ / 1kΩ divider                                             | 31V/V   | 0 – 102V               |
| Phase voltage   | 20kΩ / 1kΩ divider per phase, 20kΩ virtual neutral, 3.3V clamp | 21V/V   | Sensorless commutation |

**Protection:**

* Transient voltage suppressor on the battery input
* Gate driver VDS overcurrent monitor with fault reporting to the MCU
* ESD arrays on the flight controller, CAN, and debug connectors
* 3.3V clamps on all phase sense and telemetry nodes

**Construction:**

* 8 layer board, 1.6mm finished thickness
* 2oz outer copper, 1oz inner copper
* Filled via in pad, ENIG finish, IPC Class 2

{% content-ref url="pinout.md" %}
[pinout.md](pinout.md)
{% endcontent-ref %}

{% content-ref url="mounting-and-power-connections.md" %}
[mounting-and-power-connections.md](mounting-and-power-connections.md)
{% endcontent-ref %}

{% content-ref url="firmware.md" %}
[firmware.md](firmware.md)
{% endcontent-ref %}

{% content-ref url="3d-models.md" %}
[3d-models.md](3d-models.md)
{% endcontent-ref %}
