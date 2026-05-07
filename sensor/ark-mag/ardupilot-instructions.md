# ArduPilot Instructions

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK MAG is connected to the CAN bus using a Pixhawk standard 4 pin JST-GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

Multiple sensors can be connected by plugging additional sensors into the ARK MAG’s second CAN connector.

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [CAN\_P1\_DRIVER](https://ardupilot.org/copter/docs/parameters.html#can-p1-driver-index-of-virtual-driver-to-be-used-with-physical-can-interface) | 1 | Enable CAN port 1 driver |
| [CAN\_D1\_PROTOCOL](https://ardupilot.org/copter/docs/parameters.html#can-d1-protocol-enable-use-of-specific-protocol-over-virtual-driver) | 1 | Set protocol to DroneCAN |
| [COMPASS\_ENABLE](https://ardupilot.org/copter/docs/parameters.html#compass-enable-enable-compass) | 1 | Enable the compass subsystem |

Reboot the flight controller. The magnetometer will appear as a DroneCAN compass and can be configured via the standard `COMPASS_*` parameters. See the [ArduPilot compass setup guide](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html) for calibration and configuration details.

### CAN Node Parameters

Set the following on the magnetometer and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CANNODE_PUB_MAG` | 1 | Publish magnetometer messages on the CAN bus |

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
