# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-ark-v6s-overview.html" %}
ARKV6S ArduPilot Documentation
{% endembed %}

To build or flash ArduPilot, see [Firmware](firmware.md#ardupilot).

## Serial Port Mapping

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

## hwdef modifications for use with an IOMCU

The default build is for a carrier without an IOMCU, such as the ARK PAB Carrier, where USART6 is the RC input. For a carrier with an IOMCU on USART6, edit the [ARKV6S hwdef](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6S/hwdef.dat) and build it:

1. Comment out the first `SERIAL_ORDER` line ([L30](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6S/hwdef.dat#L30)).
2. Comment out `define DEFAULT_SERIAL8_PROTOCOL SerialProtocol_RCIN` ([L85](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6S/hwdef.dat#L85)). With USART6 removed, SERIAL8 is the second USB port.
3. Uncomment the `SERIAL_ORDER`, `IOMCU_UART` and `ROMFS io_firmware.bin` lines ([L94-L96](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6S/hwdef.dat#L94-L96)). The build fails without the IO firmware.

Keep the `PC6` and `PC7` USART6 pin lines, although the hwdef comment says to remove them; the IOMCU uses them.

Build and flash the firmware using the steps in [Firmware](firmware.md#ardupilot).
