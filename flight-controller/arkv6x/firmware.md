# Firmware

The ARKV6X ships with PX4 and can be flashed with ArduPilot. The ARKV6X Extended Range needs PX4 1.14 or later, or ArduPilot 4.5 or later.

| Firmware | Build target |
|----------|--------------|
| PX4 | `ark_fmu-v6x_default` ([boards/ark/fmu-v6x](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/fmu-v6x)) |
| ArduPilot | `ARKV6X` ([hwdef](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARKV6X)) |

## PX4

### Flashing Firmware

#### QGroundControl (USB-C)

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

#### px4\_uploader.py (USB or UART)

[`px4_uploader.py`](https://github.com/PX4/PX4-Autopilot/blob/main/Tools/px4_uploader.py) can flash firmware over USB or UART. For UART flashing, only the **Telem1** port is supported.

Over USB:

```sh
python3 Tools/px4_uploader.py build/ark_fmu-v6x_default/ark_fmu-v6x_default.px4
```

Over UART (via Telem1):

```sh
python3 Tools/px4_uploader.py --port /dev/<your-uart> build/ark_fmu-v6x_default/ark_fmu-v6x_default.px4
```

### Building Firmware

```
make ark_fmu-v6x_default
```

and optionally upload

```
make ark_fmu-v6x_default upload
```

## ArduPilot

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
./waf configure --board ARKV6X
./waf copter
```

and optionally upload

```
./waf copter --upload
```

For a carrier board with an IOMCU, change the hwdef first: see [hwdef modifications for use with an IOMCU](ardupilot-instructions.md#hwdef-modifications-for-use-with-an-iomcu).

## Recovering the Bootloader (SWD)

The application is at `0x08020000` (128 KB sectors).

```bash
st-flash write ark_fmu-v6x_bootloader.bin 0x08000000
```

Use `ark_fmu-v6x_bootloader.bin` from `boards/ark/fmu-v6x/extras/` in PX4-Autopilot, or from [PX4 GitHub releases](https://github.com/PX4/PX4-Autopilot/releases). Then flash `ark_fmu-v6x_default.px4` over USB. Setup: [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md#flashing-px4-flight-controllers).
