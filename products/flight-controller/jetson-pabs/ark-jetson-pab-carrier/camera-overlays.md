# Camera Overlays

The ARK Jetson PAB Carrier has **4 x 2-lane CSI ports**, allowing up to four cameras to be connected simultaneously. Camera configurations are managed through device tree overlays. By default, the **Camera ARK IMX219 Quad** overlay is applied.

## Available Camera Overlays

The following camera overlays are available for the ARK Jetson PAB Carrier:

| Overlay Name | Description | Status |
|--------------|-------------|--------|
| Camera ARK IMX219 Quad | Four IMX219 cameras (default) | Tested |
| Camera ARK IMX219 Single | Single IMX219 camera | Tested |
| Camera ARK IMX477 Single | Single IMX477 camera | Tested |
| Camera ARK ARDUCAM Single | Single Arducam camera | Tested |

{% hint style="info" %}
**IMX477 4-lane mode is not supported.** The 4-lane overlays have been removed because the `nv_imx477` driver's 4-lane initialization is broken upstream. 2-lane mode delivers the full 12 MP at 30 fps. See the kernel repo's [camera documentation](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/cameras.md) for details.
{% endhint %}

## Listing Available Overlays

To see all available camera overlays on your Jetson, use the Jetson-IO tool:

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
```

Example output:

```
Header 1 [default]: Jetson 40pin Header
  Available hardware modules:
  1. ARK I2S to GPIO
  2. Adafruit SPH0645LM4H
  3. Adafruit UDA1334A
  4. FE-PI Audio V1 and Z V2
  5. ReSpeaker 4 Mic Array
  6. ReSpeaker 4 Mic Linear Array
Header 2: Jetson 24pin CSI Connector
  Available hardware modules:
  1. Camera ARK ARDUCAM Single
  2. Camera ARK IMX219 Quad
  3. Camera ARK IMX219 Single
  4. Camera ARK IMX477 Single
Header 3: Jetson M.2 Key E Slot
  No hardware configurations found!
```

## Applying a Camera Overlay

Use the Jetson-IO tool to apply a camera overlay.

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera ARK IMX477 Single"
```

Reboot for the changes to take effect:

```
sudo reboot
```

## Verifying Camera Detection

After rebooting, verify that LibArgus can detect your camera sensor:

```
nvargus_nvraw --lps
```

You can also test the camera with gstreamer (requires nvidia-jetpack to be installed):

```
gst-launch-1.0 nvarguscamerasrc ! nvvidconv ! xvimagesink
```

Or test with v4l2-ctl:

```
v4l2-ctl --set-fmt-video=width=3840,height=2160,pixelformat=RG10 --stream-mmap --stream-count=300 -d /dev/video0
```

## Building Custom Camera Overlays

Camera overlays are built from the [ARK Jetson Kernel](https://github.com/ARK-Electronics/ark_jetson_kernel) repository. You can either include the overlay in a full kernel build/flash, or build it standalone and copy it onto an already-flashed Jetson. For the full list of tested cameras and test commands, see the kernel repo's [camera documentation](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/cameras.md).

Clone and set up the repository (one time):

```
git clone https://github.com/ARK-Electronics/ark_jetson_kernel
cd ark_jetson_kernel
./setup.sh
```

### Option 1: Include the Overlay in the Kernel Build

This bakes the overlay into the flashed image so it is available immediately after flashing.

#### Step 1: Create the overlay source file

Add your `.dts` to the overlay directory for this carrier, using an existing ARK overlay as a template (e.g. `tegra234-p3767-camera-p3768-ark-imx477-single.dts`):

```
products/PAB/device_tree/source/hardware/nvidia/t23x/nv-public/overlay/
```

#### Step 2: Register it in the Makefile

Add your overlay to the `Makefile` in that same directory:

```makefile
dtbo-y += your-custom-overlay.dtbo
```

#### Step 3: Build and flash

```
./build.sh PAB
./flash.sh PAB
```

Your overlay will then be listed by `config-by-hardware.py -l` after flashing.

### Option 2: Build Standalone and Copy to a Flashed System

This builds the overlay and copies it onto a Jetson that has already been flashed — no reflash required.

#### Step 1: Build the device tree overlays

```
./build.sh PAB
```

The compiled `.dtbo` files land in:

```
staging/PAB/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs/
```

#### Step 2: Copy the overlay to the Jetson

Copy via Micro-USB (default IP when connected via USB):

```
DTB_PATH="staging/PAB/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs"
OVERLAY_DTB=tegra234-p3767-camera-p3768-ark-imx477-single.dtbo
scp $DTB_PATH/$OVERLAY_DTB jetson@192.168.55.1:~
```

#### Step 3: Install and apply on the Jetson

SSH in, move the overlay to `/boot`, apply it, and reboot:

```
ssh jetson@192.168.55.1
sudo mv tegra234-p3767-camera-p3768-ark-imx477-single.dtbo /boot
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera ARK IMX477 Single"
sudo reboot
```
