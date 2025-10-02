---
description: This page details flashing the AM32 firmware using the am32-configurator.
---

# Flash AM32

You can flash firmware to the ESCs using a Betaflight or Ardupilot flight controller. The ESCs must be powered and connected to the flight controller via the signal wire.&#x20;

Download the latest release of [AM32](https://github.com/am32-firmware/AM32/releases).

{% file src="../../../.gitbook/assets/AM32_ARK_4IN1_F051_2.19 (1).hex" %}

***

Navigate to the [am32-configurator](https://am32.ca/configurator) web tool and connect your flight controller to your PC via USB. If you're using Ardupilot you must first configure Ardupilot for ESC Passthrough.\
\
Connect to your device\
![](<../../../.gitbook/assets/image (43).png>)

Once connected, select Read\
![](<../../../.gitbook/assets/image (44).png>)

If successful you should see all of the settings for each motor

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>
