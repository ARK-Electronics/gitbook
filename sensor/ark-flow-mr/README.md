---
cover: ../../.gitbook/assets/IMG_4086_Edited.JPG
coverY: 0
---

# ARK Flow MR

### Pinout

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### CAN - 4 Pin JST-GH

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>5V</td><td>5.0V</td></tr><tr><td>2</td><td>CAN_P</td><td>5.0V</td></tr><tr><td>3</td><td>CAN_N</td><td>5.0V</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>

#### Debug - 6 Pin JST-SH

<table><thead><tr><th width="153">Pin Number</th><th width="210">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>3.3V</td><td>3.3V</td></tr><tr><td>2</td><td>USART2_TX</td><td>3.3V</td></tr><tr><td>3</td><td>USART2_RX</td><td>3.3V</td></tr><tr><td>4</td><td>FMU_SWDIO</td><td>3.3V</td></tr><tr><td>5</td><td>FMU_SWCLK</td><td>3.3V</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

### Firmware

{% file src="../../.gitbook/assets/88-1.16.3c45b562.uavcan.bin" %}
ARK Flow MR Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_can-flow-mr_canbootloader (1).bin" %}
ARK Flow MR Bootloader
{% endfile %}

## Release Notes

* 88-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 88-1.16.afb2c08b - 2025-8-6
  * AFBRS50: Fix long range measurement publishing
* 88-1.16.2248a40e - 2025-7-10
  * [AFBRS40: fix Range Mode switching](https://github.com/PX4/PX4-Autopilot/pull/25185)
* 88-1.16.d0bfa548 - 2025-6-12
  * [AFBRS50 fix scheduling and refactor](https://github.com/PX4/PX4-Autopilot/pull/24837)
* 88-1.15.82ff8744- 2025-6-11
  * Add DroneCAN RawIMU publisher&#x20;
* 88-1.16.c8bed86b - 2025-2-26
  * Default to Long Range Mode (SENS\_AFBR\_MODE = 1)
  * Default to 5Hz output rate over 4m (SENS\_AFBR\_L\_RATE = 5)
* 88-1.16.61036f77 - 2025-2-7
  * Update to [AFBR 1.6.5 API](https://github.com/Broadcom/AFBR-S50-API/releases/tag/v1.6.5)
    * Improved distance sensor performance
  * Fix PAA3905 challenging surface detected spam
    * Only notify once every second
