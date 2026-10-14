---
description: >-
  After flashing the SD/EMMC you must modify the config.txt in order for the ARK
  Pi6X to function properly.
---

# After Flashing, Before Installing

Edit `config.txt` on the boot partition. On a running Pi it is **/boot/firmware/config.txt** (**/boot/config.txt** before Bookworm).

Comment out the following lines:

```
# Automatically load overlays for detected cameras
# camera_auto_detect=1

# Automatically load overlays for detected DSI displays
# display_auto_detect=1
```

Leave the stock `[cm4]` and `[cm5]` sections in place; they enable the USB port. Add the block for your compute module at the end of the file, after `[all]`. The CM5 maps the board's UARTs and cameras differently; see [Compute Module 5](../hardware.md#compute-module-5).

{% tabs %}
{% tab title="CM4" %}
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

# Drive USB Hub nRESET high. Only needed on Rev 1.
gpio=26=op,dh

# Cameras on CAM0 and CAM1 (CAM1 is the overlay default). Compute modules don't auto-detect
# cameras: use imx708 for Camera Module 3, imx219 for Camera Module 2, imx477 for HQ
dtoverlay=imx708,cam0
dtoverlay=imx708

# Pi I2C1 connector. /dev/i2c-1 also needs the i2c-dev module (add it to /etc/modules-load.d/)
dtparam=i2c_arm=on

# Fan GPIO
dtoverlay=gpio-fan,gpiopin=19
```
{% endtab %}

{% tab title="CM5" %}
```
# Turn on uart debug console
enable_uart=1

# General Purpose UART External (UART2 on the CM5)
dtoverlay=uart2,ctsrts

# Telem2 to FC (UART3 on the CM5, /dev/ttyAMA3)
dtoverlay=uart3,ctsrts

# Drive FMU_RST_REQ low
gpio=25=op,dl

# Drive USB_OTG_FS_VBUS high to enable FC USB
gpio=27=op,dh

# Drive USB Hub nRESET high. Only needed on Rev 1.
gpio=26=op,dh

# Camera on the CAM1 connector, which is cam0 on the CM5. Compute modules don't auto-detect
# cameras: use imx708 for Camera Module 3, imx219 for Camera Module 2, imx477 for HQ
dtoverlay=imx708,cam0

# Pi I2C1 connector. /dev/i2c-1 also needs the i2c-dev module (add it to /etc/modules-load.d/)
dtparam=i2c_arm=on

# Fan GPIO
dtoverlay=gpio-fan,gpiopin=19
```
{% endtab %}
{% endtabs %}
