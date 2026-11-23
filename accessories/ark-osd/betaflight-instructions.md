# Betaflight Instructions

The ARK OSD connects to the ARK FPV's SPI port or its TELEM port, as in [Wiring](hardware.md#wiring). Enter the settings for one link in the Betaflight Configurator's CLI tab. The ARK FPV defaults to `vcd_video_system = HD`, a layout for digital goggles. Each link below sets `AUTO` instead.

## SPI

[betaflight/config#1262](https://github.com/betaflight/config/pull/1262) adds the MAX7456 driver on the ARK FPV's SPI port. Until it is in a Betaflight release, use [MSP DisplayPort](#msp-displayport). Keep **OSD (Analog)** in the build options when you flash.

```text
set vcd_video_system = AUTO
set osd_displayport_device = MAX7456
save
```

With `AUTO`, Betaflight reads NTSC or PAL from the ARK OSD. The Font Manager in the [OSD tab](https://betaflight.com/docs/wiki/app/osd-tab) uploads fonts to the ARK OSD.

## MSP DisplayPort

`vcd_video_system = AUTO` gives the 13 NTSC rows. With a PAL camera, set `PAL` instead to get 16.

### Betaflight Master

```text
set vcd_video_system = AUTO
set msp_3_uart = UART7
set msp_3_baud = 115200
set osd_uart = UART7
set osd_displayport_device = MSP
save
```

### Betaflight 2026.6

In the [Ports tab](https://betaflight.com/docs/wiki/app/ports-tab), turn on **Configuration/MSP** for UART7 and set its **Peripherals** to **VTX (MSP + Displayport)**. On UART5, the VTX port, turn off MSP and set **Peripherals** to **Disabled**. Then enter:

```text
set vcd_video_system = AUTO
set osd_displayport_device = MSP
save
```

This setup hasn't been tested on hardware.
