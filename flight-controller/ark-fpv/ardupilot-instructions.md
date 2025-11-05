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

### UART Mapping

| Name    | Function                                   |
| ------- | ------------------------------------------ |
| SERIAL0 | USB                                        |
| SERIAL1 | UART7 (Telem)                              |
| SERIAL2 | UART5 (DisplayPort HD VTX)                 |
| SERIAL3 | USART1 (GPS1)                              |
| SERIAL4 | USART2 (User, SBUS pin on HD VTX, RX only) |
| SERIAL5 | UART4 (ESC Telem, RX only)                 |
| SERIAL6 | USART6 (RC Input)                          |
| SERIAL7 | OTG2 (SLCAN)                               |

All UARTS support DMA. Any UART may be re-tasked by changing its protocol parameter.



The hardware definition for Ardupilot can be found here:\
[https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP\_HAL\_ChibiOS/hwdef/ARK\_FPV](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARK_FPV)
