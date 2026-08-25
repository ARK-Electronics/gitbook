# Firmware

## Why ARK32

The ARK 4IN1 ESC runs **[ARK32](https://github.com/ARK-Electronics/ARK32)**. Flash ARK32 on this board.

ARK32 keeps DShot, PWM, KISS telemetry, and passthrough flashing, and adds work for this hardware:

* **Commutation.** The ESC times the motor two ways: **poll** (slower; used to start and to recover if timing is lost) and **interrupt** (faster; used once spinning). A missed crossing in interrupt mode is a **blind step**, not a drop back to poll. Poll is used again only on desync, stall, or a closed loop that stays slow.
* **Throttle and protection.** The ramp you set is the ramp that runs. It is scaled by pack voltage so the same setting means the same volts per millisecond on 4S or 8S. The firmware does not secretly slow the ramp after a desync. A BEMF-headroom ceiling also caps duty from measured rpm, so a snap throttle on a heavy prop cannot command more slip than the motor can follow. Repeat desyncs or stalls wait longer, then latch as stuck; zero throttle clears that.
* **Gate driver sleep.** On the ARK 4IN1 the DRV8328 is put to sleep when the ESC is not driving, braking, or beeping.
* **Tested on this board.** Hardware-in-the-loop CI runs on the ARK 4IN1. A native SITL build covers protocol and startup logic without hardware.
* **ARK bootloader.** Field updates use [ARK32-bootloader](https://github.com/ARK-Electronics/ARK32-bootloader), which includes ARK-specific fixes (for example bidirectional DShot idle detection and DRV8328 `nSLEEP`).

Full technical write-up: [What ARK32 adds](https://github.com/ARK-Electronics/ARK32#what-ark32-adds). Use the [ARK32 Configurator](https://ark32.arkelectron.com/) for this board.

### ARK32 Bootloader Firmware

Use the ARK 4IN1 image from [ARK32-bootloader releases](https://github.com/ARK-Electronics/ARK32-bootloader/releases) (PB4 signal, PA15 `nSLEEP` low). Do not use the generic PB4 bootloader on this board.

See [Flash Bootloader](flash-bootloader.md).

### ARK32 App Firmware

Use the latest release of [ARK32](https://github.com/ARK-Electronics/ARK32/releases).

See [Flash ARK32](flash-ark32.md).

### Low KV Large Prop Systems

Low KV motors swinging large props on higher cell counts (e.g. 6S with 10"+ props) can experience **desync events during rapid throttle changes**. The root cause is motor coil demagnetization time extending past the BEMF sensing window when current spikes during a fast throttle transient — the ESC temporarily loses rotor position and the motor stutters. Limiting how fast the duty cycle can change keeps the transient current in check and preserves the sensing window.

Lower the ramp rate in the [ARK32 Configurator](https://ark32.arkelectron.com/) until desync events stop. Factory ARK 4IN1 images ship at 2 %/ms. A separate slow-ramp firmware is not required — that rate is an EEPROM setting on the regular ARK32 image.
