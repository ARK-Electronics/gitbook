---
description: >-
  Essential bench tools for building, debugging, and maintaining drone
  electronics.
---

# Recommended Tools

## Why Good Tools Matter

You can build a drone with just a soldering iron and a prayer, but when something goes wrong — and it will — having the right tools on your bench turns a multi-day guessing game into a 10-minute diagnosis. Every tool on this list has earned its spot by saving real debugging time.

## Debug and Programming

### ST-LINK V3 Mini

The [ST-LINK V3 Mini](https://www.digikey.com/en/products/detail/stmicroelectronics/STLINK-V3MINIE/16284301) is the recommended programmer/debugger for all ARK products with STM32 microcontrollers. It handles both [SWD programming](swd-programming.md) and [UART debug console](serial-communication-uart.md) access through a single USB connection — no separate USB-to-serial adapter needed.

See the [ST-LINK Flashing Guide](st-link-flashing-guide.md) for setup and usage.

### ARK Pixhawk Debug Adapter

The [ARK Pixhawk Debug Adapter](https://arkelectron.com/product/ark-pixhawk-debug-adapter/) bridges the ST-LINK V3 Mini's STDC14 connector to the Pixhawk Standard 6-pin and 10-pin JST-SH debug connectors found on ARK boards. Includes debug cables. Without this adapter, you would need to manually wire the ST-LINK to JST-SH connectors.

### CAN-to-USB Adapter

A CAN-to-USB adapter like the [Zubax Babel](https://zubax.com/products/babel) lets you connect your computer directly to the [CAN bus](can-bus.md) for diagnostics, firmware updates, and parameter configuration using the [DroneCAN GUI Tool](dronecan-gui-tool-guide.md).

This is essential for:

* Updating firmware on DroneCAN nodes when no flight controller is available
* Inspecting raw CAN bus traffic to diagnose communication issues
* Configuring device parameters outside of a flight controller setup

{% hint style="info" %}
With ArduPilot, the flight controller itself can act as a CAN interface via SLCAN, so a separate adapter is not strictly required. However, a dedicated adapter is useful for standalone bench work and does not depend on a working flight controller.
{% endhint %}

## Test and Measurement

### Oscilloscope

An oscilloscope is the single most useful debugging tool for embedded electronics. When a communication bus isn't working and you've checked the obvious (wiring, baud rate, configuration), an oscilloscope shows you exactly what is happening on the wire — signal presence, voltage levels, noise, rise times, and timing.

Use it to:

* Verify [UART](serial-communication-uart.md) TX/RX signals are present and clean
* Spot power rail noise, ripple, and brownouts
* Confirm connector and solder joint integrity — a broken connection is immediately obvious
* Check voltage levels and signal rise/fall times

An oscilloscope shows you the actual analog waveform, which matters because a logic analyzer applies a voltage threshold and only shows you 1s and 0s. A signal that is ringing, has a slow rise time, or is sitting at an ambiguous voltage will show up clearly on a scope but may look perfectly fine on a logic analyzer. Always verify with a scope first, then move to a logic analyzer for protocol decoding.

Any decent digital oscilloscope with at least 100 MHz bandwidth and two channels will cover drone electronics work.

### Logic Analyzer

A logic analyzer captures and decodes digital bus traffic over time. The [Saleae Logic Pro 16](https://www.saleae.com/) is an excellent choice — 16 channels, high sample rate, and the Saleae Logic 2 software includes built-in protocol decoders for UART, I2C, SPI, and more.

This is the right tool for protocol-level debugging — verifying that the correct bytes are being sent, spotting framing errors, checking timing between messages, and decoding multi-wire buses like I2C (SCL + SDA) and SPI (SCLK + MOSI + MISO + CS) where you need to see clock and data together.

{% hint style="info" %}
**Oscilloscope first, logic analyzer second.** A logic analyzer applies a voltage threshold to classify signals as high or low — it won't tell you if a signal is noisy, has poor rise times, or is floating at an intermediate voltage. Use an oscilloscope to confirm signal integrity first, then switch to a logic analyzer for protocol decoding.
{% endhint %}

### Multimeter

A basic digital multimeter handles the everyday measurements:

* **Voltage** — verify 5V and 3.3V rails are within spec, check battery voltage
* **Continuity** — trace wires, check solder joints, find broken traces
* **Resistance** — measure [CAN bus termination](can-bus.md) (should read ~60 ohms between CAN\_H and CAN\_L with two 120-ohm terminators)

Any reputable multimeter with DC voltage, resistance, and continuity modes will work.

### Benchtop Power Supply

A benchtop power supply with adjustable voltage and current limiting lets you power your electronics safely during development without a battery.

{% hint style="warning" %}
**Quality matters here.** Cheap power supplies have high output ripple (voltage noise) that can cause the same problems you're trying to debug — sensor noise, communication errors, and erratic behavior. Look for a supply with low ripple specification (under 10 mV peak-to-peak). A supply with ripple in the hundreds of millivolts can mask or create issues that won't appear on battery power, and vice versa.
{% endhint %}

Key features to look for:

* Adjustable voltage (0–30V covers everything from 3.3V logic to 6S battery simulation)
* Current limiting — set a limit so a wiring mistake trips the supply instead of releasing the magic smoke
* Low ripple and noise (< 10 mV p-p)
* Voltage and current readout

## ESC Programming

### Betaflight-Capable Flight Controller

To configure or flash firmware on AM32 ESCs (like the [ARK 4IN1 ESC](../electronic-speed-controller/ark-4in1-esc/README.md)), you need a flight controller running Betaflight that supports ESC passthrough. The [ARK FPV](../flight-controller/ark-fpv/README.md) works for this — flash it with [Betaflight](../flight-controller/ark-fpv/betaflight-instructions.md), connect the ESC, and use the Betaflight configurator's ESC tab to configure or update AM32 firmware via passthrough.

See the [ARK 4IN1 ESC firmware guide](../electronic-speed-controller/ark-4in1-esc/firmware/README.md) for detailed instructions.

## Cables and Connectors

### JST Cable Kits

Pre-crimped cable kits let you make custom-length cables without a crimping tool:

* **JST-GH 1.25 mm** (peripheral connectors — CAN, I2C, UART, GPS, power): [GH1.25 Connectors Kit on Amazon](https://www.amazon.com/Pre-Crimped-Connectors-Pixhawk2-Pixracer-Silicone/dp/B07PBHN7TM)
* **JST-SH 1.0 mm** (debug connectors): [JST SH 1.0mm Connector Kit on Amazon](https://www.amazon.com/Teansic-Connector-Pre-Crimped-Housing-Controller/dp/B0D5X6BY5Z)

See [Connectors and Wiring](connectors-and-wiring.md) for pinout details and wire color conventions.
