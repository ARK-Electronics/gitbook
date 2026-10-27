# Firmware

The ARK FPV ships with PX4. It also runs ArduPilot and Betaflight. The ARK FPV 32X uses the same build targets.

PX4 main starts the LSM6DSV32X on an ARK FPV 32X (`ARKFPV001`), and so does release/1.18 after v1.18.0-rc1 ([backport](https://github.com/PX4/PX4-Autopilot/pull/29375)). ArduPilot master starts it too. The [ArduPilot 4.7 backport](https://github.com/ArduPilot/ardupilot/pull/34484) is open. The published Betaflight `ARK_FPV` target selects the IIM-42653; [32X support](https://github.com/betaflight/config/pull/1201) is in review.

| Firmware | Build target |
|----------|--------------|
| PX4 | `ark_fpv_default` ([boards/ark/fpv](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/fpv)) |
| ArduPilot | `ARK_FPV` ([hwdef](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARK_FPV)) |
| Betaflight | `ARK_FPV` |

## PX4

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
make ark_fpv_default
```

and optionally upload

```
make ark_fpv_default upload
```

## ArduPilot

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
./waf configure --board ARK_FPV
./waf copter
```

and optionally upload

```
./waf copter --upload
```

## Betaflight

{% hint style="info" %}
The published Betaflight `ARK_FPV` target selects the IIM-42653. On an ARK FPV 32X that leaves the IMU stopped.
{% endhint %}

### Building Firmware

See the official [Betaflight documentation](https://betaflight.com/docs/development/building/Building-in-Ubuntu) for setting up the development environment.

If you flash your flight controller using DFU via [https://app.betaflight.com/](https://app.betaflight.com/), build the `.hex`:

```
make hex CONFIG=ARK_FPV
```

If you flash your flight controller using ST-Link, build the `.bin`:

```
make binary CONFIG=ARK_FPV
```

### Flash using DFU mode via web app

Betaflight can be flashed using DFU over USB C.

1. With the board unpowered, hold the button next to the USB C port while connecting the USB cable to your PC.
2. Open [https://app.betaflight.com/](https://app.betaflight.com/) in Chrome or Edge.
3. Select `Firmware Flasher`\
   Toggle the sliders `Enable Expert Mode` and `Show release candidates` and select:\
   \- `Development`\
   \- `ARK_FPV`\
   \- `4.6.0-dev [latest]`\
   ![](<../../.gitbook/assets/image (39).png>)
4. Now select the `Load Firmware [Online]`\
   ![](<../../.gitbook/assets/image (40).png>)
5. You could also flash your own build\
   \- Select the `Load Firmware [Local]`\
   \- In this case you need a `.hex`\
   ![](<../../.gitbook/assets/image (1).png>)<br>
6. Now select `Flash Firmware`

{% hint style="info" %}
Betaflight does not have a separate bootloader. If you want to re-flash back to PX4 or Ardupilot after flashing Betaflight, you will need to re-flash the PX4 bootloader. See [Bootloader Flashing Using DFU](bootloader-flashing-using-dfu.md).
{% endhint %}

### Flash using ST-Link

For detailed instructions on ST-LINK setup, software installation, and usage, see the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md).

Connect to the 6-pin debug connector and flash:

```
st-flash write obj/ARK_FPV.bin 0x08000000
```

## Bootloader

The default ARK FPV PX4 bootloader works with PX4 and ArduPilot. DFU over USB C flashes or reflashes it.

{% content-ref url="bootloader-flashing-using-dfu.md" %}
[bootloader-flashing-using-dfu.md](bootloader-flashing-using-dfu.md)
{% endcontent-ref %}
