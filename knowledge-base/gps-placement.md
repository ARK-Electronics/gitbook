---
description: >-
  GPS module placement, interference sources, and mounting best practices for
  reliable satellite reception and compass accuracy.
---

# GPS Placement

## Why Placement Matters

ARK GPS modules do two jobs: receive satellite signals and measure the earth's magnetic field. Both are easily disrupted by nearby electronics. A GPS module that works perfectly on the bench can perform poorly on a drone if it's mounted in the wrong spot.

All GPS antennas have a **reception pattern** — they are designed to receive signals from satellites above and to the sides, but objects near the antenna can block or distort this pattern. Batteries, carbon fiber, metal brackets, and other conductive materials placed too close to the antenna will shadow parts of the sky and reduce the number of satellites the receiver can track.

Poor placement causes:

* **Low satellite count, high noise, high epv/eph** — RF interference or blocked reception pattern masks weak satellite signals, reducing position accuracy or preventing a GPS fix entirely.
* **Compass calibration failures** — magnetic fields from motor wires, battery leads, and power electronics corrupt magnetometer readings, making calibration impossible or unreliable.
* **Toilet-bowling in flight** — a corrupted compass heading causes the drone to orbit in circles during position hold or autonomous flight.
* **Inconsistent RTK fix** — RTK GPS requires strong signal quality on multiple frequency bands. Even minor RF interference can prevent a fixed solution.

## RF Interference Sources

Radio frequency interference degrades satellite signal reception. The most common on-board sources:

### USB 3.0

USB 3.0 (SuperSpeed) is the single worst source of GPS interference on most drones. USB 3.0 uses 5 Gbit/s signaling, which produces **broadband noise continuously from DC to 5 GHz**. This noise spectrum directly blankets the GPS L1 band (1575.42 MHz), L2 (1227.60 MHz), and L5 (1176.45 MHz) — all at once. The USB 3.0 cable and connectors act as antennas that radiate this noise.

This is a qualitatively different problem than USB 2.0. USB 2.0 runs at 480 MHz and only affects GPS through weak harmonics. USB 3.0 has substantial energy density across the entire GPS frequency range and can raise the noise floor by 20 dB or more, enough to completely kill satellite reception.

{% hint style="danger" %}
**USB 3.0 cables and cameras are a GPS killer.** If you are using USB 3.0 devices (cameras, SSDs, companion computers), keep all USB 3.0 cables and connectors as far from the GPS antenna as possible. If USB 3.0 bandwidth is not required, use a USB 2.0 cable instead — this eliminates the problem entirely.
{% endhint %}

If you must use USB 3.0 near a GPS module, **shield the cable**. Wrapping a USB 3.0 cable with conductive shielding (copper foil tape or a double-shielded cable) and adding ferrite chokes near the connectors can significantly reduce radiated interference. See [Alex Klimaj's demonstration of USB3 cable shielding on a Septentrio Mosaic-X5](https://x.com/alexklimaj/status/1752197126120189962) for a real-world example.

### ESC Switching Noise

ESCs switch at 10–100 kHz, but the fast switching edges produce broadband RF noise that extends well into the MHz and GHz range. This noise radiates from the ESC itself and from the motor phase wires, which act as antennas.

### Radio Transmitters and Antennas

Telemetry radios (900 MHz, 2.4 GHz), RC receivers, and Wi-Fi antennas can all desensitize the GPS receiver if mounted too close. The GPS front-end has a low-noise amplifier that can be overloaded by strong nearby transmitters, even on frequencies well outside the GPS bands.

## Magnetic Interference Sources

The magnetometer (compass) built into most GPS modules measures the earth's magnetic field to determine heading. Any current-carrying wire or magnetized component near the magnetometer will distort this measurement.

### Confirming Magnetic Interference in Logs

You can verify magnetic interference by reviewing a PX4 flight log on [PX4 Flight Review](https://review.px4.io). Look at the **magnetometer field norm** — it should remain stable throughout the flight. If the mag field norm correlates with throttle or thrust, that indicates magnetic coupling from the power system. This is a clear sign that the GPS/compass needs to be moved further from motor wires and battery leads.

### Motor Wires and Battery Leads

These carry the highest currents on the drone (tens of amps) and create proportionally strong magnetic fields. The field strength drops with distance, so even a few centimeters of additional separation makes a meaningful difference.

### ESCs and Power Distribution Boards

ESCs contain inductors and carry high switching currents. Power distribution boards concentrate high-current traces in a small area. Both are strong magnetic interference sources.

### Steel Hardware

Steel screws, nuts, and brackets near the GPS module can distort the magnetic field. Use non-magnetic hardware (nylon, brass, aluminum, titanium) for GPS mast mounting.

## Mounting Best Practices

### Use a Mast

The single most effective thing you can do for GPS performance is mount it on a mast above the frame. Even 5–10 cm of vertical separation dramatically reduces both RF and magnetic interference from the electronics below and keeps the antenna reception pattern clear of obstructions.

### Top of Frame

If a mast isn't practical, mount the GPS on the top of the frame, centered, and as far above the electronics stack as possible. Avoid mounting it underneath the frame where the entire electronics stack is between the GPS antenna and the sky.

### Keep the Reception Pattern Clear

Make sure nothing blocks the sky view around the GPS antenna. Batteries mounted on top of the frame right next to the GPS, tall carbon fiber standoffs, or other conductive objects near the antenna will shadow satellites and reduce fix quality. The GPS antenna needs a clear view of the sky above and to the sides.

### SMA Extenders for Flexible Placement

Some GPS modules support external antennas via SMA connectors. You can use SMA cables or extenders to place the GPS antenna in a more favorable location — for example, on top of a mast or away from a crowded electronics bay — while keeping the GPS receiver module closer to the flight controller.

{% hint style="warning" %}
**Update your GPS position offset parameters.** If you move the GPS antenna away from the module using an SMA extender, the antenna's physical position relative to the flight controller has changed. Update `EKF2_GPS_POS_X`, `EKF2_GPS_POS_Y`, and `EKF2_GPS_POS_Z` in PX4 to reflect the actual antenna location, not the module location.
{% endhint %}

### Orientation

Most GPS modules have an arrow or marking indicating the forward direction. Mount the module with this arrow pointing toward the front of the drone. If the module is rotated, you must set the corresponding autopilot parameter (e.g., `CAL_MAGx_ROT` in PX4) to match, or compass heading will be wrong.

### Separation Distances

There are no universal numbers — it depends on your specific hardware and how much current it draws. As a rough guide:

* **USB 3.0 cables/connectors** — as far as possible; use USB 2.0 cables or shielded cables if separation is limited
* **Motor wires and battery leads** — at least 5–10 cm, preferably on opposite side of frame
* **ESCs** — at least 5 cm
* **Radio antennas** — at least 10 cm from telemetry/RC antennas

## Common Mistakes

* **GPS mounted too close to the battery** — a LiPo battery is a large conductive object that blocks the GPS antenna reception pattern. If the battery sits right next to or above the GPS, it shadows satellites and degrades fix quality. Mount the GPS above or well away from the battery.
* **GPS too close to other antennas and RF-noisy devices** — clustering the GPS antenna near telemetry radios, RC receivers, Wi-Fi antennas, or USB 3.0 cameras creates a high-noise environment. Spread antennas out and keep the GPS away from other RF sources.
* **Power wires routed near the GPS** — high-current battery leads and motor wires near the GPS create magnetic interference that corrupts the compass. Route power wiring on the opposite side of the frame.
* **Carbon fiber infused 3D-printed enclosure** — carbon fiber is conductive. A 3D-printed enclosure made with carbon fiber filament acts as a Faraday cage around the GPS, blocking satellite signals. Use non-conductive materials (PLA, PETG, nylon) for any GPS enclosure or mount.
* **GPS blocked by the carbon fiber airframe** — mounting the GPS below a carbon fiber plate or inside a carbon fiber fuselage attenuates satellite signals. Always mount the GPS above and outside any conductive airframe structure.
* **RTK antennas mounted too close together** — dual-antenna RTK heading setups require sufficient baseline separation between the two antennas to get an accurate heading. Mounting them too close together reduces heading precision. Follow the GPS manufacturer's recommended minimum baseline distance.

## Further Reading

* [Power and Grounding](power-and-grounding.md) — voltage levels, noise sources, and signal integrity
* [CAN Bus](can-bus.md) — CAN wiring and 5V power delivery for DroneCAN GPS modules
* [PX4 Magnetometer Calibration](https://docs.px4.io/main/en/config/compass.html)
* [PX4 Flight Review](https://review.px4.io) — upload ulogs to check magnetometer field norm and GPS quality
* [USB3 cable jamming and shielding](https://x.com/alexklimaj/status/1752197126120189962) — Alex Klimaj demonstrating the impact of USB3 cable shielding on GPS reception
* [USB 3.0 Radio Frequency Interference Impact on 2.4 GHz Wireless Devices](https://www.usb.org/sites/default/files/327216.pdf) — Intel whitepaper on USB 3.0 broadband emissions
