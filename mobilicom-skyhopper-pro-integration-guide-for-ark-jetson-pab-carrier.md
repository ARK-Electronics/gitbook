# Mobilicom SkyHopper Pro Integration Guide for ARK Jetson PAB Carrier

{% embed url="https://www.youtube.com/watch?v=anxRbgtJRk0" %}

## Introduction

This guide outlines the integration process for the **Mobilicom SkyHopper Pro** radio system with the **ARK Jetson PAB Carrier**, enabling reliable wireless communication for UAVs and robotic systems.

It includes detailed instructions for hardware connections, software configuration, and troubleshooting, focusing on establishing a secure, high-throughput wireless link via the SkyHopper Pro's advanced IP-based communication capabilities. The system supports essential networking features such as multicast and QoS prioritization—ensuring stable performance in challenging environments.

Whether you're building a new platform or retrofitting an existing vehicle, this guide will help ensure a robust connection between your **Jetson-based companion computer** and the **ground control station**, with full compatibility for **ROS2**, **PX4**, **MAVLink**, and other **ARK Electronics** software components.

## Hardware setup

The **SkyHopper Pro** system consists of two main components: an **Air unit** mounted on the UAV or robot, and a **Ground unit** connected to the control station. These units communicate over a secure, IP-based wireless link, providing a high-bandwidth, low-latency connection suitable for telemetry, video, and command/control data.

To power the **Air unit**, we recommend using the **ARK 12S Payload Power Module**, which supplies clean, regulated power suitable for flight and mobile applications. Ensure the **Air** unit is securely mounted with appropriate thermal and vibration considerations.

**Networking connection:**

* Connect an **Ethernet cable** from the **Air unit's LAN port** directly to the **Ethernet port on the ARK Jetson PAB Carrier**.
* The **Ground unit** should also be connected via Ethernet to your **ground control station** (e.g., laptop or base station computer).

Once powered, the **Air** and **Ground** units automatically establish a peer-to-peer IP link. This enables transparent data exchange between the Jetson companion computer and the ground control system, supporting high-throughput communication for ROS2, PX4, MAVLink, and ARK-specific applications.

<figure><img src=".gitbook/assets/IMG_5018.JPG" alt=""><figcaption></figcaption></figure>

### PTP Link Step-by-Step Configuration

To set up a Point-to-Point (PTP) link, you'll need two SkyHopper PRO units. One unit will serve as the\
**Remote/Air** Unit, while the other will function as the **Controller/Ground** Unit. The units are shipped pre-configured as a linked pair. In the following steps, you will find how to set the most basic RF link in case the radios were returned to their defaults.

To begin setup:

1. **Connect the SkyHopper Pro Air/Remote unit** to your **host PC** (or Jetson) using an **Ethernet cable**.
2. Assign a **static IP address** on your host device in the `192.168.131.xxx` subnet. This is required to communicate with the **SkyHopper** units over the network.
3. Open a web browser on your PC or laptop (we recommend Chrome) and enter the following\
   address in the address bar: https://192.168.131.241 to access the Web GUI interface (of the\
   remote unit).\
   &#xNAN;_&#x52;emark: The default IP address of the **Remote** Unit is 192.168.131.241 and the default IP address of the **Controller** Unit is 192.168.131.242. These addresses can be changed according to customer_\
   _requirements_.
4. **Repeat these steps for your Ground/Controller unit**

> ⚠️ Use an IP address that is not already in use on the network to avoid conflicts.

***

#### **Setting a Static IP (Windows 10 or Later)**

1. Open the **Control Panel** and go to **Network and Sharing Center**.
2. Click **Change adapter settings** from the left-hand menu.
3. Right-click on the Ethernet interface connected to the SkyHopper and choose **Properties**.
4. Select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.
5. Manually configure the following for your ground PC:
   * **IP address**: `192.168.131.150`
   * **Subnet mask**: `255.255.255.0`
   * **Default gateway**: `192.168.131.1` _(optional but recommended)_



For Linux:

```
# Set static IP address with subnet mask (/24 = 255.255.255.0)
sudo nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.131.150/24

# Set the method to manual (disable DHCP)
sudo nmcli connection modify "Wired connection 1" ipv4.method manual

# Set the default gateway (optional if you don't need internet)
sudo nmcli connection modify "Wired connection 1" ipv4.gateway 192.168.131.1

# Set DNS servers (optional)
sudo nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"

# Apply the changes
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

\
\
**GUI configuration**\
Once the static IP address is assigned, you can access the radio’s web interface by navigating to its IP address in a browser.\


* Navigate to the "Basic Configuration" section and verify that the unit mode is set to **Remote**.\
  Once confirmed, you can set the frequency you intend to use for this link.
* Go to the "Advanced Configuration" section and set the TX power that you would like to work\
  with. If you don't know the needed power, set the TX power to High (default value).
* Select the RF bandwidth (RF BW) that you would like to work with and the relevant bitrate.
* These settings are the most basic configurations that you will need to establish a link. Please\
  verify that you use the apply button after any change to confirm the settings.
* Once you have configured the **Remote** Unit, connect to the second unit, and change the unit\
  mode to **Controller**. At this stage, the unit will perform a reset.
* Please reconnect to the unit and note that the IP address has been changed to 192.168.131.242.
* Once you reconnect to the **Controller** Unit, you must set the same parameters for frequency, RF\
  BW, and bitrate, and apply changes after each modification. It is highly recommended to set both\
  units with same Tx power.
* Once all the parameters are identical (except the unit type), the link should be established.
* You can verify the status of the link in the "General Information" section. The link status lines will\
  turn green, and the link uptime will start counting.

_Please note that SkyHopper PRO units offer additional features including DFS, pairing, sense, and_\
_avoid. Detailed explanations and configuration for these features can be found in their respective_\
_tabs._

<figure><img src=".gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

Set the profile as required (RF bandwidth, bitrate and ratio), the two units should match.

<figure><img src=".gitbook/assets/Screenshot from 2025-06-18 15-27-29.png" alt=""><figcaption></figcaption></figure>

The **Ground** unit and the **Air** unit should be configured as **Controller** and **Remote** respectively.

<figure><img src=".gitbook/assets/Screenshot from 2025-06-18 15-29-25.png" alt=""><figcaption></figcaption></figure>



On the Frequency Configuration page you can setup the pairing key.\
**Repeat the steps for the other radio.**\
The recommended settings are RF bandwidth of 4.2 MHz and a bit rate of 3.2 Mbps. A higher bitrate and high pover mode can be used for the RTSP stream, however, please note that this may reduce the effective transmission range.

<figure><img src=".gitbook/assets/Screenshot from 2025-07-10 17-14-41.png" alt=""><figcaption></figcaption></figure>

\
\
**Jetson setup**\
\
After setting up the radios you can connect the **Air**/**Remote** unit to you Jetson, then you can **SSH into the pre-flashed Jetson** via USB to continue configuration or verify connectivity.

Once connected via SSH, set a static IP address on the Jetson that matches the radio network’s subnet. This allows seamless communication with the other radios on the network.\
\# Set static IP address with subnet mask (/24 = 255.255.255.0)

```
sudo nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.131.100/24

# Set the method to manual (disable DHCP)
sudo nmcli connection modify "Wired connection 1" ipv4.method manual

# Set the default gateway (optional if you don't need internet)
sudo nmcli connection modify "Wired connection 1" ipv4.gateway 192.168.131.1

# Set DNS servers (optional)
sudo nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"

# Apply the changes
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

After setting the static IP, you can disconnect the USB connection and **restart the Jetson**. Once it reboots, you should be able to **SSH into the Jetson over the network** via the IP address you assigned.\
