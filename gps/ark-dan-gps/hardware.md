# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| GNSS receiver | [u-blox DAN-F10N](https://www.u-blox.com/en/product/dan-f10n-module), L1/L5/E5a/B2a |
| Interference | Integrated SAW-LNA-SAW for out-of-band jamming immunity; u-blox F10 dual-band multipath mitigation |
| Magnetometer | [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) |
| Interface | UART and I2C, Pixhawk-standard 6-pin JST-GH |
| LED | GPS fix |
| Power | 5 V, 25 mA average, 44 mA max |
| Dimensions | 4.4 × 4.4 × 1.3 cm |
| Mounting pattern | 30.5 × 30.5 mm |
| Weight | 25 g |

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

Connect the ARK DAN GPS to a UART/I2C port with a Pixhawk standard 6-pin JST-GH cable.

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_DAN\_GPS\_PCB\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_DAN_GPS/model/ARK_DAN_GPS_PCB_Rev_1.0.step) | Board, rev 1.0 |

All files: [ARK\_DAN\_GPS in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_DAN_GPS)
