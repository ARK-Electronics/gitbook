# ARK Software

If you purchased an ARK Jetson bundle with an SSD these software packages will come pre-installed.\
[https://github.com/ARK-Electronics/ARK-OS](https://github.com/ARK-Electronics/ARK-OS)

## Getting Started

On boot, if no known WiFi network is found, a hotspot will be created named **jetson-\<serial>** with the password **password**.\


<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

Open a web browser and go to [http://jetson.local](http://jetson.local). Here you can edit the WiFi hotspot or connect to your local network.\


<figure><img src="../../../.gitbook/assets/Screenshot from 2024-10-08 12-07-03.png" alt="" width="516"><figcaption></figcaption></figure>

After clicking **Apply** re-connect to your local network and refresh the page.

## Connecting to QGroundControl

In QGroundControl, when on the same network, you can connect to the flight controller by adding a UDP connection to port 14550 and the IP address of the Jetson.\
![](<../../../.gitbook/assets/image (23).png>)![](<../../../.gitbook/assets/image (24).png>)



