---
description: 4-pin JST-GH Ethernet to RJ45.
---

# ARK Ethernet Adapter

The ARK Ethernet Adapter converts the 4-pin JST-GH Ethernet port on the [ARK Pixhawk Autopilot Bus Carrier](../../flight-controller/ark-pixhawk-autopilot-bus-carrier/README.md) to an RJ45 jack. It comes with a 4-pin JST-GH cable.

[Buy the ARK Ethernet Adapter](https://arkelectron.com/product/ethernet-adapter/)

## Connectors

| Connector | Part |
| --------- | ---- |
| RJ45 | [Amphenol RJHSE-5E80](https://www.amphenol-cs.com/product/rjhse5e80.html): shielded, right angle, no LEDs |
| JST-GH | 4-pin, JST SM04B-GHS-TB |

The adapter has no magnetics. The ARK Pixhawk Autopilot Bus Carrier has them onboard; any other device driving the JST-GH side needs its own.

## Pinout

| RJ45 pin | Signal | JST-GH pin |
| -------- | ------ | ---------- |
| 1 | LAN\_TD\_P | 4 |
| 2 | LAN\_TD\_N | 3 |
| 3 | LAN\_RD\_P | 2 |
| 6 | LAN\_RD\_N | 1 |
| 4, 5, 7, 8 | 75 Ω to GND | — |
| Shell | 75 Ω to GND | — |

TD and RD are named from the carrier's side, so the RJ45 is wired MDI: it transmits on pins 1 and 2.

## 3D Model and Case

| File | Contents |
|------|----------|
| [Ethernet\_Adapter.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/Ethernet_Adapter/model/Ethernet_Adapter.step) | Board |
| [Ethernet\_Adapter\_Case.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/Ethernet_Adapter/case/Ethernet_Adapter_Case.step) | Case |

All files: [Ethernet\_Adapter in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/Ethernet_Adapter)
