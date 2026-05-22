# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/ark_v6s.html" %}
Up to date PX4 Documentation
{% endembed %}

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
make ark_fmu-v6s_default
```

and optionally upload

```
make ark_fmu-v6s_default upload
```
