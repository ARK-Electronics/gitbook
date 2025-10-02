---
description: >-
  This page details how to configure Ardupilot for use with the
  am32-configurator to flash firmware.
---

# Ardupilot ESC Passthrough

Connect the ESC to a Flight Controller flashed with Ardupilot (eg ARK FPV). Power on your ESC and Flight controller and connect to your Host PC via USB. Modify the Ardupilot parameters using [QGroundControl](https://qgroundcontrol.com/):

**Setup Ardupilot parameters to use DShot**

<pre><code>## Motor mapping
SERVO1_FUNCTION 34  	# Motor 2 -- this should match your motor layout
SERVO2_FUNCTION 35  	# Motor 3
SERVO3_FUNCTION 36  	# Motor 4
SERVO4_FUNCTION 33  	# Motor 1

## Dshot ESC setup
MOT_PWM_TYPE 6 		# DShot600
<a data-footnote-ref href="#user-content-fn-1">SERVO_DSHOT_ESC</a> 1 	# BLHeli32/Kiss

## Bidirectional Dshot ESC setup
SERVO_BLH_BDMASK 15 	# Channels 1 - 4
</code></pre>

**Setup Ardupilot parameters for ESC Passthrough**

```
## ESC Passthrough
SERVO_BLH_AUTO to 1
SERVO_BLH_MASK to 15 (if using output channels 1 - 4)
```

Follow the instructions on the [AM32 Firmware](flash-am32.md) page to flash firmware.

[^1]: 
