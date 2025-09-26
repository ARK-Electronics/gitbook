# Autopilot Connections

There are two primary communication channels between the Jetson and the Flight Controller: Serial and USB. Both interfaces are direct board to board connections and have been tested up to 3Mbps.

| Type   | Jetson device path | Flight Controller  |
| ------ | ------------------ | ------------------ |
| USB    | /dev/ttyACM0       | USB                |
| Serial | /dev/ttyTHS1       | Telem2             |

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on Serial.
{% endhint %}

## USB

The USB connection to the autopilot is muxed with the external Jetson micro USB port. When a micro USB cable is connected, the autopilot is disconnected from the Jetson and the USB port on the Jetson switches from host to device mode. After the micro USB cable is disconnected, a reboot is required to switch the USB port back to a host and connect to the autopilot.\


<figure><img src="../../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

For the USB port to be enabled on the ARKV6X flight controller, the VBUS\_SENSE pin must be driven high from the Jetson. It is connected to pin 206 GPIO07. For Jetpack 5, there is a helper python script in ARK-OS to drive the pin high. For Jetpack 6, a script cannot toggle a GPIO and leave it set. As a workaround, the VBUS\_SENSE pin is set high in the Jetson pinmux on boot. \
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/vbus\_enable.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/vbus_enable.py)

## UART

The UART connection between Jetson and the autopilot is on Jetson UART1 which appears as **/dev/ttyTHS0** in Jetpack 5 and **/dev/ttyTHS1** in Jetpack 6. This goes to **Telem2** on the Pixhawk Autopilot Bus. This connection has been tested to 3Mbps. Higher baud rates may be possible.

Flow control needs to be set to "Force Off" when using Telem2 for MAVLINK. [MAV\_X\_FLOW\_CTRL ](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#MAV_1_FLOW_CTRL)set to "0".

## Flight Controller Reset

The flight controller can be hard reset using the reset signal connected to Jetson pin 228 GPIO13. The Jetson cannot reset the flight controller while it is armed. The reset signal is gated by the nARMED signal from the flight controller.

There are a couple of helper scripts to reset the flight controller. One to drive the VBUS\_SENSE pin high before the reset to wait in the bootloader for 5 seconds. This is useful when updating the flight controller firmware and a hard reboot is needed. The other fast reset script drives the VBUS\_SENSE pin low before the reset to avoid the wait.\
\
Reset and wait in the bootloader\
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/reset\_fmu\_wait\_bl.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/reset_fmu_wait_bl.py)\
Reset quickly and skip the bootloader\
[https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/reset\_fmu\_fast.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/reset_fmu_wait_bl.py)
