---
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/micro-usb-console.md
---

# USB C Console

After plugging in a USB C cable to the Jetson carrier, a file system is mounted and a serial port is presented the the host PC.

The L4T-README drive contains text files with information on using the serial port and connecting WiFi.

## Accessing the Jetson console over the USB C

After connecting, find the serial port number in your OS of choice. Using a serial terminal program, connect to that port using baud rate 115200.

You will need to login with your username and password. If you followed the flashing guide in these docs, it will be username "jetson" password "jetson".

## Connecting to WiFi using the USB C port

If you installed an M.2 WiFi module or a USB WiFi dongle, you can use nmcli to connect using the command line.

To scan for available networks:

```
sudo nmcli device wifi
```

To connect to a network

```
sudo nmcli device wifi connect 'SSID' password 'PASSWORD'
```

### Creating a WiFi hotspot using the command line

{% embed url="https://gist.github.com/narate/d3f001c97e1c981a59f94cd76f041140" %}
