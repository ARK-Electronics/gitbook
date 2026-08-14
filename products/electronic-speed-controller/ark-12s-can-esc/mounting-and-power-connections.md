---
description: >-
  Mechanical envelope, mounting pattern, and the threaded standoffs used for
  battery and motor phase connections.
---

# Mounting and Power Connections

## Board Outline

| Property                     | Value                        |
| ---------------------------- | ---------------------------- |
| Length                       | 57.75mm                      |
| Width                        | 36.20mm                      |
| Height, installed components | 9.04mm                       |
| PCB thickness                | 1.6mm                        |
| Weight                       | 22g                          |
| Mounting holes               | 4 × Ø2.90mm, for M2 hardware |
| Mounting pattern             | 31.20mm × 37.75mm            |

The four mounting holes are **electrically floating** — they are not connected to board ground or to any other net. Metal standoffs and screws can be used without creating a ground loop through the airframe, and the mounting hardware carries no ESC current under any condition. Do not rely on the mounting holes to ground the board either; they are not a ground path.

Check clearance against the components nearest each hole before torquing anything down.

## Power and Phase Standoffs

All high current connections are made at threaded SMT standoffs. There are no solder tabs and no pigtails.

| Standoff | Connection       | Thread |
| -------- | ---------------- | ------ |
| M1       | Battery positive | M4     |
| M2       | Battery negative | M4     |
| M3       | Phase C          | M3     |
| M4       | Phase A          | M3     |
| M5       | Phase B          | M3     |

The two battery standoffs are on 26.50mm centers at one end of the board. The three phase standoffs sit in a row on 8.65mm centers at the other end. Designators are marked on the silkscreen.

### Two Ways to Connect

The standoffs are threaded and act as captive nuts, so they sit on the opposite side of the board from the side the screw enters.

* **Screws with terminals.** Put a ring or fork terminal on the pad on the side opposite the standoff, and drive a screw through it into the standoff. The screw and terminal are on one face, the standoff is on the other, and the PCB is captured between them.
* **Solder directly.** Solder the wire to the pad on the side opposite the standoff. Use this when you want the lowest possible joint resistance or do not have room for a terminal.

{% hint style="info" %}
The standoffs are round, so they cannot be counter-held with a wrench. They do not need to be. They are soldered to the board during SMT, and driving the screw in from the opposite side clamps the board rather than twisting the standoff. Tighten the screw — do not try to turn the standoff itself.
{% endhint %}

{% hint style="warning" %}
Phase order is not enforced by the hardware. Swapping any two phase connections reverses motor direction. Confirm direction at low throttle with the propeller removed.
{% endhint %}

## Grounding

Two things to know before wiring the ESC into an airframe:

* **The mounting holes are floating.** They are not a ground connection. Board ground reaches the ESC only through the battery negative standoff.
* **Battery negative is not board ground.** Battery negative reaches board ground through the 100µΩ current shunt, so the M2 standoff and board ground are **not** the same node.

{% hint style="danger" %}
Do not bond the M2 standoff to board ground externally, and do not use a chassis or frame path as a return for battery current. Either one shorts out the shunt and the ESC loses its current measurement.
{% endhint %}

See [Power and Grounding](../../../knowledge-base/power-and-grounding.md) for general practice.

## Thermal Notes

The six MOSFETs are on the power stage side of the board and dissipate the majority of the loss. The board has 2oz outer copper and filled via in pad construction to move heat into the inner planes, but at high continuous current the ESC still needs airflow or a conducted path to a heatsink. Mounting the ESC in still air inside a sealed enclosure will limit continuous current well below the overcurrent trip threshold.

The mounting holes being isolated does not prevent them from conducting heat. Metal standoffs into a frame or cold plate are a legitimate thermal path even though they are not an electrical one.
