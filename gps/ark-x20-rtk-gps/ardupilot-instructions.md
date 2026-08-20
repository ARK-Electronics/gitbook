# ArduPilot Instructions

AP\_Periph support for the ARK X20 RTK GPS is in review — [ArduPilot PR #33941](https://github.com/ArduPilot/ardupilot/pull/33941) adds the `ARK_X20_GPS` target (board ID 89). Until it merges there are no prebuilt binaries on the ArduPilot firmware server.

## Testing the WIP Firmware

Build AP\_Periph from the PR branch:

```bash
./waf configure --board ARK_X20_GPS
./waf AP_Periph
```

Flash it using either method:

* **Over CAN** — upload `AP_Periph.apj` with the DroneCAN GUI Tool, see our [DroneCAN GUI Tool Guide](../../knowledge-base/dronecan-gui-tool-guide.md). Then set `FLASH_BOOTLOADER` to `1` in the node's parameters so future updates use the AP\_Periph bootloader.
* **Over SWD** — flash the combined `AP_Periph_with_bl.hex` with an ST-LINK on the 6-pin debug connector, see the [ST-LINK Flashing Guide](../../knowledge-base/st-link-flashing-guide.md).

## Configuration

With AP\_Periph running, configuration is identical to the [ARK RTK GPS ArduPilot instructions](../ark-rtk-gps/ardupilot-instructions.md) — both the single GPS and dual GPS heading setups. Moving baseline heading requires X20P receiver firmware 2.10 or later.
