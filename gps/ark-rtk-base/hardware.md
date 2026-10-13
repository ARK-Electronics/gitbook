# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module), L1/L2 |
| Constellations | GPS, GLONASS, Galileo and BeiDou, concurrently |
| Position accuracy | Centimeter-level with RTK |
| Modes | RTK fixed base, moving base or rover |
| Interfaces | USB-C; F9P UART1 ([Pixhawk-standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf) 6-pin JST-GH); F9P UART2 (3-pin JST-GH) |
| LEDs | Power, GPS fix, RTK status |
| Power | 5 V over USB-C and/or the UART connector, 120 mA average, 150 mA max |
| Weight | 26 g |

## Pinout

### USB — USB-C

| Pin | Signal | Voltage |
|-----|--------|---------|
| 2, 11 | VBUS | 5.0 V |
| 5, 8 | USB_N | 3.3 V |
| 6, 7 | USB_P | 3.3 V |
| 1, 12 | GND | GND |

### F9P UART1 — 6-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5.0V | 5.0 V |
| 2 | F9P_RXD | 3.3 V |
| 3 | F9P_TXD | 3.3 V |
| 4 | NC | NC |
| 5 | NC | NC |
| 6 | GND | GND |

### F9P UART2 — 3-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | F9P_TXD2 | 3.3 V |
| 2 | F9P_RXD2 | 3.3 V |
| 3 | GND | GND |

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_RTK\_Base\_Rev\_1\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_Base/model/ARK_RTK_Base_Rev_1_3D_Model.step) | Board, rev 1 |

All files: [ARK\_RTK\_Base in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_RTK_Base)

## Schematic and BOM

| File | Contents |
|------|----------|
| [ARK\_RTK\_Base\_Rev\_1\_Schematic.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_Base/schematic/ARK_RTK_Base_Rev_1_Schematic.pdf) | Schematic, rev 1 |
| [ARK\_RTK\_Base\_Rev\_1\_BOM.xlsx](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_RTK_Base/bom/ARK_RTK_Base_Rev_1_BOM.xlsx) | Bill of materials, rev 1 |
