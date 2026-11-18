# Jetson Setup

ARK's Just A Jetson image includes the Boson+ driver, `nv_boson`, and a `jetson-io` overlay for each CSI port. [ark\_jetson\_kernel#163](https://github.com/ARK-Electronics/ark_jetson_kernel/pull/163) adds them. The driver sets the Boson up over the camera port's I2C and streams 640x512 at 60 fps. Driver details and bench results are in [boson.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/boson.md) in the kernel repo.

The Jetson PAB Carrier and Jetson PAB Carrier V3 have no Boson+ overlay yet.

## Cabling

The camera cable goes to CAM0 or CAM1 with the included 22-to-22-pin FFC. Video needs nothing else, because the driver controls the Boson over the camera port's I2C.

The I2C/UART connector carries the Boson's serial port on pins 2 and 3 and the IMU's I2C on pins 4 and 5. No Just A Jetson connector takes both, so split the cable:

| Use | Adapter pins | Just A Jetson connector |
| --- | ------------ | ----------------------- |
| Boson serial port | 2, 3 and 6 | UART1/GPIO, `/dev/ttyTHS1` at 921600 8N1. Cross pins 2 and 3 on a Rev 1.0 adapter |
| IMU | 4, 5 and 6 | Pins 4 and 5 of UART2/I2C0, which are I2C0 |

{% hint style="warning" %}
Do not plug the I2C/UART connector straight into UART2/I2C0. Pins 2 and 3 of that connector are the Jetson's debug console, `/dev/ttyTCU0`, at a fixed 115200.
{% endhint %}

With the whole cable in UART1/GPIO, the IMU lands on that connector's CTS and RTS pins, `PR.05` and `PR.04`. On the bench the IMU answered there over bit-banged I2C, which the image does not set up.

## Overlays

Apply the overlay for your port.

| Carrier | Port | Lanes | Overlay name | Status |
| ------- | ---- | ----- | ------------ | ------ |
| ARK Just A Jetson | CAM0 (J28) | 2 | Camera FLIR Boson+ CAM0 | Bench-tested |
| ARK Just A Jetson | CAM1 (J25) | 2 | Camera FLIR Boson+ CAM1 | Bench-tested |

List the overlays, apply the one for your port and reboot:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera FLIR Boson+ CAM1"
sudo reboot
```

## Modes

| Mode | Size | fps | V4L2 format | Boson output |
| ---- | ---- | --- | ----------- | ------------ |
| 0 | 640x512 | 60 | `UYVY` | Colourised by the Boson in its current palette (default) |
| 1 | 640x512 | 60 | `RG14` | Pre-AGC 14-bit, monochrome |

Both modes are the same size, so pick mode 1 with the `sensor_mode` control.

## Capture

The Boson appears as `vi-output, boson`. List the devices to find its number, then put that number in place of `N`:

```bash
v4l2-ctl --list-devices
v4l2-ctl -d /dev/videoN --set-fmt-video=width=640,height=512,pixelformat=UYVY \
  --set-ctrl sensor_mode=0 --stream-mmap --stream-count=300 --stream-to=boson.uyvy
```

This captures pre-AGC frames instead:

```bash
v4l2-ctl -d /dev/videoN --set-fmt-video=width=640,height=512,pixelformat=RG14 \
  --set-ctrl sensor_mode=1 --stream-mmap --stream-count=300 --stream-to=boson.raw14
```

In RAW14, each 16-bit word holds the 14-bit value in its top 14 bits, so shift it right by 2. `RG14` is a Bayer format only because the VI has no 14-bit monochrome one. Do not demosaic it.

Argus and `nvarguscamerasrc` do not work with the Boson, because its output does not go through the ISP. Use V4L2 or `v4l2src`.

## Boson settings

When a stream starts, the driver switches the Boson's output to MIPI, selects the mode's format and turns off telemetry and the MIPI embedded-data tag. It saves nothing to the Boson's flash, so a power cycle brings back the Boson's own settings. Palette, flat-field correction and frame sync stay under your control over the serial port. The factory palette is white hot, which looks grey.

## IMU and frame sync

The ICM-45686 is at `0x68` on whichever I2C bus the cable lands on. The I2C0 bus runs at 100 kHz, which carries accel and gyro at up to 400 Hz.

With the Boson as sync master, each overlay reads its pulses on the port's MCLK pad: `PP.00` for CAM0 and `PP.01` for CAM1. The other port's pad stays a driven output, so a Boson in a port whose overlay is not applied sends no pulses through. The IMU timestamps the pulses only with R13 fitted, as [Frame sync](hardware.md#frame-sync) describes.
