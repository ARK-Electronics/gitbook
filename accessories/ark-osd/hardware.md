# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| SPI | Register-compatible with the MAX7456, SPI modes 0 and 3 |
| UART | MSP DisplayPort, 115200 baud, no flow control |
| Video | NTSC and PAL composite, detected from the camera |
| Overlay | Monochrome, 30 × 13 characters on NTSC and 30 × 16 on PAL. The camera's color passes through |
| Power | 5 V on the SPI or TELEM connector |
| Power draw | TODO |
| Mounting | 4× 3.8 mm holes on a 30.5 × 23.4 mm pattern |
| Dimensions | 36 × 29 × 7.4 mm |
| Weight | 5.0 g |

## Pinout

<figure><img src="../../.gitbook/assets/ARK OSD.jpg" alt="ARK OSD, top"><figcaption><p>Top: SPI (J1), TELEM (J2), CAM (J3), VIDEO OUT (J5) and DEBUG (J4)</p></figcaption></figure>

### SPI (J1) — 8-pin JST-SH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V IN | 5.0 V |
| 2 | SPI\_SCK | 3.3 V |
| 3 | SPI\_MISO | 3.3 V |
| 4 | SPI\_MOSI | 3.3 V |
| 5 | SPI\_nCS | 3.3 V |
| 6 | SPI\_DRDY | 3.3 V |
| 7 | nRESET | 3.3 V |
| 8 | GND | GND |

The ARK OSD stays in reset while pin 7 is low. Pin 6 isn't used.

### TELEM (J2) — 6-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V IN | 5.0 V |
| 2 | UART\_RX | 3.3 V |
| 3 | UART\_TX | 3.3 V |
| 4 | UART\_RTS | 3.3 V |
| 5 | UART\_CTS | 3.3 V |
| 6 | GND | GND |

### CAM (J3) — 3-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | VPASS | Camera supply |
| 2 | VIDEO\_IN | Composite video |
| 3 | GND | GND |

### VIDEO OUT (J5) — 3-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | VPASS | Camera supply |
| 2 | VIDEO\_OUT | Composite video |
| 3 | GND | GND |

VPASS joins pin 1 of CAM and VIDEO OUT. It carries the camera's supply from the video transmitter's cable. It isn't connected to the ARK OSD's own power.

J4, a 3-pin JST-SH, is for factory programming.

## What's Included

| Item | Use |
|------|-----|
| ARK OSD | |
| 8-pin JST-SH cable | SPI port to the ARK FPV SPI port. Straight |
| 6-pin JST-GH cable | TELEM port to the ARK FPV TELEM port. Straight |

The camera and video transmitter cables are not included.

## Wiring

| ARK OSD | Connects to | Cable |
|---------|-------------|-------|
| SPI | ARK FPV SPI port | 8-pin JST-SH, straight |
| TELEM | ARK FPV TELEM port | 6-pin JST-GH, straight |
| CAM | Camera video output | 3-pin JST-GH, not included |
| VIDEO OUT | Video transmitter's camera input | 3-pin JST-GH, not included |

Connect the SPI cable, the TELEM cable or both. Either one powers the board. Video reaches the transmitter only while the ARK OSD has power.

{% hint style="danger" %}
Connect TELEM only to the ARK FPV's TELEM port, never to its VTX port. The VTX port's pin 1 carries 12 V. The ARK OSD's 5 V inputs are rated 6 V maximum.
{% endhint %}

## OSD Links

The flight controller draws the OSD over one of two links.

| | SPI | MSP DisplayPort |
|---|-----|-----------------|
| Connector | SPI | TELEM |
| PX4 driver | `atxxxx` | `msp_osd` |
| ArduPilot driver | MAX7456 | MSP DisplayPort |
| Betaflight driver | MAX7456 | MSP DisplayPort |
| Font | Uploaded by ArduPilot at boot, or from Betaflight's Font Manager | Built in, one for each autopilot |
| NTSC or PAL | Read by the flight controller | Not reported to the flight controller |

The ARK OSD keeps an uploaded font across power cycles. On NTSC the screen shows rows 0 to 12 of 16.

{% hint style="info" %}
After you move a flight controller from SPI to MSP DisplayPort, power-cycle the ARK OSD. A flight controller that turned the display on over SPI keeps the screen until the ARK OSD resets.
{% endhint %}

## 3D Model

| File | Contents |
|------|----------|
| [ARK\_OSD\_Rev\_1.0.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_OSD/model/ARK_OSD_Rev_1.0.step) | Board |
| [ARK\_OSD\_Rev\_1.0\_PDF3D.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_OSD/model/ARK_OSD_Rev_1.0_PDF3D.pdf) | 3D PDF |

All files: [ARK\_OSD in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_OSD)
