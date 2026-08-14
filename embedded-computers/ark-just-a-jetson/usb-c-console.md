---
metaLinks:
  alternates:
    - ../../products/flight-controller/jetson-pabs/ark-jetson-pab-carrier-v3/micro-usb-console.md
---

# USB-C Console

Plugged into a host PC, the Jetson enumerates as one USB composite device (`0955:7020`) providing four functions:

| Function | Host sees |
| -------- | --------- |
| RNDIS + CDC-NCM networking | Two USB Ethernet interfaces; Jetson at `192.168.55.1` |
| CDC-ACM serial | Virtual COM port with a login console |
| Mass storage | `L4T-README` drive |

## Serial Console

Use the `by-id` path — the `ttyACM` number changes between sessions:

```bash
ls -l /dev/serial/by-id/
usb-NVIDIA_Linux_for_Tegra_1613223640377-if02 -> ../../ttyACM1
```

```bash
screen /dev/serial/by-id/usb-NVIDIA_Linux_for_Tegra_*-if02 115200
```

Log in with your username and password (default `jetson` / `jetson`). Your user must be in the `dialout` group.

On macOS the port is `/dev/tty.usbmodem*`; on Windows it is a `COMx` port in Device Manager.

{% hint style="info" %}
This is not a boot console. The gadget (`nv-l4t-usb-device-mode.service`) and login prompt (`serial-getty@ttyGS0.service`) start under `multi-user.target`, so there is no UEFI, bootloader, or early kernel output — and no port at all if boot hangs before that point. For boot-level debugging use UART2 (`/dev/ttyTHS2`), see [Connections](connections.md).
{% endhint %}

## Connecting to WiFi from the Command Line

Scan for networks:

```bash
sudo nmcli device wifi
```

Connect to a network:

```bash
sudo nmcli device wifi connect 'SSID' password 'PASSWORD'
```

## Sharing Your PC's Internet over USB

The kernel repo ships a helper that NATs the Jetson's traffic out through your host PC's WiFi — see [share\_wifi.sh](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/scripts/share_wifi.sh).
