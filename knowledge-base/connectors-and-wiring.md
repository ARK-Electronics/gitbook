---
description: >-
  JST-GH vs JST-SH connectors, wire color conventions, Pixhawk standard
  pinouts, and cable kits.
---

# Connectors and Wiring

## What Are JST Connectors?

JST connectors are the small locking connectors used on virtually all Pixhawk-ecosystem flight controllers and peripherals. The **Pixhawk Connector Standard** specifies two JST connector families for different purposes:

| Connector | Pitch | Use | Found On |
|-----------|-------|-----|----------|
| **JST-GH** | 1.25 mm | Peripheral connections (CAN, I2C, UART, SPI, GPS, power) | All main board connectors |
| **JST-SH** | 1.0 mm | Debug connections (SWD + UART console) | Debug ports only |

Both are polarized locking connectors — they only plug in one way and click into place.

## How It Works

### Pixhawk Standard Pinouts

The Pixhawk Connector Standard defines pin assignments for each connector type. This means an ARK GPS plugs into any Pixhawk-compatible flight controller without custom wiring.

#### CAN — 4-Pin JST-GH

| Pin | Signal | Color |
|-----|--------|-------|
| 1 | 5V | Red |
| 2 | CAN\_H | Yellow |
| 3 | CAN\_L | Green |
| 4 | GND | Black |

Used by all ARK [DroneCAN](can-bus.md) peripherals. See [CAN Bus](can-bus.md) for protocol details.

#### I2C — 4-Pin JST-GH

| Pin | Signal | Color |
|-----|--------|-------|
| 1 | 5V | Red |
| 2 | SCL | Yellow |
| 3 | SDA | Green |
| 4 | GND | Black |

Used by [I2C devices](communication-buses.md) like external magnetometers and barometers.

#### UART/I2C (Basic GPS) — 6-Pin JST-GH

| Pin | Signal | Color |
|-----|--------|-------|
| 1 | 5V | Red |
| 2 | TX | Yellow |
| 3 | RX | Green |
| 4 | SCL | Blue |
| 5 | SDA | Orange |
| 6 | GND | Black |

Combined UART and I2C port, typically used for GPS modules with a compass.

#### TELEM — 6-Pin JST-GH

| Pin | Signal | Color |
|-----|--------|-------|
| 1 | 5V | Red |
| 2 | TX | Yellow |
| 3 | RX | Green |
| 4 | CTS | Blue |
| 5 | RTS | Orange |
| 6 | GND | Black |

Used for [MAVLink](mavlink.md) telemetry connections with hardware flow control.

#### Debug — 6-Pin JST-SH

| Pin | Signal |
|-----|--------|
| 1 | 3.3V |
| 2 | UART TX |
| 3 | UART RX |
| 4 | SWDIO |
| 5 | SWCLK |
| 6 | GND |

Used for [SWD programming](swd-programming.md) and [debug console](serial-communication-uart.md) access.

### Wire Color Conventions

Pixhawk standard cables follow a consistent color scheme:

| Color | Typical Signal |
|-------|---------------|
| **Red** | Power (5V or 3.3V) — always pin 1 |
| **Black** | Ground (GND) — always last pin |
| **Yellow** | First data signal (CAN\_H, TX, SCL) |
| **Green** | Second data signal (CAN\_L, RX, SDA) |
| **Blue** | Third data signal (CTS, SCL on combo ports) |
| **Orange** | Fourth data signal (RTS, SDA on combo ports) |

{% hint style="info" %}
**Power is always pin 1 (red), ground is always the last pin (black).** This is consistent across all Pixhawk Standard connectors and makes visual inspection easy.
{% endhint %}

### Cable Kits

If you need additional or custom-length cables, these pre-crimped kits include connectors and wires ready to assemble (no crimping tool required):

* **JST-GH 1.25 mm**: [GH1.25 Connectors Kit on Amazon](https://www.amazon.com/Pre-Crimped-Connectors-Pixhawk2-Pixracer-Silicone/dp/B07PBHN7TM)
* **JST-SH 1.0 mm**: [JST SH 1.0mm Connector Kit on Amazon](https://www.amazon.com/Teansic-Connector-Pre-Crimped-Housing-Controller/dp/B0D5X6BY5Z)
* **JST-GH 1.25 mm to JST-SH 1.0 mm**: [GH1.25 to SH1.0 Connector Kit on Amazon](https://www.amazon.com/dp/B0D2SVX4S4)

## Common Pitfalls

* **JST-GH and JST-SH are not interchangeable** — they look similar but have different pitches (1.25 mm vs 1.0 mm). Forcing the wrong connector will damage the socket.
* **Inserting cables backwards** — JST connectors are keyed, but enough force can overcome the key. Always check orientation by the latch, not by pushing harder.
* **Pulling on wires instead of the connector** — grip the plastic housing when disconnecting, not the wires. The wires will pull out of the crimps.
* **Missing the latch click** — if the connector doesn't click, it is not seated. A partially inserted connector makes intermittent contact, causing random disconnects.
* **Assuming wire colors match between vendors** — not all cable manufacturers follow the Pixhawk color standard. When in doubt, check the pinout for your specific product.

## Further Reading

* [Pixhawk Connector Standard](https://github.com/pixhawk/Pixhawk-Standards/blob/master/DS-009%20Pixhawk%20Connector%20Standard.pdf)
* [PX4 Wiring Quick Start](https://docs.px4.io/main/en/assembly/)
* [CAN Bus](can-bus.md) — CAN bus protocol and wiring details
* [SWD Programming](swd-programming.md) — debug connector usage
