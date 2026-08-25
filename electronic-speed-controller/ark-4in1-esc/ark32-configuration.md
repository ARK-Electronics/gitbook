# ARK32 Configuration

After flashing ARK32, you must configure each motor channel using the [ARK32 Configurator](https://ark32.arkelectron.com/). The default settings will not match your motor.

{% hint style="danger" %}
**KV and Pole Count must match your motor.** Incorrect values cause desync, failure to spin up, or motor stalling under load.
{% endhint %}

## Required Settings

| Setting    | Value                      | Description                                                                                |
| ---------- | -------------------------- | ------------------------------------------------------------------------------------------ |
| Motor KV   | From the motor's datasheet | RPM per volt rating of the motor. Used by ARK32 to derive timing and protection thresholds. |
| Pole Count | From the motor's datasheet | Number of **magnets on the rotor**, not stator slots                                       |

## Applying the Settings

1. Flash ARK32 — see [Flash ARK32](firmware/flash-ark32.md).
2. Open the [ARK32 Configurator](https://ark32.arkelectron.com/), connect, and click **Read**.
3. Set **Motor KV** and **Motor Poles** for each of the four motor channels.
4. Click **Write Settings**.

Every setting is documented in the configurator **Settings guide**. The same text lives in [ARK32 `doc/eeprom-settings.md`](https://github.com/ARK-Electronics/ARK32/blob/ark-release/doc/eeprom-settings.md).

## Edge Cases

Low-KV motors swinging large props (e.g. 6S with 10"+ props) may need a reduced ramp rate to avoid desync events during rapid throttle changes. See [Low KV Large Prop Systems](firmware/#low-kv-large-prop-systems).
