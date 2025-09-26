# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/arkv6x.html" %}
Up to date PX4 Documentation
{% endembed %}

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
make ark_fmu-v6x_default
```

and optionally upload

```
make ark_fmu-v6x_default upload
```

