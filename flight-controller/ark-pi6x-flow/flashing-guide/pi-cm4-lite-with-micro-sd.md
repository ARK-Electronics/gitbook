# Pi CM4 Lite with Micro SD

When using a Pi CM4 Lite without EMMC, a micro SD must be used for the OS. Follow the normal steps for flashing a micro SD using the Raspberry Pi Imager.

{% embed url="https://www.raspberrypi.com/software/" %}

If using Ubuntu:

```
wget -O pi_imager.deb https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb && sudo dpkg -i pi_imager.deb && rm pi_imager.deb
```

Apply OS customization to configure WiFi and enable SSH:

* Set the default hostname:

```
raspberrypi
```

* Set the Wifi:\
  It is recommended to add a Dummy Wifi to turn on the Wifi radio, it does not have to be a reachable/ functioning network.\
  Otherwise it can be turned on using the following command once you have ssh-d to the Pi using the debug port. This command is automatically applied once you install ARK OS, to clone ARK OS you either need Wifi or Ethernet connected to the board.

```
sudo nmcli radio wifi on
```

* Set the default **username (pi)** and **password (raspberry)**
* Enable SSH

<figure><img src="../../../.gitbook/assets/Screenshot from 2025-08-15 10-45-02.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot from 2025-08-15 10-44-47.png" alt=""><figcaption></figcaption></figure>

After flashing the SD card is complete, you will need to modify the **/boot/config.txt** file on the SD card before installing it into the Pi. See [**After Flashing, Before Installing**](after-flashing-before-installing.md)**.**
