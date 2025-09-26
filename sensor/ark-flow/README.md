---
cover: ../../.gitbook/assets/SAM_0829 (Large).JPG
coverY: 0
---

# ARK Flow

ARK Flow is an open source [DroneCAN](https://docs.px4.io/main/en/dronecan/) [optical flow](https://docs.px4.io/main/en/sensor/optical_flow.html), [distance sensor](https://docs.px4.io/main/en/sensor/rangefinders.html), and IMU module.

### Hardware Specifications <a href="#hardware-specifications" id="hardware-specifications"></a>

* [Open Source Schematic and BOM](https://github.com/ARK-Electronics/ARK_Flow)
* Sensors
  * PixArt PAW3902 Optical Flow Sensor
    * Tracks under super low light condition of >9 lux
    * Wide working range from 80mm up to 30m
    * Up to 7.4 rad/s
  * 40mW IR LED built onto board for improved low light operation
  * Broadcom AFBR-S50LV85D Time-of-Flight Distance Sensor
    * Integrated 850 nm laser light source
    * Field-of-View (FoV) of 12.4° x 6.2° with 32 pixels
    * Typical distance range up to 30m
    * Operation of up to 200k Lux ambient light
    * Works well on all surface conditions
    * Transmitter beam of 2° x 2° to illuminate between 1 and 3 pixels
  * Bosch BMI088 6-Axis IMU or Invensense ICM-42688-P 6-Axis IMU
* STM32F412CEU6 MCU
* Two Pixhawk Standard CAN Connectors (4 Pin JST GH)
* Pixhawk Standard Debug Connector (6 Pin JST SH)
* Software-toggleable built in CAN termination resistor
* Small Form Factor
  * 3cm x 3cm x 1.4cm
* LED Indicators
* USA Built

### LED Meanings <a href="#led-meanings" id="led-meanings"></a>

You will see both red and blue LEDs on the ARK Flow when it is being flashed, and a solid blue LED if it is running properly.

If you see a solid red LED there is an error and you should check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the Ark Flow has `ark_can-flow_canbootloader` installed prior to flashing `ark_can-flow_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

### Video <a href="#video" id="video"></a>

Video

{% embed url="https://www.youtube.com/watch?v=SAbRe1fi7bU&list=PLUepQApgwSozmwhOo-dXnN33i2nBEl1c0&t=1s" %}
_PX4 holding position using the ARK Flow sensor for velocity estimation (in_ [_Position Mode_](https://docs.px4.io/main/en/flight_modes_mc/position.html)_)._
{% endembed %}

### Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

### Firmware

{% file src="../../.gitbook/assets/80-1.16.3c45b562.uavcan.bin" %}
ARK Flow Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-flow_canbootloader.bin" %}
ARK Flow Bootloader
{% endfile %}

## Release Notes

* 80-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 80-1.16.afb2c08b - 2025-8-6
  * AFBRS50: Fix long range measurement publishing
* 80-1.16.2248a40e - 2025-7-10
  * [AFBRS40: fix Range Mode switching](https://github.com/PX4/PX4-Autopilot/pull/25185)
* 80-1.16.d0bfa548 - 2025-6-12
  * [AFBRS50 fix scheduling and refactor](https://github.com/PX4/PX4-Autopilot/pull/24837)
* 80-1.15.82ff8744 - 2025-6-11
  * Add DroneCAN RawIMU publisher
* 80-1.16.61036f77 - 2025-2-7
  * Update to [AFBR 1.6.5 API](https://github.com/Broadcom/AFBR-S50-API/releases/tag/v1.6.5)
    * Improved distance sensor performance
