# Firmware

{% file src="../../.gitbook/assets/92-1.16.3c45b562.uavcan.bin" %}
ARK DIST Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_dist_canbootloader (1).bin" %}
ARK DIST Bootloader
{% endfile %}

## Source

Firmware is the PX4 cannode build for this board:

* [`boards/ark/dist`](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/dist) in [PX4-Autopilot](https://github.com/PX4/PX4-Autopilot)
* Targets: `ark_dist_default`, `ark_dist_canbootloader`

[ARK-Electronics/ARK_DIST](https://github.com/ARK-Electronics/ARK_DIST) has hardware and case files only.

## Release Notes

* 92-1.16.3c45b562 - 2025-9-26
  * Migrate to build server
* 92-1.16.e448eba4 - 2025-8-8
  * Initial Release
