# PX4 Instructions

{% embed url="https://docs.px4.io/main/en/flight_controller/ark_v6xrt" %}
PX4 user guide for the ARKV6X-RT
{% endembed %}

The board ships with PX4. Source and the build target live in [boards/ark/fmu-v6xrt](https://github.com/PX4/PX4-Autopilot/tree/main/boards/ark/fmu-v6xrt).

### Hardware Type

Rev 1.0 reports hardware type `ARKV6XRT000`. `init/rc.board_sensors` starts the internal IMUs only for that type:

```sh
icm45686 -R 6 -b 1 -s start
lsm6dsv -R 1 -b 3 -s -T 80 start
iim20670 -R 2 -b 2 -s start
```

The IIS2MDC starts on I2C3, and the BMP390 starts on I2C2 (`bmp388 -I -b 2 start`), for every hardware type.

Rev 2.0 has different IMUs: three LSM6DSV32X parts, on SPI1, SPI2, and SPI3, in place of the ICM-45686, IIM-20670, and LSM6DSV80X. It also sets the FMUM hardware revision to 1 and moves the BMP390 to I2C3. A firmware build that only matches `ARKV6XRT000` prints `unsupported FMU hwtype, internal IMUs not started` on that board, and it still looks for the barometer on I2C2. The Rev 1.0 start commands above do not probe the LSM6DSV32X.

### Flashing Firmware

#### QGroundControl (USB)

Firmware flashes over the carrier USB-C port with [QGroundControl](https://qgroundcontrol.com/).

#### px4\_uploader.py (USB or TELEM2)

[`px4_uploader.py`](https://github.com/PX4/PX4-Autopilot/blob/main/Tools/px4_uploader.py) flashes a `.px4` over USB, or over UART while the bootloader is running.

Over USB:

```sh
python3 Tools/px4_uploader.py build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.px4
```

Over UART, use the carrier **TELEM2** port. The bootloader enables LPUART8 and leaves the other UARTs off. TELEM1, the port the ARKV6X bootloader uses, stays silent on this board.

```sh
python3 Tools/px4_uploader.py --port /dev/<telem2-uart> build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.px4
```

### Building Firmware

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

### IMUs

These rates are for Rev 1.0. Rev 2.0 fits three LSM6DSV32X IMUs instead, and the startup script above does not start them.

On Rev 1.0, each IMU runs at the widest full scale of the channel it publishes, with as little on-chip filtering as the part allows. PX4 filters downstream.

| IMU        | Bus  | Full scale          | Publish rate |
| ---------- | ---- | ------------------- | ------------ |
| ICM-45686  | SPI1 | ±32 g / ±4000 dps   | 800 Hz       |
| LSM6DSV80X | SPI3 | ±16 g / ±4000 dps   | 768 Hz       |
| IIM-20670  | SPI2 | ±65.5 g / ±1966 dps | 1000 Hz      |

Startup order is ICM-45686, then LSM6DSV80X, then IIM-20670. At equal calibration priority the voter keeps the lowest instance, and `CAL_ACC0_PRIO` / `CAL_GYRO0_PRIO` are seeded on the ICM-45686, so that part is the primary.

The IIM-20670 starts last on purpose. Its gyro low-pass cannot be set wider than 60 Hz, which is too much group delay for the rate loop, so it is the navigation and fallback IMU. Its gyro trace looks smoother and later than the other two.

The LSM6DSV80X publishes its ±16 g accelerometer. The ±80 g element stays powered down.

### Heater

The heater is closed-loop on the ICM-45686 die temperature. `HEATER1_SENS_ID` defaults to that sensor (`3407882`). The pad warms the whole board. The parameter only selects which die is the feedback.

Run the accelerometer calibration after `heater status` reports that the setpoint has been reached.

### PWM Outputs

The module provides 12 FMU PWM outputs, and 8 more from PX4IO on a carrier that has one. How many of those reach a connector depends on the carrier.

FMU outputs 1–8 support DShot and bidirectional DShot. Outputs 9–12 are PWM only.

Each FMU output has its own FlexPWM submodule, so protocol and rate are set per output.

### Power

The module is powered at 5 V from the carrier. Two digital power bricks are supported. `SENS_EN_INA226` is enabled by default. The INA228 and INA238 drivers are built in for carriers that use those parts. Set `ADC_ADS1115_EN` to use an ADS1115 instead of the onboard ADC for analog monitoring.

### GPS and Compass

* GPS1 (LPUART3) is the full GPS port on a PAB carrier: safety switch, buzzer, LED, and compass I2C.
* GPS2 (LPUART5) is the basic GPS port.

The onboard IIS2MDC is a backup. Yaw normally comes from an external compass in the GPS module.

### Debug Console

The PX4 system console is LPUART1, on the carrier FMU Debug connector, at 57600 baud. SWD is on the same connector. An NXP MCU-Link's virtual COM port is this console.

### Recovering Firmware over SWD

USB upload works after a bootloader is on the NOR. A blank or wiped NOR has nothing for the uploader to talk to, so recovery is over SWD. Use pyOCD and NXP's RT1176 device pack. FlexSPI has to be put back into a mode the algorithm can use.

Full notes are in the [board README](https://github.com/PX4/PX4-Autopilot/blob/main/boards/ark/fmu-v6xrt/README.md). The procedure below is that recovery path.

#### What you need

* An NXP MCU-Link (`1fc9:0143`). Its JST-GH cable mates with the carrier debug connector.
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

#### Flash layout

| Region      | Address      | Size                                      |
| ----------- | ------------ | ----------------------------------------- |
| Bootloader  | `0x30000000` | 128 KB                                    |
| Application | `0x30020000` | 4 MB - 128 KB, inside the 64 MB NOR       |

Both images carry their own boot header. Flash the raw `.bin`. The `.px4` is the container the USB uploader uses.

#### 1. Precondition FlexSPI

Do this every session, before any flash. PX4 leaves the NOR in octal DDR. The pack's flash algorithm hangs against that configuration. This command also halts the core.

```bash
pyocd cmd -t mimxrt1170_cm7 -f 4000k -O resume_on_disconnect=false \
  -c "read32 0x400CC000" -c "write32 0x400CC000 0xffffa700"
```

`0x400CC000` is FlexSPI1 `MCR0`.

#### 2. Flash

Use the pack target `mimxrt1176dvmaa` here. The built-in `mimxrt1170_cm7` target is only for the preconditioning step and the reset.

```bash
pyocd flash -t mimxrt1176dvmaa -f 4000k -O resume_on_disconnect=false \
  --format bin --base-address 0x30000000 \
  build/ark_fmu-v6xrt_bootloader/ark_fmu-v6xrt_bootloader.bin

pyocd flash -t mimxrt1176dvmaa -f 4000k -O resume_on_disconnect=false \
  --format bin --base-address 0x30020000 \
  build/ark_fmu-v6xrt_default/ark_fmu-v6xrt_default.bin
```

`programmed 0 bytes … identical` means the NOR already matches the image. Pass `-O smart_flash=false` to force an erase and program.

#### 3. Reset

```bash
pyocd reset -t mimxrt1170_cm7 -f 4000k -O reset_type=hw
```

`reset_type=hw` is required. A core reset leaves boot-mode bits set, and the board sits halted. NRST reloads them from the boot pins.

#### Boot button

Holding the onboard button selects the ROM serial downloader (`BOOT_MODE[1:0] = 01`). Released, the board boots from fuses (`BOOT_MODE[1:0] = 00`). The SWD steps above are for a board whose fuses are already programmed.
