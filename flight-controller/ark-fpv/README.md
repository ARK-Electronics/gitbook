---
cover: ../../.gitbook/assets/IMG_3628_edited.JPG
coverY: 0
---

# ARK FPV

The ARK FPV is a flight controller based on the [ARKV6X](../arkv6x/README.md) in a 30.5 mm mounting pattern, with an [STM32H743IIK6](https://www.st.com/en/microcontrollers-microprocessors/stm32h743ii.html) MCU, a [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/pressure-sensors-bmp390.html) barometer and an [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) magnetometer. It takes 3S–12S battery input and has a regulated 12 V 2 A output for video transmitters and payloads. It ships with PX4 and also runs ArduPilot and Betaflight. USA built and NDAA compliant.

Buy: [ARK FPV](https://arkelectron.com/product/ark-fpv-flight-controller/) · [ARK FPV 32X](https://arkelectron.com/product/ark-fpv-32x-flight-controller/)

CAD: [3D model](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_FPV/model) · [case](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_FPV/case)

The ARK FPV 32X is the same board with an [ST LSM6DSV32X](https://www.st.com/en/mems-and-sensors/lsm6dsv32x.html) IMU. Connectors, power, and the case are unchanged. The ARK FPV is [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).

| Variant | IMU | PX4 hardware type |
|---------|-----|-------------------|
| ARK FPV | [Invensense IIM-42653](https://invensense.tdk.com/products/smartindustrial/iim-42653/) | `ARKFPV000` |
| ARK FPV 32X | [ST LSM6DSV32X](https://www.st.com/en/mems-and-sensors/lsm6dsv32x.html) | `ARKFPV001` |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | Build targets, building and flashing PX4, ArduPilot and Betaflight, bootloader |
| [Hardware Reference](hardware.md) | Specifications, pinout, UART port mapping, 3D model and case |
| [PX4 Instructions](px4-instructions.md) | PX4 documentation |
| [ArduPilot Instructions](ardupilot-instructions.md) | ArduPilot documentation and UART mapping |
| [Betaflight Instructions](betaflight-instructions.md) | Connecting to the Betaflight app |
