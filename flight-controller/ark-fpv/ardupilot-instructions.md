# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-ark-fpv-overview.html" %}
ARK FPV ArduPilot Documentation
{% endembed %}

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
./waf configure --board ARK_FPV
./waf copter
```

and optionally upload&#x20;

```
./waf copter --upload
```

