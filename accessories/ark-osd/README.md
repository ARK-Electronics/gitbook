---
cover: ../../.gitbook/assets/TODO-ark-osd-cover.jpg
coverY: 0
---

# ARK OSD

An analog on-screen display board that goes between an FPV camera and an analog video transmitter. It takes the OSD from the [ARK FPV](../../flight-controller/ark-fpv/README.md) or another flight controller over SPI or UART.

<a href="https://arkelectron.com/product/ark-osd/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_OSD/model" class="button secondary" data-icon="cube">3D model</a>

* **Processor:** Raspberry Pi RP2354A
* **Interface:** SPI, register-compatible with the MAX7456, on an 8-pin JST-SH. MSP DisplayPort over UART on a 6-pin JST-GH
* **Video:** NTSC and PAL composite, camera in and video out on 3-pin JST-GH
* **Power:** 5 V from the SPI or TELEM connector
* **Autopilots:** PX4, ArduPilot, Betaflight
* **Compliance:** USA built, NDAA

## Documentation

* [Firmware](firmware.md)
* [Hardware Reference](hardware.md)
* [PX4 Instructions](px4-instructions.md)
* [ArduPilot Instructions](ardupilot-instructions.md)
* [Betaflight Instructions](betaflight-instructions.md)
