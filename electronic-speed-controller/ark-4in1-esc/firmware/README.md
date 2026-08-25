# Firmware

## Why ARK32 instead of upstream AM32

The ARK 4IN1 ESC runs **[ARK32](https://github.com/ARK-Electronics/ARK32)**, ARK Electronics' fork of [AM32](https://github.com/am32-firmware/AM32). Flash ARK32 on this board — not stock upstream AM32.

ARK32 keeps upstream AM32 protocols (DShot, PWM, KISS telemetry, passthrough flashing) and adds work that stock AM32 does not have:

* **Commutation.** The ESC times the motor two ways: **poll** (slower; used to start and to recover if timing is lost) and **interrupt** (faster; used once spinning). Upstream AM32 drops back to poll whenever the average step time looks long. On this hardware that was a trap: one missed zero-cross made the average look slower, poll stayed in control, and the motor bounced between the two modes instead of spooling. ARK32 still uses poll to start and to recover. A missed crossing in interrupt mode is a **blind step**, not a drop back to poll. Poll is used again only on desync, stall, or a closed loop that stays slow.
* **Throttle and protection.** The ramp you set is the ramp that runs. It is scaled by pack voltage so the same setting means the same volts per millisecond on 4S or 8S. The firmware does not secretly slow the ramp after a desync. A BEMF-headroom ceiling also caps duty from measured rpm, so a snap throttle on a heavy prop cannot command more slip than the motor can follow. Repeat desyncs or stalls wait longer, then latch as stuck; zero throttle clears that.
* **Gate driver sleep.** On the ARK 4IN1 the DRV8328 is put to sleep when the ESC is not driving, braking, or beeping.
* **Tested on this board.** Hardware-in-the-loop CI runs on the ARK 4IN1. A native SITL build covers protocol and startup logic without hardware.
* **ARK bootloader.** Field updates use [ARK32-bootloader](https://github.com/ARK-Electronics/ARK32-bootloader), which includes ARK-specific fixes (for example bidirectional DShot idle detection).

Full technical write-up: [What ARK32 adds](https://github.com/ARK-Electronics/ARK32#what-ark32-adds). Use the [ARK32 Configurator](https://ark32.arkelectron.com) for this board.

### AM32 Bootloader Firmware

The ARK 4IN1 uses AM32\_F051\_BOOTLOADER\_PB4. You can find the latest release [here](https://github.com/ARK-Electronics/ARK32-bootloader/releases).&#x20;

{% file src="../../../.gitbook/assets/AM32_F051_BOOTLOADER_PB4_V15.hex" %}

### AM32 App Firmware

Use the latest release of [ARK32](https://github.com/ARK-Electronics/ARK32/releases).

{% file src="../../../.gitbook/assets/AM32_ARK_4IN1_F051_2.20.hex" %}

### Low KV Large Prop Systems

Low KV motors swinging large props on higher cell counts (e.g. 6S with 10"+ props) can experience **desync events during rapid throttle changes**. The root cause is motor coil demagnetization time extending past the BEMF sensing window when current spikes during a fast throttle transient — the ESC temporarily loses rotor position and the motor stutters. Limiting how fast the duty cycle can change keeps the transient current in check and preserves the sensing window.

**Option 1 — lower the ramp rate via configurator.** As of AM32 v2.19, ramp speed is adjustable in the [AM32 Configurator](https://am32.ca/) (Config Tool v1.93+). This is sufficient for most high-inertia configurations — lower the ramp rate until desync events stop.

**Option 2 — `ARK_4IN1_RAMP_F051` firmware.** A dedicated build with a much lower ramp ceiling baked into flash. Use this when the configurable ramp rate on standard firmware is still too aggressive, or when you want the cap locked so a configurator session can't override it.

Differences vs standard firmware:

* Main loop rate halved (20 kHz → 10 kHz). Side effect: 2× coarser BEMF sampling.
* Ramp rate ceiling reduced \~12× at low RPM and \~32× at high RPM.
* Uniform ramp across the RPM range (no high/low-RPM split).

**Not suitable** for systems that need fast throttle tracking (e.g. interceptors, competition acro) — the reduced ramp rate limits mechanical response authority.

When flashing back and forth between the standard `ARK_4IN1` and the RAMP firmware, select "Ignore current MCU layout" in the configurator.

{% file src="../../../.gitbook/assets/AM32_ARK_4IN1_RAMP_F051_2.20.hex" %}

