---
description: >-
  Flashing firmware over SWD, CAN, or a PX4 flight controller, plus the debug
  console and status LEDs.
---

# Firmware

The ARK 12S CAN ESC runs ARK32 with a DroneCAN interface. The build target is `ARK_G431_CAN`.

Two images live in flash: a bootloader at the start of flash and the application above it. The bootloader is what makes updates over CAN possible, so leave it in place unless you are deliberately recovering a board.

{% hint style="warning" %}
Remove the propeller before powering the ESC on the bench. Several of the procedures below power the motor stage.
{% endhint %}

***

## Flashing over SWD

Use this for first bring up, for loading a factory image, or to recover a board that no longer appears on the CAN bus.

Connect an ST-LINK to J3:

| ST-LINK         | J3 Pin |
| --------------- | ------ |
| SWDIO           | 4      |
| SWCLK           | 5      |
| GND             | 6      |
| 3.3V (optional) | 1      |

{% hint style="danger" %}
Do not connect the ST-LINK 3.3V line while the ESC is powered from a battery or bench supply. Connect SWDIO, SWCLK, and GND only.
{% endhint %}

Flash the combined **factory image** to `0x08000000`. It contains the bootloader, padding up to the application offset, the application itself, and the EEPROM defaults, so one write leaves the ESC in the state it ships in.

| Region      | Address              |
| ----------- | -------------------- |
| Bootloader  | `0x08000000`         |
| Application | Above the bootloader |
| EEPROM      | `0x0801F800`         |

{% hint style="danger" %}
Do not write a bare application binary to `0x08000000`. It overwrites the bootloader. The flashing tool reports success, but the ESC will not appear on the CAN bus and cannot be updated over CAN afterwards. Recover by flashing the factory image over SWD.
{% endhint %}

For ST-LINK setup, udev rules, and command line invocations, see the [ST-LINK Flashing Guide](../../../knowledge-base/st-link-flashing-guide.md).

***

## Updating from a PX4 Flight Controller

PX4 flashes DroneCAN nodes automatically at boot. This is the least equipment intensive method — it needs nothing beyond the flight controller and its SD card.

{% hint style="danger" %}
**Disable the actuator outputs before flashing.** An ESC that is receiving actuator commands will not accept firmware. A zero throttle command still counts — idle is not the same as no command, and an ESC sitting at zero input will silently stay on its old firmware.
{% endhint %}

1. **Disable the ESC outputs.** Either unassign the DroneCAN ESC outputs under _Vehicle Setup > Actuators_, or set [UAVCAN\_ENABLE](https://docs.px4.io/main/en/advanced_config/parameter_reference.html#UAVCAN_ENABLE) to `2`, which keeps dynamic node allocation and firmware update working without driving ESC outputs.
2. Copy the firmware binary to the root of the flight controller's SD card.
3. Power cycle the vehicle and wait for the update to finish.
4. **Restore the outputs.** Set `UAVCAN_ENABLE` back to `3` and re-assign the actuator outputs.

On boot PX4 reads the board ID from the metadata block embedded in the binary, moves the file to `/fs/microsd/ufw/`, and deletes it from the SD card root. The file name does not matter — only the embedded metadata is used to match the file to the node.

{% hint style="warning" %}
The flight controller must have an SD card installed. PX4 uses it for both dynamic node allocation and CAN firmware update — without one the ESC is never assigned a node ID and will not appear on the bus.
{% endhint %}

{% hint style="info" %}
The firmware stays in `/fs/microsd/ufw/` and PX4 re-flashes any matching ESC on the bus whose firmware differs from it. This keeps a replacement ESC in sync automatically, but it also means you must clear that file before flashing a different version by any other method.
{% endhint %}

{% hint style="info" %}
For remote or scripted updates, upload to `/fs/microsd/ufw_staging/` instead. PX4 moves the file into `/fs/microsd/ufw/` on the next boot, which avoids write conflicts if the file lands while the vehicle is running.
{% endhint %}

### If the Update Never Starts

Work through these in order:

* ESC outputs are still enabled and the ESC is receiving commands — the most common cause.
* No SD card in the flight controller, or the binary was left in `/fs/microsd/ufw/` from a previous update at the same version.
* `UAVCAN_ENABLE` is `0` or `1`, so the node is never allocated an ID.

***

## Updating with the DroneCAN GUI Tool

Use this when the ESC is not connected to a PX4 flight controller, or when you want to flash a single ESC directly. You need:

* A USB-to-CAN adapter that supports SLCAN, such as the Zubax Babel, on the same CAN bus. PX4 cannot expose its own CAN bus to the tool — see the _ArduPilot - Flight Controller as CAN Interface_ section of the [DroneCAN GUI Tool Guide](../../../knowledge-base/dronecan-gui-tool-guide.md) for the ArduPilot alternative.
* A dynamic node ID allocation server on the bus. Either a flight controller with `UAVCAN_ENABLE` set to `2` or `3`, or the DroneCAN GUI Tool's own allocation server, started with the rocket icon in the tool's main window.

Upload the firmware binary to the node — see the [DroneCAN GUI Tool Guide](../../../knowledge-base/dronecan-gui-tool-guide.md) for connection and upload steps.

{% hint style="warning" %}
If a flight controller is on the same bus acting as the allocation server, disable its ESC outputs first. The ESC will not accept firmware while it is being commanded, whichever tool is doing the flashing.
{% endhint %}

{% hint style="warning" %}
If the flight controller still has firmware in `/fs/microsd/ufw/`, it will re-flash the ESC on the next boot and undo the update. Clear that file from the SD card first.
{% endhint %}

***

## ARK32 Configurator

[https://ark32.arkelectron.com](https://ark32.arkelectron.com)

The ARK32 Configurator is the web tool for reading and writing ESC settings and for updating firmware. Use it to check what version an ESC is running, adjust the protection and ramp settings, and restore defaults.

{% hint style="warning" %}
A restore to defaults returns the ESC to the protection envelope it shipped with, not to the configurator's own disabled defaults. Confirm the current and temperature limits after any restore.
{% endhint %}

### Shipped Protection Defaults

| Setting                    | Default |
| -------------------------- | ------- |
| Current limit              | 200A    |
| Temperature foldback onset | 105°C   |
| Temperature derate band    | 15°C    |

These are firmware limits and they sit well below the hardware overcurrent trip. Foldback reduces power progressively across the derate band rather than cutting output abruptly.

***

## Status LEDs

The ESC has red, green, and blue LEDs driven directly by the microcontroller.

{% hint style="info" %}
Pattern meanings are still being finalised in firmware. Until they are published, use the debug console below for fault detail — it names the fault directly rather than encoding it in a blink pattern.
{% endhint %}

***

## Debug Console

The console comes out on **J3 pin 2 at 115200 baud, 8N1**. It is transmit only — the ESC prints, it does not accept commands. Connect J3 pin 2 to your adapter's RX and J3 pin 6 to GND.

On startup the ESC prints a banner identifying the firmware and the console configuration. After that it prints two kinds of line:

* **State transitions** — `esc: <from> -> <to>`
* **Faults and events** — `fault: <name>`

### Event Names

| Name          | Meaning                                                          |
| ------------- | ---------------------------------------------------------------- |
| `boot`        | Firmware started                                                 |
| `nFAULT`      | Gate driver fault, unclassified                                  |
| `nFAULT UVLO` | Gate driver fault with a low bus voltage — undervoltage class    |
| `nFAULT OCP`  | Gate driver fault with high current or drive — overcurrent class |
| `nFAULT OTW`  | Gate driver fault with high temperature — overtemperature class  |
| `stuck`       | Rotor is not turning when it should be                           |
| `LVC`         | Low voltage cutoff reached                                       |
| `signal_lost` | Input signal lost                                                |
| `desync`      | Commutation lost sync with the rotor                             |
| `acq_desync`  | Sync lost during acquisition, before closed loop                 |
| `stall`       | Motor stalled                                                    |
| `gd_wake`     | Gate driver woken from sleep                                     |
| `gd_sleep`    | Gate driver put to sleep on idle                                 |

A queue overflow line means events were produced faster than the console could drain them, and some were dropped. It does not indicate a motor fault.

{% hint style="info" %}
The three `nFAULT` classes are the firmware's interpretation of a single gate driver fault line, cross referenced against bus voltage, current, and temperature at the moment the fault arrived. Treat the class as a strong hint rather than a definitive diagnosis, and check the plain `nFAULT` case against the bench conditions.
{% endhint %}
