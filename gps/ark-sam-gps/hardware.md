# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox SAM-M10Q](https://www.u-blox.com/en/product/sam-m10q-module), 4 concurrent GNSS, under 38 mW |
| Interference | Spoofing and jamming detection |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Interface | UART and I2C, Pixhawk-standard 6-pin JST-GH |
| LED | GPS fix |
| Power | 5 V, 15 mA average, 20 mA max |
| Dimensions | ARK SAM GPS: 3.6 × 3.6 × 0.8 cm. ARK SAM GPS MINI: 3.225 × 1.6 × 0.8 cm |
| Weight | ARK SAM GPS: 11 g. ARK SAM GPS MINI: 8 g |

## Pinout

### UART/I2C — 6-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | RX | 3.3 V |
| 3 | TX | 3.3 V |
| 4 | SCL | 3.3 V |
| 5 | SDA | 3.3 V |
| 6 | GND | GND |

## Wiring

Connect the ARK SAM GPS to a UART/I2C port with a Pixhawk standard 6-pin JST-GH cable.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_SAM\_GPS\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_SAM_GPS/model/ARK_SAM_GPS_Rev_1.0.step) | ARK SAM GPS board, rev 1.0 |
| [ARK\_SAM\_GPS\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_SAM_GPS/model/ARK_SAM_GPS_Rev_1.0_PDF3D.pdf) | ARK SAM GPS board, rev 1.0, 3D PDF |
| [ARK\_SAM\_GPS\_PCB\_MINI\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_SAM_GPS_MINI/model/ARK_SAM_GPS_PCB_MINI_Rev_1.0.step) | ARK SAM GPS MINI board, rev 1.0 |
| [ARK\_SAM\_GPS\_MINI\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_SAM_GPS_MINI/model/ARK_SAM_GPS_MINI_Rev_1.0_PDF3D.pdf) | ARK SAM GPS MINI board, rev 1.0, 3D PDF |

All files: [ARK\_SAM\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_SAM_GPS) · [ARK\_SAM\_GPS\_MINI in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_SAM_GPS_MINI)
