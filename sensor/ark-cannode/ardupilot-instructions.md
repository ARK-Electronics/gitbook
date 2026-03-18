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

### CANnode

Flash the ARK CANnode with AP\_Periph firmware using the DroneCAN GUI Tool. See the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for detailed instructions on connecting and uploading firmware.

1. Download the latest AP\_Periph firmware for the ARK CANnode from [firmware.ardupilot.org/AP\_Periph](https://firmware.ardupilot.org/AP_Periph/)
2. Connect the CANnode to the flight controller's CAN bus
3. Open the DroneCAN GUI Tool
4. Double-click the CANnode in the node list
5. Click **Update Firmware** and select the `.apj` AP\_Periph firmware file

{% hint style="info" %}
You can build the AP\_Periph firmware yourself:

```
./waf configure --board ARK_CANNODE
./waf AP_Periph
```

The bootloader can be updated from the running AP\_Periph firmware by setting `FLASH_BOOTLOADER = 1` on the CANnode via the DroneCAN GUI Tool.
{% endhint %}

## Enable CAN on the Flight Controller

Set the following parameters on the flight controller and reboot:

| Parameter       | Value | Description            |
| --------------- | ----- | ---------------------- |
| `CAN_P1_DRIVER` | 1     | Enable first CAN driver |
| `CAN_D1_PROTOCOL` | 1   | Set protocol to DroneCAN |

After rebooting, the CANnode should appear in the DroneCAN GUI Tool node list with a solid blue LED.

## CANnode as PWM Expander

The ARK CANnode has 8 PWM outputs that can be driven over CAN from the flight controller. This is useful for expanding servo outputs beyond what the flight controller provides, or for placing servos far from the flight controller.

### How It Works

The flight controller sends DroneCAN actuator commands based on its servo channel assignments. Each servo channel in the `CAN_D1_UC_SRV_BM` bitmask is transmitted with an actuator ID matching the channel number. The CANnode receives these commands and routes them to its PWM outputs based on the `OUT*_FUNCTION` parameters.

By default, the CANnode output functions are:

| CANnode Parameter | Default Value | Maps To            |
| ----------------- | ------------- | ------------------- |
| `OUT1_FUNCTION`   | 51            | FC Servo Channel 1  |
| `OUT2_FUNCTION`   | 52            | FC Servo Channel 2  |
| `OUT3_FUNCTION`   | 53            | FC Servo Channel 3  |
| `OUT4_FUNCTION`   | 54            | FC Servo Channel 4  |
| `OUT5_FUNCTION`   | 55            | FC Servo Channel 5  |
| `OUT6_FUNCTION`   | 56            | FC Servo Channel 6  |
| `OUT7_FUNCTION`   | 57            | FC Servo Channel 7  |
| `OUT8_FUNCTION`   | 58            | FC Servo Channel 8  |

{% hint style="info" %}
The `OUT*` parameters are accessed through the DroneCAN parameter interface. In the DroneCAN GUI Tool, double-click the CANnode and click **Fetch All** to view them.
{% endhint %}

### Servo Output Example: Gripper/Dropper

This example configures the first CANnode PWM output as a servo gripper for a dropping mechanism.

#### Flight Controller Parameters

| Parameter           | Value | Description                                      |
| ------------------- | ----- | ------------------------------------------------ |
| `CAN_D1_UC_SRV_BM` | 1     | Enable Servo Channel 1 over CAN (bitmask bit 0)  |
| `SERVO1_FUNCTION`   | 28    | Gripper                                           |
| `GRIP_ENABLE`       | 1     | Enable gripper                                    |
| `GRIP_TYPE`         | 0     | Servo                                             |
| `GRIP_GRAB`         | 1000  | PWM value for grab/close (adjust to your servo)   |
| `GRIP_RELEASE`      | 1200  | PWM value for release/open (adjust to your servo) |

{% hint style="warning" %}
After setting `GRIP_ENABLE = 1`, a reboot is required before the other `GRIP_*` parameters will appear.
{% endhint %}

{% hint style="info" %}
`CAN_D1_UC_SRV_BM` defaults to 0, meaning no servo commands are sent over CAN. This is the most commonly missed parameter.
{% endhint %}

#### CANnode Parameters

The defaults should work without changes:

| Parameter       | Value | Description                     |
| --------------- | ----- | ------------------------------- |
| `OUT1_FUNCTION` | 51    | RCPassThru1 (maps to FC Servo 1) |

#### Using Multiple Servos

To use the first 3 CANnode outputs, set `CAN_D1_UC_SRV_BM = 7` (bits 0, 1, 2) and configure `SERVO1_FUNCTION`, `SERVO2_FUNCTION`, and `SERVO3_FUNCTION` on the flight controller.

#### Using Higher Servo Channels

If the flight controller's lower servo channels are already in use for motors or control surfaces, you can use higher numbered channels. For example, to use FC Servo Channels 9-11:

**Flight Controller:**

| Parameter           | Value | Description                     |
| ------------------- | ----- | ------------------------------- |
| `CAN_D1_UC_SRV_BM` | 1792  | Bits 8, 9, 10 (Servo 9, 10, 11) |
| `SERVO9_FUNCTION`   | 28    | Gripper (or desired function)    |

**CANnode:**

| Parameter       | Value | Description                      |
| --------------- | ----- | -------------------------------- |
| `OUT1_FUNCTION` | 59    | RCPassThru9 (maps to FC Servo 9)  |
| `OUT2_FUNCTION` | 60    | RCPassThru10 (maps to FC Servo 10) |
| `OUT3_FUNCTION` | 61    | RCPassThru11 (maps to FC Servo 11) |

### Servo Output While Disarmed

CAN servo output is gated by the safety switch, not vehicle arming. To allow servo holding current while disarmed, disable the safety switch on the flight controller:

| Parameter         | Value | Description           |
| ----------------- | ----- | --------------------- |
| `BRD_SAFETY_DEFLT` | 0    | Disable safety switch  |

## Triggering the Gripper

### Via RC

Assign a switch on your transmitter to control the gripper:

| Parameter      | Value | Description    |
| -------------- | ----- | -------------- |
| `RCx_OPTION`   | 19    | Gripper Release |

Replace `x` with the RC channel number mapped to your desired switch.

### Via MAVLink

The gripper can also be controlled programmatically using `MAV_CMD_DO_GRIPPER`. The following Python script sends gripper open/close commands over USB:

{% file src="gripper_cmd.py" %}

Usage:

```bash
python3 gripper_cmd.py open
python3 gripper_cmd.py close
python3 gripper_cmd.py open --port /dev/ttyACM0
```

The script auto-detects ARK flight controllers connected via USB. Use `--port` to specify a device manually.

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

The hardware definition can be found here:\
[https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP\_HAL\_ChibiOS/hwdef/ARK\_CANNODE](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARK_CANNODE)
