# Autopilot Connections

There are two communication channels between the Pi and the flight controller: USB and serial. Both are direct board-to-board connections tested up to 3 Mbps.

<table><thead><tr><th width="138">Type</th><th width="189">Pi device path</th><th>Flight Controller</th></tr></thead><tbody><tr><td>USB</td><td> /dev/ttyACM0</td><td>USB</td></tr><tr><td>Serial</td><td>/dev/ttyAMA4</td><td>Telem2</td></tr></tbody></table>

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on serial. ARK-OS's defaults do exactly this — see [Services](../ark-services/services.md).
{% endhint %}

## USB

The Pi CM4 has one USB 2.0 OTG interface, muxed between the external Micro USB port and an onboard USB hub. The hub connects the flight controller, the USB-C port, and the two USB JST-GH ports.

<figure><img src="../../../.gitbook/assets/Screenshot from 2024-10-08 16-42-38.png" alt=""><figcaption></figcaption></figure>

While a Micro USB cable is connected, the Pi switches to USB device mode and the flight controller (and all hub ports) are disconnected. After unplugging, reboot the Pi to restore them.

For the flight controller's USB to enumerate, its VBUS\_SENSE pin (Pi GPIO27) must be driven high. This is set in `config.txt` at boot, so it works out of the box.

## Serial

The serial connection is Pi UART4 (`/dev/ttyAMA4`) to **Telem2** on the flight controller, tested to 3 Mbps. When running MAVLink on Telem2, set flow control to off: [MAV\_x\_FLOW\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL) = 0.

## Flight Controller Reset

The Pi can hard-reset the flight controller via the reset signal on GPIO25. The reset is gated by the nARMED signal — the Pi cannot reset the flight controller while it is armed.

ARK-OS ships two reset helpers on `PATH`:

```bash
reset_fmu_fast.py       # reset and boot straight into the application
reset_fmu_wait_bl.py    # reset and wait in the bootloader (for firmware flashing)
```
