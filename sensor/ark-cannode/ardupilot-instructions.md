---
description: >-
  Guide for setting up an ARK CANnode as a PWM servo expander with ArduPilot
  AP_Periph firmware, including gripper/dropper configuration.
---

# ArduPilot Instructions

The ARK CANnode can run [ArduPilot AP\_Periph](https://ardupilot.org/dev/docs/ap-periph-landing-page.html) firmware, enabling it to act as a DroneCAN peripheral node for expanding servo outputs, ESC control, and sensor connectivity over CAN.

## Flashing Firmware

### Flight Controller

Flash your ARK flight controller with ArduPilot firmware using [QGroundControl](https://qgroundcontrol.com/) over USB.

### Enable CAN on the Flight Controller

Set the following parameters on the flight controller and reboot:

| Parameter          | Value | Description             |
| ------------------ | ----- | ----------------------- |
| `CAN_P1_DRIVER`   | 1     | Enable first CAN driver |
| `CAN_D1_PROTOCOL`  | 1     | Set protocol to DroneCAN |

### CANnode

Flash the ARK CANnode with AP\_Periph firmware using the DroneCAN GUI Tool. See the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for detailed instructions on connecting and uploading firmware.

1. Download the latest AP\_Periph firmware for the ARK CANnode from [firmware.ardupilot.org/AP\_Periph](https://firmware.ardupilot.org/AP_Periph/)
2. Connect the CANnode to the flight controller's CAN bus
3. Open the DroneCAN GUI Tool
4. Double-click the CANnode in the node list
5. Click **Update Firmware** and select the `.apj` AP\_Periph firmware file

## Gripper/Dropper Setup

This example configures the first CANnode PWM output as a servo gripper for a dropping mechanism.

### Flight Controller Parameters

| Parameter           | Value | Description                                      |
| ------------------- | ----- | ------------------------------------------------ |
| `CAN_D1_UC_SRV_BM` | 1     | Enable Servo Channel 1 over CAN (bitmask bit 0)  |
| `SERVO1_FUNCTION`   | 28    | Gripper                                           |
| `GRIP_ENABLE`       | 1     | Enable gripper                                    |
| `GRIP_TYPE`         | 0     | Servo                                             |
| `GRIP_GRAB`         | 1000  | PWM value for grab/close (adjust to your servo)   |
| `GRIP_RELEASE`      | 1200  | PWM value for release/open (adjust to your servo) |
| `BRD_SAFETY_MASK`   | 1     | Allow Servo Channel 1 to output with safety on    |

{% hint style="warning" %}
After setting `GRIP_ENABLE = 1`, a reboot is required before the other `GRIP_*` parameters will appear.
{% endhint %}

{% hint style="info" %}
`CAN_D1_UC_SRV_BM` defaults to 0, meaning no servo commands are sent over CAN. This is the most commonly missed parameter.
{% endhint %}

### CANnode Parameters

The defaults should work without changes. The CANnode output functions map to flight controller servo channels by default (OUT1 maps to FC Servo 1, OUT2 to Servo 2, etc.).

{% hint style="info" %}
The `OUT*` parameters are accessed through the DroneCAN parameter interface. In the DroneCAN GUI Tool, double-click the CANnode and click **Fetch All** to view them.
{% endhint %}

### Triggering the Gripper

#### Via RC

Assign a switch on your transmitter to control the gripper:

| Parameter      | Value | Description     |
| -------------- | ----- | --------------- |
| `RCx_OPTION`   | 19    | Gripper Release |

Replace `x` with the RC channel number mapped to your desired switch.

#### Via MAVLink

The gripper can also be controlled programmatically using `MAV_CMD_DO_GRIPPER`. The following Python script sends gripper open/close commands over USB:

{% file src="gripper_cmd.py" %}

Usage:

```bash
python3 gripper_cmd.py open
python3 gripper_cmd.py close
```

The script auto-detects ARK flight controllers connected via USB. Use `--port` to specify a device manually:

```bash
python3 gripper_cmd.py open --port /dev/ttyACM0
```

## Using Multiple Servos

To use the first 3 CANnode outputs, set `CAN_D1_UC_SRV_BM = 7` (bits 0, 1, 2) and configure `SERVO1_FUNCTION`, `SERVO2_FUNCTION`, and `SERVO3_FUNCTION` on the flight controller. Update `BRD_SAFETY_MASK` accordingly (e.g., 7 for channels 1-3).

## Building Firmware

### Application

```
./waf configure --board ARK_CANNODE
./waf AP_Periph
```

### Bootloader

```
./waf configure --board ARK_CANNODE --bootloader
./waf bootloader
```

The bootloader can also be updated from the running AP\_Periph firmware by setting `FLASH_BOOTLOADER = 1` on the CANnode via the DroneCAN GUI Tool.

The hardware definition can be found here:\
[https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP\_HAL\_ChibiOS/hwdef/ARK\_CANNODE](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARK_CANNODE)
