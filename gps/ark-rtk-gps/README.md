---
cover: ../../.gitbook/assets/ark_rtk_gps_1.jpg
coverY: 0
---

# ARK RTK GPS

Find additional documentation at [https://docs.px4.io/main/en/dronecan/ark\_rtk\_gps.html](https://docs.px4.io/main/en/dronecan/ark_rtk_gps.html)

Find 3D models and case files at [https://github.com/ARK-Electronics/ARK\_RTK\_GPS](https://github.com/ARK-Electronics/ARK_RTK_GPS)

## L1L5 Variant

The [ARK RTK GPS L1L5](https://arkelectron.com/product/ark-rtk-gps-l1-l5/) is a variant of the ARK RTK GPS built around the u-blox ZED-F9P-15B, which receives the L1/L5 bands instead of L1/L2. The L5 band improves resilience to interference and multipath.

{% hint style="info" %}
The L1L5 variant does **not** support moving baseline heading. For dual-GPS heading use the standard L1/L2 ARK RTK GPS, or see the [ARK G5H RTK Heading GPS](../ark-g5-rtk-heading-gps/README.md) for a dual-antenna solution.
{% endhint %}

Aside from the receiver, the L1L5 variant is identical to the standard ARK RTK GPS: it uses the same DroneCAN interface, onboard sensors, pinout, and firmware.

## Firmware

Follow the steps for updating the firmware through the flight controller — see [Firmware Update](px4-instructions.md#firmware-update) in the PX4 instructions.

If the node does not appear on the CAN bus — for example after a bad flash that erased the bootloader — recover it over SWD with an ST-LINK. See [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes).

The F9P receiver's own firmware is updated separately with u-center — see [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md).

See the latest firmware below.

{% file src="../../.gitbook/assets/82-1.18.76e683ea.uavcan.bin" %}
ARK RTK GPS Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-rtk-gps_canbootloader.bin" %}
ARK RTK GPS Bootloader
{% endfile %}

Node firmware 1.18 and later can rewrite its own CAN bootloader: set `SYS_BL_UPDATE` to `1` on the node. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`.

## Release Notes

* 82-1.18.76e683ea - 2026-10-3
  * PX4 v1.18 base
  * Fix the IMU not starting after some resets until the next power cycle
  * The antenna mounting for moving baseline heading is set on the flight controller (`GPS_YAW_OFFSET` removed), see [PX4 Instructions](px4-instructions.md#moving-baseline-gps-heading-configuration)
  * Moving base and rover run at 5 Hz
  * Fix timestamps from the receiver's time pulse
  * A moving baseline rover uses only its moving base's corrections
  * Receiver UART1 at 921600 baud
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
* 82-1.16.e68afe1e - 2025-2-12
  * Disable mag bias estimator by default

## LED Meanings

With the connectors at the bottom edge, the GNSS LEDs are on the right edge and the status LED (red, green and blue) is on the left edge. The GNSS LEDs are driven by the receiver; the status LED by the node firmware.

| GNSS LED | Meaning |
|-----|---------|
| Green, one flash per second | Receiver time pulse. Starts once the receiver has a fix. |
| Blue, blinking | Corrections received and in use, RTK Float |
| Blue, solid | RTK Fixed |

| Status LED | Meaning |
|-----|---------|
| Green, fast blink (10 Hz) | Node firmware running. It does not change with CAN traffic. |
| Green, slow blink (1 Hz) | Bootloader listening for CAN traffic |
| Blue, blinking (2 Hz) | Bootloader waiting for a node ID from the flight controller |
| Blue and green, blinking (3 Hz) | Bootloader waiting up to 3 s for the flight controller to start a firmware update |
| Red, green and blue together (3 Hz) | Firmware update in progress |
| Red, blinking | Firmware update error. 1 Hz: the flight controller returned a file error. 2 Hz: the flight controller stopped responding. 4 Hz: the image failed its CRC check. A failed update restarts the node after 20 s. |
| White, fast blink (10 Hz) | GPS passthrough, entered by holding the safety switch at power-up. See [u-blox Firmware Update](../../knowledge-base/ublox-firmware-update.md). |

Without valid firmware the node stays in the bootloader until the flight controller flashes it.

## Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### F9P UART2 - 3 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>F9P_TXD2</td><td>3.3V</td></tr><tr><td>2</td><td>F9P_RXD2</td><td>3.3V</td></tr><tr><td>3</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>
