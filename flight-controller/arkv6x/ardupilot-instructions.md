# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-ark-v6x-overview.html" %}
ARKV6X ArduPilot Documentation
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

The default build is for a carrier without an IOMCU, such as the ARK PAB Carrier, where USART6 is the RC input. For a carrier with an IOMCU on USART6, edit the [ARKV6X hwdef](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6X/hwdef.dat) and build it:

1. Swap the `SERIAL_ORDER` line comments ([L30-L33](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6X/hwdef.dat#L30-L33)) to remove USART6 from the serial ports.
2. Comment out `define DEFAULT_SERIAL8_PROTOCOL SerialProtocol_RCIN` ([L88](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6X/hwdef.dat#L88)), present from ArduPilot 4.7.0. With USART6 removed, SERIAL8 is the second USB port.
3. Uncomment `IOMCU_UART USART6` ([L91](https://github.com/ArduPilot/ardupilot/blob/Copter-4.7.1/libraries/AP_HAL_ChibiOS/hwdef/ARKV6X/hwdef.dat#L91)).

Keep the `PC6` and `PC7` USART6 pin lines; the IOMCU uses them.

Build and flash the firmware using the steps in [Firmware](firmware.md#ardupilot).
