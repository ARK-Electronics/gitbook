# Bootloader Flashing Using DFU

DFU can be used to flash or reflash the bootloader with the following steps.

1. With the board unpowered, hold the button next to the USB C port while connecting the USB cable to your PC.
2. Open [https://devanlai.github.io/webdfu/dfu-util/](https://devanlai.github.io/webdfu/dfu-util/) in Chrome.
3.  Select `Connect`, then select `DFU in FS Mode`.

    <figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption><p>DFU Device Selection</p></figcaption></figure>
4.  Now select the `@Internal Flash` option.

    <figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption><p>Select the @Internal Flash Option</p></figcaption></figure>
5. Now choose the bootloader binary you wish to flash. In this case we are using the default ARK FPV PX4 bootloader which is compatible with PX4 and Ardupilot.

{% file src="../../.gitbook/assets/ark_fpv_bootloader.bin" %}
ARK FPV PX4 Bootloader Built on Commit [1043aebf5ddd8fd0f6825a27d9a060fa24b616eb](https://github.com/PX4/PX4-Autopilot/commit/1043aebf5ddd8fd0f6825a27d9a060fa24b616eb)
{% endfile %}

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption><p>Firmware Selection</p></figcaption></figure>

6.  Select `Download` to flash the firmware.

    <figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption><p>Start the Firmware Download</p></figcaption></figure>
7. The flash will finish and the firmware will start.
