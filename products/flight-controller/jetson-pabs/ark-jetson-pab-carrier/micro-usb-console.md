# Micro USB Console

Plugging a Micro USB cable into the Jetson carrier disconnects the flight controller from the Jetson's USB and puts the Jetson in USB device mode. The host PC sees a USB network interface (Jetson at `192.168.55.1`), a serial console, and an `L4T-README` drive.

{% hint style="warning" %}
After disconnecting the Micro USB cable, reboot the Jetson to reconnect the flight controller USB.
{% endhint %}

## Serial Console

Find the serial port on your host PC and connect with a serial terminal at baud rate **115200**. Log in with your username and password (default `jetson` / `jetson`).

## Connecting to WiFi from the Command Line

Scan for networks:

```
sudo nmcli device wifi
```

Connect to a network:

```
sudo nmcli device wifi connect 'SSID' password 'PASSWORD'
```

## Sharing Your PC's Internet over USB

The kernel repo ships a helper that NATs the Jetson's traffic out through your host PC's WiFi, giving the Jetson internet access over the USB cable — see [share\_wifi.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/share_wifi.md).
