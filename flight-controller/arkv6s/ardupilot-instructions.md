# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-ark-v6s-overview.html" %}
ARKV6S ArduPilot Documentation
{% endembed %}

### Flashing Firmware

Firmware can be flashed over USB C using [QGroundControl](https://qgroundcontrol.com/).

### Building Firmware

```
./waf configure --board ARKV6S
./waf copter
```

and optionally upload&#x20;

```
./waf copter --upload
```

### Serial Port Mapping

{% hint style="info" %}
Serial Port Mapping for Default Firmware with No IOMCU
{% endhint %}

| **UART** | **Serial Number** | **Port**      |
| -------- | ----------------- | ------------- |
| UART7    | SERIAL1           | TELEM1        |
| UART5    | SERIAL2           | TELEM2        |
| USART1   | SERIAL3           | GPS           |
| UART8    | SERIAL4           | GPS2          |
| USART2   | SERIAL5           | TELEM3        |
| UART4    | SERIAL6           | UART4 & I2C   |
| USART3   | SERIAL7           | Debug Console |
| USART6   | SERIAL8           | PX4IO/RC      |

### hwdef modifications for use with an IOMCU

When using the ARKV6S on a carrier board with an IOMCU, the following modifications to the hwdef need to be made.&#x20;

Swap the SERIAL\_ORDER line comments to remove USART6 from the available serial ports.

Uncomment the IOMCU\_UART line to use USART6 for the IOMCU.

Build and flash the firmware using the steps above.
