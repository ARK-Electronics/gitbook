---
cover: ../../.gitbook/assets/ark_v6x_no_sd_7.jpg
coverY: 0
---

# ARKV6X

A flight controller module built to the Pixhawk FMUv6X and Autopilot Bus standards. It plugs into any PAB carrier, such as the [ARK Pixhawk Autopilot Bus Carrier](../ark-pixhawk-autopilot-bus-carrier/README.md).

<a href="https://github.com/ARK-Electronics/ark-hardware/tree/main/ARKV6X/model" class="button secondary" data-icon="cube">3D model</a> <a href="https://github.com/ARK-Electronics/ark-hardware/blob/main/ARKV6X/datasheet/ARKV6X_Datasheet.pdf" class="button secondary" data-icon="file-pdf">Datasheet</a>

* **Processor:** STM32H743, 480 MHz
* **Sensors:** three synced IMUs, Bosch BMP390 barometer, Bosch BMM150 magnetometer
* **Autopilots:** PX4 (preinstalled), ArduPilot
* **Compliance:** USA built, NDAA, FCC, Blue Framework listed

## Variants

| Variant | IMUs | Range | Module | On PAB carrier |
|---------|------|-------|--------|----------------|
| **ARKV6X** | 2× ICM-42688-P, IIM-42652 | 2000 dps, 16 g | [Buy](https://arkelectron.com/product/arkv6x/) | [Buy](https://arkelectron.com/product/arkv6x-bundle/) |
| **ARKV6X Extended Range** | 3× IIM-42653 | 4000 dps, 32 g | [Buy](https://arkelectron.com/product/arkv6x-iim-42653/) | [Buy](https://arkelectron.com/product/arkv6x-extended-range-bundle/) |

## Documentation

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Firmware</strong></td><td>Build targets, flashing PX4 and ArduPilot, bootloader recovery</td><td><a href="firmware.md">firmware.md</a></td></tr><tr><td><strong>Hardware Reference</strong></td><td>Specifications, pinout, serial port mapping</td><td><a href="hardware.md">hardware.md</a></td></tr><tr><td><strong>PX4 Instructions</strong></td><td>Setting up PX4</td><td><a href="px4-instructions.md">px4-instructions.md</a></td></tr><tr><td><strong>ArduPilot Instructions</strong></td><td>Serial port mapping, hwdef changes for an IOMCU</td><td><a href="ardupilot-instructions.md">ardupilot-instructions.md</a></td></tr></tbody></table>
