# Camera Overlays

The ARK Jetson PAB Carrier V3 has **2× dual-lane CSI ports** on 22-pin FFC connectors. Camera configuration is managed through device tree overlays, and the image ships with the **IMX219 dual** overlay active — IMX219 cameras work on both ports out of the box.

## Supported Cameras

| Sensor | Resolution | Overlay | Status |
| --- | --- | --- | --- |
| IMX219 | 3280x2464 | Camera IMX219 Dual | Working (default) |
| IMX477 | 4056x3040 | Camera IMX477 Dual | Working |
| IMX708 | 4608x2592 | Camera IMX708 Dual | Working |

See [cameras.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/cameras.md) in the kernel repo for sensor details, verification commands, and known issues.

## Switching Overlays

List the overlays available on your Jetson:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
```

Apply one and reboot:

```bash
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera IMX477 Dual"
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
