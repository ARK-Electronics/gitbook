---
metaLinks:
  alternates:
    - ../../ark-jetson-pab-carrier/setup/
---

# Set Up Your Carrier

## What's Pre-Installed

Bundles ship ready to use — no flashing required:

* **Jetson**: Latest ARK Jetson image (JetPack 6 / L4T r36) on the NVMe SSD, with [ARK-OS](https://github.com/ARK-Electronics/ARK-OS) pre-installed
* **Flight Controller**: Latest PX4 stable firmware
* **Credentials**: Username `jetson`, password `jetson`, hostname `jetson`

{% hint style="info" %}
The default password is well known — change it (`passwd`) before putting the vehicle on a network you don't control.
{% endhint %}

A bare carrier board (no Jetson module or SSD) has no OS on it. Install your module and NVMe SSD, then follow the [Flashing Guide](../flashing-guide.md).

## Steps

1. [Connect](connect.md) — reach the Jetson over USB-C, WiFi hotspot, or Ethernet.
2. [Get Online](get-online.md) — join it to your WiFi network.
3. [ARK-OS](../../../../ark-os/) — the preinstalled services and the ARK-UI web interface.
4. [Autopilot Connections](../autopilot-connections/) — connect QGroundControl or Mission Planner.
