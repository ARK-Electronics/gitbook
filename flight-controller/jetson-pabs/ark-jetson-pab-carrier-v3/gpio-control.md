# GPIO Control

Unlike the original PAB Carrier and Just a Jetson, the V3 does not route the Jetson's I2S0 pins to a dedicated GPIO connector. Jetson GPIO on the V3 is available on the **Pixhawk Payload Bus** and avionics connectors — see the [Pinout](/broken/pages/22TqfKKHo21jaoZgsIMt) for which pins carry GPIO-capable signals.

Additional PWM/GPIO capable outputs are provided by the flight controller side of the board: 16 PWM outputs (8 FMU + 8 IO) on the avionics connectors.

For how Jetson GPIO behaves on ARK carriers — idle states, `libgpiod`/`Jetson.GPIO` usage, and safe-state patterns for actuators — see the [ARK Jetson Kernel GPIO docs](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/gpio.md).
