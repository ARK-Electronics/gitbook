# Autopilot Connections

There are two primary communication channels between the Pi and the Flight Controller: Serial and USB. Both interfaces are direct board to board connections and have been tested up to 3Mbps.

<table><thead><tr><th width="138">Type</th><th width="189">Pi device path</th><th>Flight Controller</th></tr></thead><tbody><tr><td>USB</td><td> /dev/ttyACM0</td><td>USB</td></tr><tr><td>Serial</td><td>/dev/ttyAMA4</td><td>Telem2</td></tr></tbody></table>

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on Serial.
{% endhint %}

## USB

The Pi CM4 has one USB 2.0 OTG interface. It is muxed between the external Micro-USB port and a built in USB hub. The USB hub connects to the flight controller, USB C port, and the two USB JST-GH ports.&#x20;

<figure><img src="../../.gitbook/assets/Screenshot from 2024-10-08 16-42-38.png" alt=""><figcaption></figcaption></figure>

The USB connection to the autopilot is muxed with the external Pi micro USB port. When a micro USB cable is connected, the autopilot is disconnected from the Pi and the USB port on the Pi switches from host to device mode. After the micro USB cable is disconnected, a reboot is required to switch the USB port back to a host and connect to the autopilot and external ports.

For the USB port to be enabled on the ARKV6X flight controller, the VBUS\_SENSE pin must be driven high from the Pi. It is connected to pin GPIO27. There is a helper python script in ARK-OS to drive the pin high. \
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/vbus\_enable.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/vbus_enable.py)

## UART

The UART connection between Pi and the autopilot is on Pi UART4 which appears as **/dev/ttyAMA4** in Linux. This goes to **Telem2** on the Flight Controller. This connection has been tested to 3Mbps.&#x20;

Flow control needs to be set to "Force Off" when using Telem2 for MAVLINK. [MAV\_X\_FLOW\_CTRL ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL)set to "0".

## Flight Controller Reset

The flight controller can be hard reset using the reset signal connected to Pi pin GPIO25. The Pi cannot reset the flight controller while it is armed. The reset signal is gated by the nARMED signal from the flight controller.

There are a couple of helper scripts to reset the flight controller. One to drive the VBUS\_SENSE pin high before the reset to wait in the bootloader for 5 seconds. This is useful when updating the flight controller firmware and a hard reboot is needed. The other fast reset script drives the VBUS\_SENSE pin low before the reset to avoid the wait.\
\
Reset and wait in the bootloader\
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/reset\_fmu\_wait\_bl.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/reset_fmu_wait_bl.py)\
Reset quickly and skip the bootloader\
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/reset\_fmu\_fast.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/scripts/reset_fmu_wait_bl.py)
