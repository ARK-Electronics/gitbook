# ArduPilot Instructions

## Firmware Setup

The ARK X20 RTK GPS ships with ARK firmware. ArduPilot uses its GPS, magnetometer, barometer and safety switch over DroneCAN.

[AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html) has no ARK X20 RTK GPS target in ArduPilot yet: [ArduPilot PR #33941](https://github.com/ArduPilot/ardupilot/pull/33941) adds it and is not merged. To build AP\_Periph from that PR and flash it, see [ArduPilot Firmware](firmware.md#ardupilot-firmware).

***

## Single GPS Configuration

Connect the ARK X20 RTK GPS to the flight controller's CAN port with a 4-pin JST-GH cable.

### Flight Controller Parameters

#### Required

| Parameter | Value | Description |
|-----------|-------|-------------|
| `CAN_P1_DRIVER` | 1 | Enable CAN port 1 driver |
| `CAN_D1_PROTOCOL` | 1 | Set protocol to DroneCAN |
| `GPS1_TYPE` | 9 | DroneCAN |
| `GPS_AUTO_CONFIG` | 1 | Auto-configure serial GPSes only |

{% hint style="warning" %}
With ARK firmware, keep `GPS_AUTO_CONFIG` at 1. At 2 or 3, ArduPilot waits for a `GPS_TYPE` parameter on the node, which only AP\_Periph has, and never uses the GPS data.
{% endhint %}

Reboot the flight controller. ArduPilot detects the magnetometer and barometer as DroneCAN sensors.

#### Optional

| Parameter | Description |
|-----------|-------------|
| `GPS1_POS_X` / `GPS1_POS_Y` / `GPS1_POS_Z` | Antenna offset from the vehicle center of gravity (meters) |

### CAN Node Parameters

The node publishes GPS, magnetometer and barometer data with its default parameters. To terminate the bus, fix the node ID or choose constellations, see [Node Parameters](firmware.md#node-parameters).

***

## AP\_Periph Configuration

With AP\_Periph built from that PR, configuration matches the [ARK RTK GPS ArduPilot instructions](../ark-rtk-gps/ardupilot-instructions.md), both the single GPS and dual GPS heading setups. Moving baseline heading requires X20P receiver firmware 2.10 or later.
