---
description: >-
  After flashing the SD/EMMC you must modify the boot/config.txt in order for
  the ARK Pi6X to function properly.
---

# After Flashing, Before Installing

Comment out the following lines in **boot/config.txt**

```
# Automatically load overlays for detected cameras
# camera_auto_detect=1

# Automatically load overlays for detected DSI displays
# display_auto_detect=1
```

Add the following to the **boot/config.txt**

```
# Turn on uart debug console
enable_uart=1

# General Purpose UART External
dtoverlay=uart3,ctsrts

# Telem2 to FC
dtoverlay=uart4,ctsrts

# Drive FMU_RST_REQ low
gpio=25=op,dl

# Drive USB_OTG_FS_VBUS high to enable FC USB
gpio=27=op,dh

# Drive USB Hub nRESET high. Only on needed on Rev 1.
gpio=26=op,dh

# For pi cam v2, change model for different camera/s
dtoverlay=imx219,cam0
dtoverlay=imx219,cam1

# Fan GPIO
dtoverlay=gpio-fan,gpiopin=19
```

