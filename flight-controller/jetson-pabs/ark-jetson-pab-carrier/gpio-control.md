# GPIO Control

The I2S0 connector pins come up as general-purpose GPIOs by default — no overlay or jetson-io step is needed. At idle the SoC drives none of them: the four output-capable pins sit hi-z, held HIGH by 604Ω pull-ups on the carrier, and DIN is a floating input. A pin wired to a relay or actuator never transitions at boot.

## I2S0 Connector Pin Mapping

| ARK Pin | Signal | 40-Pin Header | libgpiod Name | Idle at Boot |
| --- | --- | --- | --- | --- |
| 1 | VDD_5V_JPERIPH | - | - | - |
| 2 | I2S0_DOUT_3V3 | Pin 40 | `PI.00` | HIGH (pulled) |
| 3 | I2S0_DIN_3V3 | Pin 38 | `PI.01` | hi-z (input) |
| 4 | I2S0_LRCLK_3V3 | Pin 35 | `PI.02` | HIGH (pulled) |
| 5 | I2S0_SCLK_3V3 | Pin 12 | `PH.07` | HIGH (pulled) |
| 6 | AUD_MCLK_3V3 | Pin 7 | `PAC.06` | HIGH (pulled) |
| 7 | GND | - | - | - |

Confirm the lines are exposed:

```bash
sudo gpioinfo | grep -E '"P(H\.07|I\.0[0-2]|AC\.06)"'
```

## Using the GPIOs

Drive and read the lines with `libgpiod` (`gpioset` / `gpioget`) or the Jetson.GPIO Python library. Jetson.GPIO addresses pins by their 40-pin header number and needs version 2.1.12 or newer:

```bash
sudo pip3 install 'Jetson.GPIO>=2.1.12'
```

The example below jumpers HDR40 pin 40 (DOUT) to pin 38 (DIN) and toggles HIGH/LOW, reading each transition back as a loopback test:

```python
import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)  # I2S0_DOUT
GPIO.setup(38, GPIO.IN)                     # I2S0_DIN

try:
    for level in (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.LOW):
        GPIO.output(40, level)
        time.sleep(0.2)
        got = GPIO.input(38)
        print(f"wrote {level} read {got} {'PASS' if got == level else 'FAIL'}")
finally:
    GPIO.cleanup()
```

ARK-OS ships a complete version of this loopback as `i2s_gpio_example.py` (on `PATH`).

{% hint style="warning" %}
**GPIO state after your app exits**

While your app owns a line, the kernel guarantees its value. On release (clean exit, crash, or kill), **the pin retains its last-written value** until the next reboot re-asserts the pulled-HIGH idle state. If a line must be safe-off for an active-high load, add an external pull-down or keep a process owning the line (`gpioset --mode=signal`).
{% endhint %}

For the full pin reference, electrical details, and safe-state patterns, see the [ARK Jetson Kernel GPIO docs](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/gpio.md).
