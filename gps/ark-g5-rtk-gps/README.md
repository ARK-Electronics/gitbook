---
cover: ../../.gitbook/assets/IMG_5857_edited.JPG
coverY: 0
---

# ARK G5 RTK GPS

[ARK G5 RTK GPS](https://arkelectron.com/product/ark-g5-rtk-gps/) · [ARK G5H RTK Heading GPS](https://arkelectron.com/product/ark-g5-rtk-heading-gps/)

## G5 vs G5H

The ARK G5 RTK GPS and the ARK G5H RTK GPS share the same PCB design but use different Septentrio G5 modules. The G5 uses the P3 and the G5H uses the P3H. Note that the G5/P3 only support a single antenna and the ANT2 connector is not active.

## DroneCAN Messages

The ARK G5 / G5H RTK GPS publishes:

* GNSS solution: [`uavcan.equipment.gnss.Fix2`](../../knowledge-base/dronecan-messages.md#fix2) and [`uavcan.equipment.gnss.Auxiliary`](../../knowledge-base/dronecan-messages.md#gnss-auxiliary)
* IMU: [`uavcan.equipment.ahrs.RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) (when `CANNODE_PUB_IMU=1`)
* GPS heading (G5H only, when [dual-antenna heading is enabled](ardupilot-instructions.md#dual-antenna-heading-configuration-g5h-only)): [`ardupilot.gnss.RelPosHeading`](../../knowledge-base/dronecan-messages.md#relposheading)

Like every DroneCAN node it also emits [`NodeStatus`](../../knowledge-base/dronecan-messages.md#nodestatus) and responds to [`GetNodeInfo`](../../knowledge-base/dronecan-messages.md#getnodeinfo).

See [DroneCAN Messages](../../knowledge-base/dronecan-messages.md) for full message definitions.

## Firmware

Follow the steps for updating the firmware through the flight controller.

{% embed url="https://docs.px4.io/main/en/dronecan/#firmware-update" %}

See the latest firmware below.

{% file src="../../.gitbook/assets/91-1.16.c8403786.uavcan.bin" %}
ARK G5 RTK GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_g5-gps_canbootloader.bin" %}
ARK G5 RTK GPS Bootloader
{% endfile %}

## Release Notes

* 91-1.16.c8403786 - 2026-2-12
  * Septentrio sensor\_gnss\_relative
  * General heading improvement
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
50: 50 ms\
100: 100 ms\
200: 200 ms\
500: 500 ms

#### SEP\_DUAL\_ANT (bitmask)

Configures the receiver frontend for dual antenna operation, enabling GNSS-based heading. Requires a heading-capable module (e.g. mosaic-G5 P3H or P6) with two antennas connected. Fixed ambiguities provide the highest accuracy. Float ambiguities are less accurate but more robust. Set both for Fixed+Float (receiver will use best available).

bit:\
0: Fixed\
1: Float\
default: 3

#### SEP\_PVT\_MODE (bitmask)

Bitmask of allowed PVT modes for Rover operation. The receiver will use the most accurate mode available.

bit:\
0: StandAlone\
1: DGNSS\
2: RTKFloat\
3: RTKFixed\
default: 15

#### SEP\_RCV\_DYN (enum)

Configures the receiver dynamics model to match the expected motion profile of the vehicle.

values:\
0: Static\
1: Quasistatic\
2: Pedestrian\
3: Automotive\
4: RaceCar\
5: HeavyMachinery\
6: UAV\
7: Unlimited\
default: 6

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
2. Launch RxControl
3. Connect to the module on the USB serial connection\
   ![](<../../.gitbook/assets/image (70).png>)
4. Under File, select "Upgrade Receiver using Current Connection"\
   ![](<../../.gitbook/assets/image (71).png>)
5. Select the SUF firmware file downloaded from [Septentrio's website](https://www.septentrio.com/en/products/gnss-receivers/gnss-receiver-modules/mosaic-G5-P3#resources)\
   ![](<../../.gitbook/assets/image (72).png>)
6. Run the upgrade
