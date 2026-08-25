# ARK32 Configuration

After flashing ARK32, you must configure each motor channel using the [ARK32 Configurator](https://ark32.arkelectron.com/). The default settings will not match your motor.

{% hint style="danger" %}
**KV and Pole Count must match your motor.** Incorrect values cause desync, failure to spin up, or motor stalling under load.
{% endhint %}

{% hint style="warning" %}
**Set the ramp rate for your prop.** This is how fast throttle may change. The factory value is **2 %/ms** (0→100% takes 50 ms), which is the right starting point for 5–10"+ vehicles. Too fast a ramp desyncs on a heavy prop. Raise it only if you need punch on a small high-kV motor (the firmware still caps each rpm band; 16 %/ms is the high-rpm ceiling).
{% endhint %}

## Required Settings

| Setting    | Value                                      | Description                                                                                |
| ---------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ |
| Motor KV   | From the motor's datasheet                 | RPM per volt rating of the motor. Used by ARK32 to derive timing and protection thresholds. |
| Pole Count | From the motor's datasheet                 | Number of **magnets on the rotor**, not stator slots                                       |
| Ramp Rate  | **2 %/ms** factory; lower for large props  | How fast duty may change, in percent of full throttle per millisecond                      |

## Applying the Settings

1. Flash ARK32 — see [Flash ARK32](firmware/flash-ark32.md).
2. Open the [ARK32 Configurator](https://ark32.arkelectron.com/), connect, and click **Read**.
3. Set **Motor KV**, **Motor Poles**, and **Ramp Rate** for each of the four motor channels.
4. Click **Write Settings**.

Every setting is documented in the configurator **Settings guide**. The same text lives in [ARK32 `doc/eeprom-settings.md`](https://github.com/ARK-Electronics/ARK32/blob/ark-release/doc/eeprom-settings.md).

## Edge Cases

Low-KV motors swinging large props (e.g. 6S with 10"+ props) may need a **lower** ramp rate to avoid desync on rapid throttle changes. If a snap throttle stutters, reduce ramp until it stays locked. See [Low KV Large Prop Systems](firmware/#low-kv-large-prop-systems).
