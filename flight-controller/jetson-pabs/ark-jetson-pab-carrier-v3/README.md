---
cover: ../../../.gitbook/assets/IMG_5983_edited.JPG
coverY: 0
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/
---

# ARK Jetson PAB Carrier V3

An NVIDIA Jetson Orin Nano/NX carrier board built around the ARKV6X flight controller and the Pixhawk Autopilot Bus. It runs PX4 and ships with ARK-OS pre-installed. The V3 adds a dedicated I/O co-processor (16 PWM outputs), consolidates wiring into two 40-pin avionics connectors, and adds a 30-pin Pixhawk Payload Bus — see the [comparison table](../).

## Where to Start

**Your bundle arrived preflashed.** The Jetson already runs ARK-OS and the flight controller already has PX4. Go to [Set Up Your Carrier](setup/), then manage it from the ARK-UI web interface.

**You have a bare board, or you want to flash it yourself.** Install a Jetson module and NVMe SSD, then start at the [Flashing Guide](flashing-guide.md).

## Sections

* [Set Up Your Carrier](setup/) — connect to it and get it on your network
* [Using ARK-OS](using-ark-os.md) — services, web interface, autopilot connections
* [Hardware Reference](hardware.md) — pinout, GPIO, cameras
* [Developer Guide](developer.md) — flashing, serial console, building from source
