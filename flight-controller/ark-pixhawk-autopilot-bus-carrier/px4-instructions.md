# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/arkpab.html" %}
Up to date PX4 Docs
{% endembed %}

### Debug Port <a href="#debug-port" id="debug-port"></a>

The [PX4 System Console](https://docs.px4.io/main/en/debug/system_console.html) and [SWD interface](https://docs.px4.io/main/en/debug/swd_debug.html) run on the **FMU Debug** port.

The pinouts and connector comply with the [Pixhawk Debug Full](https://docs.px4.io/main/en/debug/swd_debug.html#pixhawk-debug-full) interface defined in the [Pixhawk Connector Standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf) interface (JST SM10B connector).

| Pin      | Signal           | Volt  |
| -------- | ---------------- | ----- |
| 1 (red)  | `Vtref`          | +3.3V |
| 2 (blk)  | Console TX (OUT) | +3.3V |
| 3 (blk)  | Console RX (IN)  | +3.3V |
| 4 (blk)  | `SWDIO`          | +3.3V |
| 5 (blk)  | `SWCLK`          | +3.3V |
| 6 (blk)  | `SWO`            | +3.3V |
| 7 (blk)  | NFC GPIO         | +3.3V |
| 8 (blk)  | PH11             | +3.3V |
| 9 (blk)  | nRST             | +3.3V |
| 10 (blk) | `GND`            | GND   |

For information about using this port see:

* [SWD Debug Port](https://docs.px4.io/main/en/debug/swd_debug.html)
* [PX4 System Console](https://docs.px4.io/main/en/debug/system_console.html) (Note, the FMU console maps to USART3).

![ARKPAB Top Down Photo](https://docs.px4.io/main/assets/ark_pab_top.C8on0kwA.jpg)

![ARKPAB Bottom Photo](https://docs.px4.io/main/assets/ark_pab_back.BMAKz_xS.jpg)
