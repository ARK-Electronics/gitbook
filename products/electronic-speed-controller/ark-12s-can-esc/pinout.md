---
description: Connector locations, pinouts, and status LEDs on the ARK 12S CAN ESC.
---

# Pinout

The two CAN connectors are on the same side of the board as the power stage and the status LEDs. The flight controller and debug connectors are on the opposite side, along with the microcontroller.

## CAN (J1, J4)

4 pin JST GH, 1.25mm pitch. The two connectors are wired in parallel so the ESC can be daisy chained in the middle of a CAN bus.

| Pin | Signal        |
| --- | ------------- |
| 1   | Not connected |
| 2   | CAN H         |
| 3   | CAN L         |
| 4   | GND           |

{% hint style="info" %}
Pin 1 is not connected. The ESC neither draws power from the CAN bus nor supplies power to it, so a standard Pixhawk 4 pin CAN cable can be used without modification. Both ends of the bus still need to be terminated.
{% endhint %}

The ESC has a **software switchable 120Ω termination resistor** across the bus. Enable it only when the ESC is physically at one end of the bus, and leave it off for any node in the middle. See [CAN Bus](../../../knowledge-base/can-bus.md) for background on termination.

## Flight Controller (J2)

5 pin JST SR, 1.0mm pitch. This connector carries the direct signal interface, used when the ESC is driven by a flight controller output rather than over CAN.

| Pin | Signal         | Notes                                                      |
| --- | -------------- | ---------------------------------------------------------- |
| 1   | VBAT           | Unregulated battery voltage, direct from the battery input |
| 2   | Current output | Analog, 10mV/A, 0 – 3.0V for 0 – 300A                      |
| 3   | Telemetry TX   | Single wire serial output from the ESC, 330Ω series        |
| 4   | Signal input   | PWM or DShot input, 5V tolerant, 100Ω series               |
| 5   | GND            |                                                            |

{% hint style="danger" %}
Pin 1 is battery voltage, not 5V. On 12S that is over 50V. It is not fused, regulated, or current limited, and it is present whenever the battery is connected. Confirm what your flight controller expects on this pin before plugging in a cable, and do not assume the pinout matches another manufacturer's ESC.
{% endhint %}

Pins 2, 3, and 4 are ESD protected. Pin 1 is not.

## SWD and Console (J3)

6 pin JST SR, 1.0mm pitch. Combines the SWD debug port and the debug console on one connector.

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

The console is transmit only at 115200 baud. See [Firmware](firmware.md) for what it prints, and [Serial Communication (UART)](../../../knowledge-base/serial-communication-uart.md) if you are new to connecting a console.

## Status LEDs

A red, green, and blue LED are driven directly by the microcontroller. Pattern meanings are defined by the firmware — see [Firmware](firmware.md).
