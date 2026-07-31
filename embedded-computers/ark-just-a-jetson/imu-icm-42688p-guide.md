# IMU ICM-42688P Guide

The onboard ICM-42688P IMU is connected to SPI1 on the Just a Jetson and shows up in Linux as `/dev/spidev1.0`. See the [pinmux spreadsheet](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/products/JAJ/Jetson_Orin_NX_and_Orin_Nano_series_Pinmux_Config_Jetpack_6.xlsm) for the GPIO assignments.

To enable the SPI bus, enable **spi3** with the Jetson Expansion Header Tool and reboot:

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

To read the IMU, run the test script that ships with ARK-OS (on `PATH`):

```
icm42688p_test.py
```

Source: [icm42688p\_test.py](https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/jetson/scripts/extras/icm42688p_test.py)
