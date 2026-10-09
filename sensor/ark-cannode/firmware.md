# Firmware

ARK CANnode runs the [PX4 DroneCAN Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html). As such, it supports firmware update over the CAN bus and [dynamic node allocation](https://docs.px4.io/main/en/dronecan/#node-id-allocation). It can also run [ArduPilot AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) firmware; see [ArduPilot Firmware](#ardupilot-firmware).

## Updating

To flash the application firmware you can use the SD card method as [documented here](https://docs.px4.io/main/en/dronecan/#firmware-update) or you can use the DroneCAN GUI Tool and a USB-to-CAN adaptor to flash the firmware directly.

## Downloads

{% file src="../../.gitbook/assets/83-1.18.d1f97771.uavcan.bin" %}
ARK CANnode Firmware
{% endfile %}

{% file src="../../.gitbook/assets/ark_cannode_canbootloader.bin" %}
ARK CANnode Bootloader
{% endfile %}

## Building and Flashing over SWD

ARK CANnode boards ship with recent firmware pre-installed, but if you want to build and flash the latest firmware yourself see [PX4 DroneCAN Firmware > Building the Firmware](https://docs.px4.io/main/en/dronecan/px4_cannode_fw.html#building-the-firmware).

### Building the Application

```
make ark_cannode
```

### Building the Bootloader

```
make ark_cannode_canbootloader
```

### Flashing the Bootloader

To flash the bootloader firmware you need an ST-LINK programmer. See the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md) for setup instructions.

```
st-flash write <bootloader_binary_path> 0x08000000
```

### Flashing the Application

If you flash the application over SWD instead of over CAN, it goes at the application offset — `0x08000000` is the bootloader's address:

```
st-flash write <application_binary_path> 0x08010000
```

## ArduPilot Firmware

For flight controller setup with AP\_Periph, see [ArduPilot Instructions](ardupilot-instructions.md).

### Flashing over CAN

Flash the ARK CANnode with AP\_Periph firmware using the DroneCAN GUI Tool. See the [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md) for detailed instructions on connecting and uploading firmware.

1. Download the latest AP\_Periph firmware for the ARK CANnode from [firmware.ardupilot.org/AP\_Periph](https://firmware.ardupilot.org/AP_Periph/)
2. Connect the CANnode to the flight controller's CAN bus
3. Open the DroneCAN GUI Tool
4. Double-click the CANnode in the node list
5. Click **Update Firmware** and select the `.bin` AP\_Periph firmware file

### Flashing over SWD

If the CANnode has no bootloader and does not show up on the CAN bus, flash it with an ST-LINK using the combined bootloader + application image:

```bash
st-flash --format ihex write AP_Periph_with_bl.hex
```

Do not write `AP_Periph.bin` to `0x08000000` — the bootloader lives there and the application starts at `0x08010000`. See [Flashing DroneCAN Nodes](../../knowledge-base/st-link-flashing-guide.md#flashing-dronecan-nodes) for details.

### Building

Application:

```
./waf configure --board ARK_CANNODE
./waf AP_Periph
```

Bootloader:

```
./waf configure --board ARK_CANNODE --bootloader
./waf bootloader
```

The bootloader can also be updated from the running AP\_Periph firmware by setting `FLASH_BOOTLOADER = 1` on the CANnode via the DroneCAN GUI Tool.

The hardware definition can be found here: [https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP\_HAL\_ChibiOS/hwdef/ARK\_CANNODE](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_HAL_ChibiOS/hwdef/ARK_CANNODE)

## Node Parameters

These apply to the PX4 DroneCAN firmware. Set them on the CANnode, then reboot it. Use [QGroundControl](https://docs.px4.io/main/en/dronecan/#qgc-cannode-parameter-configuration), where each CAN node is a separate _Component X_ under **Vehicle Settings > Parameters**, or the [DroneCAN GUI Tool](../../knowledge-base/dronecan-gui-tool-guide.md).

| Parameter | Default | Description |
|-----------|---------|-------------|
| [CANNODE\_TERM](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_TERM) | 0 | Enable the built-in CAN bus termination resistor. Set to `1` only if this device is the last node on the CAN bus |
| `CANNODE_NODE_ID` | 0 | Fixed node ID (1–125). `0` uses dynamic node allocation |
| [CANNODE\_PUB\_IMU](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#CANNODE_PUB_IMU) | 0 | Set to `1` to publish `RawIMU` messages from the onboard IMU. PX4 also needs `UAVCAN_SUB_IMU` set to `1` |
| `CANNODE_PUB_MAG` | 1 | Publish data from a connected magnetometer. External magnetometers are detected at boot |
| `CANNODE_PUB_BAR` | 1 | Publish data from a connected barometer |
| `SENS_EN_*` | 0 | Start the driver for an external I2C or SPI sensor, for example `SENS_EN_SDP3X` for a Sensirion SDP3x airspeed sensor |
| `SYS_BL_UPDATE` | 0 | Set to `1` to rewrite the CAN bootloader from the running firmware. The flight controller logs `bootloader updated`, `bootloader unchanged` or `bootloader update failed`, and the parameter returns to `0`. Firmware built before October 2026 lacks this parameter |

PWM output parameters (`PWM_MAIN_*`, `DSHOT_TEL_CFG`) are set per use case; see [CANnode as PWM Expander](px4-instructions.md#cannode-as-pwm-expander).

## Release Notes

* 83-1.18.d1f97771 - 2026-10-3
  * PX4 v1.18 base
  * SCH16T driver built in
  * Bootloader update from the running firmware (`SYS_BL_UPDATE`)
