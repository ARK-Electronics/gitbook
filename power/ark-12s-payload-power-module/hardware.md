# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Power monitor | [TI INA238](https://www.ti.com/product/INA238), 0.1 mΩ shunt, I2C |
| 5V regulator | 5.2 V 6 A step-down, 10 V minimum input at 6 A out, output over-current protection |
| 12V regulator | 12.0 V 6 A step-down, 15 V minimum input at 6 A out, output over-current protection |
| Input voltage | 75 V maximum (12S) |
| Continuous current | 100 A battery at 20 °C ambient |
| Battery input and output | Solder pads |
| Avionics output | 6-pin Molex CLIK-Mate, 5 V, matches the [ARK PAB carrier power pinout](https://docs.px4.io/main/en/flight_controller/arkpab.html#power1) |
| Payload output | 4-pin Molex CLIK-Mate, 12 V |
| Dimensions | 3.7 × 3.5 × 1.3 cm |
| Weight | 20.5 g |

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

### 12V — 4-pin Molex CLIK-Mate

2.00 mm pitch Molex [CLIK-Mate 502494](https://www.molex.com/en-us/part-list/502494). Mating plug [5024390400](https://www.digikey.com/en/products/detail/molex/5024390400/2380424), pre-crimped wires [0797581014](https://www.digikey.com/en/products/detail/molex/0797581014/6346648).

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 12V | 12.0V |
| 2 | 12V | 12.0V |
| 3 | GND | GND |
| 4 | GND | GND |

## Current Rating and Cooling

The ARK 12S Payload Power Module is rated for 100A continuous battery current at 20C ambient. It is recommended to run multiple power modules in parallel if more than 100A continuous current is required.

When operating at high battery current and/or high 5V/12V regulator output current, it is recommended to actively cool the board.

## Datasheet

* [ARK 12S Payload Power Module](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_12S_Payload_Power_Module/datasheet/ARK_12S_Payload_Power_Module_Datasheet.pdf)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_12S\_Payload\_Power\_Module\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_Payload_Power_Module/model/ARK_12S_Payload_Power_Module_Rev_1.0.step) | Board, rev 1.0 |
| [ARK\_12S\_Payload\_Power\_Module\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_12S_Payload_Power_Module/model/ARK_12S_Payload_Power_Module_Rev_1.0_PDF3D.pdf) | Board, rev 1.0, 3D PDF |

All files: [ARK\_12S\_Payload\_Power\_Module in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_12S_Payload_Power_Module)
