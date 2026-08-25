# Firmware

## Why ARK32

The ARK 4IN1 ESC runs **[ARK32](https://github.com/ARK-Electronics/ARK32)**.

ARK32 keeps DShot, PWM, KISS telemetry, and passthrough flashing. Changes that matter on this board:

| Change | Why it matters |
| ------ | -------------- |
| More reliable commutation | A missed zero-cross is one extra step, not a drop back to open-loop timing. The motor stays locked instead of bouncing between modes. |
| The ramp you set is the ramp that runs | Scaled by pack voltage so the same setting means the same volts per millisecond on 4S or 8S. The firmware does not secretly slow the ramp after a desync. |
| Bidirectional DShot idle detection | The bootloader uses pulse width, not pin level, so the ESC does not get stuck in the bootloader when DShot idles high. |
| Hardware-in-the-loop CI | Tested on the ARK 4IN1, not only simulated. |

Full write-up: [What ARK32 adds](https://github.com/ARK-Electronics/ARK32#what-ark32-adds).

## Configuration

Use the [ARK32 Configurator](https://ark32.arkelectron.com/). See [ARK32 Configuration](../ark32-configuration.md).

## Bootloader

Download **`AM32_F051_BOOTLOADER_ARK4IN1`** from [ARK32-bootloader releases](https://github.com/ARK-Electronics/ARK32-bootloader/releases). The filename includes a version suffix (for example `_V18`).

See [Flash Bootloader](flash-bootloader.md).

## App firmware

Download **`ARK32_ARK_4IN1_F051`** from [ARK32 releases](https://github.com/ARK-Electronics/ARK32/releases).

See [Flash ARK32](flash-ark32.md).

## Low KV Large Prop Systems

Low KV motors swinging large props on higher cell counts (e.g. 6S with 10"+ props) can experience **desync events during rapid throttle changes**. The root cause is motor coil demagnetization time extending past the BEMF sensing window when current spikes during a fast throttle transient — the ESC temporarily loses rotor position and the motor stutters. Limiting how fast the duty cycle can change keeps the transient current in check and preserves the sensing window.

Set ramp rate in the [ARK32 Configurator](https://ark32.arkelectron.com/). These are **rough starting points** — raise for more punch, lower if the motor stutters when throttle increases quickly:

| Motor kV | Typical prop | Starting ramp |
| -------- | ------------ | ------------- |
| High (~1800+) | 5–7" | 16 %/ms |
| Mid (~800–1500) | 7–10" | **2 %/ms** (factory) |
| Low (~500 and below) | 10"+ | 1 %/ms or lower |

Factory ARK 4IN1 images ship at 2 %/ms. A separate slow-ramp firmware is not required — ramp rate is an EEPROM setting on the regular ARK32 image.
