---
description: >-
  NDAA compliant, made in the USA, 4 in 1 electronic speed controller running
  open source ARK32 firmware.
cover: ../../.gitbook/assets/IMG_3371 edited (Large).JPG
coverY: -23.514666666666663
---

# ARK 4IN1 ESC

The ARK 4IN1 ESC drives four brushless motors from a 3S–8S pack, with four STM32F051 MCUs, one per motor channel, and [TI DRV8328](https://www.ti.com/product/DRV8328) gate drivers. It runs [ARK32](https://github.com/ARK-Electronics/ARK32), ARK's open source fork of AM32, configured with the [ARK32 Configurator](https://ark32.arkelectron.com/), and takes DShot or PWM from PX4, ArduPilot and Betaflight flight controllers. USA built, NDAA compliant and [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).

Buy: [ARK 4IN1 ESC](https://arkelectron.com/product/ark-4in1-esc/) · [ARK 4IN1 ESC CONS](https://arkelectron.com/product/ark-4in1-esc-cons/)

| Variant | Motor and battery connections | Current per motor | Weight |
|---------|-------------------------------|-------------------|--------|
| ARK 4IN1 ESC | Solder | 50 A continuous, 75 A burst | 14.5 g |
| ARK 4IN1 ESC CONS | MR30 motor connectors, M2.5 threaded battery standoffs | 30 A continuous, 40 A burst (MR30 connector limit) | 24.0 g |

| Page | Contents |
|------|----------|
| [Firmware](firmware/) | ARK32, updating, downloads, default settings, ramp rate for large props |
| [ARK32 Configuration](ark32-configuration.md) | Setting KV, pole count and ramp rate before first use |
| [Ardupilot ESC Passthrough](firmware/ardupilot-esc-passthrough.md) | ArduPilot parameters for DShot and ESC passthrough |
| [Flash ARK32](firmware/flash-ark32.md) | Flashing ARK32 with the ARK32 Configurator |
| [Flash Bootloader](firmware/flash-bootloader.md) | Bootloader update, factory image and SWD recovery |
| [Hardware Reference](hardware.md) | Specifications, pinout, capacitance, datasheets, 3D model |
| [Motor Spin Direction](motor-spin-direction.md) | Reversing motors with DShot in PX4 and Betaflight |
| [PWM Calibration](pwm-calibration.md) | Calibrating the PWM input range |
