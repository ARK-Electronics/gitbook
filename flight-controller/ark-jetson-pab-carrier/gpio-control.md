# GPIO Control

The ARK Jetson PAB Carrier includes an I2S0 connector that can be reconfigured as general-purpose GPIOs using a device tree overlay.

## I2S0 Connector Pin Mapping

| ARK Pin | ARK Signal     | 40-Pin Header | Pinmux Name |
|---------|----------------|---------------|-------------|
| 1       | VDD_5V_JPERIPH | -             | -           |
| 2       | I2S0_DOUT_3V3  | Pin 40        | I2S0_DOUT   |
| 3       | I2S0_DIN_3V3   | Pin 38        | I2S0_DIN    |
| 4       | I2S0_LRCLK_3V3 | Pin 35        | I2S0_FS     |
| 5       | I2S0_SCLK_3V3  | Pin 12        | I2S0_SCLK   |
| 6       | AUD_MCLK_3V3   | Pin 7         | GPIO09      |
| 7       | GND            | -             | -           |

## Enabling the GPIO Overlay

The I2S pins are configured for I2S audio by default. To use them as GPIOs, you need to apply the "ARK I2S to GPIO" overlay using jetson-io.

```
sudo /opt/nvidia/jetson-io/config-by-hardware.py -n "ARK I2S to GPIO"
sudo reboot
```

## Using the GPIOs

After applying the overlay and rebooting, you can control the pins using the Jetson.GPIO Python library. The pins are addressed by their 40-pin header number.

```
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)  # I2S0_DOUT as output
GPIO.setup(38, GPIO.IN)   # I2S0_DIN as input

GPIO.output(40, GPIO.HIGH)
value = GPIO.input(38)

GPIO.cleanup()
```

For a complete working example, see the [i2s_gpio_example.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/i2s_gpio_example.py) script in ARK-OS.

## Creating Custom Overlays

To create your own overlay for different pins, refer to the annotated example overlay in the [ark_jetson_kernel](https://github.com/ARK-Electronics/ark_jetson_kernel) repository:

```
device_tree/ark_pab/Linux_for_Tegra/source/hardware/nvidia/t23x/nv-public/overlay/ark_i2s_gpio.dts
```

The overlay file contains documentation explaining how to:

1. Find your connector's signals in the carrier board schematic
2. Map signals to 40-pin header pins using the Jetson Pinmux Spreadsheet
3. Look up SoC GPIO names in the GPIO header file
4. Configure pin properties (tristate, input enable, pull resistors)

For more information on Jetson device tree overlays, see the [NVIDIA Jetson-IO Documentation](https://docs.nvidia.com/jetson/archives/r36.4/DeveloperGuide/HR/ConfiguringTheJetsonExpansionHeaders.html).
