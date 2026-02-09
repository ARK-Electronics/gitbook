# Getting Started

## What's Pre-Installed

When you order an ARK Jetson PAB Carrier bundle, everything comes pre-flashed:

- **Flight Controller**: Latest PX4 stable firmware
- **Jetson**: Latest ARK kernel + ARK-OS (bundle purchases)
- **Credentials**: Username `jetson`, password `jetson`

## Important: Custom Kernel Required

{% hint style="warning" %}
The ARK Jetson PAB Carrier requires a custom device tree to enable all hardware features. If you reflash your Jetson, you must use the ARK kernel with the correct device tree.
{% endhint %}

Device tree files: [https://github.com/ARK-Electronics/ark_jetson_kernel/tree/main/device_tree/ark_pab](https://github.com/ARK-Electronics/ark_jetson_kernel/tree/main/device_tree/ark_pab)

See the [Flashing Guide](flashing-guide.md) for complete instructions.

## WiFi Setup

### MHF4 Antenna Cables (Not Included)

{% hint style="info" %}
MHF4 to RP-SMA antenna cables are required for WiFi and are not included. You can purchase compatible cables from Amazon:

- [Option 1: 2-Pack MHF4 to RP-SMA](https://www.amazon.com/female-Pigtail-Antenna-Extension-wireless/dp/B07GTL2G69)
- [Option 2: 2-Pack MHF4 to RP-SMA (alternate)](https://www.amazon.com/dp/B076SGTMFS)
{% endhint %}

### First Boot: WiFi Hotspot

On first boot, if no known WiFi network is found, the Jetson will create a hotspot:

- **Network**: `jetson-<serial>`
- **Password**: `password`

Connect to the hotspot, then open a web browser and go to [http://jetson.local](http://jetson.local) to configure your WiFi network.

<figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

After clicking **Apply**, reconnect to your local network and refresh the page.

## Connecting to Your Jetson

### Option 1: SSH over WiFi

Once connected to the same network as your Jetson:

```bash
ssh jetson@jetson.local
```

### Option 2: Via Micro USB

{% hint style="danger" %}
**Micro USB + Flight Controller Conflict**

The Micro USB port is muxed with the Flight Controller USB connection. When Micro USB is connected:
- The Flight Controller is **disconnected** from the Jetson
- MAVLink routing and other FC-dependent services will not work
- You **MUST reboot** after disconnecting Micro USB to restore FC connectivity

See [Micro USB Console](micro-usb-console.md) for more details.
{% endhint %}

When connected via Micro USB, the Jetson appears as a USB network device:
- PC IP: `192.168.55.100`
- Jetson IP: `192.168.55.1`

```bash
ssh jetson@192.168.55.1
```

## ARK-UI Web Interface

ARK-UI provides a web interface for managing your Jetson. Access it at [http://jetson.local](http://jetson.local).

From ARK-UI you can:
- Configure WiFi networks
- Manage ARK-OS services
- Update flight controller firmware
- View system logs

<figure><img src="../../.gitbook/assets/Screenshot from 2024-10-08 12-07-03.png" alt="" width="516"><figcaption></figcaption></figure>

## Next Steps

- [ARK Services](ark-services/) - Learn about the pre-installed ARK-OS services
- [Autopilot Connections](autopilot-connections/) - Connect QGroundControl or MissionPlanner
- [Flashing Guide](flashing-guide.md) - Update or reflash your Jetson
