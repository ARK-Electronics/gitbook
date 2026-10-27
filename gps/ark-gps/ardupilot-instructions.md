# ArduPilot Instructions

## Firmware Setup

The ARK GPS ships with ARK firmware. ArduPilot uses its GPS, magnetometer, barometer and safety switch over DroneCAN. To replace the ARK firmware with ArduPilot's [AP\_Periph](https://ardupilot.org/dev/docs/ap-peripheral-landing-page.html), see [Updating to AP\_Periph](firmware.md#updating-to-ap_periph).

***

## Single GPS Configuration

Connect the ARK GPS to the flight controller's CAN port with a 4-pin JST-GH cable.

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

The node publishes GPS, magnetometer and barometer data with its default parameters. To terminate the bus or fix the node ID, see [Node Parameters](firmware.md#node-parameters).
