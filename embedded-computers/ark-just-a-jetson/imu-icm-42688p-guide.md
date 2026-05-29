# IMU ICM-42688P Guide

The ICM-42688P is connected to SPI1 on the Just a Jetson. See the [pinmux spreadsheet](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/products/JAJ/Jetson_Orin_NX_and_Orin_Nano_series_Pinmux_Config_Jetpack_6.xlsm) for the GPIO assignments.&#x20;

The device shows up in linux under /dev/spidev1.0

To enable the SPI bus using the Jetson Expansion Header Tool, enable spi3.

```
sudo /opt/nvidia/jetson-io/jetson-io.py
```

```
Configure Jetson 40pin Header
Configure header pins manually
```

```
  =================== Jetson Expansion Header Tool ===================
 |                                                                    |
 |                                                                    |
 |                Select desired functions (for pins):                |
 |                                                                    |
 |                [ ] aud            (7)                              |
 |                [ ] extperiph3_clk (29)                             |
 |                [ ] extperiph4_clk (31)                             |
 |                [ ] i2s2           (12,35,38,40)                    |
 |                [ ] pwm1           (15)                             |
                  [ ] pwm5           (33)                             |
 |                [ ] pwm7           (32)                             |
 |                [ ] spi1           (19,21,23,24,26)                 |
 |                [*] spi3           (13,16,18,22,37)                 |
 |                [*] uarta-cts/rts  (11,36)                          |
 |                                                                    |
 |                                Back                                |
 |                                                                    |
  ====================================================================
```

An example Python driver is provided here.

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/icm42688p_driver.py" %}
