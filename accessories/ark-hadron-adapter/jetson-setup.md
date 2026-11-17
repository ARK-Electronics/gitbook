# Jetson Setup

The ARK Jetson images carry the driver for the Hadron's visible (EO) camera, `nv_ov64b40`, and one `jetson-io` overlay for each CSI port the adapter can plug into. The thermal camera (Boson) is a UVC device over USB and needs no overlay. The driver, the overlays and the bench results are in [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md) in the kernel repo.

## Cabling

| Adapter connector | Carrier connector |
| ----------------- | ----------------- |
| EO Camera (22-pin FFC) | A CSI camera port, see the overlay table below. The 22-to-22-pin cable fits the Just A Jetson and PAB Carrier V3; the 22-to-15-pin cable fits the PAB Carrier |
| IR Camera / USB (4-pin JST-GH) | Any USB 2.0 JST-GH port |
| I2C (6-pin JST-GH) | Just A Jetson: UART2/I2C0, with the included straight cable. Jetson PAB Carrier: Jetson I2C0, a 4-pin JST-GH with SCL on pin 2 and SDA on pin 3, which needs a 6-to-4-pin cable (not included). Jetson PAB Carrier V3: no Jetson I2C connector; the IMU can be reached by bit-banging I2C with the kernel's `i2c-gpio` driver on GPIO01 (pin 23) and GPIO12 (pin 12) of the Pixhawk Payload Bus connector, which the image does not set up. Those pins are 1.8 V and the adapter's I2C port is 3.3 V, so a level translator goes between them |

## Overlays

Each overlay is for one port. Pick the row for your carrier and port.

| Carrier | Port | Lanes | Overlay name | Status |
| ------- | ---- | ----- | ------------ | ------ |
| ARK Just A Jetson | CAM0 (J28) | 2 | Camera FLIR Hadron EO CAM0 2-lane | Bench-tested |
| ARK Just A Jetson | CAM1 (J25) | 4 | Camera FLIR Hadron EO CAM1 4-lane | Bench-tested |
| ARK Jetson PAB Carrier V3 | CAM0 (J28) | 4 | Camera FLIR Hadron EO CAM0 4-lane | Untested on hardware |
| ARK Jetson PAB Carrier V3 | CAM1 (J25) | 4 | Camera FLIR Hadron EO CAM1 4-lane | Untested on hardware |
| ARK Jetson PAB Carrier | CAM0–CAM3 | 2 | Camera FLIR Hadron EO CAM*n* 2-lane | Untested on hardware; use the included 22-to-15-pin FFC |

Both Just A Jetson ports carry four lanes. The CAM0 overlay uses two of them, because L4T runs 4-lane only from CSI0_CLK or CSI2_CLK and CAM0's clock is on CSI1_CLK, so each mode runs there at half its 4-lane frame rate.

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
| 3 | 9248x6936 | 13.2 | 6.6 | Full array. At full size through Argus it ran out of memory on an Orin Nano 4GB and ran on an Orin NX 16GB; see [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md#argus) |

Through Argus, mode 2 on a 4-lane port delivers about 100 fps, or the full 120 fps after `sudo jetson_clocks`.

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

The Hadron EO is always `sensor-id=0`, because each overlay disables the other camera modules the image enables at flash time. Argus needs the black-level ISP file that the image installs; if your image predates it, [hadron.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/hadron.md#argus) says how to install it by hand.

## Demo

A browser demo shows both cameras side by side with their settings, the adapter's IMU as an attitude indicator, and a switch that makes the Boson the frame-sync master. Run it from a PC, in a checkout of [ark\_jetson\_kernel](https://github.com/ARK-Electronics/ark_jetson_kernel):

```bash
scripts/camera/hadron/demo.sh jetson@jetson.local
```

It copies the demo to the Jetson over SSH, starts it and opens `http://jetson.local:8642/` in your browser. Press Ctrl-C to stop it.

## IMU

The adapter's ICM-45686 is at `0x68` on whichever I2C bus the 6-pin cable lands on. The scripts in the kernel repo find it by its ID. The I2C0 connector's bus runs at 100 kHz, which carries accel and gyro at up to 400 Hz; a 400 kHz bus carries 1600 Hz.
