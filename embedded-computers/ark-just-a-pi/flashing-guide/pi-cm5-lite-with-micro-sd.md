# Pi CM5 Lite with Micro SD

When using a Pi CM5 Lite without EMMC, a micro SD must be used for the OS. Follow the normal steps for flashing a micro SD using the Raspberry Pi Imager.

{% embed url="https://www.raspberrypi.com/software/" %}

If using Ubuntu:

```
wget -O pi_imager.deb https://downloads.raspberrypi.org/imager/imager_latest_amd64.deb && sudo dpkg -i pi_imager.deb && rm pi_imager.deb
```

{% hint style="info" %}
Select a **64-bit** Raspberry Pi OS. ARK-OS ships packages for both current Raspberry Pi OS (Debian 13 Trixie) and Legacy (Debian 12 Bookworm) — the install script picks the matching one automatically.
{% endhint %}

Apply OS customization to configure WiFi and enable SSH:

* Set the default hostname:

```
just-a-pi
```

* Set the Wifi:\
  It is recommended to add a Dummy Wifi to turn on the Wifi radio, it does not have to be a reachable/ functioning network.\
  Otherwise it can be turned on using the following command once you have ssh-d to the Pi using the debug port.

```
sudo nmcli radio wifi on
```

* Set the default **username (pi)** and **password (pi)**
* Enable SSH

<figure><img src="../../../.gitbook/assets/Screenshot from 2025-08-15 10-45-02.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot from 2025-08-15 10-44-47.png" alt=""><figcaption></figcaption></figure>

After flashing the SD card is complete, you will need to modify the **/boot/firmware/config.txt** file on the SD card before installing it into the Pi. See [**After Flashing, Before Installing**](after-flashing-before-installing.md)**.**
