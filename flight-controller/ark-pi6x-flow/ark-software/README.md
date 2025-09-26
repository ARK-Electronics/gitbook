# ARK Software

If you purchased an ARK Pi6X Flow with a Pi included these software packages will come pre-installed.\
[https://github.com/ARK-Electronics/ARK-OS](https://github.com/ARK-Electronics/ARK-OS)

## Getting Started

On boot, if no known WiFi network is found, a hotspot will be created named **raspberrypi-\<serial>** with the password **password**.

Open a web browser and go to [http://raspberrypi.local/](http://raspberrypi.local/) Here you can edit the WiFi hotspot or connect to your local network.\


<figure><img src="../../../.gitbook/assets/Screenshot from 2024-10-09 12-53-22.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot from 2024-10-09 13-16-28 (1).png" alt="" width="516"><figcaption></figcaption></figure>

After clicking **Apply** re-connect to your local network and refresh the page.

## Connecting to QGroundControl

In QGroundControl, when on the same network, you can connect to the flight controller by adding a UDP connection to port 14550 and the IP address of the Pi.\
![](<../../../.gitbook/assets/image (23).png>)![](<../../../.gitbook/assets/Screenshot from 2024-10-09 12-42-32.png>)



