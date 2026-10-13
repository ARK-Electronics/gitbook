# ArduPilot Instructions

Connect the ARK MAG to the flight controller's CAN port as described in [Wiring](hardware.md#wiring).

## Flight Controller Parameters

### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver-index-of-virtual-driver-to-be-used-with-physical-can-interface) | 1 | Enable CAN port 1 driver |
| [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol-enable-use-of-specific-protocol-over-virtual-driver) | 1 | Set protocol to DroneCAN |
| [COMPASS\_ENABLE](https://ardupilot.org/copter/docs/parameters.html#compass-enable-enable-compass) | 1 | Enable the compass subsystem |

Reboot the flight controller. The magnetometer will appear as a DroneCAN compass and can be configured via the standard `COMPASS_*` parameters. See the [ArduPilot compass setup guide](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html) for calibration and configuration details.

## CAN Node Parameters

The node publishes magnetometer data with its default parameters (`CANNODE_PUB_MAG` is `1`). To terminate the bus or fix the node ID, see [Node Parameters](firmware.md#node-parameters).
