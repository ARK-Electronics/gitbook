# ARK-OS

[ARK-OS](https://github.com/ARK-Electronics/ARK-OS) is ARK's companion computer software suite: a set of systemd services for MAVLink routing, video streaming, flight log management, firmware updates, and network RTK corrections, plus a web UI to manage it all. It comes pre-installed on the golden image that ships with Just A Pi bundles.

## ARK-UI

The web UI is served at [http://just-a-pi.local](http://just-a-pi.local) (or the Pi's IP). Pages: **System** (hardware and resource info, hostname), **Autopilot** (status, firmware update, and reset for a USB-connected flight controller), **Connections** (WiFi/Ethernet/LTE, data usage), **Services** (start/stop, autostart, logs, config editing), **Video** (live camera stream), and **Logs** (flight log download and upload to Flight Review).

<figure><img src="../../../.gitbook/assets/ark-ui-services-pi.png" alt=""><figcaption><p>Services page — start/stop services, toggle autostart, view logs, edit configs</p></figcaption></figure>

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
```

## Installing and Updating ARK-OS

ARK-OS is distributed as a Debian package on the [releases page](https://github.com/ARK-Electronics/ARK-OS/releases) — `ark-os-pi-trixie` for Raspberry Pi OS based on Debian 13, `ark-os-pi-bookworm` for Debian 12. The install script picks the right one automatically and is also the supported way to update. Run it from a clone of the repo on the Pi:

```bash
git clone https://github.com/ARK-Electronics/ARK-OS.git
cd ARK-OS
sudo ./packaging/install_ark_os.sh --ark-os-version=X.Y.Z
```

{% hint style="warning" %}
Upgrading resets the service configuration under `/etc/ark-os/` to packaged defaults — reconfigure via the web UI afterward.
{% endhint %}
