# Setup

Microhard documents the radio itself. Its operating manuals and firmware are on the [Microhard support portal](https://support.microhardcorp.com/portal/en/home), and each module's product page is linked under [Supported modules](hardware.md#specifications).

## Power

| Input | Range |
|-------|-------|
| Battery | 5.5–55 V, 2-pin Molex Nano-Fit |
| USB-C | 5–20 V, USB Power Delivery |

Both inputs can stay connected. The higher voltage powers the radio. The serial connector carries no power, so a flight controller can't power the radio. On a vehicle, wire the battery input.

The radio takes about a minute to boot.

## Radio Access

The carrier's USB-C port is the radio's USB port. A computer sees the radio as a USB Ethernet adapter and gets an address from the radio's DHCP server. Open the web UI at the radio's address.

| Setting | Microhard factory default |
|---------|---------------------------|
| IP address | `192.168.168.1` |
| Login | `admin` / `admin`, changed at first login |

Every radio ships at `192.168.168.1`. Give each radio its own address before linking them.

The **CONFIG** and **RESET** buttons drive the module's pins of the same name. The module's manual describes them.

## Linking Radios

Under **Wireless > RF**, set one radio as master and the others as remotes. Every radio in the network needs the same network ID, frequency, channel bandwidth and compatibility mode.

## Flight Controller

Connect the carrier's serial connector to a flight controller TELEM port with a 6-pin JST-GH cable. The radio bridges its serial port onto the network. In the air radio's serial port settings, match the flight controller's baud rate and send UDP to the ground computer's address on port 14550, where QGroundControl and Mission Planner listen. The ground computer needs a static address on the radio's subnet for this.

The radio's serial port runs at up to 230400 baud. TELEM1 runs MAVLink at 57600 baud by default on both PX4 and ArduPilot. To use another port or rate:

* PX4: [MAVLink Peripherals](https://docs.px4.io/main/en/peripherals/mavlink_peripherals.html)
* ArduPilot: [Serial Port Configuration](https://ardupilot.org/copter/docs/common-serial-options.html)

## Companion Computer

Connect a companion computer to the LAN or WAN port. The [ARK Jetson PAB Carrier integration guide](../../radio-integration/ark-microhard-ddl-carrier-integration-for-ark-jetson-pab-carrier.md) sets up a two-radio network with static addresses.
