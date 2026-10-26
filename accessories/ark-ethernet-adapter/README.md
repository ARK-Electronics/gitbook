---
---

# ARK Ethernet Adapter

An adapter from a Pixhawk-standard 4-pin JST-GH Ethernet port, such as the one on the [ARK Pixhawk Autopilot Bus Carrier](../../flight-controller/ark-pixhawk-autopilot-bus-carrier/README.md), to an RJ45 jack. It comes with a 4-pin JST-GH cable.

<a href="https://arkelectron.com/product/ethernet-adapter/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/Ethernet_Adapter/model" class="button secondary" data-icon="cube">3D model</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/Ethernet_Adapter/case" class="button secondary" data-icon="box">Case</a>

## Connectors

| Connector | Part |
| --------- | ---- |
| RJ45 | [Amphenol RJHSE-5E80](https://www.amphenol-cs.com/product/rjhse5e80.html): shielded, right angle, no LEDs |
| JST-GH | 4-pin, JST SM04B-GHS-TB |

The adapter has no magnetics; the device on the JST-GH side must have them.

## Pinout

| RJ45 pin | Signal | JST-GH pin |
| -------- | ------ | ---------- |
| 1 | LAN\_TD\_P | 4 |
| 2 | LAN\_TD\_N | 3 |
| 3 | LAN\_RD\_P | 2 |
| 6 | LAN\_RD\_N | 1 |
| 4, 5, 7, 8 | 75 Ω to GND | — |
| Shell | 75 Ω to GND | — |

TD and RD are named from the JST-GH device's side, so the RJ45 is wired MDI: it transmits on pins 1 and 2.
