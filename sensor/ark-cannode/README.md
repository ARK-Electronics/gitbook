---
cover: ../../.gitbook/assets/ark_can_3.jpg
coverY: 0
---

# ARK CANnode

The ARK CANnode is an open source generic [DroneCAN](https://docs.px4.io/main/en/dronecan/) node that includes a 6 degree of freedom IMU ([InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/) or [Bosch BMI088](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/)). Its main purpose is to enable the use of non-CAN sensors (I2C, SPI, UART) on the CAN bus. It also has PWM outputs to expand a vehicle's control outputs in quantity and physical distance. It runs PX4 DroneCAN firmware or ArduPilot AP\_Periph. USA built and FCC compliant.

[Buy the ARK CANnode](https://arkelectron.com/product/ark-cannode/)

| Page | Contents |
|------|----------|
| [Firmware](firmware.md) | PX4 and AP\_Periph firmware: building, flashing and node parameters |
| [Hardware Reference](hardware.md) | Specifications, pinout, LEDs, wiring, 3D model, case, schematic and BOM |
| [PX4 Instructions](px4-instructions.md) | Configuring with PX4, and using the CANnode as a PWM expander |
| [ArduPilot Instructions](ardupilot-instructions.md) | Configuring with ArduPilot, gripper and servo setup |
