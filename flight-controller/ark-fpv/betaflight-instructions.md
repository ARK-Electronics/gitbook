# Betaflight Instructions

## Connection to the Flight Controller

If your FC is flashed with Betaflight:

1. Power your board
2. Open [https://app.betaflight.com/](https://app.betaflight.com/) in Chrome or Edge.
3. Click on Connect

<figure><img src="../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

## Building Firmware

See the official [Betaflight documentation](https://betaflight.com/docs/development/building/Building-in-Ubuntu) for setting up the development environment.\
\
Build the ARK FPV firmware:

If you flash your Flight controller using DFU via [https://app.betaflight.com/](https://app.betaflight.com/) , build the `.hex`&#x20;

```
make hex CONFIG=ARK_FPV
```

If you flash your Flight controller using ST-Link, build the `.bin`

```
make binary CONFIG=ARK_FPV
```

## Flashing Firmware

#### Flash using DFU mode via web app

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
5. You could also flash your own build\
   \- Select the `Load Firmware [Local]`\
   \- In this case you need a `.hex`\
   ![](<../../.gitbook/assets/image (1).png>)<br>
6. Now select `Flash Firmware`

{% hint style="info" %}
Betaflight does not have a separate bootloader. If you want to re-flash back to PX4 or Ardupilot after flashing Betaflight, you will need to re-flash the PX4 bootloader.
{% endhint %}

#### Flash using ST-Link

For detailed instructions on ST-LINK setup, software installation, and usage, see the [ST-LINK Flashing Guide](../../resources/st-link-flashing-guide.md).

Connect to the 6-pin debug connector and flash:

```
st-flash write obj/ARK_FPV.bin 0x08000000
```
