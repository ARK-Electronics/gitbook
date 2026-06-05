# Getting Started

The ARK Just A Pi is a compact carrier board for the Raspberry Pi Compute Module 5. This guide covers preparing the board and connecting to it for the first time.

<!-- TODO: Document what comes pre-installed/pre-configured on bundle orders, if anything. -->

## Flashing the Compute Module

If you are installing your own Compute Module, follow the [Flashing Guide](flashing-guide/README.md) to image the CM5 (micro SD for the CM5 Lite, or eMMC over USB-C) and prepare it for first boot.

If you set up the OS using the Raspberry Pi Imager customization options described in the flashing guide, the board comes up with:

- **Username**: `pi`
- **Password**: `pi`
- **Hostname**: `just-a-pi`

## Connecting

### Serial Debug Console

The **UART0 Debug** connector (6-pin JST-GH) exposes the Compute Module's serial console at 3.3V. Connect a 3.3V USB-to-serial adapter to reach the console before the network is configured. See the [Pinout](pinout.md) for the connector pin assignments.

### SSH over the network

Once Wi-Fi or Ethernet is configured (see [Wi-Fi Setup](flashing-guide/wi-fi-setup.md) and [SSH](flashing-guide/ssh.md)), connect over SSH:

```bash
ssh pi@just-a-pi.local
```

If mDNS is not available on your network, use the Pi's IP address instead.

## Next Steps

- [Flashing Guide](flashing-guide/README.md) – Image the Compute Module and prepare it for first boot
- [Pinout](pinout.md) – Connector and pin assignments
- [Block Diagram](block-diagram.md) – Board architecture overview
- [3D Model](3d-model.md) – STEP files
