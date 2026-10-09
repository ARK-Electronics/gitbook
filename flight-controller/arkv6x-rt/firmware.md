# Firmware

The board ships with PX4. Source and the build target live in [boards/ark/fmu-v6xrt](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/fmu-v6xrt).

| Firmware | Build target |
|----------|--------------|
| PX4 | `ark_fmu-v6xrt_default` |
| PX4 bootloader | `ark_fmu-v6xrt_bootloader` |

Rev 2.0 needs a build that recognizes FMUM revision 1. See [Hardware Type](px4-instructions.md#hardware-type).

## Flashing Firmware

### QGroundControl (USB)

[QGroundControl](https://qgroundcontrol.com/) can't download stock firmware for this board yet. The `ark_fmu-v6xrt` build target is on PX4 `main` but isn't in a PX4 release, and QGroundControl has no firmware entry for the board ID (62). Flash a file you built instead:

1. [Build the firmware](#building-firmware).
2. In QGroundControl, open the **Firmware** setup page, then connect the carrier USB-C port.
3. Check **Advanced settings**, choose **Custom firmware file...**, and select `ark_fmu-v6xrt_default.px4`.

### px4\_uploader.py (USB or TELEM2)

[`px4_uploader.py`](https://github.com/PX4/PX4-Autopilot/blob/main/Tools/px4_uploader.py) flashes a `.px4` over USB, or over the carrier TELEM2 UART.

Over USB:

```sh
python3 Tools/px4_uploader.py build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.px4
```

Over UART, use the carrier **TELEM2** port. The bootloader enables LPUART8 and leaves the other UARTs off. TELEM1, the port the ARKV6X bootloader uses, stays silent on this board. The bootloader runs TELEM2 at 1,500,000 baud. TX, RX, and GND are enough: the module pulls its CTS input low, so the port doesn't block with CTS unconnected. If you do connect CTS, the adapter must hold RTS asserted, or the bootloader can stop transmitting. The uploader defaults to 115200, so pass `--baud-bootloader 1500000`:

```sh
python3 Tools/px4_uploader.py --port /dev/<telem2-uart> --baud-bootloader 1500000 \
  build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.px4
```

That command works only while the bootloader is listening, for example on a board with no valid firmware. When PX4 is installed and no USB cable is connected, the bootloader starts PX4 right away. The uploader then has to reboot the board into the bootloader with a MAVLink command on TELEM2. TELEM2 has no MAVLink instance by default, so first set `MAV_1_CONFIG` to `TELEM 2` and reboot. Then also pass the TELEM2 baud (`SER_TEL2_BAUD`, 921600 by default) as `--baud-flightstack`:

```sh
python3 Tools/px4_uploader.py --port /dev/<telem2-uart> --baud-bootloader 1500000 --baud-flightstack 921600 \
  build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.px4
```

## Building Firmware

```sh
make ark_fmu-v6xrt_default
```

Upload over USB once a bootloader is present:

```sh
make ark_fmu-v6xrt_default upload
```

The bootloader image is a separate target:

```sh
make ark_fmu-v6xrt_bootloader
```

## Recovering Firmware over SWD

USB upload works after a bootloader is on the NOR. A blank or wiped NOR has nothing for the uploader to talk to, so recovery is over SWD. Use pyOCD and NXP's RT1176 device pack. FlexSPI has to be put back into a mode the algorithm can use.

Full notes are in the [board README](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/fmu-v6xrt/README.md). The procedure below is that recovery path.

### What you need

* An NXP MCU-Link (`1fc9:0143`), wired to the carrier FMU Debug connector. That connector is a 10-pin JST-SH (Pixhawk Debug Full), not JST-GH.
* pyOCD from pip, so `cmsis-pack-manager` is included:

```bash
pip install pyocd
pyocd pack install mimxrt1176
```

* Permission to open the probe:

```
# /etc/udev/rules.d/60-mcu-link.rules
ATTRS{idVendor}=="1fc9", ATTRS{idProduct}=="0143", MODE="0666", GROUP="plugdev"
```

### Flash layout

| Region      | Address      | Size                                      |
| ----------- | ------------ | ----------------------------------------- |
| Bootloader  | `0x30000000` | 128 KB                                    |
| Application | `0x30020000` | 4 MB - 128 KB, inside the 64 MB NOR       |

Both images carry their own boot header. Flash the raw `.bin`. The `.px4` is the container the USB uploader uses.

### 1. Precondition FlexSPI

Do this every session, before any flash. PX4 leaves the NOR in octal DDR. The pack's flash algorithm hangs against that configuration. This command also halts the core.

```bash
pyocd cmd -t mimxrt1170_cm7 -f 4000k -O resume_on_disconnect=false \
  -c "read32 0x400CC000" -c "write32 0x400CC000 0xffffa700"
```

`0x400CC000` is FlexSPI1 `MCR0`.

### 2. Flash

Use the pack target `mimxrt1176dvmaa` here. The chip is marked MIMXRT1176DVMAB, but the DVMAA target is the right one, and PX4 builds for DVMAA as well. The built-in `mimxrt1170_cm7` target is only for the preconditioning step and the reset.

You don't have to build the bootloader. A prebuilt image is in the PX4 tree at [`boards/ark/fmu-v6xrt/extras/ark_fmu-v6xrt_bootloader.bin`](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/fmu-v6xrt/extras/ark_fmu-v6xrt_bootloader.bin). Use that path in place of `build/ark_fmu-v6xrt_bootloader/ark_fmu-v6xrt_bootloader.bin` below.

```bash
pyocd flash -t mimxrt1176dvmaa -f 4000k -O resume_on_disconnect=false \
  --format bin --base-address 0x30000000 \
  build/ark_fmu-v6xrt_bootloader/ark_fmu-v6xrt_bootloader.bin

pyocd flash -t mimxrt1176dvmaa -f 4000k -O resume_on_disconnect=false \
  --format bin --base-address 0x30020000 \
  build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.bin
```

`programmed 0 bytes … identical` means the NOR already matches the image. Pass `-O smart_flash=false` to force an erase and program.

### 3. Reset

```bash
pyocd reset -t mimxrt1170_cm7 -f 4000k -O reset_type=hw
```

`reset_type=hw` is required. A core reset leaves boot-mode bits set, and the board sits halted. NRST reloads them from the boot pins.

### Boot button

The boot mode is read only at power-on or reset. Holding the onboard button through power-on or reset selects the ROM serial downloader (`BOOT_MODE[1:0] = 01`). Otherwise the board boots from fuses (`BOOT_MODE[1:0] = 00`). Pressing the button on a running board does nothing. The SWD steps above are for a board whose fuses are already programmed.
