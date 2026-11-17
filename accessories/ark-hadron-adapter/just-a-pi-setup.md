# Just A Pi Setup

The `justapi-cm5` image carries the driver for the Hadron's visible (EO) camera, `ov64b40`, built with DKMS, and its overlay. The thermal camera (Boson) is a UVC camera ("FLIR Video") at 30 fps. The driver and the bench results are in [ark\_pi\_image](https://github.com/ARK-Electronics/ark_pi_image).

The Pi 5's CSI-2 receiver takes at most 1.5 Gbps per lane, so the EO runs one mode here: 2304x1728 RAW10 (RGGB) at 20 fps on two lanes, and up to 29.4 fps through `VBLANK`. libcamera does not support the sensor, so `rpicam-*` and ARK-OS's RTSP server do not see it. Capture raw frames with V4L2.

## Cabling

| Adapter connector | Carrier connector |
| ----------------- | ----------------- |
| EO Camera (22-pin FFC) | CAM1 (J2), or CAM2 (J1) |
| IR Camera / USB (4-pin JST-GH) | USB 2.0 JST-GH |
| I2C (6-pin JST-GH) | UART2 connector, straight cable |

The Just A Pi has no free I2C connector, so the adapter's I2C goes to the UART2 connector, where SCL and SDA land on GPIO6 and GPIO7 (the connector's CTS and RTS). The RP1 bit-bangs that bus. UART2 keeps TX and RX.

## config.txt

In `/boot/firmware/config.txt`, with the Hadron on CAM1:

1. Change `dtoverlay=imx708,cam0` to `dtoverlay=ov64b40,cam0`.
2. Change `dtoverlay=uart2,ctsrts` to `dtoverlay=uart2`.
3. Uncomment `dtoverlay=i2c-gpio,i2c_gpio_sda=7,i2c_gpio_scl=6,bus=7`, which gives `/dev/i2c-7`.

With the Hadron on CAM2 instead, keep `dtoverlay=imx708,cam0` and change the plain `dtoverlay=imx708` line to `dtoverlay=ov64b40`. CAM2's pin 17 is tied high on the carrier, so the Hadron's reset is always released, and CAM2 has no pin 18, so the Pi cannot read the sync pulses there; the IMU still tags them.

Reboot after editing.

## Capture

Device numbers depend on probe order, so look the sensor up by name:

```bash
for m in /dev/media*; do media-ctl -d $m -p | grep -q ': ov64b40 ' && MEDIA=$m; done
SENSOR=$(media-ctl -d $MEDIA -e "$(media-ctl -d $MEDIA -p | sed -n 's/^- entity [0-9]*: \(ov64b40 [^ ]*\) .*/\1/p')")
VIDEO=$(media-ctl -d $MEDIA -e rp1-cfe-csi2_ch0)
F='fmt:SRGGB10_1X10/2304x1728 field:none colorspace:raw xfer:none ycbcr:601 quantization:full-range'
media-ctl -d $MEDIA -l '"csi2":4 -> "rp1-cfe-csi2_ch0":0 [1]'
media-ctl -d $MEDIA -V "\"csi2\":0 [$F], \"csi2\":4 [$F]"
v4l2-ctl -d $VIDEO --set-fmt-video=width=2304,height=1728,pixelformat=pRAA
v4l2-ctl -d $VIDEO --stream-mmap --stream-count=20 --stream-to=frames.raw
```

Exposure (lines), analogue gain (`0x100` = 1x), vertical blanking (998 for 20 fps, down to 128 for 29.4 fps) and a colour-bar test pattern are controls on the sensor's subdevice: `v4l2-ctl -d $SENSOR -l`.

To reload the driver, reboot. Unloading and reloading a sensor module oopses the Pi kernel's CSI-2 receiver driver.

## IMU and frame sync

The adapter's ICM-45686 is at `0x68` on `/dev/i2c-7`. The Hadron's sync line runs through R11 to CAM1 pin 18 (GPIO35), which the Pi reads as an input, and through R12 to the IMU's FSYNC pin. With the Boson as sync master, the Pi sees its 60 Hz pulses on GPIO35 and the IMU tags them.

The CM5 pulls GPIO35 up to 3.3 V through 15 kΩ on the module. While the Boson drives the line, which it does from power-on, the pull-up only loads its output. The line floats above the Hadron's 1.8 V inputs only when nothing drives it: for a moment during boot, with the Boson as a sync slave, or with the Hadron unpowered while the CM5 is on. The inputs then clamp it at about 2.2 V.
