# INA238 Power Monitor Guide

The INA238 power monitor is connected to I2C bus 1, which is Linux bus 7, at address `0x45`:

```
sudo i2cdetect -y -r 7
```

Always pass `-r` — without it, `i2cdetect` skips the `0x40–0x4F` range on Tegra. See the [I2C bus map](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/i2c.md) for which connector maps to which Linux bus.

To read voltage, current, and power, run the test script that ships with ARK-OS (on `PATH`):

```
ina238_test.py
```

Source: [ina238\_test.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/extras/ina238_test.py)
