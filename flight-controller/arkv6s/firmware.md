# Firmware

The ARKV6S ships with PX4 and can be flashed with ArduPilot.

| Firmware | Build target |
|----------|--------------|
| PX4 | `ark_fmu-v6s_default` ([boards/ark/fmu-v6s](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/fmu-v6s)) |
| ArduPilot | `ARKV6S` ([ArduPilot pull request](https://github.com/ArduPilot/ardupilot/pull/33157)) |

## PX4

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

## ArduPilot

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
./waf configure --board ARKV6S
./waf copter
```

and optionally upload

```
./waf copter --upload
```

For a carrier board with an IOMCU, change the hwdef first: see [hwdef modifications for use with an IOMCU](ardupilot-instructions.md#hwdef-modifications-for-use-with-an-iomcu).
