# Just A Pi Setup

This setup needs:

* A Compute Module 5. With a CM4, the Just A Pi has no UART2 and no CAM2.
* A `justapi-cm5` image with the Boson+ driver, `boson`, and its overlay. [ark\_pi\_image#15](https://github.com/ARK-Electronics/ark_pi_image/pull/15) adds them. On older images the `config.txt` edits below do nothing.

The driver streams 640x512 at 60 fps on two lanes, colourised by the Boson or as pre-AGC 14-bit data. libcamera does not support the camera, so `rpicam-*` and ARK-OS's RTSP server do not see it. Capture with V4L2.

## Cabling

| Adapter connector | Carrier connector |
| ----------------- | ----------------- |
| Camera (22-pin FFC) | CAM1 (J2) or CAM2 (J1) |
| I2C/UART (6-pin JST-GH) | UART2. Cross pins 2 and 3 on a Rev 1.0 adapter |

Video needs only the camera cable, because the driver controls the Boson over the camera port's I2C. The I2C/UART cable gives you the Boson's serial port on `/dev/ttyAMA2` at 921600 8N1 and the IMU on `/dev/i2c-7`. The IMU's SCL and SDA land on UART2's CTS and RTS pins, GPIO6 and GPIO7, where the kernel's `i2c-gpio` driver bit-bangs the bus.

## config.txt

In `/boot/firmware/config.txt`, change the camera line for your port:

| Port | Change | To |
| ---- | ------ | -- |
| CAM1 | `dtoverlay=imx708,cam0` | `dtoverlay=boson,cam0` |
| CAM2 | `dtoverlay=imx708` | `dtoverlay=boson` |

For the serial port and the IMU on UART2, change `dtoverlay=uart2,ctsrts` to `dtoverlay=uart2` and uncomment `dtoverlay=i2c-gpio,i2c_gpio_sda=7,i2c_gpio_scl=6,bus=7`. The bus appears as `/dev/i2c-7`.

Reboot after editing.

## Capture

Device numbers depend on probe order, so look the camera up by name. This captures 60 colourised frames:

```bash
for m in /dev/media*; do media-ctl -d $m -p | grep -q ': boson ' && MEDIA=$m; done
SENSOR=$(media-ctl -d $MEDIA -p | sed -n 's/^- entity [0-9]*: \(boson [^ ]*\) .*/\1/p')
VIDEO=$(media-ctl -d $MEDIA -e rp1-cfe-csi2_ch0)
F='fmt:UYVY8_1X16/640x512 field:none colorspace:srgb'
media-ctl -d $MEDIA -l '"csi2":4 -> "rp1-cfe-csi2_ch0":0 [1]'
media-ctl -d $MEDIA -V "\"$SENSOR\":0 [$F], \"csi2\":0 [$F], \"csi2\":4 [$F]"
v4l2-ctl -d $VIDEO --set-fmt-video=width=640,height=512,pixelformat=UYVY
v4l2-ctl -d $VIDEO --stream-mmap --stream-count=60 --stream-to=frames.uyvy
```

For pre-AGC 14-bit frames, set `F='fmt:Y14_1X14/640x512 field:none colorspace:raw xfer:none ycbcr:601 quantization:full-range'` and `pixelformat=Y14P`. The Pi 5's CSI-2 receiver does not unpack RAW14, so unpack it in software. Every 7 bytes hold 4 pixels: first each pixel's top 8 bits, then a 24-bit little-endian word with each pixel's low 6 bits, the first pixel's in bits 0 to 5. The Boson+ refuses 16-bit output over MIPI.

Reboot to reload the driver. Unloading the camera module crashes the Pi kernel's CSI-2 receiver driver. If the Boson rejects the stream setup, the driver logs `stream start failed` and the capture waits with no frames.

## Streaming

This sends the colourised video as RTP H.264 to port 5600, which QGroundControl's UDP h.264 video source plays. Run it after the capture setup above, with your ground station's address in place of `192.168.0.96`:

```bash
gst-launch-1.0 v4l2src device=$VIDEO ! video/x-raw,format=UYVY,width=640,height=512,framerate=60/1 \
  ! videoconvert ! video/x-raw,format=I420 \
  ! x264enc tune=zerolatency speed-preset=ultrafast bitrate=4000 key-int-max=60 \
  ! rtph264pay config-interval=1 pt=96 ! udpsink host=192.168.0.96 port=5600 sync=false
```

The Pi 5 has no H.264 encoder, so x264 encodes on the CPU and takes about a third of one core. Keep the `I420` and `framerate` caps. Without them x264 gets 4:4:4 video, which most decoders cannot play, and assumes 120 fps.

## Boson settings

The driver changes only the video output and saves nothing to the Boson's flash. Palette, flat-field correction and frame sync go over the Boson's serial port, `/dev/ttyAMA2` at 921600 8N1, with FLIR's protocol. The factory palette is white hot, which looks grey.

## IMU and frame sync

The ICM-45686 is at `0x68` on `/dev/i2c-7`. On CAM1 the Boson's sync line reaches the Pi on GPIO35, through pin 18, and the Pi only reads it. With the Boson as sync master, the Pi sees its 60 Hz pulses there. CAM2 has no pin 18. The IMU timestamps the pulses only with R13 fitted, as [Frame sync](hardware.md#frame-sync) describes.

{% hint style="info" %}
The CM5 pulls GPIO35 up to 3.3 V through 15 kΩ, and no setting removes it. The Boson holds the line low from power-on and drives it as sync master, so the pull-up only loads its output. The line rises above the Boson's 1.8 V only when nothing drives it, as with the Boson set as a sync slave on CAM1. Check FLIR's rating for `EXT_SYNC` before doing that.
{% endhint %}
