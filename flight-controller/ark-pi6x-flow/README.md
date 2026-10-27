---
cover: ../../.gitbook/assets/IMG_1650_edited (Large).JPG
coverY: 0
---

# ARK Pi6X Flow

A Raspberry Pi compute module carrier with a flight controller, a power module and 4-in-1 ESC mounting on one board. The Pi runs [ARK-OS](../../ark-os/README.md).

<a href="https://arkelectron.com/product-category/flight-controllers/pi6x/" class="button primary" data-icon="cart-shopping">Buy</a> <a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Pi6X/model" class="button secondary" data-icon="cube">3D model</a>

* **Flight controller:** STM32H743, dual InvenSense ICM-42688-P IMUs, Bosch BMP390 barometer, ST IIS2MDC magnetometer
* **Companion computer:** Raspberry Pi Compute Module 4; a Compute Module 5 fits, with some interfaces lost
* **Power:** 2S–6S battery input, 30.5 × 30.5 mm 4-in-1 ESC mounting
* **Autopilots:** PX4 (preinstalled), ArduPilot
* **Compliance:** USA built, NDAA, Blue Framework listed

## Variants

| Variant | Optical flow and distance sensors | Buy |
|---------|-----------------------------------|-----|
| **ARK Pi6X Flow** | PAW3902 flow, AFBR-S50LV85D distance | [Buy](https://arkelectron.com/product/ark-pi6x-flow/) |
| **ARK Pi6X** | None | [Buy](https://arkelectron.com/product/ark-pi6x/) |

ArduPilot does not support the AFBR-S50LV85D.

## Documentation

* [Firmware](firmware.md)
* [Hardware Reference](hardware.md)
* [Flashing Guide](flashing-guide/README.md)
* [Using ARK-OS](using-ark-os.md)
* [Autopilot Connections](autopilot-connections/README.md)
