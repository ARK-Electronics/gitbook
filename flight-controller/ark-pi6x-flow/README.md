---
cover: ../../.gitbook/assets/IMG_1650_edited (Large).JPG
coverY: 0
---

# ARK Pi6X Flow

The ARK Pi6X Flow puts a Raspberry Pi Compute Module 4 carrier, an ARKV6X flight controller, an ARK PAB power module and 4-in-1 ESC mounting on one board. The flight controller has dual [Invensense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/) IMUs, a [Bosch BMP390](https://www.bosch-sensortec.com/products/environmental-sensors/pressure-sensors/bmp390/) barometer and an [ST IIS2MDC](https://www.st.com/en/mems-and-sensors/iis2mdc.html) magnetometer; the Pi6X Flow adds a [PixArt PAW3902](https://www.pixart.com/products-detail/93/PAW3902JF-TXQT) optical flow sensor and a [Broadcom AFBR-S50LV85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lv85d) distance sensor. It runs PX4 and can be flashed with ArduPilot, and the Pi runs [ARK-OS](../../ark-os/). A Compute Module 5 also fits, with some interfaces lost. USA built, NDAA compliant and [Blue Framework listed](https://tyrionprod.servicenowservices.com/gsp?id=framework_list).

Buy: [ARK Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow/) · [ARK Pi6X](https://arkelectron.com/product/ark-pi6x/)

CAD: [3D model](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Pi6X/model)

| Variant | Optical flow and distance sensors |
|---------|-----------------------------------|
| ARK Pi6X Flow | PAW3902 and AFBR-S50LV85D (the AFBR-S50LV85D is not supported in ArduPilot) |
| ARK Pi6X | None |

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | PX4 and ArduPilot targets, updating from the Pi, bootloader recovery |
| [Hardware Reference](hardware.md) | Specifications, Compute Module 5 differences, USB, pinout, serial port mapping, block diagram, 3D model |
| [Flashing Guide](flashing-guide/README.md) | Imaging your own compute module and its `config.txt` |
| [Using ARK-OS](using-ark-os.md) | ARK-OS services and web UI on this board |
| [Autopilot Connections](autopilot-connections/README.md) | USB and serial links between the Pi and flight controller, flight controller reset, QGroundControl |
