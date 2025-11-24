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

**What You'll Need**

* ARK FPV
* ST-Link V2 or V3 programmer
* Computer running Windows or Ubuntu

**Software Installation**

**Windows**

Download the ST-Link Utility from the ST-LINK [website](https://www.st.com/en/development-tools/st-link-v2.html#tools-software).

Open the GUI and follow the [ST Documentation](https://www.st.com/en/development-tools/stsw-link007.html#documentation) to program the MCU.

**Ubuntu**

Follow the instructions on the official ST-LINK[ github page](https://github.com/stlink-org/stlink) to install the stlink tools.

**Test the Connection**

Connect the hardware components(using DEBUG port)

```
st-info --probe
```

You should see output similar to:

```
Found 1 stlink programmers
  version:    V3J8
  serial:     003800333433510937363934
  flash:      2097152 (pagesize: 131072)
  sram:       131072
  chipid:     0x450
  dev-type:   STM32H74x_H75x
```

**Flash**

Navigate to the betaflight folder, your folder structure should look like this:

<pre><code><strong>betaflight/
</strong> ├── obj/
 │    ├── ARK_FPV.bin          ← this is what you are flashing
 │    ├── ARK_FPV_somevariant.bin
 │    └── other build files...
 └── other project files...
</code></pre>

Then you can flash your FC

```
st-flash write obj/ARK_FPV.bin 0x08000000
```

Expected output:

```
2025-11-24T11:58:47 INFO common_flash.c: Starting verification of write complete
2025-11-24T11:58:53 INFO common_flash.c: Flash written and verified! jolly good!
2025-11-24T11:58:53 INFO common_legacy.c: Go to Thumb mode
st-flash 1.8.0-121-g8c34a4e
2025-11-24T11:58:53 INFO common_legacy.c: STM32H74x_H75x: 128 KiB SRAM, 2048 KiB flash in at least 128 KiB pages.
2025-11-24T11:58:53 INFO common_legacy.c: NRST is not connected --> using software reset via AIRCR
2025-11-24T11:58:53 INFO common_legacy.c: Go to Thumb mode
2025-11-24T11:58:53 INFO common_legacy.c: Go to Thumb mode
```
