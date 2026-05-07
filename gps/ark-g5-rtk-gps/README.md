---
cover: ../../.gitbook/assets/IMG_5857_edited.JPG
coverY: 0
---

# ARK G5 RTK GPS

[ARK G5 RTK GPS](https://arkelectron.com/product/ark-g5-rtk-gps/)

The ARK G5 RTK GPS is built around the Septentrio mosaic-G5 P3 module. The P3 only supports a single antenna and the ANT2 connector is not active. For dual antenna heading, see the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/README.md).

## DroneCAN Messages

The ARK G5 RTK GPS publishes:

* GNSS solution: [`uavcan.equipment.gnss.Fix2`](../../knowledge-base/dronecan-messages.md#fix2) and [`uavcan.equipment.gnss.Auxiliary`](../../knowledge-base/dronecan-messages.md#gnss-auxiliary)
* Magnetometer: [`uavcan.equipment.ahrs.MagneticFieldStrength2`](../../knowledge-base/dronecan-messages.md#magneticfieldstrength2)
* IMU: [`uavcan.equipment.ahrs.RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) (when `CANNODE_PUB_IMU=1`)

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
