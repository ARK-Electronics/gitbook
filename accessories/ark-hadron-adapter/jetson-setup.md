# Jetson Setup

ARK's Jetson images include the driver for the Hadron's visible (EO) camera, `nv_ov64b40`, and a `jetson-io` overlay for each CSI port. The Boson thermal camera is a USB UVC device and needs no overlay. Driver details and bench results are in [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md) in the kernel repo.

## Cabling

The IR camera's 4-pin cable goes to any USB 2.0 JST-GH port. The EO camera cable and the I2C connection depend on the carrier:

| Carrier | EO camera cable | I2C |
| ------- | --------------- | --- |
| ARK Just A Jetson | Included 22-to-22-pin FFC | UART2/I2C0, with the included 6-pin cable |
| ARK Jetson PAB Carrier V3 | Included 22-to-22-pin FFC | None, see below |
| ARK Jetson PAB Carrier | Included 22-to-15-pin FFC | Jetson I2C0, a 4-pin JST-GH with SCL on pin 2 and SDA on pin 3. Needs a 6-to-4-pin cable, not included |

The Jetson PAB Carrier V3 has no Jetson I2C connector. To reach the IMU, bit-bang I2C with the kernel's `i2c-gpio` driver on GPIO01 at pin 23 and GPIO12 at pin 12 of the [Pixhawk Payload Bus connector](../../flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/pinout.md). The image does not set this up. Those pins are 1.8 V and the adapter's I2C is 3.3 V, so a level translator goes between them.

## Overlays

Apply the overlay for your carrier and port.

| Carrier | Port | Lanes | Overlay name | Status |
| ------- | ---- | ----- | ------------ | ------ |
| ARK Just A Jetson | CAM0 (J28) | 2 | Camera FLIR Hadron EO CAM0 2-lane | Bench-tested |
| ARK Just A Jetson | CAM1 (J25) | 4 | Camera FLIR Hadron EO CAM1 4-lane | Bench-tested |
| ARK Jetson PAB Carrier V3 | CAM0 (J28) | 4 | Camera FLIR Hadron EO CAM0 4-lane | Untested on hardware |
| ARK Jetson PAB Carrier V3 | CAM1 (J25) | 4 | Camera FLIR Hadron EO CAM1 4-lane | Untested on hardware |
| ARK Jetson PAB Carrier | CAM0–CAM3 | 2 | Camera FLIR Hadron EO CAM*n* 2-lane | Untested on hardware |

Both Just A Jetson ports carry four lanes, but L4T runs CAM0 on only two of them. Each mode on CAM0 runs at half its 4-lane frame rate.

List the overlays, apply the one for your port and reboot:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera FLIR Hadron EO CAM1 4-lane"
sudo reboot
```

## Modes

| Mode | Size | fps, 4-lane | fps, 2-lane | Notes |
| ---- | ---- | ----------- | ----------- | ----- |
| 0 | 4624x3468 | 30 | 15 | 4-cell binned (default) |
| 1 | 3840x2160 | 60 | 30 | |
| 2 | 2304x1296 | 120 | 60 | |
| 3 | 9248x6936 | 13.2 | 6.6 | Full array |

Through Argus, mode 2 on a 4-lane port delivers about 100 fps, or the full 120 fps after `sudo jetson_clocks`. Mode 3 at full size ran out of memory in Argus on an Orin Nano 4GB and ran on an Orin NX 16GB. [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md#argus) has the measurements.

## Verifying the camera

The EO appears as `vi-output, ov64b40` and the Boson as a UVC camera:

```bash
v4l2-ctl --list-devices
nvargus_nvraw --lps
```

Record mode 2 at 60 fps through Argus, scaled to 720p:

```bash
gst-launch-1.0 -e nvarguscamerasrc sensor-id=0 sensor-mode=2 ! \
  'video/x-raw(memory:NVMM),width=2304,height=1296,framerate=60/1' ! \
  nvvidconv ! 'video/x-raw,format=I420,width=1280,height=720' ! \
  x264enc tune=zerolatency speed-preset=ultrafast bitrate=6000 ! h264parse ! mp4mux ! \
  filesink location=hadron.mp4
```

The Hadron EO is always `sensor-id=0`, because its overlay disables the image's other cameras. Argus needs a black-level ISP file that the image installs. On older images, install it by hand as [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md#argus) describes.

## Demo

The browser demo shows both cameras with their settings, the IMU as an attitude indicator and a switch that makes the Boson the frame-sync master. Run it from a PC in a checkout of [ark\_jetson\_kernel](https://github.com/ARK-Electronics/ark_jetson_kernel):

```bash
scripts/camera/hadron/demo.sh jetson@jetson.local
```

It copies the demo to the Jetson over SSH, starts it and opens `http://jetson.local:8642/`. Ctrl-C stops it.

## IMU

The ICM-45686 is at `0x68` on whichever I2C bus the cable lands on. The kernel repo's scripts find it by its ID. The I2C0 bus runs at 100 kHz, which carries accel and gyro at up to 400 Hz. A 400 kHz bus carries 1600 Hz.
