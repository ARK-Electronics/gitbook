---
metaLinks:
  alternates:
    - ../../ark-jetson-pab-carrier/autopilot-connections/
---

# Autopilot Connections

There are three communication channels between the Jetson and the flight controller: USB, serial, and Ethernet. USB and serial are direct board-to-board connections tested up to 3 Mbps; Ethernet runs through the onboard 100 Mbps switch.

| Type     | Jetson device path | Flight Controller |
| -------- | ------------------ | ----------------- |
| USB      | /dev/ttyACM0       | USB               |
| Serial   | /dev/ttyTHS1       | Telem2            |
| Ethernet | enP8p1s0           | eth0              |

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on serial. ARK-OS's defaults do exactly this — see [Services](../ark-services/services.md).
{% endhint %}

## USB

For the flight controller's USB to enumerate, its VBUS\_SENSE pin must be driven high by the Jetson. This is set in the Jetson pinmux at boot, so it works out of the box.

## Serial

The serial connection is Jetson UART1 (`/dev/ttyTHS1`) to **Telem2** on the flight controller, tested to 3 Mbps. When running MAVLink on Telem2, set flow control to off: [MAV\_x\_FLOW\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL) = 0.

## Ethernet

The flight controller and Jetson are connected through a 100 Mbps switch on the board, along with two external connections: the 4-pin JST-GH Ethernet connector and the Pixhawk Payload Bus FFC.

To set up the flight controller side, follow the [PX4 Ethernet guide](https://docs.px4.io/main/en/advanced_config/ethernet_setup) or the [ArduPilot network guide](https://ardupilot.org/copter/docs/common-network.html). If one of the external connections leads to a router running DHCP, both the Jetson and flight controller get addresses from it; otherwise configure static IPs on both ends.

## Flight Controller Reset

The Jetson can hard-reset the flight controller via a GPIO reset line. The reset is gated by the nARMED signal — the Jetson cannot reset the flight controller while it is armed.

ARK-OS ships two reset helpers on `PATH`:

```bash
reset_fmu_fast.py       # reset and boot straight into the application
reset_fmu_wait_bl.py    # reset and wait in the bootloader (for firmware flashing)
```
