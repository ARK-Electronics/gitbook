---
description: Flash PX4 or ArduPilot firmware on a USB-connected flight controller.
---

# Updating the Flight Controller Firmware

The Just a Jetson has no onboard flight controller, but ARK-OS can flash one connected over USB.

## From the Web UI

Open the [ARK-UI](http://jetson.local) **Autopilot** page, select the **Firmware** tab, and upload a `.px4` or `.apj` firmware file.

<figure><img src="../../.gitbook/assets/ark-ui-autopilot-firmware.png" alt=""><figcaption></figcaption></figure>

## From the Command Line

SSH into the Jetson and run the ARK-OS flashing tool (on `PATH`):

```bash
flash_firmware.sh <firmware.px4>
```

## Firmware Binaries

* **PX4**: [PX4 releases page](https://github.com/PX4/PX4-Autopilot/releases/)
* **ArduPilot**: [firmware.ardupilot.org](https://firmware.ardupilot.org/)
