# PX4 Instructions

Find additional documentation at [https://docs.px4.io/main/en/dronecan/ark\_cannode.html](https://docs.px4.io/main/en/dronecan/ark_cannode.html)

ARK CANnode runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

## CANnode Firmware

ARK CANnode boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

#### Building the Application&#x20;

```
make ark_cannode
```

#### Building the Bootloader&#x20;

```
make ark_cannode_canbootloader
```

#### Flashing the Bootloader

To flash the bootloader firmware you need an ST-LINK programmer. See the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md) for setup instructions.

```
st-flash write <bootloader_binary_path> 0x08000000
```

#### Flashing the Application

To flash the application firmware you can use the SD card method as [documented here](https://docs.px4.io/main/en/dronecan/#firmware-update) or you can use the DroneCAN GUI Tool and a USB-to-CAN adaptor to flash the firmware directly.

If you flash the application over SWD instead, it goes at the application offset — `0x08000000` is the bootloader's address:

```
st-flash write <application_binary_path> 0x08010000
```

## Configuration

Connect the ARK CANnode to the flight controller's CAN bus using a standard 4-pin JST-GH cable.

DroneCAN configuration in PX4 is explained in more detail in [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan).

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation. Set to `3` if using [DroneCAN ESCs](https://docs.px4.io/main/en/dronecan/escs.html) |

#### Optional

Enable a `UAVCAN_SUB_*` subscriber for each sensor connected to the ARK CANnode. The onboard IMU subscriber is listed below; for other sensors (airspeed, barometer, etc.), see the parameters named `UAVCAN_SUB_*` in the [PX4 parameter reference](https://docs.px4.io/main/en/advanced_config/parameter_reference.html).

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` to subscribe to DroneCAN `RawIMU` messages from the onboard IMU. Requires `CANNODE_PUB_IMU` to also be set on the ARK CANnode |

### CAN Node Parameters

Set the following on the CANnode and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | Set to `1` if this is the last node on the CAN bus |
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | Set to `1` to publish `RawIMU` messages from the onboard ICM-42688-P IMU on the CAN bus. Requires `UAVCAN_SUB_IMU` to also be set on the flight controller |

## CANnode as PWM Expander

The ARK CANnode can be used as a PWM Expander over CAN, allowing you to drive additional servos or ESCs from the flight controller.

### Common Setup

Regardless of whether you are using servos or ESCs, the following flight controller parameters must be configured:

```
UAVCAN_ENABLE 3  # Sensors and Actuators (ESCs) Automatic Config
UAVCAN_PUB_ARM 1 # Required to publish arming state to CANnode
```

On the CANnode, set the timer output protocol using `PWM_MAIN_TIMx` parameters. You can see the timer-to-output mapping here:\
[https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/cannode/src/timer\_config.cpp#L43-L50](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/cannode/src/timer_config.cpp#L43-L50)

### Servos

For servo outputs, we recommend using standard 50Hz PWM. Set the timer protocol to 50Hz on the CANnode:

```
PWM_MAIN_TIM0 50
```

#### Flight Controller Parameters

```
UAVCAN_EC_FUNC1 201 # Servo 1
UAVCAN_EC_FUNC2 202 # Servo 2
UAVCAN_EC_FUNC3 203 # Servo 3
UAVCAN_EC_FUNC4 204 # Servo 4
```

#### CANnode Parameters

Using the DroneCAN GUI Tool or QGroundControl, configure the parameters to map your PWM outputs:

```
PWM_MAIN_FUNC1 201 # Servo 1
PWM_MAIN_FUNC2 202 # Servo 2
PWM_MAIN_FUNC3 203 # Servo 3
PWM_MAIN_FUNC4 204 # Servo 4
```

You can also optionally adjust the min, max, and disarmed values:

```
PWM_MAIN_DIS1 1500
PWM_MAIN_MIN1 1000
PWM_MAIN_MAX1 2000
```

### ESCs

For ESC outputs, we recommend using DShot300. Set the timer protocol on the CANnode:

```
PWM_MAIN_TIM0 -4 # DShot300
```

{% hint style="info" %}
PWM over CAN update rate is limited to 400Hz, so it is recommended to keep ESCs on the flight controller's outputs if possible.
{% endhint %}

#### Flight Controller Parameters

```
UAVCAN_EC_FUNC1 101 # Motor 1
UAVCAN_EC_FUNC2 102 # Motor 2
UAVCAN_EC_FUNC3 103 # Motor 3
UAVCAN_EC_FUNC4 104 # Motor 4
```

#### CANnode Parameters

Using the DroneCAN GUI Tool or QGroundControl, configure the parameters to map your PWM outputs:

```
PWM_MAIN_FUNC1 101 # Motor 1
PWM_MAIN_FUNC2 102 # Motor 2
PWM_MAIN_FUNC3 103 # Motor 3
PWM_MAIN_FUNC4 104 # Motor 4
```

You can also optionally adjust the min, max, and disarmed values:

```
PWM_MAIN_DIS1 1000
PWM_MAIN_MIN1 1100
PWM_MAIN_MAX1 1900
```

{% hint style="info" %}
Bidirectional DShot on the CANnode is not yet supported.
{% endhint %}

#### DShot Telemetry

When using DShot you can also receive ESC telemetry via UART from the Telem pin of the ESC. Connect the Telem pin from the ESC to the USART1\_RX pin of the[ UART1/I2C port](https://arkelectron.gitbook.io/ark-documentation/sensor/ark-cannode#uart1-i2c1-6-pin-jst-gh) of the CANnode. Set the **DSHOT\_TEL\_CFG** parameter on the CANnode to 201.
