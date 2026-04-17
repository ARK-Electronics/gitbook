# Firmware

### AM32 Bootloader Firmware

The ARK 4IN1 uses AM32\_F051\_BOOTLOADER\_PB4. You can find the latest release [here](https://github.com/am32-firmware/AM32-bootloader/releases).&#x20;

{% file src="../../../.gitbook/assets/AM32_F051_BOOTLOADER_PB4_V15.hex" %}

### AM32 App Firmware

Use the latest release of [AM32](https://github.com/am32-firmware/AM32/releases).

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

