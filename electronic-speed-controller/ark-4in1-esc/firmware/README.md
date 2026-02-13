# Firmware

### AM32 Bootloader Firmware

The ARK 4IN1 uses AM32\_F051\_BOOTLOADER\_PB4. You can find the latest release [here](https://github.com/am32-firmware/AM32-bootloader/releases).&#x20;

{% file src="../../../.gitbook/assets/AM32_F051_BOOTLOADER_PB4_V15.hex" %}

### AM32 App Firmware

Use the latest release of [AM32](https://github.com/am32-firmware/AM32/releases).

{% file src="../../../.gitbook/assets/AM32_ARK_4IN1_F051_2.20.hex" %}

### Low KV Large Prop Systems

As of AM32 v2.19, ramp speed is adjustable directly in the [AM32 configurator](https://am32.ca/) (Config Tool v1.93+). For low KV motors and large props, lower the ramp rate in the settings. A separate firmware is no longer required.

Alternatively, you can use the ARK\_4IN1\_RAMP\_F051 firmware which increases the maximum 0-100% ramp time to 200ms. When flashing back and forth from the standard ARK\_4IN1 firmware, select "Ignore current MCU layout".&#x20;

{% file src="../../../.gitbook/assets/AM32_ARK_4IN1_RAMP_F051_2.20.hex" %}

