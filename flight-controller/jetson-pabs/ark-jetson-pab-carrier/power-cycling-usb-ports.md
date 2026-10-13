# Power Cycling USB Ports

The single USB 2.0 port and the two USB 3 ports on the combined connector are powered through the USB hub, so uhubctl cycles them. Ports 1 and 2 are the USB 3 connectors and port 3 is the USB 2.0 connector.

```
sudo uhubctl -l 1-2 -a off
sudo uhubctl -l 1-2 -a on
```

The standalone USB 3 port's VBUS is owned by the kernel (regulator `VDD_5V0_USBSS0`, enabled with the USB host controller) and cannot be switched with gpioset. Rebinding the host controller re-trains every port instead:

```
echo 3610000.usb | sudo tee /sys/bus/platform/drivers/tegra-xusb/unbind
echo 3610000.usb | sudo tee /sys/bus/platform/drivers/tegra-xusb/bind
```
