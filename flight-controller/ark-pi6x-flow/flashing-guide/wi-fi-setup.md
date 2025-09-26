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

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/common/wifi/ConnectionTemplate.nmconnection" %}

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

