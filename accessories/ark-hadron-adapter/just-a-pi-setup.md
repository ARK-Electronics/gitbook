# Just A Pi Setup

This setup needs:

* A Compute Module 5. With a CM4, the Just A Pi has no UART2 and no CAM2.
* A `justapi-cm5` image with the driver for the Hadron's visible (EO) camera, `ov64b40`, and its overlay. [ark\_pi\_image#11](https://github.com/ARK-Electronics/ark_pi_image/pull/11) adds them. On older images the `config.txt` edits below do nothing.

The Boson thermal camera appears as the UVC camera "FLIR Video" at 30 fps and needs no driver.

The Pi 5's CSI-2 receiver limits the EO camera to one mode: 2304x1728 RAW10 RGGB on two lanes. It runs at 20 fps, or up to 29.4 fps with a shorter vertical blanking. libcamera does not support the sensor, so `rpicam-*` and ARK-OS's RTSP server do not see it. Capture raw frames with V4L2.

## Cabling

| Adapter connector | Carrier connector |
| ----------------- | ----------------- |
| EO Camera (22-pin FFC) | CAM1 (J2) or CAM2 (J1) |
| IR Camera / USB (4-pin JST-GH) | USB 2.0 JST-GH |
| I2C (6-pin JST-GH) | UART2, straight cable |

On CAM2 the Pi cannot reset the Hadron or read its sync pulses. The carrier ties CAM2's pin 17 high and leaves pin 18 unconnected. The IMU still timestamps the pulses.

The Just A Pi has no free I2C connector, so the I2C cable goes to UART2. SCL and SDA land on the connector's CTS and RTS pins, GPIO6 and GPIO7, where the kernel's `i2c-gpio` driver bit-bangs the bus. UART2 keeps TX and RX.

## config.txt

In `/boot/firmware/config.txt`, change the camera line for your port:

| Port | Change | To |
| ---- | ------ | -- |
| CAM1 | `dtoverlay=imx708,cam0` | `dtoverlay=ov64b40,cam0` |
| CAM2 | `dtoverlay=imx708` | `dtoverlay=ov64b40` |

For the I2C on UART2, change `dtoverlay=uart2,ctsrts` to `dtoverlay=uart2` and uncomment `dtoverlay=i2c-gpio,i2c_gpio_sda=7,i2c_gpio_scl=6,bus=7`. The bus appears as `/dev/i2c-7`.

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

The sensor's controls are on its subdevice. List them with `v4l2-ctl -d $SENSOR -l`.

| Control | Value |
| ------- | ----- |
| Exposure | In lines |
| Analogue gain | `0x100` is 1x |
| Vertical blanking | 998 for 20 fps, down to 128 for 29.4 fps |
| Test pattern | Colour bars |

Reboot to reload the driver. Unloading the sensor module crashes the Pi kernel's CSI-2 receiver driver.

## IMU and frame sync

The ICM-45686 is at `0x68` on `/dev/i2c-7`. On CAM1 the Hadron's sync line reaches the Pi on GPIO35, through pin 18. With the Boson as sync master, the Pi sees its 60 Hz pulses on GPIO35 and the IMU timestamps them.

{% hint style="warning" %}
With the Hadron on CAM1, keep its USB connected while the CM5 is on, and do not set the Boson as a sync slave. The CM5 pulls GPIO35 up to 3.3 V through 15 kΩ, and no setting removes it. The Boson holds the line at or below 1.8 V from power-on unless it is a sync slave. Undriven, the line sits at about 2.2 V, above the Hadron's 2.1 V input rating.
{% endhint %}
