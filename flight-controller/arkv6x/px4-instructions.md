# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/arkv6x.html" %}
Up to date PX4 Documentation
{% endembed %}

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

#### Flashing over UART

Firmware can also be flashed from a companion computer over UART using `px_uploader.py`. Connect to the **Telem1** port:

```sh
python3 Tools/px_uploader.py --port /dev/<your-uart> build/ark_fmu-v6x_default/ark_fmu-v6x_default.px4
```

The ARKV6X bootloader enables only `UART7` (the Telem1 port), so it appears as `/dev/ttyS0` inside the bootloader. The runtime serial port mapping (where `/dev/ttyS0` is GPS1) does not apply during bootloader operation — only Telem1 will respond to `px_uploader.py`.

### Building Firmware

```
make ark_fmu-v6x_default
```

and optionally upload

```
make ark_fmu-v6x_default upload
```

