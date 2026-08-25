---
description: This page details flashing ARK32 firmware using the ARK32 Configurator.
---

# Flash ARK32

You can flash firmware to the ESCs using a Betaflight or Ardupilot flight controller. The ESCs must be powered and connected to the flight controller via the signal wire.

Download **`ARK32_ARK_4IN1_F051`** from the latest [ARK32 release](https://github.com/ARK-Electronics/ARK32/releases).

***

Navigate to the [ARK32 Configurator](https://ark32.arkelectron.com/) and connect your flight controller to your PC via USB. If you're using Ardupilot you must first configure Ardupilot for ESC Passthrough.\
\
Connect to your device\
![](<../../../.gitbook/assets/image (43).png>)

Once connected, select Read\
![](<../../../.gitbook/assets/image (44).png>)

If successful you should see all of the settings for each motor

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

***

{% hint style="danger" %}
**Flashing alone is not enough.** You must now set **KV** and **Pole Count** for each motor channel — see [ARK32 Configuration](../ark32-configuration.md).
{% endhint %}
