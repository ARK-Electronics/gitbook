# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Power monitor | [TI INA226](https://www.ti.com/product/INA226), 0.0005 Ω shunt, I2C |
| Regulator | 5.2 V 6 A step-down, output over-voltage and over-current protection |
| Input voltage | 33 V maximum, 5.8 V minimum at 6 A out |
| Continuous current | 60 A battery at 20 °C ambient |
| Battery input and output | XT60 (ARK PAB Power Module), solder pads (No Connector) |
| Avionics output | 6-pin Molex CLIK-Mate, matches the [ARK PAB carrier power pinout](https://docs.px4.io/main/en/flight_controller/arkpab.html#power1) |
| Dimensions | 4.75 × 3.43 × 1.15 cm (ARK PAB Power Module), 4.75 × 3.43 × 0.86 cm (No Connector) |
| Weight | 17.9 g (ARK PAB Power Module), 9.5 g (No Connector) |

## Current Rating and Cooling

The ARK PAB Power Module is rated for 60A continuous battery current at 20C ambient. However, when running 60A battery current at 20C without cooling, the 5V regulator is de-rated to 3A continuous output. It is recommended to run multiple power modules in parallel if more than 60A continuous current is required.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_PAB\_Power\_Module\_Rev\_3.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_PAB_Power_Module/model/ARK_PAB_Power_Module_Rev_3.step) | Board, rev 3 |
| [ARK\_PAB\_Power\_Module\_Rev\_3\_without\_XT60.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_PAB_Power_Module/model/ARK_PAB_Power_Module_Rev_3_without_XT60.step) | Board, rev 3, No Connector |
| [Top\_Power\_Module\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_PAB_Power_Module/case/Top_Power_Module_Case.stl) | Case top |
| [Bottom\_Power\_Module\_Case.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_PAB_Power_Module/case/Bottom_Power_Module_Case.stl) | Case bottom |

All files: [ARK\_PAB\_Power\_Module in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_PAB_Power_Module)
