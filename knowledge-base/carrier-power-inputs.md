---
description: How the 5V inputs on ARK carrier boards combine, and how much current they can supply.
---

# Carrier Power Inputs

| Board | 5V inputs | Combining |
| --- | --- | --- |
| [ARK Pixhawk Autopilot Bus Carrier](../flight-controller/ark-pixhawk-autopilot-bus-carrier/README.md) | POWER1, POWER2 (6 A each), USB | Priority select |
| [ARK Jetson PAB Carrier](../flight-controller/jetson-pabs/ark-jetson-pab-carrier/README.md) | POWER1–3 (6 A each) | Ideal-diode OR |
| [ARK Jetson PAB Carrier V3](../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/README.md) | Power 1–3 (4 A each) | Ideal-diode OR |
| [ARK Just A Jetson](../embedded-computers/ark-just-a-jetson/README.md) | 5V IN (6 A), BAT IN through the onboard 5.2 V regulator | Ideal-diode OR |
| [ARK VOXL2 RTK PAB Carrier](../flight-controller/ark-voxl2-rtk-pab-carrier/README.md) | VBRICK1, VBRICK2 on POWER (6 A each) | Ideal-diode OR |

Per-input ratings come from the connector's two power pins (3 A each on CLIK-Mate, 2 A each on Micro-Lock PLUS), not from the power module.

## Priority Select

The highest-priority valid input powers the board and the others are disconnected: POWER1 > POWER2 > USB. An input is valid between 3.81 V and 5.85 V. Inputs never share current, so the 5V load must stay within the rating of the selected input.

## Ideal-Diode OR

Each input feeds the 5V bus through its own ideal diode, which blocks backfeed between inputs. There is no input priority.

* Two or more of the same ARK power module share the load, so the total 5V draw can exceed one input's rating. Keep each input within its own rating.
* Inputs at different voltages don't share: the highest-voltage input carries the load. The [ARK PAB Power Module](../power/ark-pab-power-module/README.md) outputs 5.27 V and the [ARK 12S PAB Power Module](../power/ark-12s-pab-power-module/README.md) 5.2 V, so mixing them adds redundancy but not capacity.
* An input above 5.84 V is disconnected.
