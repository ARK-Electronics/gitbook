# Camera Overlays

The ARK Just A Jetson Carrier has **2 x 4-lane CSI ports**, providing high-bandwidth connections for cameras. Camera configurations are managed through device tree overlays. Camera overlays need to be built and installed from the [ARK Jetson Kernel repository](https://github.com/ARK-Electronics/ark_jetson_kernel).

## Available Camera Overlays

The following camera overlays are available for the ARK Just A Jetson:

| Overlay Name | Description | Status |
|--------------|-------------|--------|
| Camera ARK IMX219 Quad | Four IMX219 cameras (using camera mux board) | Tested |
| Camera ARK IMX219 Single | Single IMX219 camera | Tested |
| Camera ARK IMX477 Single | Single IMX477 camera | Tested |
| Camera IMX477 Dual 4 lane | Dual IMX477 cameras using 4-lane CSI | Not Working |

{% hint style="warning" %}
**4-Lane CSI Mode Not Working on JetPack 6**

The 4-lane CSI overlays are currently non-functional due to a bug in the JetPack 6 kernel. This affects the "Camera IMX477 Dual 4 lane" overlay. See the [NVIDIA Developer Forum issue](https://forums.developer.nvidia.com/t/imx477-4lane-on-cam1/333270) for updates on a fix.
{% endhint %}

## Building and Installing Camera Overlays

Camera overlays must be built from source. Clone the ARK Jetson Kernel repository and follow the setup instructions:

```
git clone https://github.com/ARK-Electronics/ark_jetson_kernel
cd ark_jetson_kernel
./setup.sh
```

Build the device tree overlays:

```
export CROSS_COMPILE=$HOME/l4t-gcc/aarch64--glibc--stable-2022.08-1/bin/aarch64-buildroot-linux-gnu-
export KERNEL_HEADERS=$PWD/source_build/Linux_for_Tegra/source/kernel/kernel-jammy-src
cd source_build/Linux_for_Tegra/source/
make dtbs
```

Copy the overlay DTB to the Jetson via Micro-USB:

```
DTB_PATH="$PWD/source_build/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs/"
OVERLAY_DTB=tegra234-p3767-camera-p3768-ark-imx219-quad.dtbo
scp $DTB_PATH/$OVERLAY_DTB jetson@192.168.55.1:~
```

SSH into the Jetson and move the overlay to `/boot`:

```
ssh jetson@192.168.55.1
sudo mv tegra234-p3767-camera-p3768-ark-imx219-quad.dtbo /boot
```

## Listing Available Overlays

To see all available camera overlays on your Jetson, use the Jetson-IO tool:

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
```

Example output:

```
 Header 1 [default]: Jetson 40pin Header
   Available hardware modules:
   1. Adafruit SPH0645LM4H
   2. Adafruit UDA1334A
   3. FE-PI Audio V1 and Z V2
   4. ReSpeaker 4 Mic Array
   5. ReSpeaker 4 Mic Linear Array
 Header 2: Jetson 24pin CSI Connector
   Available hardware modules:
   1. Camera ARK IMX219 Quad
   2. Camera ARK IMX477 Single
```

## Applying a Camera Overlay

Use the Jetson-IO tool to apply a camera overlay. The overlay is applied to Header 2 (Jetson 24pin CSI Connector):

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera ARK IMX219 Quad"
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
