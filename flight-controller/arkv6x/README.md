---
cover: ../../.gitbook/assets/ark_v6x_no_sd_7.jpg
coverY: 0
---

# ARKV6X

The ARKV6X is a flight controller module based on the [FMUV6X and Pixhawk Autopilot Bus open source standards](https://github.com/pixhawk/Pixhawk-Standards), with an [STM32H743IIK6](https://www.st.com/en/microcontrollers-microprocessors/stm32h743ii.html) MCU, a [Bosch BMP390](https://www.bosch-sensortec.com/en/products/environmental-sensors/pressure-sensors/bmp390) barometer and a [Bosch BMM150](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmm150-ds001.pdf) magnetometer. With triple synced IMUs, data averaging, voting, and filtering is possible. The Pixhawk Autopilot Bus (PAB) form factor enables the ARKV6X to be used on any [PAB-compatible carrier board](https://docs.px4.io/main/en/flight_controller/pixhawk_autopilot_bus.html), such as the [ARK Pixhawk Autopilot Bus Carrier](../ark-pixhawk-autopilot-bus-carrier/README.md). It ships with PX4 and can be flashed with ArduPilot. USA built, NDAA compliant, FCC compliant and [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).

Buy: [ARKV6X](https://arkelectron.com/product/arkv6x/) · [ARKV6X Extended Range](https://arkelectron.com/product/arkv6x-iim-42653/) · [ARKV6X Bundle](https://arkelectron.com/product/arkv6x-bundle/) · [ARKV6X Extended Range Bundle](https://arkelectron.com/product/arkv6x-extended-range-bundle/)

| Variant | IMUs | Gyro range | Accel range | On an ARK PAB Carrier |
|---------|------|------------|-------------|------------------------|
| ARKV6X | Dual ICM-42688-P, IIM-42652 | 2000 dps | 16 g | No |
| ARKV6X Extended Range | Triple IIM-42653 | 4000 dps | 32 g | No |
| ARKV6X Bundle | Dual ICM-42688-P, IIM-42652 | 2000 dps | 16 g | Yes |
| ARKV6X Extended Range Bundle | Triple IIM-42653 | 4000 dps | 32 g | Yes |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Build targets, flashing PX4 and ArduPilot, bootloader recovery |
| [Hardware Reference](hardware.md) | Specifications, pinout, serial port mapping, datasheet, 3D model |
| [PX4 Instructions](px4-instructions.md) | PX4 documentation |
| [ArduPilot Instructions](ardupilot-instructions.md) | ArduPilot documentation, serial port mapping, hwdef changes for an IOMCU |
