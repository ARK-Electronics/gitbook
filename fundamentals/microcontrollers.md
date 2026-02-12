---
description: >-
  What microcontrollers are, the STM32 family, firmware vs bootloaders, and the
  NuttX RTOS.
---

# Microcontrollers

## What is a Microcontroller?

A microcontroller (MCU) is a small computer on a single chip. It contains a processor, memory, and input/output peripherals all in one package. Unlike a full computer (like a Raspberry Pi or Jetson), an MCU has no operating system by default, runs a single firmware image, and boots in milliseconds.

Microcontrollers are the core of nearly every ARK product. They read sensors, drive outputs, and handle communication buses — all in real time.

## How It Works

### The STM32 Family

ARK products use STM32 microcontrollers from STMicroelectronics. These are ARM Cortex-M based chips that are widely used in the drone industry.

| Series | Core | Example MCU | Used In |
|--------|------|-------------|---------|
| STM32F4 | Cortex-M4 | STM32F412CGU6 | ARK CANnode, ARK Flow, ARK MAG |
| STM32H7 | Cortex-M7 | STM32H743 | ARKV6X, ARK FPV |

Key characteristics of STM32 MCUs:

* **Flash memory** — stores firmware persistently (survives power cycles)
* **SRAM** — working memory for runtime data (lost on power off)
* **Hardware peripherals** — UART, SPI, I2C, CAN, timers, ADC, and more are built into the chip
* **Clock speeds** — typically 100–480 MHz depending on the series

### Firmware vs Bootloader

An MCU runs two distinct pieces of software:

* **Bootloader** — a small program that lives at the start of flash memory. It runs first on power-up and decides whether to enter firmware update mode or jump to the main firmware. On ARK DroneCAN products, the bootloader enables over-the-air firmware updates via CAN bus.
* **Firmware** — the main application. For flight controllers this is PX4 or ArduPilot. For DroneCAN sensors it is a PX4 CANnode build or AP\_Periph build.

The bootloader is flashed once (usually via [SWD](swd-programming.md)) and rarely changes. Firmware is updated regularly as new versions are released.

### NuttX RTOS

PX4 runs on top of **NuttX**, a real-time operating system (RTOS). NuttX provides:

* A POSIX-like environment (file-based device access, shell commands)
* Task scheduling with deterministic timing
* Device drivers for STM32 peripherals

When you connect to the [debug console](serial-communication-uart.md), you are interacting with the NuttX shell (NSH). You can list running tasks, read sensor data, and set parameters directly.

## How ARK Products Use It

* **Flight controllers** ([ARKV6X](../flight-controller/arkv6x/README.md), [ARK FPV](../flight-controller/ark-fpv/README.md)) run PX4 or ArduPilot on STM32H7 MCUs, handling sensor fusion, control loops, and communication at hundreds of Hz.
* **DroneCAN sensors** ([ARK CANnode](../sensor/ark-cannode/README.md), [ARK Flow](../sensor/ark-flow/README.md), [ARK MAG](../sensor/ark-mag/README.md)) run lightweight firmware on STM32F4 MCUs, reading a sensor and publishing data over [CAN bus](can-bus.md).
* **ESCs** ([ARK 4IN1 ESC](../electronic-speed-controller/ark-4in1-esc/README.md)) use STM32F0 MCUs running AM32 open source firmware for motor control.

## Common Pitfalls

* **Flashing the wrong firmware** — each MCU variant needs a firmware binary compiled specifically for it. An ARKV6X binary will not run on an ARK FPV, even though both use STM32H7 chips.
* **Forgetting the bootloader** — DroneCAN nodes need a bootloader flashed via SWD before they can accept firmware updates over CAN. If the bootloader is missing or corrupted, the node will not appear on the bus.
* **Confusing flash and SRAM** — parameters stored in flash persist across reboots. A mass erase (`st-flash erase`) wipes everything, including saved parameters.

## Further Reading

* [STM32 Product Page](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
* [NuttX Documentation](https://nuttx.apache.org/docs/latest/)
* [PX4 Autopilot Architecture](https://docs.px4.io/main/en/concept/architecture.html)
* [SWD Programming](swd-programming.md) — how to flash firmware onto an MCU
