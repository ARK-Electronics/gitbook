---
hidden: true
---

# Doodle Labs Nimble Integration Guide for ARK Jetson PAB Carrier

## Introduction

This guide provides step-by-step instructions for integrating the **Mini Mesh Rider Radio system** with the **ARK Jetson PAB Carrier**, designed for seamless deployment in UAV and robotic platforms.

It covers hardware connections, software configuration, and troubleshooting tips to enable robust, high-throughput wireless communication over a **private WDS/ Mesh network** using the Doodle Labs platform. Standard Wi-Fi modes are also supported for more conventional networking setups.

Whether you're setting up a new vehicle or retrofitting an existing system, this integration guide ensures a reliable link between the **Jetson-based companion computer** and ground control station, optimized for use with **ROS2, PX4, MAVLink**, and other ARK Electronics software frameworks.



## Hardware setup

In this case, you will need the Mini evaluation test board. Once it is connected, it must be powered using an additional power module via the barrel jack port. This auxiliary power supply can also serve as a good redundant power source for the Jetson. After powering the board, you can use the Ethernet ports to connect the Mini (expansion board) to the Jetson carrier.

## ~~Jetson setup~~



Once you are done you should ssh to your Jetson:

```
ssh jetson@jetson.local
```

Password:**jetson**\
\
You should also install the [Broken link](/broken/pages/Yxqz8349jGsIQFKfvban "mention")

## Mesh Rider Radio software setup



## Supported Networking Modes <a href="#supported-networking-modes" id="supported-networking-modes"></a>

One of the two main networking layouts we expect Nimble to operate as is Nimble as Access Point and Client, the photo below is an example of such a layout. The Nimble radio is integrated into a ground control station and acts as an Access Point. The drones are each integrated with a Nimble radio and are configured to be clients.

There are two ways to proceed. One option is to configure for Nimble to be in Access Point mode and the other is to configure Nimble to be in Client/Station mode.

### Wifi AP/Client

#### Client Mode

To install and configure the radio to be in Client mode do the following

Navigate to the Nimble/nimble\_installer directory in a terminal and run the following command

```
cd Nimble/nimble_installer
sudo ./nimble_installer.sh Client 
```

Reboot the device after installation is complete

```
sudo reboot
```

The device will act as a WiFi Client device with the following parameters

**SSID: wireless-hotspot** \
**PSK: DoodleSmartRadio**\
**IP: DHCP Client**

If an access point is running with the above credentials, on the same channel and bandwidth (it should be if it is the default Nimble AP installation). Check if this client/station is connected to AP using following commands, please use the DoodleLabs WiFi card interface name, for example “wlp3s0”

```
sudo iw wlp3s0 info 
sudo iw wlp3s0 station dump 
```

#### Access Point Mode

To install and configure the radio to be in AP mode do the following

Navigate to the Nimble/nimble\_installer directory in a terminal and run the following command

```
cd Nimble/nimble_installer
sudo ./nimble_installer.sh AP 
```

Reboot the device after installation is complete

```
sudo reboot
```

Check if the AP is functional using iw command, please use the DoodleLabs WiFi card interface name, for example “wlp3s0”

```
sudo iw wlp3s0 info
```

The device will act as a WiFi AP with the following settings

**SSID: wireless-hotspot**\
**PSK: DoodleSmartRadio**\
**IP: 10.223.3.1/16 and running a DHCP server**

#### **Notes**

You can switch between AP and Client mode by running the nimble\_installer.sh script again with the desired mode and rebooting.

##

## **WDS Client/WDS AP**

The other networking layout we expect is for customers to use Nimble in Mesh Rider interoperability mode. This allows Nimble to function as either WDS AP or WDS Client. The Mesh Rider radio must also be configured to operate in the appropriate WDS AP or WDS Client mode. Here is a possible network setup possible with Nimble and Mesh Rider.

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

The default mode on Nimble is with Mesh Rider Radio interoperability disabled, and it acts as a normal AP/Client. To achieve the Mesh Rider <-> Nimble network architecture as illustrated in the network diagram above, Mesh Rider interoperability must be enabled using the Nimble Configuration script nimble\_config.sh mentioned earlier.&#x20;

This will allow the Nimble radio to connect with Mesh Rider radios in WDS AP/Client mode. The Mesh Rider radio also needs to be configured in WDS mode for Nimble to connect.&#x20;

You have to be in Client/AP Mode already, then you can enable WDS using Nimble Software Configuration Utility.<br>

To configure the Nimble transceiver, navigate to the nimble\_config folder /Nimble/nimble\_config/then run the nimble\_config shell script as root.

```
cd /Nimble/nimble_config
sudo ./nimble_config.sh 
```

Select option 5 and enter 1 to Enable Meshrider interoperability then select 6 to exit to save and close the Configuration Utility

{% stepper %}
{% step %}
Select option 5&#x20;

To edit Meshrider interoperability
{% endstep %}

{% step %}
Enter 1&#x20;

To enable Meshrider interoperability
{% endstep %}

{% step %}
Select option 6&#x20;

To exit to save and close the Configuration Utility
{% endstep %}
{% endstepper %}

## Ground station radio setup

This section provides detailed instructions for setting up and connecting to Doodle Labs Mesh Rider Radios.\
Your options are:

* Wearable
* Mini & Nano OEM
* OEM

Regardless which radio you use as the base station the network setup is the same.&#x20;

After establishing a connection through Ethernet, you must set a static IP address for your host machine within the 10.223.0.0/16 subnet to access the radios. The method for assigning an IP address differs between operating systems (Windows, macOS, Linux, etc.).&#x20;

For a Windows 10 or later system, navigate to the Network Connections folder in the Control Panel. Right-click on the Wi-Fi or Ethernet adapter your host is using and select Properties. In the properties window, choose Internet Protocol Version 4 and then click Properties. Set the IP address to the 10.223.0.0/16 subnet. Since these addresses are statically assigned, make sure not to use the same IP address for another device on the network. Refer to the figure below for guidance on manually setting the IP address.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

For Linux:

<pre><code><strong>nmcli connection modify "Wired connection 1" ipv4.addresses 10.223.0.100/16
</strong>nmcli connection modify "Wired connection 1" ipv4.method manual
nmcli connection modify "Wired connection 1" ipv4.gateway 10.223.0.1
nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"

# Apply changes by restarting the connection
nmcli connection down "Wired connection 1"
nmcli connection up "Wired connection 1"
</code></pre>

Once the setup is complete you can go ahead and and open a web browser and navigate to the IP address written on your device

<figure><img src="../.gitbook/assets/20250328_141507.jpg" alt=""><figcaption></figcaption></figure>

Key setups for connection

Same SSID

* Same SSID
* Same Key
* Same Frequency (2.4ghz band should be one both of the radios can talk on)
* Same bandwidth

On the Jetson you could run the following command to see the correct setup

```
sudo iw wlan0 info
```

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption><p>WDS AP on Ground Control Station Radio</p></figcaption></figure>



<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption><p>WDS Client on Ground Control Station Radio</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption><p>Ground station in AP</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption><p>Ground station in Client</p></figcaption></figure>

Once you have established the connection you should remove the usb connection and reboot the Jetson.

With this setup, your Jetson is part of your IP network, which means if it’s running a MAVLink server or any MAVLink-compatible device, you should be able to connect to it via QGroundControl (QGC) over the network. Additionally, you can access the Jetson remotely using SSH for monitoring or configuration tasks.

Resources:<br>

{% embed url="https://techlibrary.doodlelabs.com/whats-in-the-box-w/quick-start-guide-ch2#physical-setup-instructions" %}

[ark-jetson-pab-carrier](../flight-controller/ark-jetson-pab-carrier/ "mention")
