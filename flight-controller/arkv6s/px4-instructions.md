# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/ark_v6s.html" %}
Up to date PX4 Documentation
{% endembed %}

To build or flash PX4, see [Firmware](firmware.md#px4).

## PWM Outputs

FMU outputs 1–6 support DShot and bidirectional DShot. Outputs 7–8 are PWM and OneShot only.

Protocol and rate are set per timer: outputs 1–4, 5–6 and 7–8. PX4 lists the FMU outputs as AUX. On a carrier with PX4IO, the MAIN outputs come from PX4IO and are PWM only.
