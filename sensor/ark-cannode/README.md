---
cover: ../../.gitbook/assets/ark_can_3.jpg
coverY: 0
---

# ARK CANnode

[ARK CANnode](https://arkelectron.com/product/ark-cannode/) is an open source generic [DroneCAN](https://docs.px4.io/main/en/dronecan/) node that includes a 6 degree of freedom IMU. Its main purpose is to enable the use of non-CAN sensors (I2C, SPI, UART) on the CAN bus. It also has PWM outputs to expand a vehicle's control outputs in quantity and physical distance.

![ARK CANnode](https://docs.px4.io/main/assets/ark_cannode.-X5QpRbg.jpg)

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_CANNODE](https://github.com/ARK-Electronics/ARK_CANNODE)

### Hardware Specifications <a href="#hardware-specifications" id="hardware-specifications"></a>

* [Open Source Schematic and BOM](https://github.com/ARK-Electronics/ARK_CANNODE)
* Sensors
  * Bosch BMI088 6-Axis IMU or Invensense ICM-42688-P 6-Axis IMU
* STM32F412CGU6 MCU
  * 1MB Flash
* Two Pixhawk Standard CAN Connectors
  * 4 Pin JST GH
* Pixhawk Standard I2C Connector
  * 4 Pin JST GH
* Pixhawk Standard UART/I2C Connector (Basic GPS Port)
  * 6 Pin JST GH
* Pixhawk Standard SPI Connector
  * 7 Pin JST GH
* PWM Connector
  * 10 Pin JST JST
  * 8 PWM Outputs
  * Matches Pixhawk 4 PWM Connector Pinout
* Pixhawk Standard Debug Connector
  * 6 Pin JST SH
* Small Form Factor
  * 3cm x 3cm x 1.3cm
* LED Indicators
* USA Built
* Power Requirements
  * 5V
  * Current dependent on connected peripherals

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK CANnode is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

### LED Meanings <a href="#led-meanings" id="led-meanings"></a>

You will see both red and blue LEDs on the ARK CANnode when it is being flashed, and a solid blue LED if it is running properly.

If you see a solid red LED there is an error and you should check the following:

* Make sure the flight controller has an SD card installed.
* Make sure the ARK CANnode has `ark_cannode_canbootloader` installed prior to flashing `ark_cannode_default`.
* Remove binaries from the root and ufw directories of the SD card and try to build and flash again.

### Ark CANNode Configuration <a href="#ark-cannode-configuration" id="ark-cannode-configuration"></a>

On the ARK CANnode, you may need to configure the following parameters:

| Parameter                                                                                          | Description                   |
| -------------------------------------------------------------------------------------------------- | ----------------------------- |
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | CAN built-in bus termination. |

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### UART1/I2C1 - 6 Pin JST-GH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>USART1_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART1_RX</td><td>3.3V</td></tr><tr><td>4</td><td>I2C1_SCL</td><td>3.3V</td></tr><tr><td>5</td><td>I2C1_SDA</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### I2C1 - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5.0V Out (500mA)</td><td>5.0V</td></tr><tr><td>2</td><td>I2C1_SCL</td><td>3.3V</td></tr><tr><td>3</td><td>I2C1_SDA</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
