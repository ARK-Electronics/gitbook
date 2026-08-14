# Autopilot Connections

There are two communication channels between the Jetson and the flight controller: USB and serial. Both are direct board-to-board connections tested up to 3 Mbps.

| Type   | Jetson device path | Flight Controller |
| ------ | ------------------ | ----------------- |
| USB    | /dev/ttyACM0       | USB               |
| Serial | /dev/ttyTHS1       | Telem2            |

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on serial. ARK-OS's defaults do exactly this — see [Services](../../../../ark-os/services.md).
{% endhint %}

## USB

The flight controller's USB connection is muxed with the external Micro USB port. While a Micro USB cable is connected, the flight controller is disconnected from the Jetson. After unplugging, reboot the Jetson to restore the connection.

<figure><img src="../../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

For the flight controller's USB to enumerate, its VBUS\_SENSE pin must be driven high by the Jetson. This is set in the Jetson pinmux at boot, so it works out of the box.

## Serial

The serial connection is Jetson UART1 (`/dev/ttyTHS1`) to **Telem2** on the flight controller, tested to 3 Mbps. When running MAVLink on Telem2, set flow control to off: [MAV\_x\_FLOW\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL) = 0.

## Flight Controller Reset

The Jetson can hard-reset the flight controller via a GPIO reset line. The reset is gated by the nARMED signal — the Jetson cannot reset the flight controller while it is armed.

ARK-OS ships two reset helpers on `PATH`:

```bash
reset_fmu_fast.py       # reset and boot straight into the application
reset_fmu_wait_bl.py    # reset and wait in the bootloader (for firmware flashing)
```
