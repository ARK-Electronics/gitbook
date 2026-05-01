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
  1. ARK I2S to GPIO
  2. Adafruit SPH0645LM4H
  3. Adafruit UDA1334A
  4. FE-PI Audio V1 and Z V2
  5. ReSpeaker 4 Mic Array
  6. ReSpeaker 4 Mic Linear Array
Header 2: Jetson 24pin CSI Connector
  Available hardware modules:
  1. ARK IMX477 Dual 4 lane
  2. ARK IMX477 Single 4 lane
  3. Camera ARK ARDUCAM Single
  4. Camera ARK IMX219 Quad
  5. Camera ARK IMX219 Single
  6. Camera ARK IMX477 Single
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

There are two approaches for building and deploying camera overlays:

1. **Include in kernel build** - The overlay is built and included in the flashed image
2. **Build standalone** - Build the overlay separately and copy it to an already-flashed system

### Option 1: Include Overlay in Kernel Build

This approach includes the overlay in the kernel build so it's available immediately after flashing.

#### Step 1: Create the overlay source file

Create your `.dts` file in the device tree overlay directory:

```
device_tree/ark_pab/Linux_for_Tegra/source/hardware/nvidia/t23x/nv-public/overlay/
```

You can use an existing ARK overlay as a template (e.g., `tegra234-p3767-camera-p3768-ark-imx477-single.dts`).

#### Step 2: Add to the Makefile

Edit the Makefile in the same directory and add your overlay to the build:

```
device_tree/ark_pab/Linux_for_Tegra/source/hardware/nvidia/t23x/nv-public/overlay/Makefile
```

Add a line like:

```makefile
dtbo-y += your-custom-overlay.dtbo
```

#### Step 3: Add to copy_dtbs_to_prebuilt.sh

Edit `copy_dtbs_to_prebuilt.sh` in the repository root to copy your overlay to the prebuilt directory. Add lines like:

```bash
sudo cp $DTBS_SOURCE_PATH/your-custom-overlay.dtbo $PREBUILT_PATH/rootfs/boot/
sudo cp $DTBS_SOURCE_PATH/your-custom-overlay.dtbo $PREBUILT_PATH/kernel/dtb/
```

#### Step 4: Build and flash

Run the build and flash scripts:

```
./build_kernel.sh   # Select PAB when prompted
./flash.sh
```

Your overlay will now be available via `config-by-hardware.py -l` after flashing.

### Option 2: Build Standalone and Copy to Flashed System

This approach builds an overlay and copies it to a Jetson that has already been flashed.

#### Step 1: Set up the build environment

If you haven't already, clone and set up the repository:

```
git clone https://github.com/ARK-Electronics/ark_jetson_kernel
cd ark_jetson_kernel
./setup.sh
```

#### Step 2: Build the device tree overlays

```
export CROSS_COMPILE=$HOME/l4t-gcc/aarch64--glibc--stable-2022.08-1/bin/aarch64-buildroot-linux-gnu-
export KERNEL_HEADERS=$PWD/source_build/Linux_for_Tegra/source/kernel/kernel-jammy-src
cd source_build/Linux_for_Tegra/source/
make dtbs
```

The compiled `.dtbo` files will be in:

```
source_build/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs/
```

#### Step 3: Copy overlay to the Jetson

Copy the overlay via Micro-USB (default IP when connected via USB):

```
DTB_PATH="$PWD/source_build/Linux_for_Tegra/source/kernel-devicetree/generic-dts/dtbs/"
OVERLAY_DTB=tegra234-p3767-camera-p3768-ark-imx477-single.dtbo
scp $DTB_PATH/$OVERLAY_DTB jetson@192.168.55.1:~
```

#### Step 4: Install the overlay on the Jetson

SSH into the Jetson and move the overlay to `/boot`:

```
ssh jetson@jetson.local
sudo mv tegra234-p3767-camera-p3768-ark-imx477-single.dtbo /boot
```

#### Step 5: Apply and reboot

Verify the overlay is available:

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -l
```

Apply the overlay:

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n 2="Camera ARK IMX477 Single"
sudo reboot
```
