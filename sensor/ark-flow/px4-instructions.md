# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/dronecan/ark_flow.html" %}
Most up to date PX4 Documentation
{% endembed %}

### Hardware Setup <a href="#hardware-setup" id="hardware-setup"></a>

#### Wiring <a href="#wiring" id="wiring"></a>

The ARK Flow is connected to the CAN bus using a Pixhawk standard 4 pin JST GH cable. For more information, refer to the [CAN Wiring](https://docs.px4.io/main/en/can/#wiring) instructions.

#### Mounting <a href="#mounting" id="mounting"></a>

The recommended mounting orientation is with the connectors on the board pointing towards **back of vehicle**, as shown in the following picture.

![ARK Flow align with Pixhawk](https://docs.px4.io/main/assets/ark_flow_orientation.auMVvxJ0.png)

This corresponds to the default value (`0`) of the parameter [SENS\_FLOW\_ROT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_ROT). Change the parameter appropriately if using a different orientation.

The sensor can be mounted anywhere on the frame, but you will need to specify the focal point position, relative to vehicle centre of gravity, during [PX4 configuration](https://docs.px4.io/main/en/dronecan/ark_flow.html#px4-configuration).

### Firmware Setup <a href="#firmware-setup" id="firmware-setup"></a>

ARK Flow runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation).

ARK Flow boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

* Firmware target: `ark_can-flow_default`
* Bootloader target: `ark_can-flow_canbootloader`

### Flight Controller Setup <a href="#flight-controller-setup" id="flight-controller-setup"></a>

{% hint style="info" %}
The ARK Flow will not boot if there is no SD card in the flight controller when powered on.
{% endhint %}

Connect the ARK Flow CAN to the flight controller's CAN port. Once parameters are set the module will be detected on boot. See [DroneCAN > Enabling DroneCAN](https://docs.px4.io/main/en/dronecan/#enabling-dronecan) for more detail.

### Flight Controller Parameters

Set the following in _QGroundControl_ and reboot the flight controller.

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) | 2 | Enable DroneCAN with dynamic node allocation (use `3` if also driving DroneCAN ESCs) |
| [EKF2\_OF\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_CTRL) | 1 | Enable optical flow fusion in the EKF |
| [UAVCAN\_SUB\_FLOW](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_FLOW) | 1 | Subscribe to DroneCAN optical flow messages |
| [UAVCAN\_SUB\_RNG](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_RNG) | 1 | Subscribe to DroneCAN range finder messages |
| [EKF2\_RNG\_A\_HMAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_A_HMAX) | 10 | Max range used by the EKF |
| [EKF2\_RNG\_QLTY\_T](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_RNG_QLTY_T) | 0.2 | Range finder quality time |
| [UAVCAN\_RNG\_MIN](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MIN) | 0.08 | Min reported range |
| [UAVCAN\_RNG\_MAX](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_RNG_MAX) | 30 | Max reported range |
| [SENS\_FLOW\_MINHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MINHGT) | 0.08 | Min height for optical flow fusion |
| [SENS\_FLOW\_MAXHGT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXHGT) | 25 | Max height for optical flow fusion |
| [SENS\_FLOW\_MAXR](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_MAXR) | 7.4 | Max angular flow rate (PAW3902 limit) |

#### Optional

| Parameter | Description |
|-----------|-------------|
| [UAVCAN\_SUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_SUB_IMU) | Set to `1` to subscribe to DroneCAN [`RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) messages. Requires `CANNODE_PUB_IMU` to also be set on the ARK Flow |
| [EKF2\_GPS\_CTRL](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_GPS_CTRL) | Set to `0` to disable GPS aiding (e.g. indoor flight) |
| [EKF2\_OF\_POS\_X](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_X) / [EKF2\_OF\_POS\_Y](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Y) / [EKF2\_OF\_POS\_Z](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#EKF2_OF_POS_Z) | ARK Flow offset from the vehicle center of gravity (meters) |
| [SENS\_FLOW\_ROT](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#SENS_FLOW_ROT) | Sensor rotation if mounted in a non-default orientation (default `0`) |

### CAN Node Parameters

Optical flow and range finder messages are published by the ARK Flow by default — no CAN node parameters are required for those streams.

Set the following on the sensor and reboot the node. CAN node parameters can be configured using either:

* [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration) — each CAN node appears as a separate _Component X_ entry under **Vehicle Settings > Parameters**.
* The [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

#### Optional

| Parameter | Description |
|-----------|-------------|
| `CANNODE_TERM` | Set to `1` if this is the last node on the CAN bus |
| `CANNODE_PUB_IMU` | Set to `1` to publish [`RawIMU`](../../knowledge-base/dronecan-messages.md#rawimu) messages on the CAN bus. Pair with `UAVCAN_SUB_IMU` on the flight controller |
