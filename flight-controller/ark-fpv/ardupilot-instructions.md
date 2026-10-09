# ArduPilot Instructions

{% embed url="https://ardupilot.org/copter/docs/common-ark-fpv.html" %}
ARK FPV ArduPilot Documentation
{% endembed %}

To build or flash ArduPilot, see [Firmware](firmware.md#ardupilot).

## UART Mapping

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
