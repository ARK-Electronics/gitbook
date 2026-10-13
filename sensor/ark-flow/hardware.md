# Hardware Reference

## Specifications

| Specification | Value |
|---------------|-------|
| Optical flow sensor | [PixArt PAW3902](https://www.pixart.com/products-detail/93/PAW3902JF-TXQT) |
| Flow working range | 80 mm to infinity |
| Low light | Tracks under super low light conditions of >9 lux. 40 mW IR LED on the board for improved low light operation |
| Max flow rate | 7.4 rad/s |
| Distance sensor | [Broadcom AFBR-S50LV85D](https://www.broadcom.com/products/optical-sensors/time-of-flight-3d-sensors/afbr-s50lv85d) time-of-flight, integrated 850 nm laser light source |
| Distance range | Typically up to 30 m, works well on all surface conditions |
| Field of view | 12.4° × 6.2° with 32 pixels. 2° × 2° transmitter beam illuminates 1 to 3 pixels |
| Ambient light | Operates up to 200k lux |
| IMU | [Bosch BMI088](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi088/) or [InvenSense ICM-42688-P](https://invensense.tdk.com/products/motion-tracking/6-axis/icm-42688-p/), 6-axis |
| MCU | STM32F412CEU6 |
| CAN | 2× Pixhawk-standard 4-pin JST-GH, software-toggleable built-in termination resistor |
| Debug | Pixhawk-standard 6-pin JST-SH |
| Power | 5 V, 71 mA average, 76 mA max |
| Dimensions | 3 × 3 × 1.4 cm |
| Weight | 5 g |

## Pinout

### CAN (×2) — 4-pin JST-GH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 5V | 5.0 V |
| 2 | CAN_P | 5.0 V |
| 3 | CAN_N | 5.0 V |
| 4 | GND | GND |

### Debug — 6-pin JST-SH

| Pin | Signal | Voltage |
|-----|--------|---------|
| 1 | 3.3V | 3.3 V |
| 2 | USART2_TX | 3.3 V |
| 3 | USART2_RX | 3.3 V |
| 4 | FMU_SWDIO | 3.3 V |
| 5 | FMU_SWCLK | 3.3 V |
| 6 | GND | GND |

## LEDs

You will see both red and blue LEDs on the ARK Flow when it is being flashed, and a solid blue LED if it is running properly.

If you see a solid red LED there is an error and you should check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the Ark Flow has `ark_can-flow_canbootloader` installed prior to flashing `ark_can-flow_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

## Wiring

The ARK Flow is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK Flow's second CAN connector.

## Mounting

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

## 3D Model and Case

| File | Contents |
|------|----------|
| [ARK\_Flow\_Rev\_2\_3D\_Model.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/model/ARK_Flow_Rev_2_3D_Model.step) | Board, rev 2 |
| [ARK\_Flow\_Rev\_2\_3D\_Model\_With\_FOV.step](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/model/ARK_Flow_Rev_2_3D_Model_With_FOV.step) | Board, rev 2, with the sensor field of view |
| [Top\_Case\_Rev\_1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/case/Top_Case_Rev_1.stl) | Case top, rev 1 |
| [Bottom\_Case\_Rev\_1.stl](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/case/Bottom_Case_Rev_1.stl) | Case bottom, rev 1 |

All files: [ARK\_Flow in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_Flow)

## Schematic and BOM

| File | Contents |
|------|----------|
| [ARK\_Flow\_Rev\_2\_Schematic.pdf](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/schematic/ARK_Flow_Rev_2_Schematic.pdf) | Schematic, rev 2 |
| [ARK\_Flow\_Rev\_2\_BOM.xlsx](https://github.com/ARK-Electronics/ark-hardware/raw/main/ARK_Flow/bom/ARK_Flow_Rev_2_BOM.xlsx) | Bill of materials, rev 2 |
