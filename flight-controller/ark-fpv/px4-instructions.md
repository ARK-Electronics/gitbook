# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/ark_fpv.html" %}
ARK FPV PX4 Documentation
{% endembed %}

PX4 main starts the LSM6DSV32X on an ARK FPV 32X. To build or flash PX4, see [Firmware](firmware.md#px4).

## PWM Outputs

Outputs 1–8 support DShot and bidirectional DShot. Output 9 is PWM and OneShot only.

Protocol and rate are set per timer: outputs 1–4, 5–8 and 9.
