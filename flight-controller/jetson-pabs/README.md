# Jetson PABs

{% content-ref url="ark-jetson-pab-carrier/" %}
[ark-jetson-pab-carrier](ark-jetson-pab-carrier/)
{% endcontent-ref %}

{% content-ref url="ark-jetson-pab-carrier-v3/" %}
[ark-jetson-pab-carrier-v3](ark-jetson-pab-carrier-v3/)
{% endcontent-ref %}

The ARK Jetson PAB Carrier and ARK Jetson PAB Carrier V3 are NVIDIA Jetson Orin Nano/NX carrier boards built around the ARKV6X flight controller and the Pixhawk Autopilot Bus. Both run PX4 and ship with ARK-OS pre-installed. The V3 is a re-architected revision that adds a dedicated I/O co-processor (doubling the PWM outputs to 16), consolidates wiring into two 40-pin avionics connectors, and adds a 30-pin Pixhawk Payload Bus.

## Comparison

| Feature | ARK Jetson PAB Carrier | ARK Jetson PAB Carrier V3 |
| --- | --- | --- |
| Compute module | Jetson Orin Nano / NX | Jetson Orin Nano / NX |
| Flight controller | ARKV6X (Pixhawk Autopilot Bus) | ARKV6X (Pixhawk Autopilot Bus) |
| I/O co-processor | None | STM32F103C8T7 IOMCU |
| PWM outputs | 8 (FMU) | 16 (8 FMU + 8 IO) |
| Avionics wiring | Discrete JST-GH connectors per function (CAN, TELEM, GPS, RC, PWM, I2C, UART) | Two 40-pin Molex Pico-Clasp bundles (Primary + Secondary Avionics) |
| Pixhawk Payload Bus | — | 30-pin FFC (USB 2.0, Ethernet, CAN, I2C, UART, PWM, GPIO) |
| CAN buses | 2× FC CAN + 1× Jetson CAN | 2× FC CAN + 1× Jetson CAN |
| Power inputs | 3× 5V / 6A, Molex Clik-Mate (6-pin) | 3× 5V / 4A, Molex Micro-Lock PLUS (6-pin) |
| CSI camera inputs | 4× 15-pin FFC (CSI0–CSI3) | 2× 22-pin dual-lane FFC (CSI0–CSI3) |
| Ethernet | Gigabit, RJ45 | 10/100, onboard switch → JST-GH (4-pin) + Payload Bus |
| USB host | 3x USB 3.0 A Ports; 1x USB 2.0 A Port | 2× USB 2.0 (JST-GH); USB 3.0 on USB-C |
| Display output | Mini DisplayPort | Micro HDMI |
| Jetson console / recovery | Micro USB (muxed with FC USB) | USB-C |
| NVMe storage | M.2 Key M 2242, PCIe ×4 | M.2 Key M 2242, PCIe ×4 |
| M.2 Key E 2230 slot | PCIe x2, USB, UART, I2S | PCIe x2, USB, UART, I2S |