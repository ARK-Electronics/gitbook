---
description: >-
  If WiFi was not setup via the OS Customization options in the Pi Imager UI you
  can follow these steps to setup your network.
---

# Wi-Fi Setup

Mount the SD card or EMMC on your computer and open the root filesystem directory.

## Bookworm

Create a new NeworkManager connection profile in **/etc/NetworkManager/system-connections/**

Name the file **YourNetworkSSID**.nmconnection and make sure to replace **YourNetworkSSID** and **YourNetworkPassword**.

```
[connection]
id=YourNetworkSSID
uuid=0e214bd8-4501-4394-9a46-123badc0ffee
type=wifi

[wifi]
mode=infrastructure
ssid=YourNetworkSSID

[wifi-security]
key-mgmt=wpa-psk
psk=YourNetworkPassword

[ipv4]
method=auto

[ipv6]
addr-gen-mode=default
method=auto

[proxy]
```

## Prior to Bookworm

Create a file called **wpa\_supplicant.conf**

Edit the file in a text editor.

Replace `<YOUR TWO LETTER COUNTRY CODE>` with your country code, ie `US`.

Replace `<YOUR NETWORK NAME>` and `<YOUR NETWORK PASSWORD>` with your network info.

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<YOUR TWO LETTER COUNTRY CODE>

network={
    ssid="<YOUR NETWORK NAME>"
    psk="<YOUR NETWORK PASSWORD>"
    key_mgmt=WPA-PSK
}

```

Save the file. On the next boot of the Pi, it will move the file to **/etc/wpa\_supplicant/**
