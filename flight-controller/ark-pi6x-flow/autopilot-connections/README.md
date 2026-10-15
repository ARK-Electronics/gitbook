# Autopilot Connections

There are two direct board-to-board links between the Pi and the flight controller: USB and serial.

| Type | Pi device path | Flight controller |
|------|----------------|-------------------|
| USB | `/dev/ttyACM0` | USB |
| Serial | `/dev/ttyAMA4` (CM4), `/dev/ttyAMA3` (CM5) | TELEM2 |

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on serial. ARK-OS runs MAVLink on USB by default; enable **dds-agent** on the ARK-UI **Services** page for XRCE-DDS. See [Services](../../../ark-os/services.md).
{% endhint %}

## USB

The flight controller sits behind the board's full-speed (12 Mbps) USB hub, shared with the USB-C and USB JST-GH ports. Plugging a cable into the programming micro USB disconnects the hub until the Pi reboots. See [USB](../hardware.md#usb).

For the flight controller's USB to enumerate, its VBUS\_SENSE pin (Pi GPIO27) must be driven high. This is set in `config.txt` at boot.

## Serial

TELEM2 on the flight controller is wired to Pi UART4 (`/dev/ttyAMA4`) on a CM4 and to UART3 (`/dev/ttyAMA3`) on a CM5, tested to 3 Mbps. ARK-OS's dds-agent defaults to `/dev/ttyAMA4`; on a CM5, change its device on the ARK-UI **Services** page, and again after an ARK-OS upgrade. PX4 doesn't start its DDS client on TELEM2 by default: set `UXRCE_DDS_CFG` and `SER_TEL2_BAUD` as listed in [Services](../../../ark-os/services.md). When running MAVLink on TELEM2, set flow control to off: [MAV\_x\_FLOW\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL) = 0.

## Ground Station

ARK-OS serves MAVLink on UDP port 14550. In QGroundControl, add a UDP comm link with server `pi6x.local:14550`; in Mission Planner, connect with **UDPCl** to the same address.

## Flight Controller Reset

The Pi can hard-reset the flight controller via the reset signal on GPIO25. The reset is gated by the nARMED signal — the Pi cannot reset the flight controller while it is armed.

ARK-OS ships two reset helpers on `PATH`:

```bash
reset_fmu_fast.py       # reset and boot straight into the application
reset_fmu_wait_bl.py    # reset and wait in the bootloader (for firmware flashing)
```
