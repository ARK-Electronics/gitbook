# Setup

This page covers the carrier and getting started with the radio. For everything else about the radio, see the operating manual for your module on the [Microhard support portal](https://support.microhardcorp.com/portal/en/home).

## Power

| Input | Range |
|-------|-------|
| Battery | 5.5–55 V, 2-pin Molex Nano-Fit |
| USB-C | 5–20 V, USB Power Delivery |

On a vehicle, power the carrier from the battery input. The serial connector has no power pin, so the flight controller can't power the radio. You can connect battery and USB-C at the same time, and the carrier runs from whichever is the higher voltage.

The radio takes about a minute to boot.

## Radio Access

Connect the carrier's USB-C port to a computer. The radio shows up as a network adapter and gives the computer an address, so you can open the radio's web UI at `192.168.168.1` in a browser. The factory login is `admin` / `admin`, and the radio asks you to change the password the first time you log in.

Every radio ships at `192.168.168.1`, so give each one its own address before linking them.

**RESET** reboots the radio. Holding **CONFIG** after the radio has booted resets it to factory settings. The hold time depends on the module, so check its manual.

## Linking Radios

In the web UI, open **Wireless > RF**. Set one radio as the master and the others as remotes. All radios in the network need the same network ID, frequency, channel bandwidth and compatibility mode.

## Flight Controller

Connect the carrier's serial connector to a TELEM port on the flight controller with a 6-pin JST-GH cable. The radio sends the flight controller's serial data over the network as UDP. In the air radio's web UI, set its serial port to the flight controller's baud rate and send to the ground computer's address on port 14550. QGroundControl and Mission Planner listen on that port. Give the ground computer a static address on the radio's network so it doesn't change.

PX4 and ArduPilot both run MAVLink on TELEM1 at 57600 baud by default. The radio's serial port goes up to 230400 baud. To use another port or rate:

* PX4: [MAVLink Peripherals](https://docs.px4.io/main/en/peripherals/mavlink_peripherals.html)
* ArduPilot: [Serial Port Configuration](https://ardupilot.org/copter/docs/common-serial-options.html)

## Companion Computer

Connect a companion computer to the LAN or WAN port. The [ARK Jetson PAB Carrier integration guide](../../radio-integration/ark-microhard-ddl-carrier-integration-for-ark-jetson-pab-carrier.md) sets up a two-radio network with static addresses.
