---
cover: ../.gitbook/assets/IMG_5857_edited.JPG
coverY: 0
---

# ARK G5 RTK GPS

## G5 vs G5H

The ARK G5 RTK GPS and the ARK G5H RTK GPS share the same PCB design but use different Septentrio G5 modules. The G5 uses the P3 and the G5H uses the P3H. Note that the G5/P3 only support a single antenna and the ANT2 connector is not active.&#x20;

## DroneCAN

Please read through the PX4 Documentation for DroneCAN GPS parameter configuration.

{% embed url="https://docs.px4.io/main/en/dronecan/#gps" %}

## Firmware

Follow the steps for updating the firmware through the flight controller.&#x20;

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../.gitbook/assets/91-1.16.c53f8d8e.uavcan.bin" %}
ARK G5 RTK GPS Firmware
{% endfile %}

{% file src="../.gitbook/assets/ark_g5-gps_canbootloader.bin" %}
ARK G5 RTK GPS Bootloader
{% endfile %}

## Release Notes

* 91-1.16.c53f8d8e - 2025-12-18
  * Initial release

## Parameter Reference

#### SEP\_OFFS\_YAW (float)

Heading offset angle for dual antenna GPS setups that support heading estimation.\
Set this to 0 if the antennas are parallel to the forward-facing direction of the vehicle and the Rover/ANT2 antenna is in front.\
The offset angle increases clockwise.\
Set this to 90 if the ANT2 antenna is placed on the right side of the vehicle and the Moving Base/MAIN antenna is on the left side.

Default: 0\
Min: -360\
Max: 360\
Unit: degree

#### SEP\_OFFS\_PITCH (float)

Vertical offsets can be compensated for by adjusting the Pitch offset.\
Note that this can be interpreted as the "roll" angle in case the antennas are aligned along the perpendicular axis. This occurs in situations where the two antenna ARPs may not be exactly at the same height in the vehicle reference frame. Since pitch is defined as the right-handed rotation about the vehicle Y axis, a situation where the main antenna is mounted lower than the aux antenna (assuming the default antenna setup) will result in a positive pitch.

Default: 0\
Min: -90\
Max: 90\
Unit: degree

#### SEP\_OUT\_RATE (enum)

Configures the output rate for GNSS data messages.

-1: OnChange\
&#x20;50: 50 ms\
100: 100 ms\
200: 200 ms\
500: 500 ms

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### USB C

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>2, 11</td><td>VBUS</td><td>5.0V</td></tr><tr><td>5, 8</td><td>USB_N</td><td>3.3V</td></tr><tr><td>6,7</td><td>USB_P</td><td>3.3V</td></tr><tr><td>1,12</td><td>GND</td><td>GND</td></tr></tbody></table>

#### GPS UART2 + Timepulse - 5 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>TXD2</td><td>3.3V</td></tr><tr><td>2</td><td>RXD2</td><td>3.3V</td></tr><tr><td>3</td><td>TIMEPULSE</td><td>3.3V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

## 3D Model

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_G5\_RTK\_GPS](https://github.com/ARK-Electronics/ARK_G5_RTK_GPS)

## Septentrio G5 Module Firmware Updating

The Septentrio G5 module firmware can be updated using the [Septentrio RxTools](https://www.septentrio.com/en/products/gps-gnss-receiver-software/rxtools) application.

1. Install [RxTools](https://www.septentrio.com/en/products/gps-gnss-receiver-software/rxtools)
2. &#x20;Launch RxControl
3. Connect to the module on the USB serial connection\
   ![](<../.gitbook/assets/image (70).png>)
4. Under File, select "Upgrade Receiver using Current Connection"\
   ![](<../.gitbook/assets/image (71).png>)
5. Select the SUF firmware file downloaded from [Septentrio's website](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3#resources)\
   ![](<../.gitbook/assets/image (72).png>)
6. Run the upgrade

