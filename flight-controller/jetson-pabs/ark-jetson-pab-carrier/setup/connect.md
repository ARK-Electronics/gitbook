# Connect

## Micro USB

Connect the Micro USB port to your PC. The Jetson appears as a USB network device at `192.168.55.1`:

```bash
ssh jetson@192.168.55.1
```

The web UI is reachable the same way at [http://192.168.55.1](http://192.168.55.1).

{% hint style="danger" %}
**Micro USB + Flight Controller Conflict**

The Micro USB port is muxed with the flight controller's USB connection. While a Micro USB cable is connected, the flight controller is disconnected from the Jetson and MAVLink routing will not work. After unplugging, **reboot the Jetson** to restore the flight controller connection.
{% endhint %}

The same cable also carries a serial login console — see [Micro USB Console](../micro-usb-console.md).

## WiFi Hotspot

On first boot, if no known WiFi network is available, the Jetson brings up a hotspot:

* **Network**: `jetson-<serial>`
* **Password**: `password`

Connect to it and open [http://jetson.local](http://jetson.local).

{% hint style="info" %}
**WiFi antennas and MHF4 cables are not included.** Connect an [MHF4 to RP-SMA cable](https://www.amazon.com/dp/B07GTL2G69) to each MHF4 connector on the WiFi card, then an RP-SMA WiFi antenna to each cable. Any dual-band (2.4/5 GHz) antenna works; the 6 GHz band needs one rated for Wi-Fi 6E, such as these [tri-band antennas](https://www.amazon.com/dp/B0C344ZWZP). Some bundles ship without the WiFi card — the hotspot only appears when a WiFi card is installed.
{% endhint %}

## Ethernet

Plug the RJ45 port into your network — the Jetson requests an address over DHCP.

Once the Jetson is on your network:

```bash
ssh jetson@jetson.local
```
