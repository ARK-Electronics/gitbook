# DTC BluSDR Radio integration Guide for ARK Jetson PAB Carrier

## Introduction

This guide provides step-by-step instructions for integrating the **DTC radio system** with the **ARK Jetson PAB Carrier**, enabling seamless deployment in **UAV** and robotic platforms.

It covers hardware connections, software configuration, and troubleshooting tips to establish a robust, high-throughput wireless link over a private **DTC mesh network**. Standard IP networking features were designed from the ground up for robust performance in the most demanding\
dynamic environments, free from the compromises of competitor solutions based on consumer\
standards.

Whether you're configuring a new vehicle or upgrading an existing system, this integration guide ensures a reliable connection between the **Jetson-based** companion computer and your ground control station—optimized for use with **ROS2**, **PX4**, **MAVLink**, and other **ARK Electronics Software Frameworks**.

## Hardware setup

The **DTC BluSDR radio** requires external power to operate reliably. We recommend using the **ARK 12S Payload Power Module**, which provides regulated and protected power suitable for airborne and mobile robotics platforms.

In addition to powering the **BluSDR**, connect an Ethernet cable from the radio's LAN port directly to the **Ethernet port on the ARK Jetson PAB Carrier**. This connection enables high-throughput data exchange between the Jetson companion computer and the mesh network formed by the **DTC** radios.

Note: CA4005 battery or **6-18VDC** power source can be used as power options (**ARK 12S Payload Power Module**)

<figure><img src="../.gitbook/assets/image (83).png" alt=""><figcaption><p>DTC User Guide</p></figcaption></figure>



<figure><img src="../.gitbook/assets/20260116_130446 (1).jpg" alt="" width="563"><figcaption><p>Setup using <strong>ARK 12S Payload Power Module</strong></p></figcaption></figure>



<figure><img src="../.gitbook/assets/image (82).png" alt="" width="563"><figcaption></figcaption></figure>



<figure><img src="../.gitbook/assets/20260116_130852 (1).jpg" alt="" width="375"><figcaption><p>Heat sink attached to the radio using thermal pads</p></figcaption></figure>



You also need the radio for the Ground side, see below:

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>



⚠️ Ensure all connections are secure and that antennas are properly attached to avoid damage during operation.

You can pick your two radios from the **DTC BluSDR™** Radio Technology Family:

[https://www.dtccodan.com/products/the-blusdr-family](https://www.dtccodan.com/products/the-blusdr-family)\
\
For this integration the following hardware were used:

| Description            | Link                                                                                                                                                                                                                 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BluSDR-6               | [https://www.dtccodan.com/assets/general-downloads/Datasheets/DTC-UK/BluSDR-30-2W-BluSDR-Radio-Module.pdf](https://www.dtccodan.com/assets/general-downloads/Datasheets/DTC-UK/BluSDR-30-2W-BluSDR-Radio-Module.pdf) |
| BluSDR-30              | [https://www.dtccodan.com/assets/general-downloads/Datasheets/DTC-UK/BluSDR-30-2W-BluSDR-Radio-Module.pdf](https://www.dtccodan.com/assets/general-downloads/Datasheets/DTC-UK/BluSDR-30-2W-BluSDR-Radio-Module.pdf) |
| ARK Jetson PAB Carrier | [https://arkelectron.com/product/ark-jetson-pab-carrier/](https://arkelectron.com/product/ark-jetson-pab-carrier/)                                                                                                   |





## DTC Software Setup

#### &#x20;Configure Radios <a href="#configure-radios" id="configure-radios"></a>

* You will need to be on a **Windows computer** for the initial setup, to download DTC’s `Node Finder` software, from [here](https://www.domotactical.com/setup).
* After downloading the Node Finder software, run it.
* Connect the radio to your PC temporary while powering it up.
* Hit the `reload` button until a radio shows up.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 231241.png" alt=""><figcaption></figcaption></figure>

* You might observe, the IP address is `0.0.0.0`. This is because it is currently in DHCP mode. But you want it to have a static IP so you can access the configuration page. Right click on the radio, click `Configure Network`, and assign a static IP for the radio.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 231309.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 231328.png" alt=""><figcaption></figcaption></figure>



* Set a static IP address for the host PC in the same subnet as what you set for the radio.
  * Note: You have to repeat this step on **Linux** once the radios are configured in case you use **Linux** (In case of the **Jetson** at least)
* In a web browser, enter the IP you set for the radio on `Domo Node Finder`. A login screen should be brought up. Leave the username blank and enter “Eastwood” for the password. You should now be in the radio configuration screen.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 231724.png" alt=""><figcaption></figcaption></figure>

* On the left navbar, go to Presets -> Mesh Settings
* `Mesh id` should be the same for all radios on the same mesh, so no need to change it.
* `Node id` should be unique for each radio on a mesh network. By default is it set to 0. Set this radio’s `Node id` to 1.
* Check `Enable Transmitter`. Set the frequency, PA linearity, and channel bandwidth to what is desired.
* Hit the save button to save the desired settings.
* Once you are done, turn off the radio and swap it with the one you are going to use on the Jetson side. Temporarily wire the **Jetson Radio** to your **GCS** computer so you can configure it.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 232741.png" alt=""><figcaption></figcaption></figure>

* Repeat the steps above for the **Jetson Radio**, making sure to match the settings. Make sure the `Node ID` on the **Jetson Radio** is different than the `Node ID` on the **GCS** radio.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 232819.png" alt=""><figcaption></figcaption></figure>

* Also make sure to make IP address of the second radio different than the first radio.

<figure><img src="../.gitbook/assets/Screenshot 2026-01-05 233326.png" alt=""><figcaption></figcaption></figure>



| Properties  | Ground Radio  | Air Radio     | Ground PC     | Jetson        |
| ----------- | ------------- | ------------- | ------------- | ------------- |
| Ip          | 192.168.0.128 | 192.168.0.41  | 192.168.0.98  | 192.168.0.99  |
| Subnet mask | 255.255.255.0 | 255.255.255.0 | 255.255.255.0 | 255.255.255.0 |



#### Ground PC

**Linux**

```
sudo nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.0.98/24
sudo nmcli connection modify "Wired connection 1" ipv4.method manual
sudo nmcli connection modify "Wired connection 1" ipv4.gateway 192.168.0.1
sudo nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"

# Apply the changes
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

**Windows**

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

#### Jetson



After connecting the radio, you can **SSH into the pre-flashed Jetson** via Micro USB to continue configuration or verify connectivity.

Once connected via SSH, set a static IP address on the Jetson that matches the radio network’s subnet. This allows seamless communication with the DTC radio and other devices on the mesh network.

```
sudo nmcli connection modify "Wired connection 1" ipv4.addresses 192.168.0.99/24
sudo nmcli connection modify "Wired connection 1" ipv4.method manual
sudo nmcli connection modify "Wired connection 1" ipv4.gateway 192.168.0.1
sudo nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8 1.1.1.1"

# Apply the changes
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

After setting the static IP, you can disconnect the USB connection and **restart the Jetson**. Once it reboots, you should be able to **SSH into the Jetson over the network** via the IP address you assigned.

### Establishing the connection



Once you set up all the static IP-s on both the Ground PC and the Jetson you can go ahead and power up the drone. You'll be able to reach to both IP-s from the Ground PC and you can also **SSH** to the Jetson from the established network.



`jetson.local` should load, here you can interact with our services<br>

<figure><img src="../.gitbook/assets/image (74).png" alt="jetson.local"><figcaption><p>jetson.local</p></figcaption></figure>





<figure><img src="../.gitbook/assets/image (75).png" alt=""><figcaption><p>RTSP server is ready at IP:5600/camera1</p></figcaption></figure>





### **QGround Control**

You can go ahead and add the Link for the Drone in QGC, `jetson.local` should give you the correct address you set previously.

<figure><img src="../.gitbook/assets/image (76).png" alt=""><figcaption><p>Adding the Jetson</p></figcaption></figure>

Finally, you can add the RTSP video stream using the same IP and `:5600/camera1`

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption><p>RTSP stream</p></figcaption></figure>

As you can see below the connection and the camera stream are established

<figure><img src="../.gitbook/assets/image (78).png" alt=""><figcaption><p>Connection and stream are ready</p></figcaption></figure>

