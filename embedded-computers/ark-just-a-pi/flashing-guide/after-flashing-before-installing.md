---
description: >-
  After flashing the SD/EMMC you must modify the config.txt in order for the ARK
  Just a Pi to function properly.
---

# After Flashing, Before Installing

Edit `config.txt` on the boot partition. On a running Pi it is **/boot/firmware/config.txt**.

Comment out the following lines:

```
# Automatically load overlays for detected cameras
# camera_auto_detect=1

# Automatically load overlays for detected DSI displays
# display_auto_detect=1
```

Leave the stock `[cm4]` and `[cm5]` sections in place. Add the block for your compute module at the end of the file, after `[all]`. For `/dev/i2c-1`, also add `i2c-dev` to a file in `/etc/modules-load.d/`. A CM4 can't use some interfaces; see [Compute Module 4](../hardware.md#compute-module-4).

{% tabs %}
{% tab title="CM5" %}
```
# Ethernet switch 1.2V rail, Ethernet switch out of reset, 3.3V camera rail
gpio=27=op,dh
gpio=20=op,dh
gpio=22=op,dh

# CAM1 connector (MIPI0) takes cam0; CAM2 (MIPI1) is the overlay default. Compute modules don't
# auto-detect cameras: use imx708 for Camera Module 3, imx219 for Camera Module 2, imx477 for HQ
dtoverlay=imx708,cam0
dtoverlay=imx708

# I2C1 (GPIO2/3)
dtparam=i2c_arm=on

# UART0 debug console (GPIO14/15)
enable_uart=1
# UART2 connector, with flow control (GPIO4-7)
dtoverlay=uart2,ctsrts
# UART3 connector, with flow control (GPIO8-11)
dtoverlay=uart3,ctsrts
# UART4 connector, TX/RX only (GPIO12/13)
dtoverlay=uart4

# PCIe FFC connector, off by default on the CM5. Uncomment the second line for Gen 3
# if the cable and device run cleanly at Gen 3
dtparam=pciex1
#dtparam=pciex1_gen=3

# USB 2.0 host port VBUS
gpio=24=op,dh

# Fan: temperatures in millidegrees Celsius, speed 0-255
dtparam=cooling_fan=on
dtparam=fan_temp0=40000
dtparam=fan_temp0_speed=120
dtparam=fan_temp1=50000
dtparam=fan_temp2=60000
dtparam=fan_temp3=70000

# Power LED on
dtparam=pwr_led_trigger=default-on
```
{% endtab %}

{% tab title="CM4" %}
```
# Ethernet switch 1.2V rail, Ethernet switch out of reset, 3.3V camera rail
gpio=27=op,dh
gpio=20=op,dh
gpio=22=op,dh

# Camera on the CAM1 connector (the overlay default on a CM4). Compute modules don't
# auto-detect cameras: use imx708 for Camera Module 3, imx219 for Camera Module 2, imx477 for HQ
dtoverlay=imx708

# I2C1 (GPIO2/3)
dtparam=i2c_arm=on

# UART0 debug console (GPIO14/15)
enable_uart=1
# UART3 connector, with flow control (uart4 on the CM4, GPIO8-11)
dtoverlay=uart4,ctsrts
# UART4 connector, TX/RX only (uart5 on the CM4, GPIO12/13)
dtoverlay=uart5

# USB 2.0 host port VBUS
gpio=24=op,dh

# Power LED on
dtparam=pwr_led_trigger=default-on
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
With a CM5, a Camera Module 3 (IMX708) on CAM2 streams only after a software reset at each power-up. The golden image does this at boot. On a manual install, run this at boot before anything opens the camera (needs `i2c-tools` and the `i2c-dev` module):

```
sudo i2ctransfer -f -y 0 w3@0x1a 0x01 0x03 0x01
```
{% endhint %}
