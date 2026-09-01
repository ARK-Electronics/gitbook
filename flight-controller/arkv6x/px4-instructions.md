# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/arkv6x.html" %}
Up to date PX4 Documentation
{% endembed %}

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

### Recovering the Bootloader (SWD)

The application is at `0x08020000` (128 KB sectors). `0x08010000` is the DroneCAN-node offset.

```bash
st-flash write ark_fmu-v6x_bootloader.bin 0x08000000
```

Use `ark_fmu-v6x_bootloader.bin` from `boards/ark/fmu-v6x/extras/` in PX4-Autopilot, or from [PX4 GitHub releases](https://github.com/PX4/PX4-Autopilot/releases). Then flash `ark_fmu-v6x_default.px4` over USB. Setup: [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md#flashing-px4-flight-controllers).

