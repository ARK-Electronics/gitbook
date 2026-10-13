# Firmware

{% hint style="danger" %}
**Before first use**, configure **KV**, **Pole Count**, and **Ramp Rate** for each motor channel in the [ARK32 Configurator](https://ark32.arkelectron.com/). The KV/pole defaults will not match your motor. Factory ramp is 2 %/ms — lower it for large props. See [ARK32 Configuration](../ark32-configuration.md).
{% endhint %}

The ARK 4IN1 ESC runs **[ARK32](https://github.com/ARK-Electronics/ARK32)**. Use ARK32 on this board.

## Why ARK32

ARK32 keeps DShot, PWM, KISS telemetry, and passthrough flashing. Changes that matter on this board:

| Change | Why it matters |
| ------ | -------------- |
| More reliable commutation | A missed zero-cross is one extra step, not a drop back to open-loop timing. The motor stays locked instead of bouncing between modes. |
| No hidden ramp back-off | Scaled by pack voltage, so one setting means the same volts per millisecond on 4S or 8S. Nothing at runtime lowers it — the firmware does not quietly slow the ramp after a desync. |
| Bidirectional DShot idle detection | The bootloader uses pulse width, not pin level, so the ESC does not get stuck in the bootloader when DShot idles high. |
| Hardware-in-the-loop CI | Tested on the ARK 4IN1, not only simulated. |

Full write-up: [What ARK32 adds](https://github.com/ARK-Electronics/ARK32#what-ark32-adds).

## Updating

Flash ARK32 through a Betaflight or ArduPilot flight controller with the [ARK32 Configurator](https://ark32.arkelectron.com/). See [Flash ARK32](flash-ark32.md); ArduPilot needs [ESC passthrough](ardupilot-esc-passthrough.md) set up first. For a blank or corrupted ESC, or to update the bootloader, see [Flash Bootloader](flash-bootloader.md).

## Downloads

### App firmware

Download **`ARK32_ARK_4IN1_F051`** from [ARK32 releases](https://github.com/ARK-Electronics/ARK32/releases).

### Bootloader

Download **`AM32_F051_BOOTLOADER_ARK4IN1`** from [ARK32-bootloader releases](https://github.com/ARK-Electronics/ARK32-bootloader/releases). The filename includes a version suffix (for example `_V18`).

## Settings

Factory defaults, per motor channel. Set them with the [ARK32 Configurator](https://ark32.arkelectron.com/); see [ARK32 Configuration](../ark32-configuration.md).

| Setting | Default | Description |
|---------|---------|-------------|
| Motor KV | 1020 | Motor nameplate kV. Set it to your motor's |
| Motor Poles | 14 | Magnets on the rotor. Set it to your motor's |
| Ramp Rate | 2 %/ms | How fast duty may change, in percent of full throttle per millisecond. See [Low KV Large Prop Systems](#low-kv-large-prop-systems) |
| Timing Advance | 15°, fixed | How early the ESC commutates relative to the BEMF zero-cross |
| PWM Type | By RPM | Switching frequency follows commutation speed |
| Protocol | DShot | Throttle input. PWM input needs a [PWM Calibration](../pwm-calibration.md) |
| Low / High Threshold | 1020 µs / 1980 µs | PWM pulse treated as zero and full throttle. Ignored under DShot |
| Temperature Limit | Off | Folds duty back as FET temperature approaches this value |
| Current Limit | Off | All four channels share one current shunt, so this is not a per-motor limit |

## Low KV Large Prop Systems

Low KV motors swinging large props on higher cell counts (e.g. 6S with 10"+ props) can experience **desync events during rapid throttle changes**. The root cause is motor coil demagnetization time extending past the BEMF sensing window when current spikes during a fast throttle transient — the ESC temporarily loses rotor position and the motor stutters. Limiting how fast the duty cycle can change keeps the transient current in check and preserves the sensing window.

Set ramp rate in the [ARK32 Configurator](https://ark32.arkelectron.com/). These are **rough starting points** — raise for more punch, lower if the motor stutters when throttle increases quickly:

| Motor kV | Typical prop | Starting ramp |
| -------- | ------------ | ------------- |
| High (~1800+) | 5–7" | 16 %/ms |
| Mid (~800–1500) | 7–10" | **2 %/ms** (factory) |
| Low (~500 and below) | 10"+ | 1 %/ms or lower |

The setting is a **ceiling on all three rpm bands**, not a rate the ESC always applies. The firmware ramps at up to 2 %/ms during startup, 6 %/ms at low rpm and 16 %/ms once spun up, and your value lowers each of those. The factory 2 %/ms therefore flattens the progression — the ESC ramps at the startup rate everywhere, including cruise, which is what makes it safe on a large prop. Set 16 %/ms or higher and all three bands run at their firmware defaults.

A separate slow-ramp firmware is not required — ramp rate is an EEPROM setting on the regular ARK32 image.

## Release Notes

See [ARK32 releases](https://github.com/ARK-Electronics/ARK32/releases).
