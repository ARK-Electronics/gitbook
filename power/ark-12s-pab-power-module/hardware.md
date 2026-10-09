# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Power monitor | [TI INA238](https://www.ti.com/product/INA238), 0.1 mΩ shunt, I2C |
| Regulator | 5.2 V 6 A step-down, output over-current protection |
| Input voltage | 75 V maximum (12S), 10 V minimum at 6 A out |
| Continuous current | 100 A battery at 20 °C ambient |
| Battery input and output | Solder pads |
| Avionics output | 6-pin Molex CLIK-Mate, matches the [ARK PAB carrier power pinout](https://docs.px4.io/main/en/flight_controller/arkpab.html#power1) |
| Dimensions | 3.7 × 2.2 × 1.3 cm |
| Weight | 11.5 g |

## Pinout

### 5V and I2C — 6-pin Molex CLIK-Mate

2.00 mm pitch Molex [CLIK-Mate 502494](https://www.molex.com/en-us/part-list/502494). Mating plug [5024390600](https://www.digikey.com/en/products/detail/molex/5024390600/2380425), pre-crimped wires [0797581014](https://www.digikey.com/en/products/detail/molex/0797581014/6346648).

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | VBRICK | 5.2V |
| 2 | VBRICK | 5.2V |
| 3 | SCL | 3.3V |
| 4 | SDA | 3.3V |
| 5 | GND | GND |
| 6 | GND | GND |

## Current Rating and Cooling

The ARK 12S PAB Power Module is rated for 100A continuous battery current at 20C ambient. It is recommended to run multiple power modules in parallel if more than 100A continuous current is required.

When operating at high battery current and/or high 5V regulator output current, it is recommended to actively cool the board.

## Capacitor and TVS Diode

<figure><img src="../../.gitbook/assets/IMG_3824 edited.JPG" alt=""><figcaption><p>12S with Capacitor and TVS Diode</p></figcaption></figure>

When operating with 12S batteries, it is recommended to solder the included capacitor and TVS diode to the output side of the board. The negative of the capacitor is indicated on the cylinder. The cathode(line) on the TVS diode should be soldered to the positive side of the output.

## Datasheet

* [ARK 12S PAB Power Module](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_12S_PAB_Power_Module/datasheet/ARK_12S_PAB_Power_Module_Datasheet.pdf)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_12S\_PAB\_Power\_Module\_Rev\_3.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_PAB_Power_Module/model/ARK_12S_PAB_Power_Module_Rev_3.0.step) | Board, rev 3.0 |
| [ARK\_12S\_PAB\_Power\_Module\_Rev\_3.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_PAB_Power_Module/model/ARK_12S_PAB_Power_Module_Rev_3.0_PDF3D.pdf) | Board, rev 3.0, 3D PDF |

All files: [ARK\_12S\_PAB\_Power\_Module in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_12S_PAB_Power_Module)
