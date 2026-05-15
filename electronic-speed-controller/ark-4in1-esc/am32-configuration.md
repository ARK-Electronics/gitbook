# AM32 Configuration

After flashing AM32, you must configure each motor channel using the [AM32 Configurator](https://am32.ca/configurator). The default settings will not match your motor.

{% hint style="danger" %}
**KV and Pole Count must match your motor.** Incorrect values cause desync, failure to spin up, or motor stalling under load.
{% endhint %}

## Required Settings

| Setting    | Value                                                  | Description                                                                                                                  |
| ---------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Motor KV   | From the motor's datasheet                             | RPM per volt rating of the motor. Used by AM32 to derive timing and protection thresholds.                                   |
| Pole Count | From the motor's datasheet                             | Number of **magnets on the rotor**, not stator slots |

## Applying the Settings

1. Flash AM32 — see [Flash AM32](firmware/flash-am32.md).
2. Open the [AM32 Configurator](https://am32.ca/configurator), connect, and click **Read**.
3. Set **Motor KV** and **Motor Poles** for each of the four motor channels.
4. Click **Write Settings**.

## Edge Cases

Low-KV motors swinging large props (e.g. 6S with 10"+ props) may need a reduced ramp rate to avoid desync events during rapid throttle changes. See [Low KV Large Prop Systems](firmware/#low-kv-large-prop-systems).
