# Autopilot Connections

There are two primary communication channels between the VOXL and the Flight Controller: Serial and USB.

<table><thead><tr><th width="138">Type</th><th width="189">VOXL</th><th>Flight Controller</th></tr></thead><tbody><tr><td>USB</td><td>USB</td><td>USB</td></tr><tr><td>Serial</td><td>UART13</td><td>Telem2</td></tr></tbody></table>

{% hint style="info" %}
We recommend running MAVLink on USB and XRCE-DDS on Serial.
{% endhint %}

## Flight Controller USB Enable

The flight controller USB will not start until GPIO\_154\_VBUS\_SENSE from the VOXL is driven high. If this signal is high when the flight controller is reset, it will wait in the bootloader for 5 seconds before booting. If it is low, the flight controller will boot immediately.

## Flight Controller Reset

The flight controller can be hard reset using the reset signal connected to VOXL pin GPIO\_153\_FMU\_RST\_REQ. The VOXL cannot reset the flight controller while it is armed. The reset signal is gated by the nARMED signal from the flight controller.
