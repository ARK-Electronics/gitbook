# PX4 Instructions

Find most up to date documentation at [https://docs.px4.io/main/en/dronecan/ark\_cannode.html](https://docs.px4.io/main/en/dronecan/ark_cannode.html)

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

To flash the bootloader firmware you need to use an ST-Link and the software of your choice. On Linux you can use the [ST Link Tools](https://github.com/stlink-org/stlink) on the command line:

```
st-flash write <bootloader_binary_path> 0x8000000
```

#### Flashing the Application

To flash the application firmware you can use the SD card method as [documented here](https://docs.px4.io/main/en/dronecan/#firmware-update) or you can use the DroneCAN GUI Tool and a USB-to-CAN adaptor to flash the firmware directly.

## Flight Controller Parameters

In order to use the ARK CANnode board, connect it to the Pixhawk CAN bus and enable the DroneCAN driver by setting parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` for dynamic node allocation (or `3` if using [DroneCAN ESCs](https://docs.px4.io/main/en/dronecan/escs.html)).

The steps are:

* In _QGroundControl_ set the parameter [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2` or `3` and reboot (see [Finding/Updating Parameters](https://docs.px4.io/main/en/advanced_config/parameters.html)).
* Connect ARK CANnode CAN to the Pixhawk CAN.

Once enabled, the module will be detected on boot.

DroneCAN configuration in PX4 is explained in more detail in [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan).

#### Enable Sensors <a href="#enable-sensors" id="enable-sensors"></a>

You will need to enable the subscriber appropriate for each of the sensors that are connected to the ARK CANnode.

This is done using the the parameters named like `UAVCAN_SUB_*` in the parameter reference (such as [UAVCAN\_SUB\_ASPD](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_ASPD), [UAVCAN\_SUB\_BARO](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_BARO) etc.).

## CANnode as PWM Expander

The ARK CANnode can be used as a PWM Expander over CAN. This allows configuring additional servos or ESCs over CAN. The update rate is limited to 400Hz, so it is recommneded to keep ESCs on the Flight Controllers outputs if possible and use the PWM Expander for servos only.\
\
As an example, this is how you would configure 4 Motors:

### Flight Controller Parameters

```
UAVCAN_PUB_ARM 1    # required
UAVCAN_EC_FUNC1 101 # Motor 1
UAVCAN_EC_FUNC2 102 # Motor 2
UAVCAN_EC_FUNC3 103 # Motor 3
UAVCAN_EC_FUNC4 104 # Motor 4
```

### CANnode Parameters

Using the DroneCAN GUI Tool or QGroundControl, configure the parameters to map your PWM outputs.

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

#### DShot

You can also use the DShot protocol on the CANnode. Make sure to set the timer output protocol for the outputs you are using for DShot. You can see the timer-to-output mapping here:\
[https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/cannode/src/timer\_config.cpp#L43-L50](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/cannode/src/timer_config.cpp#L43-L50)

```
PWM_MAIN_TIM0 -3 #DShot600
PWM_MAIN_TIM1 -3 #DShot600
PWM_MAIN_TIM2 -3 #DShot600
```

{% hint style="info" %}
Bidirectional DShot on the CANnode is not yet supported.
{% endhint %}

#### DShot Telemetry

When using DShot you can also receive ESC telemetry via UART from the Telem pin of the ESC. Connect the Telem pin from the ESC to the USART1\_RX pin of the[ UART1/I2C port](https://arkelectron.gitbook.io/ark-documentation/sensor/ark-cannode#uart1-i2c1-6-pin-jst-gh) of the CANnode. Set the **DSHOT\_TEL\_CFG** parameter on the CANnode to 201.
