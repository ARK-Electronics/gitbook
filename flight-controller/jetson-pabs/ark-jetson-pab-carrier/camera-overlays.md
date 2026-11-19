# Camera Overlays

The ARK Jetson PAB Carrier has **4× 2-lane CSI ports**. Camera configuration is managed through device tree overlays, and the image ships with the **IMX219 quad** overlay active — IMX219 cameras work on all four ports out of the box.

## Supported Cameras

| Sensor | Resolution | Overlay | Status |
| --- | --- | --- | --- |
| IMX219 | 3280x2464 | Camera IMX219 Quad | Working (default) |
| IMX477 | 4056x3040 | Camera IMX477 Quad | Working |
| IMX708 | 4608x2592 | Camera IMX708 Quad | Working |
| OV64B40 (FLIR Hadron EO) | 9248x6936 | Camera FLIR Hadron EO CAM0-CAM3 2-lane | Untested on hardware, through the [ARK Hadron Adapter](../../../accessories/ark-hadron-adapter/jetson-setup.md) with the included 22-to-15-pin FFC |
| FLIR Boson+ (thermal, MIPI) | 640x512 | Camera FLIR Boson+ CAM0-CAM3 | Working, through the [ARK Boson Adapter](../../../accessories/ark-boson-adapter/jetson-setup.md) with the included 22-to-15-pin FFC |

4-lane CSI modes are not supported — 2-lane provides full resolution at 30 fps for the IMX477. See [cameras.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/cameras.md) in the kernel repo for sensor details, verification commands, and known issues.

## Switching Overlays

List the overlays available on your Jetson:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
```

Apply one and reboot:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera IMX477 Quad"
sudo reboot
```

## Verifying a Camera

Check that the sensor is detected:

```bash
nvargus_nvraw --lps
```

ARK-OS also ships `check_cameras.sh` (on `PATH`) which stream-tests every connected CSI camera, and the [ARK-UI](http://jetson.local) **Video** page shows a live stream of the first camera.

## Custom Overlays

To build your own camera overlay — or install one on an already-flashed system — follow [camera\_overlays.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/camera_overlays.md) in the kernel repo.
