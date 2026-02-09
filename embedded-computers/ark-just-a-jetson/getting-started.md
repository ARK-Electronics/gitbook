# Getting Started

## What's Pre-Installed

When you order an ARK Just A Jetson bundle:

- **Jetson**: Latest ARK kernel
- **Credentials**: Username `jetson`, password `jetson`

## Important: Custom Kernel Required

{% hint style="warning" %}
The ARK Just A Jetson requires a custom device tree to enable all hardware features. If you reflash your Jetson, you must use the ARK kernel with the correct device tree.
{% endhint %}

Device tree files: [https://github.com/ARK-Electronics/ark_jetson_kernel/tree/main/device_tree/ark_jaj](https://github.com/ARK-Electronics/ark_jetson_kernel/tree/main/device_tree/ark_jaj)

See the [Flashing Guide](flashing-guide.md) for complete instructions.

## WiFi Setup

### MHF4 Antenna Cables (Not Included)

{% hint style="info" %}
MHF4 to RP-SMA antenna cables are required for WiFi and are not included. You can purchase compatible cables from Amazon:

- [Option 1: 2-Pack MHF4 to RP-SMA](https://www.amazon.com/female-Pigtail-Antenna-Extension-wireless/dp/B07GTL2G69)
- [Option 2: 2-Pack MHF4 to RP-SMA (alternate)](https://www.amazon.com/dp/B076SGTMFS)
{% endhint %}

## Connecting via USB-C

The USB-C port supports dual role operation (host/device). When connected to a PC, the Jetson appears as a USB network device:

- **PC IP**: `192.168.55.100`
- **Jetson IP**: `192.168.55.1`

```bash
ssh jetson@192.168.55.1
```

Or if mDNS is working on your network:

```bash
ssh jetson@jetson.local
```

## Next Steps

- [Connections](connections.md) - Hardware connection details
- [Flashing Guide](flashing-guide.md) - Update or reflash your Jetson
- [Pinout](pinout.md) - Pin assignments and connector information
