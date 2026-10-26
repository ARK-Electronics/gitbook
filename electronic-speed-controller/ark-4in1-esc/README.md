---
description: >-
  NDAA compliant, made in the USA, 4 in 1 electronic speed controller running
  open source ARK32 firmware.
cover: ../../.gitbook/assets/IMG_3371 edited (Large).JPG
coverY: -23.514666666666663
---

# ARK 4IN1 ESC

A 4-in-1 ESC that drives four brushless motors. It takes DShot or PWM from PX4, ArduPilot and Betaflight flight controllers.

<a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_4IN1_ESC/model" class="button secondary" data-icon="cube">3D model</a>

* **MCUs:** four STM32F051, one per motor, with TI DRV8328 gate drivers
* **Input:** 3S–8S
* **Mounting:** 30.5 mm
* **Firmware:** ARK32, ARK's open source AM32 fork, set up with the ARK32 Configurator
* **Compliance:** USA built, NDAA, Blue Framework listed

## Variants

| Variant | Motor and battery connections | Current per motor | Datasheet | Buy |
|---------|-------------------------------|-------------------|-----------|-----|
| **ARK 4IN1 ESC** | Solder | 50 A continuous, 75 A burst | [PDF](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_4IN1_ESC/datasheet/ARK_4IN1_ESC_Datasheet.pdf) | [Buy](https://arkelectron.com/product/ark-4in1-esc/) |
| **ARK 4IN1 ESC CONS** | MR30 motor connectors, M2.5 battery standoffs | 30 A continuous, 40 A burst (MR30 limit) | [PDF](https://github.com/ARK-Electronics/ark-hardware/blob/main/ARK_4IN1_ESC/datasheet/ARK_4IN1_ESC_CONS_Datasheet.pdf) | [Buy](https://arkelectron.com/product/ark-4in1-esc-cons/) |

## Documentation

* [Firmware](firmware/README.md)
* [Hardware Reference](hardware.md)
* [Motor Spin Direction](motor-spin-direction.md)
* [PWM Calibration](pwm-calibration.md)
