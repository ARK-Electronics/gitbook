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
| ARK IMX477 Single 4 lane | Single IMX477 with 4-lane CSI (requires ARK CSI-2-1 Adaptor) | Not Working |
| ARK IMX477 Dual 4 lane | Dual IMX477 with 4-lane CSI (requires ARK CSI-2-1 Adaptor) | Not Working |

{% hint style="warning" %}
**4-Lane CSI Mode Not Working on JetPack 6**

The 4-lane CSI overlays are currently non-functional due to a bug in the JetPack 6 kernel. This affects the "ARK IMX477 Single 4 lane" and "ARK IMX477 Dual 4 lane" overlays. See the [NVIDIA Developer Forum issue](https://forums.developer.nvidia.com/t/imx477-4lane-on-cam1/333270) for updates on a fix.
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

If you need to build or modify camera overlays from source, see the [ARK Jetson Kernel repository](https://github.com/ARK-Electronics/ark_jetson_kernel).

To build the camera overlay DTBs:

```
export CROSS_COMPILE=$HOME/l4t-gcc/aarch64--glibc--stable-2022.08-1/bin/aarch64-buildroot-linux-gnu-
export KERNEL_HEADERS=$PWD/source_build/Linux_for_Tegra/source/kernel/kernel-jammy-src
cd source_build/Linux_for_Tegra/source/
make dtbs
```

Copy the overlay DTB to the Jetson via Micro-USB:

```
DTB_PATH="$PWD/source_build/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs/"
OVERLAY_DTB=<your_overlay>
scp $DTB_PATH/$OVERLAY_DTB jetson@192.168.55.1:~
```

SSH into the Jetson and move the overlay to `/boot`:

```
ssh jetson@192.168.55.1
sudo mv <your_overlay> /boot
```

You can then apply the overlay using the Jetson-IO tool as described above.
