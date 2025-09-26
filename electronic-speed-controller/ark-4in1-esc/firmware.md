# Firmware

### AM32 Bootloader Firmware

The ARK 4IN1 uses AM32\_F051\_BOOTLOADER\_PB4. You can find the latest release [here](https://github.com/am32-firmware/AM32-bootloader/releases).&#x20;

{% file src="../../.gitbook/assets/AM32_F051_BOOTLOADER_PB4_V15.hex" %}

#### Flashing Bootloader (ESC Passthrough method)

You can update the bootloader using the [AM32 Configurator](https://am32.ca/configurator). Once connected select "Flash firmware" and select the "Bootloader" tab. Download the **AM32-bootloader-updaters-amj.zip** from the [AM32-bootloader release artifacts](https://github.com/am32-firmware/AM32-bootloader/releases). Select the **AM32\_F051\_BL\_UPDATER\_PB4\_V15.amj.**

### AM32 App Firmware

Use the latest release of [AM32](https://github.com/am32-firmware/AM32/releases).

{% file src="../../.gitbook/assets/AM32_ARK_4IN1_F051_2.19 (1).hex" %}

### Low KV Large Prop Systems

For low KV motors and large props, use the ARK\_4IN1\_RAMP\_F051 firmware which increases the maximum 0-100% ramp time to 200ms. When flashing back and forth from the standard ARK\_4IN1 firmware, select "Ignore current MCU layout".&#x20;

{% file src="../../.gitbook/assets/AM32_ARK_4IN1_RAMP_F051_2.19 (1).hex" %}

***

## Flashing Firmware

You can flash firmware using ESC Passthrough (Betaflight and Ardupilot) or using SWD. The easiest method is to use Betaflight ESC Passthrough.

### Betaflight ESC Passthrough

Connect the ESC to a Flight Controller flashed with Betaflight (eg ARK FPV). Power on your ESC and Flight controller and connect to your Host PC via USB. Navigate to [https://am32.ca/configurator](https://am32.ca/configurator).\
\
Connect to your device\
![](<../../.gitbook/assets/image (43).png>)

Once connected, select Read\
![](<../../.gitbook/assets/image (44).png>)

If successful you should see all of the settings for each motor

<figure><img src="../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

***

### Ardupilot ESC Passthrough

Connect the ESC to a Flight Controller flashed with Ardupilot (eg ARK FPV). Power on your ESC and Flight controller and connect to your Host PC via USB. Modify the Ardupilot parameters using [QGroundControl](https://qgroundcontrol.com/):

**Setup Ardupilot parameters to use DShot**

<pre><code>## Motor mapping
SERVO1_FUNCTION 34  	# Motor 2
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

From here the rest is the same as Betalfight. Navigate to [https://am32.ca/configurator](https://am32.ca/configurator) and select the `Connect` and `Read` buttons.

[^1]: 
