# ARK32 Configuration

After flashing ARK32, you must configure each motor channel using the [ARK32 Configurator](https://ark32.arkelectron.com/). The default settings will not match your motor.

{% hint style="danger" %}
**KV and Pole Count must match your motor.** Incorrect values cause desync, failure to spin up, or motor stalling under load.
{% endhint %}

{% hint style="warning" %}
**Set the ramp rate for your prop.** Ramp rate is how fast throttle may change, in percent of full throttle per millisecond. The factory value is **2 %/ms** — throttle can move 2% of full throttle every millisecond, so going from zero to full throttle takes 50 ms. That is the right starting point for 5–10" vehicles. Too fast a ramp desyncs on a heavy prop. Raise it only if you need punch on a small high-kV motor. The setting is a **ceiling on all three rpm bands** — the firmware's own limits are 2 %/ms at startup, 6 %/ms at low rpm and 16 %/ms once spun up, and your value lowers each of them. At the factory 2 %/ms all three are flattened to 2.
{% endhint %}

## Required Settings

| Setting    | Value                                      | Description                                                                                |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Motor KV   | From the motor's datasheet                 | RPM per volt rating of the motor. Used by ARK32 to derive timing and protection thresholds. |
| Pole Count | From the motor's datasheet. **2–128**.     | Number of **magnets on the rotor**, not stator slots.                                       |
| Ramp Rate  | **2 %/ms** factory. **0.1–20 %/ms**.       | How fast duty may change, in percent of full throttle per millisecond. Caps all three rpm bands (firmware limits: startup 2, low rpm 6, high rpm 16 %/ms). Values under 1 %/ms use a finer 0.1 %/ms step. |

Starting ramp rates by motor kV: [Low KV Large Prop Systems](firmware/#low-kv-large-prop-systems).

## Applying the Settings

1. Flash ARK32 — see [Flash ARK32](firmware/flash-ark32.md).
2. Open the [ARK32 Configurator](https://ark32.arkelectron.com/), connect, and click **Read**.
3. Set **Motor KV**, **Motor Poles**, and **Ramp Rate** for each of the four motor channels.
4. Click **Write Settings**.

Every setting is documented in the configurator **Settings guide**. The same text lives in [ARK32 `doc/eeprom-settings.md`](https://github.com/ARK-Electronics/ARK32/blob/ark-release/doc/eeprom-settings.md).

## Edge Cases

Low-KV motors swinging large props (e.g. 6S with 10"+ props) may need a **lower** ramp rate to avoid desync on rapid throttle changes. If the motor stutters when you raise throttle quickly, reduce ramp until it stays locked. See [Low KV Large Prop Systems](firmware/#low-kv-large-prop-systems).
