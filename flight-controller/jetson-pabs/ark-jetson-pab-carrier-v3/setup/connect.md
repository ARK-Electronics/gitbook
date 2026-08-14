---
metaLinks:
  alternates:
    - ../../ark-jetson-pab-carrier/setup/connect.md
---

# Connect

## USB-C

Connect the USB-C port to your PC. The Jetson appears as a USB network device at `192.168.55.1`:

```bash
ssh jetson@192.168.55.1
```

The web UI is reachable the same way at [http://192.168.55.1](http://192.168.55.1).

The same cable also carries a serial login console — see [USB-C Console](../micro-usb-console.md).

## WiFi Hotspot

On first boot, if no known WiFi network is available, the Jetson brings up a hotspot:

* **Network**: `jetson-<serial>`
* **Password**: `password`

Connect to it and open [http://jetson.local](http://jetson.local).

{% hint style="info" %}
**MHF4 antenna cables are required for WiFi and are not included.** Compatible MHF4 to RP-SMA cables: [option 1](https://www.amazon.com/female-Pigtail-Antenna-Extension-wireless/dp/B07GTL2G69), [option 2](https://www.amazon.com/dp/B076SGTMFS). Some bundles ship without the WiFi card — the hotspot only appears when a WiFi card is installed.
{% endhint %}

## Ethernet

Connect the 4-pin JST-GH Ethernet port to your network — the Jetson requests an address over DHCP. The onboard switch also connects the flight controller and the Pixhawk Payload Bus, see [Autopilot Connections](../autopilot-connections/).

Once the Jetson is on your network:

```bash
ssh jetson@jetson.local
```
