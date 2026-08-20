# u-blox Firmware Update

The u-blox receiver's firmware is separate from the ARK module's CAN node firmware, and is updated with u-blox's [u-center](https://www.u-blox.com/en/product/u-center) desktop tools — u-center for the ZED-F9P, u-center 2 for the ZED-X20P. The procedure applies to the [ARK RTK GPS](../gps/ark-rtk-gps/README.md), [ARK RTK Base](../gps/ark-rtk-base/README.md), and [ARK X20 RTK GPS](../gps/ark-x20-rtk-gps/README.md).

## Connecting

* **ARK RTK Base** — connect over USB-C. The F9P enumerates directly as a USB serial port.
* **CAN modules (ARK RTK GPS, ARK X20 RTK GPS)** — attach a 3.3V USB-serial adapter to the module's `UART2` connector (adapter RX to module TX, adapter TX to module RX, GND to GND) and set `GPS_UBX_MODE` to `7`, which opens `UART2` as a bidirectional UBX port — see [u-blox Diagnostics with u-center](https://docs.px4.io/main/en/gps_compass/u-center.html) in the PX4 docs. Connect u-center at the `GPS_UBX_BAUD2` baudrate (default `230400`).
* **Without a `UART2` connector, or with node firmware that predates `GPS_UBX_MODE` 7** — hold the safety switch while powering the module through a CAN port, until all three LEDs blink rapidly. This bridges the F9P's `UART1` to the debug connector's UART (pins 2/3 of the 6-pin JST-SH, plus GND) — attach a 3.3V USB-serial adapter there and connect u-center to that COM port. For a firmware update, check _Use this baudrate for update_ and select `115200`. See the [PX4 ARK RTK GPS page](https://docs.px4.io/main/en/dronecan/ark_rtk_gps.html) for the full procedure.

## Updating

1. Check the installed version: in u-center open **View > Messages View > UBX > MON > VER**; u-center 2 shows the firmware version on the device page.
2. Download the firmware image from the u-blox product page — [ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module) or [ZED-X20P](https://www.u-blox.com/en/product/zed-x20p-module), under _Documentation & resources_.
3. Run the firmware update tool (**Tools > Firmware Update** in u-center, **Firmware Update** on the device page in u-center 2), select the downloaded image, and leave the remaining settings at their defaults.
4. When the update completes, power cycle the module and re-check the version.

{% hint style="warning" %}
Do not power cycle the module while the update is running.
{% endhint %}
