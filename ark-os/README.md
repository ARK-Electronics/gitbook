# ARK-OS

[ARK-OS](https://github.com/ARK-Electronics/ARK-OS) is ARK's companion computer software suite: a set of systemd services for MAVLink routing, video streaming, flight log management, firmware updates, and network RTK corrections, plus a web UI to manage it all. It comes pre-installed on the ARK Jetson image.

## ARK-UI

The web UI is served at [http://jetson.local](http://jetson.local) (or the Jetson's IP). Pages: **System** (hardware and resource info, hostname), **Autopilot** (status, firmware update, reset), **Connections** (WiFi/Ethernet/LTE, data usage), **Services** (start/stop, autostart, logs, config editing), **Video** (live camera stream), and **Logs** (flight log download and upload to Flight Review).

<figure><img src="../.gitbook/assets/ark-ui-services.png" alt=""><figcaption><p>Services page — start/stop services, toggle autostart, view logs, edit configs</p></figcaption></figure>

## Services

See the [Services](services.md) page for what each service does and which are enabled by default.

## Command-Line Tools

ARK-OS puts its operator scripts on `PATH` (open a login shell and run them by name):

```
mavlink_shell.py              # interactive PX4 NSH shell over MAVLink
px4_shell_command.py <cmd>    # run a single PX4 console command
flash_firmware.sh <fw.px4>    # flash flight controller firmware
reset_fmu_fast.py             # reset the flight controller
reset_fmu_wait_bl.py          # reset the flight controller into bootloader
jetson_serial_number.py       # print the carrier serial number
can_check.py can0             # check DroneCAN traffic on a CAN interface
check_cameras.sh              # stream-test the CSI cameras
check_fan.sh                  # verify the cooling fan
```

## Updating ARK-OS

ARK-OS is distributed as a Debian package on the [releases page](https://github.com/ARK-Electronics/ARK-OS/releases). To update a device, run the install script from a clone of the repo on the Jetson:

```bash
git clone https://github.com/ARK-Electronics/ARK-OS.git
cd ARK-OS
sudo ./packaging/install_ark_os.sh --ark-os-version=X.Y.Z
```

{% hint style="warning" %}
Upgrading resets the service configuration under `/etc/ark-os/` to packaged defaults — reconfigure via the web UI afterward.
{% endhint %}
