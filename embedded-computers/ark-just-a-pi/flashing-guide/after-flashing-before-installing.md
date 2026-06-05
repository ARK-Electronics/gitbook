---
description: >-
  After flashing the SD/EMMC you must modify the config.txt in order for the ARK
  Just a Pi to function properly.
---

# After Flashing, Before Installing

Edit **/boot/firmware/config.txt**

Comment out the following lines

```
# Automatically load overlays for detected cameras
# camera_auto_detect=1

# Automatically load overlays for detected DSI displays
# display_auto_detect=1
```

Add the following

```
# ---- Board power/enable lines (ARK PiCM5 Carrier) ----
# Enable KSZ8794 Ethernet switch 1.2V rail
gpio=27=op,dh
# Release Ethernet switch from reset
gpio=20=op,dh
# Enable 3.3V camera rail feeding both CSI connectors
gpio=22=op,dh

# CAM0 = J2 on MIPI0 (I2C0), CAM1 = J1 on MIPI1 (ID_SD/ID_SC). Swap imx219 for your sensor.
dtoverlay=imx219,cam0
dtoverlay=imx219,cam1

# ---- UARTs ----
enable_uart=1                 # UART0 debug console, J6 (GPIO14/15)
dtoverlay=uart2,ctsrts        # UART2/SPI3, flow control (GPIO4-7)
dtoverlay=uart3,ctsrts        # UART3/SPI4, flow control (GPIO8-11)
dtoverlay=uart4               # UART4, TX/RX only (GPIO12/13) doesn't work on cm5 needs rc.local on boot

# PCIe FFC — off by default on CM5
dtparam=pciex1
dtparam=pciex1_gen=3          # only if your endpoint is Gen3-clean

# USB2 host port VBUS — needed to power downstream devices
gpio=24=op,dh

# Enable the Fan
dtparam=cooling_fan=on
dtparam=fan_temp0=40000        # 40.0 °C, was 50000
dtparam=fan_temp0_speed=120    # 0-255, was 75
dtparam=fan_temp1=50000
dtparam=fan_temp2=60000
dtparam=fan_temp3=70000

# Drive the power LED on by default
dtparam=pwr_led_trigger=default-on
```
