# Betaflight Instructions

The ARK OSD connects to the ARK FPV's SPI port or its TELEM port, as in [Wiring](hardware.md#wiring). Enter the settings for one link in the Betaflight Configurator's CLI tab. Builds with the HD OSD option default to `vcd_video_system = HD`, a layout for digital goggles, so each link below sets `AUTO`.

Keep **OSD (Analog)** in the build options when you flash. Without it, Betaflight sets `vcd_video_system` back to `HD` whenever MSP DisplayPort starts, and items placed outside the ARK OSD's 30 × 13 grid don't show.

{% hint style="warning" %}
Until [betaflight/config#1262](https://github.com/betaflight/config/pull/1262) merges, the ARK OSD needs a Betaflight master build on [MSP DisplayPort](#msp-displayport).
{% endhint %}

## SPI

[betaflight/config#1262](https://github.com/betaflight/config/pull/1262) adds the MAX7456 driver on the ARK FPV's SPI port.

```text
set vcd_video_system = AUTO
set osd_displayport_device = MAX7456
save
```

With `AUTO`, Betaflight reads NTSC or PAL from the ARK OSD. The Font Manager in the [OSD tab](https://betaflight.com/docs/wiki/app/osd-tab) uploads fonts to the ARK OSD.

## MSP DisplayPort

These settings need a Betaflight master build. `vcd_video_system = AUTO` gives the 13 NTSC rows. With a PAL camera, set `PAL` instead to get 16.

```text
set vcd_video_system = AUTO
set msp_3_uart = UART7
set msp_3_baud = 115200
set osd_uart = UART7
set osd_displayport_device = MSP
save
```
