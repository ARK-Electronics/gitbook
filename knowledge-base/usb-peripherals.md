---
description: Tested USB Wi-Fi and Bluetooth adapters, and USB camera EMI on GPS.
---

# USB Peripherals

Applies to every ARK Jetson carrier. Adapters below were tested against the [ARK Jetson Kernel](https://github.com/ARK-Electronics/ark_jetson_kernel).

## Wi-Fi Adapters

<table><thead><tr><th>Wi-Fi Adapter</th><th>Status</th><th data-hidden></th></tr></thead><tbody><tr><td><a href="https://a.co/d/3MhAIhk">Edimax Wi-Fi 4 802.11n Adapter</a></td><td>Working with rtl8xxxu driver</td><td></td></tr><tr><td><a href="https://a.co/d/afkaRWw">TP-Link TL-WN725N</a></td><td>Module exists in kernel but is missing driver</td><td></td></tr><tr><td><a href="https://a.co/d/gagruxP">TP-Link AX1800</a></td><td>Does not work. No kernel driver in 5.15</td><td></td></tr><tr><td><a href="https://a.co/d/at9haBv">TP-Link AC1300</a></td><td>Does not work. No kernel driver in 5.15</td><td></td></tr></tbody></table>

## Bluetooth Adapters

<table><thead><tr><th>Bluetooth Adapter</th><th>Status</th><th data-hidden></th></tr></thead><tbody><tr><td><a href="https://a.co/d/bp0okc0">TP-Link UB500</a></td><td>Working with btusb driver</td><td></td></tr><tr><td><a href="https://a.co/d/2u3XvwS">UGREEN 5.3 Bluetooth Adapter</a></td><td>No driver exists in 5.15 for the Actions ATS2851 chipset</td><td></td></tr></tbody></table>

## USB Cameras and GPS

USB 3.0 signalling emits broadband EMI overlapping the GPS L1, L2, and L5 bands. It raises the noise floor enough to degrade or prevent GPS lock.

Use a USB 2.0 camera where possible. If not, shield the cable and connectors with faraday tape.

Before flight testing:

1. **Measure** the noise floor across the GPS bands with the camera active, using a GPS receiver with spectrum monitoring or a spectrum analyzer.
2. **Shield** the cable, connectors, and exposed sections with faraday/EMI tape if interference is severe.
3. **Re-measure** to confirm the noise floor recovered.

See [this post from Alex Klimaj](https://x.com/ArkElectron/status/1752197126120189962).
