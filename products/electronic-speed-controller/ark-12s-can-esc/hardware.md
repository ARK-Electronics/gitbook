---
description: >-
  Specifications, design limits, connector pinouts and status LEDs of the ARK
  12S CAN ESC.
---

# Hardware Reference

* [Mounting and Power Connections](mounting-and-power-connections.md) — board outline, mounting holes, power and phase standoffs, grounding, thermal notes

## Specifications

| Specification | Value |
|---------------|-------|
| MCU | STM32G431 |
| Gate driver | [TI DRV8350H](https://www.ti.com/product/DRV8350) |
| Input voltage | 4S–12S LiPo, 9 V minimum, 70 V absolute maximum |
| Current | Continuous TBD, burst TBD. 0–300 A measurement range, 10 mV/A |
| Motor outputs | 1 motor, 3 phases, 6 × 120 V 1.7 mΩ MOSFETs |
| Bulk capacitance | 380 µF, see [Capacitance](#capacitance) |
| CAN | CAN FD, up to 5 Mbps, software switchable termination |
| Signal input | Single wire, 5 V tolerant |
| Telemetry | Single wire serial telemetry output |
| Current output | Analog, 10 mV/A |
| Debug | SWD and debug console |
| Dimensions | 57.75 × 36.20 × 9.04 mm |
| Mounting pattern | 31.20 × 37.75 mm |
| Weight | 22 g |
| Operating temperature | −40 °C to +85 °C |
| PCB | 8 layer, 1.6 mm finished thickness, 2 oz outer copper, 1 oz inner copper, filled via in pad, ENIG finish, IPC Class 2 |

{% hint style="info" %}
The board runs down to 9V input, but 4S remains the minimum recommended cell count. Below 4S there is very little margin between a sagging pack and the low voltage cutoff under load.
{% endhint %}

{% hint style="warning" %}
**Continuous and burst current ratings are TBD.**

These are thermal limits, not silicon limits. The current at which this ESC can run indefinitely depends on how it is mounted, how much airflow it gets, and whether it is heatsinked — the same board will hold very different numbers bolted to a cold plate versus sitting in still air inside a sealed enclosure.

Ratings will be published once thermal validation is complete. Until then, treat the hardware overcurrent trip below as a fault threshold, not as an operating target, and validate current limits in your own airframe.
{% endhint %}

## Board Maximum Design Specifications

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

Firmware applies its own protection well below these limits. See [Node Parameters](firmware.md#node-parameters) for the shipped current and temperature defaults.

## Capacitance

The ARK 12S CAN ESC has 380µF of 100V ceramic bulk capacitance on the battery input. There are no electrolytic capacitors on the board, so there is nothing to derate with age or temperature.

{% hint style="warning" %}
The input transient suppressor begins conducting at approximately 78V. Long battery leads increase loop inductance and make switching and inrush transients worse. On 12S, or with leads longer than a few inches, add an external bulk capacitor at the battery input.
{% endhint %}

## Sensing

| Measurement     | Method                                                         | Scaling | Range                  |
| --------------- | -------------------------------------------------------------- | ------- | ---------------------- |
| Battery current | 100µΩ shunt, low side, sense amplifier at 100V/V               | 10mV/A  | 0 – 300A               |
| Battery voltage | 30kΩ / 1kΩ divider                                             | 31V/V   | 0 – 102V               |
| Phase voltage   | 20kΩ / 1kΩ divider per phase, 20kΩ virtual neutral, 3.3V clamp | 21V/V   | Sensorless commutation |

## Protection

* Transient voltage suppressor on the battery input
* Gate driver VDS overcurrent monitor with fault reporting to the MCU
* ESD arrays on the flight controller, CAN, and debug connectors
* 3.3V clamps on all phase sense and telemetry nodes

## Pinout

The two CAN connectors are on the same side of the board as the power stage and the status LEDs. The flight controller and debug connectors are on the opposite side, along with the microcontroller.

### CAN (×2) — 4-pin JST-GH

J1 and J4, 1.25mm pitch. The two connectors are wired in parallel so the ESC can be daisy chained in the middle of a CAN bus.

| Pin | Signal        |
| --- | ------------- |
| 1   | Not connected |
| 2   | CAN H         |
| 3   | CAN L         |
| 4   | GND           |

{% hint style="info" %}
Pin 1 is not connected. The ESC neither draws power from the CAN bus nor supplies power to it, so a standard Pixhawk 4 pin CAN cable can be used without modification. Both ends of the bus still need to be terminated.
{% endhint %}

The ESC has a **software switchable 120Ω termination resistor** across the bus, set with `CAN_TERM_ENABLE` (see [Node Parameters](firmware.md#node-parameters)). Enable it only when the ESC is physically at one end of the bus, and leave it off for any node in the middle. See [CAN Bus](../../../knowledge-base/can-bus.md) for background on termination.

### Flight Controller — 5-pin JST-SR

J2, 1.0mm pitch. This connector carries the direct signal interface, used when the ESC is driven by a flight controller output rather than over CAN.

| Pin | Signal         | Notes                                                      |
| --- | -------------- | ---------------------------------------------------------- |
| 1   | VBAT           | Unregulated battery voltage, direct from the battery input |
| 2   | Current output | Analog, 10mV/A, 0 – 3.0V for 0 – 300A                      |
| 3   | Telemetry TX   | Single wire serial output from the ESC, 330Ω series        |
| 4   | Signal input   | PWM or DShot input, 5V tolerant, 100Ω series               |
| 5   | GND            |                                                            |

{% hint style="danger" %}
Pin 1 is battery voltage, not 5V. On 12S that is over 50V. It is not fused, regulated, or current limited, and it is present whenever the battery is connected. Do not connect it to a 5V input on your flight controller. Confirm what your flight controller expects on this pin before plugging in a cable, and do not assume the pinout matches another manufacturer's ESC.
{% endhint %}

Pins 2, 3, and 4 are ESD protected. Pin 1 is not.

### SWD and Console — 6-pin JST-SR

J3, 1.0mm pitch. Combines the SWD debug port and the debug console on one connector.

| Pin | Signal                                         |
| --- | ---------------------------------------------- |
| 1   | 3.3V                                           |
| 2   | Console TX (ESC output)                        |
| 3   | Console RX (wired, unused by current firmware) |
| 4   | SWDIO                                          |
| 5   | SWCLK                                          |
| 6   | GND                                            |

{% hint style="warning" %}
If the ESC is powered from a battery or bench supply, do not connect the 3.3V line from your ST-LINK. Connect SWDIO, SWCLK, and GND only. See [ST-LINK Flashing Guide](../../../knowledge-base/st-link-flashing-guide.md).
{% endhint %}

The console is transmit only at 115200 baud. See [Debug Console](firmware.md#debug-console) for what it prints, and [Serial Communication (UART)](../../../knowledge-base/serial-communication-uart.md) if you are new to connecting a console.

## LEDs

A red, green, and blue LED are driven directly by the microcontroller. Pattern meanings are defined by the firmware.

{% hint style="info" %}
Pattern meanings are still being finalised in firmware. Until they are published, use the [debug console](firmware.md#debug-console) for fault detail — it names the fault directly rather than encoding it in a blink pattern.
{% endhint %}

## Datasheet

* [ARK 12S CAN ESC](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_12S_CAN_ESC/datasheet/ARK_12S_CAN_ESC_Datasheet.pdf)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_12S\_CAN\_ESC\_Rev\_2.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_CAN_ESC/model/ARK_12S_CAN_ESC_Rev_2.0.step) | Board, rev 2.0 |
| [ARK\_12S\_CAN\_ESC\_Top\_Case\_Rev2.0.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_CAN_ESC/case/ARK_12S_CAN_ESC_Top_Case_Rev2.0.stl) | Case top, rev 2.0 |
| [ARK\_12S\_CAN\_ESC\_Bottom\_Case\_Rev2.0.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_CAN_ESC/case/ARK_12S_CAN_ESC_Bottom_Case_Rev2.0.stl) | Case bottom, rev 2.0 |

All files: [ARK\_12S\_CAN\_ESC in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_12S_CAN_ESC)
