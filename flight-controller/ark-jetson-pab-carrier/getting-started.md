# Getting Started

The Jetson OS and flight controller firmware both come pre-flashed when you order. We flash the latest version of our Jetson kernel and the latest version of PX4 stable.\
\
You can ssh into your Jetson via the Micro USB cable. The username and password are both **jetson**.

```
ssh jetson@jetson.local
```

&#x20;If you purchased a bundle the [ARK-OS](https://github.com/ARK-Electronics/ARK-OS) comes pre-installed. Please see the [ARK Software](ark-software/) section.

You can also re-flash your Jetson using our [ark\_jetson\_kernel](https://github.com/ARK-Electronics/ark_jetson_kernel) repository to ensure you're running the latest OS. You can find more instructions for re-flashing the Jetson in our [Flashing Guide](flashing-guide.md).
