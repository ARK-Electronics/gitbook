---
description: >-
  Wire a GNSS receiver's pulse-per-second (PPS) output to the ARK Just a Pi and
  discipline the system clock with chrony.
---

# PPS Input

Pin 4 of the **UART4/PWM/GPIO** connector (GPIO18) is a pulse-per-second (PPS) input by default. Wire a GNSS receiver's PPS output to it and the pulses appear on `/dev/pps0`, where chrony can use them to discipline the system clock. This works with a CM5 or a CM4.

## Wiring

UART4/PWM/GPIO — 6-pin JST-GH

| Pin | Signal | Connect to |
|---|---|---|
| 1 | VDD_5V_IN (500 mA) | Receiver power, if the receiver is powered from this cable |
| 2 | UART4_TXD/GPIO12 | Receiver RX (optional, see [GNSS serial](#discipline-the-clock-with-chrony)) |
| 3 | UART4_RXD/GPIO13 | Receiver TX (optional) |
| 4 | PPS/GPIO18 | Receiver PPS |
| 5 | GPIO19 | — |
| 6 | GND | Receiver GND |

{% hint style="warning" %}
The PPS signal must be 3.3V logic. The Compute Module's GPIOs are not 5V tolerant, so put a level shifter in front of a 5V PPS output.
{% endhint %}

ARK GPS modules output their receiver's PPS at 3.3V on a TIMEPULSE pin:

| GPS | Connector | Pin |
|---|---|---|
| [ARK X20 RTK GPS](../../gps/ark-x20-rtk-gps/hardware.md), [ARK G5 RTK GPS](../../gps/ark-g5-rtk-gps/hardware.md), [ARK G5 RTK Heading GPS](../../gps/ark-g5-rtk-heading-gps/hardware.md) | GPS UART2 and Timepulse | 3 |
| [ARK Teseo GPS](../../gps/ark-teseo-gps/hardware.md) | I2C and Timepulse | 4 |

Wire TIMEPULSE to pin 4 and the GPS's GND to pin 6. The GPS stays on the flight controller's CAN bus, so use the [NTP server](#discipline-the-clock-with-chrony) setup below for the time of day.

## Pin Configuration

The Just a Pi image sets pin 4 up in **/boot/firmware/config.txt**:

```
# GNSS PPS input on the UART4 connector's pin 4 (GPIO18) as /dev/pps0
dtoverlay=pps-gpio,gpiopin=18,pull=down
```

The pull-down holds the pin low when nothing is connected. If the line is missing, as on older images or your own Raspberry Pi OS install, add it after `[all]` and reboot. If the receiver's pulse is active low, append `,assert_falling_edge`.

### Using Pin 4 as PWM2

To use pin 4 as PWM2 instead, replace the `pps-gpio` line with this and reboot:

```
dtoverlay=pwm,pin=18,func=2
```

Removing the line without a replacement leaves pin 4 as a plain GPIO.

## Check the Pulse

```bash
sudo apt install pps-tools
sudo ppstest /dev/pps0
```

Each second prints an `assert` line:

```
trying PPS source "/dev/pps0"
found PPS source "/dev/pps0"
ok, found 1 source(s), now start fetching data...
source 0 - assert 1761235200.000002114, sequence: 85 - clear  0.000000000, sequence: 0
source 0 - assert 1761235201.000001873, sequence: 86 - clear  0.000000000, sequence: 0
```

Most receivers only output PPS once they have a fix. If `ppstest` reports `Connection timed out`, check the fix and the wiring, and look for the PPS source in `dmesg | grep pps`.

## Discipline the Clock with chrony

Raspberry Pi OS keeps time with `systemd-timesyncd`, which can't read PPS. Install chrony, which replaces it:

```bash
sudo apt install chrony
```

A pulse marks the start of a second but not which second it is, so chrony also needs a time-of-day source. Choose the one that matches your setup:

{% tabs %}
{% tab title="GNSS serial" %}
Use this when the receiver's UART is wired to pins 2 and 3 and outputs NMEA. It works without a network.

```bash
sudo apt install gpsd
```

Point gpsd at the UART in **/etc/default/gpsd**. With a CM4, the UART4 connector is `/dev/ttyAMA5`.

```
DEVICES="/dev/ttyAMA4"
GPSD_OPTIONS="-n"
USBAUTO="false"
```

Create **/etc/chrony/conf.d/pps.conf**:

```
# Time of day from gpsd, used only to number the PPS seconds
refclock SHM 0 refid NMEA offset 0.2 delay 0.2 noselect
# Second edges from the PPS input
refclock PPS /dev/pps0 refid PPS lock NMEA prefer
```

Restart both services:

```bash
sudo systemctl enable gpsd
sudo systemctl restart gpsd chrony
```

{% hint style="info" %}
If you turn on **dds-agent** in ARK-UI, it uses `/dev/ttyAMA4` by default. Move one of them to the UART2 or UART3 connector.
{% endhint %}
{% endtab %}

{% tab title="NTP server" %}
Use this when only the PPS pin is wired and the Just a Pi can reach an NTP server. chrony numbers the pulses from the server it has synchronized to. Debian's default `pool` line is enough with internet access; for a local server, add a `server <address> iburst` line.

Create **/etc/chrony/conf.d/pps.conf**:

```
# Second edges from the PPS input, numbered by the NTP source
refclock PPS /dev/pps0 refid PPS prefer
```

Restart chrony:

```bash
sudo systemctl restart chrony
```

chrony ignores the pulses until it has synchronized to the server once.
{% endtab %}
{% endtabs %}

## Check chrony

```bash
chronyc sources
chronyc sourcestats
```

After a minute or two, `PPS` is marked `#*` in `chronyc sources`: chrony is synchronized to it. With the GNSS serial setup, if `PPS` never gets selected, look at the `NMEA` offset in `chronyc sourcestats` and change `offset` in **pps.conf** until NMEA reads close to zero.
