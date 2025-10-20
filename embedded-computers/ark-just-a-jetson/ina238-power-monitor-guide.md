# INA238 Power Monitor Guide

The INA238 is connected to I2C bus 1. In Linux, this is bus 7 with address 0x45.&#x20;

```
sudo i2cdetect -y -r 7
```

A example Python driver is provided here.&#x20;

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/ina238_test.py" %}
