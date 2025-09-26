# Betaflight Instructions

## Flashing Firmware

Betaflight can be flashed using DFU over USB C.

1. With the board unpowered, hold the button next to the USB C port while connecting the USB cable to your PC.
2. Open [https://app.betaflight.com/](https://app.betaflight.com/) in Chrome or Edge.
3. Select `Firmware Flasher`\
   Toggle the sliders `Enable Expert Mode` and `Show release candidates` and select:\
   \- `Development`\
   \- `ARK_FPV`\
   \- `4.6.0-dev [latest]`\
   ![](<../../.gitbook/assets/image (39).png>)
4. Now select the `Load Firmware [Online]`\
   ![](<../../.gitbook/assets/image (40).png>)
5. Now select `Flash Firmware`

{% hint style="info" %}
Betaflight does not have a separate bootloader. If you want to re-flash back to PX4 or Ardupilot after flashing Betaflight, you will need to re-flash the PX4 bootloader.
{% endhint %}

## Building Firmware

See the official [Betaflight documentation](https://betaflight.com/docs/development/building/Building-in-Ubuntu) for setting up the development environment.\
\
Build the ARK FPV firmware:

```
make binary CONFIG=ARK_FPV
```
