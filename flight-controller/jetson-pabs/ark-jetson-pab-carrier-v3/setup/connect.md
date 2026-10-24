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
**WiFi antennas and MHF4 cables are not included.** Connect an [MHF4 to RP-SMA cable](https://www.amazon.com/dp/B07GTL2G69) to each MHF4 connector on the WiFi card, then an RP-SMA WiFi antenna to each cable. Any dual-band (2.4/5 GHz) antenna works; the 6 GHz band needs one rated for Wi-Fi 6E, such as these [tri-band antennas](https://www.amazon.com/dp/B0C344ZWZP). Some bundles ship without the WiFi card — the hotspot only appears when a WiFi card is installed.
{% endhint %}

## Ethernet

Connect the 4-pin JST-GH Ethernet port to your network — the Jetson requests an address over DHCP. The onboard switch also connects the flight controller and the Pixhawk Payload Bus, see [Autopilot Connections](../autopilot-connections/).

Once the Jetson is on your network:

```bash
ssh jetson@jetson.local
```
