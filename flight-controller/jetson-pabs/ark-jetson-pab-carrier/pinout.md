# Pinout

{% file src="../../../.gitbook/assets/ARK Jetson Carrier Board Pinout Reference Poster 7-22-2025.pdf" %}
Pinout reference poster (PDF)
{% endfile %}

### **POWER1**

| Pin Number | Signal Name           | Voltage |
| ---------- | --------------------- | ------- |
| 1          | VBRICK1               | 5.0V    |
| 2          | VBRICK1               | 5.0V    |
| 3          | I2C1\_SCL\_PWR\_EXT   | 3.3V    |
| 4          | I2C1\_SDA\_PWR\_EXT   | 3.3V    |
| 5          | GND                   | GND     |
| 6          | GND                   | GND     |

### **POWER2**

| Pin Number | Signal Name                | Voltage |
| ---------- | -------------------------- | ------- |
| 1          | VBRICK2                    | 5.0V    |
| 2          | VBRICK2                    | 5.0V    |
| 3          | I2C2\_SCL\_BASE\_PWR\_EXT  | 3.3V    |
| 4          | I2C2\_SDA\_BASE\_PWR\_EXT  | 3.3V    |
| 5          | GND                        | GND     |
| 6          | GND                        | GND     |

### **POWER3**

| Pin Number | Signal Name           | Voltage |
| ---------- | --------------------- | ------- |
| 1          | VBRICK3               | 5.0V    |
| 2          | VBRICK3               | 5.0V    |
| 3          | I2C3\_SCL\_PWR\_EXT   | 3.3V    |
| 4          | I2C3\_SDA\_PWR\_EXT   | 3.3V    |
| 5          | GND                   | GND     |
| 6          | GND                   | GND     |

### **TELEM1**

| Pin Number | Signal Name              | Voltage |
| ---------- | ------------------------ | ------- |
| 1          | VDD\_5V\_HIPOWER         | 5.0V    |
| 2          | UART7\_TX\_TELEM1\_EXT   | 3.3V    |
| 3          | UART7\_RX\_TELEM1\_EXT   | 3.3V    |
| 4          | UART7\_CTS\_TELEM1\_EXT  | 3.3V    |
| 5          | UART7\_RTS\_TELEM1\_EXT  | 3.3V    |
| 6          | GND                      | GND     |

### **TELEM3**

| Pin Number | Signal Name               | Voltage |
| ---------- | ------------------------- | ------- |
| 1          | VDD\_5V\_HIPOWER          | 5.0V    |
| 2          | USART2\_TX\_TELEM3\_EXT   | 3.3V    |
| 3          | USART2\_RX\_TELEM3\_EXT   | 3.3V    |
| 4          | USART2\_CTS\_TELEM3\_EXT  | 3.3V    |
| 5          | USART2\_RTS\_TELEM3\_EXT  | 3.3V    |
| 6          | GND                       | GND     |

### **GPS1**

| Pin Number | Signal Name                    | Voltage           |
| ---------- | ------------------------------ | ----------------- |
| 1          | VDD\_5V\_PERIPH                | 5.0V              |
| 2          | USART1\_TX\_GPS1\_EXT          | 3.3V              |
| 3          | USART1\_RX\_GPS1\_EXT          | 3.3V              |
| 4          | I2C1\_SCL\_GPS1\_EXT           | 3.3V              |
| 5          | I2C1\_SDA\_GPS1\_EXT           | 3.3V              |
| 6          | NSAFETY\_SWITCH\_IN\_EXT       | 3.3V              |
| 7          | NSAFETY\_SWITCH\_LED\_OUT\_EXT | 3.3V              |
| 8          | 3V3\_FMU                       | 3.3V              |
| 9          | BUZZER\_EXT                    | 5.0V (open drain) |
| 10         | GND                            | GND               |

### **GPS2**

| Pin Number | Signal Name                 | Voltage |
| ---------- | --------------------------- | ------- |
| 1          | VDD\_5V\_HIPOWER            | 5.0V    |
| 2          | UART8\_TX\_GPS2\_EXT        | 3.3V    |
| 3          | UART8\_RX\_GPS2\_EXT        | 3.3V    |
| 4          | I2C2\_SCL\_BASE\_GPS2\_EXT  | 3.3V    |
| 5          | I2C2\_SDA\_BASE\_GPS2\_EXT  | 3.3V    |
| 6          | GND                         | GND     |

### **CAN1**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_HIPOWER | 5.0V    |
| 2          | CAN1\_H          | 3.3V    |
| 3          | CAN1\_L          | 3.3V    |
| 4          | GND              | GND     |

### **CAN2**

| Pin Number | Signal Name     | Voltage |
| ---------- | --------------- | ------- |
| 1          | VDD\_5V\_PERIPH | 5.0V    |
| 2          | CAN2\_H         | 3.3V    |
| 3          | CAN2\_L         | 3.3V    |
| 4          | GND             | GND     |

### **RC**

| Pin Number | Signal Name                  | Voltage |
| ---------- | ---------------------------- | ------- |
| 1          | VDD\_5V\_SBUS\_RC            | 5.0V    |
| 2          | RX\_SBUS\_IN\_EXT            | 3.3V    |
| 3          | USART6\_TX\_RC\_OUTPUT\_EXT  | 3.3V    |
| 4          | VDD\_3V3\_SPEKTRUM           | 3.3V    |
| 5          | GND                          | GND     |

### **PWM**

| Pin Number | Signal Name             | Voltage    |
| ---------- | ----------------------- | ---------- |
| 1          | VDD SERVO (NO CONNECT)  | NO CONNECT |
| 2          | FMU\_CH1\_EXT           | 3.3V       |
| 3          | FMU\_CH2\_EXT           | 3.3V       |
| 4          | FMU\_CH3\_EXT           | 3.3V       |
| 5          | FMU\_CH4\_EXT           | 3.3V       |
| 6          | FMU\_CH5\_EXT           | 3.3V       |
| 7          | FMU\_CH6\_EXT           | 3.3V       |
| 8          | FMU\_CH7\_EXT           | 3.3V       |
| 9          | FMU\_CH8\_EXT           | 3.3V       |
| 10         | GND                     | GND        |

### **ADIO**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_PERIPH  | 5.0V    |
| 2          | FMU\_CAP\_EXT    | 3.3V    |
| 3          | NARMED\_EXT      | 3.3V    |
| 4          | ADC1\_3V3\_EXT   | 3.3V    |
| 5          | ADC1\_6V6\_EXT   | 6.6V    |
| 6          | GND              | GND     |

### **SPI6**

| Pin Number | Signal Name        | Voltage |
| ---------- | ------------------ | ------- |
| 1          | VDD\_5V\_PERIPH    | 5.0V    |
| 2          | SPI6\_SCK\_EXT     | 3.3V    |
| 3          | SPI6\_MISO\_EXT    | 3.3V    |
| 4          | SPI6\_MOSI\_EXT    | 3.3V    |
| 5          | SPI6\_NCS1\_EXT    | 3.3V    |
| 6          | SPI6\_NCS2\_EXT    | 3.3V    |
| 7          | SPIX\_NSYNC\_EXT   | 3.3V    |
| 8          | SPI6\_DRDY1\_EXT   | 3.3V    |
| 9          | SPI6\_DRDY2\_EXT   | 3.3V    |
| 10         | SPI6\_NRESET\_EXT  | 3.3V    |
| 11         | GND                | GND     |

### **I2C3**

| Pin Number | Signal Name     | Voltage |
| ---------- | --------------- | ------- |
| 1          | VDD\_5V\_PERIPH | 5.0V    |
| 2          | I2C3\_SCL\_EXT  | 3.3V    |
| 3          | I2C3\_SDA\_EXT  | 3.3V    |
| 4          | GND             | GND     |

### **UART4/I2C3**

| Pin Number | Signal Name     | Voltage |
| ---------- | --------------- | ------- |
| 1          | VDD\_5V\_PERIPH | 5.0V    |
| 2          | UART4\_TX\_EXT  | 3.3V    |
| 3          | UART4\_RX\_EXT  | 3.3V    |
| 4          | I2C3\_SCL\_EXT  | 3.3V    |
| 5          | I2C3\_SDA\_EXT  | 3.3V    |
| 6          | GND             | GND     |

### **FC Debug**

| Pin Number | Signal Name             | Voltage |
| ---------- | ----------------------- | ------- |
| 1          | 3V3\_FMU                | 3.3V    |
| 2          | USART3\_TX\_DEBUG       | 3.3V    |
| 3          | USART3\_RX\_DEBUG\_EXT  | 3.3V    |
| 4          | FMU\_SWDIO              | 3.3V    |
| 5          | FMU\_SWCLK              | 3.3V    |
| 6          | SPI6\_SCK\_EXTERNAL1    | 3.3V    |
| 7          | NFC\_GPIO               | 3.3V    |
| 8          | PD15                    | 3.3V    |
| 9          | FMU\_NRST               | 3.3V    |
| 10         | GND                     | GND     |

### **Jetson SPI0**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_JPERIPH | 5.0V    |
| 2          | SPI0\_MOSI\_3V3  | 3.3V    |
| 3          | SPI0\_SCK\_3V3   | 3.3V    |
| 4          | SPI0\_MISO\_3V3  | 3.3V    |
| 5          | SPI0\_CS0N\_3V3  | 3.3V    |
| 6          | SPI0\_CS1N\_3V3  | 3.3V    |
| 7          | GND              | GND     |

### **Jetson SPI1**

| Pin Number | Signal Name      | Voltage    |
| ---------- | ---------------- | ---------- |
| 1          | VDD\_5V\_JPERIPH | 5.0V       |
| 2          | SPI1\_MOSI\_3V3  | 3.3V       |
| 3          | SPI1\_SCK\_3V3   | 3.3V       |
| 4          | SPI1\_MISO\_3V3  | 3.3V       |
| 5          | SPI1\_CS0N\_3V3  | 3.3V       |
| 6          | NO CONNECT       | NO CONNECT |
| 7          | GND              | GND        |

### **Jetson I2S0**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_JPERIPH | 5.0V    |
| 2          | I2S0\_DOUT\_3V3  | 3.3V    |
| 3          | I2S0\_DIN\_3V3   | 3.3V    |
| 4          | I2S0\_LRCLK\_3V3 | 3.3V    |
| 5          | I2S0\_SCLK\_3V3  | 3.3V    |
| 6          | AUD\_MCLK\_3V3   | 3.3V    |
| 7          | GND              | GND     |

### **Jetson I2C0**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_JPERIPH | 5.0V    |
| 2          | I2C0\_SCL\_EXT   | 3.3V    |
| 3          | I2C0\_SDA\_EXT   | 3.3V    |
| 4          | GND              | GND     |

### **Jetson CAN**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | VDD\_5V\_JPERIPH | 5.0V    |
| 2          | JCAN\_H          | 3.3V    |
| 3          | JCAN\_L          | 3.3V    |
| 4          | GND              | GND     |

### **Jetson Fan**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | GND              | GND     |
| 2          | VDD\_5V\_JPERIPH | 5.0V    |
| 3          | FAN\_TACH\_CON   | 5.0V    |
| 4          | FAN\_PWM\_Q\*    | 5.0V    |

### **Jetson M.2 Key E**

| Pin Number   | Signal Name                | Voltage |
| ------------ | -------------------------- | ------- |
| 2, 4, 72, 74 | 3V3                        | 3.3V    |
| 3            | HUB\_USB4\_M2\_P           | 3.3V    |
| 5            | HUB\_USB4\_M2\_N           | 3.3V    |
| 8            | I2S1\_SCLK                 | 1.8V    |
| 10           | I2S1\_LRCLK                | 1.8V    |
| 12           | I2S1\_DIN                  | 1.8V    |
| 14           | I2S1\_DOUT                 | 1.8V    |
| 20           | BT\_M2\_WAKE\_AP (GPIO02)  | 1.8V    |
| 22           | UART0\_RXD\_1V8            | 1.8V    |
| 32           | UART0\_TXD\_1V8            | 1.8V    |
| 34           | UART0\_CTS\_1V8            | 1.8V    |
| 36           | UART0\_RTS\_1V8            | 1.8V    |
| 58           | I2C\_M2\_DATA\_1V8         | 1.8V    |
| 60           | I2C\_M2\_CLK\_1V8          | 1.8V    |

### **Jetson Debug**

| Pin Number | Signal Name      | Voltage    |
| ---------- | ---------------- | ---------- |
| 1          | 3V3              | 3.3V       |
| 2          | UART2\_TXD\_3V3  | 3.3V       |
| 3          | UART2\_RXD\_3V3  | 3.3V       |
| 4          | NO CONNECT       | NO CONNECT |
| 5          | NO CONNECT       | NO CONNECT |
| 6          | GND              | GND        |

### **Jetson CSI0**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | 3V3              | 3.3V    |
| 2          | CAM0\_SDA        | 3.3V    |
| 3          | CAM0\_SCL        | 3.3V    |
| 4          | CAM0\_MCLK       | 1.8V    |
| 5          | CAM0\_PWDN\_3V3  | 3.3V    |
| 6          | GND              | GND     |
| 7          | CSI0\_CLK\_P     | 1.2V    |
| 8          | CSI0\_CLK\_N     | 1.2V    |
| 9          | GND              | GND     |
| 10         | CSI0\_D1\_P      | 1.2V    |
| 11         | CSI0\_D1\_N      | 1.2V    |
| 12         | GND              | GND     |
| 13         | CSI0\_D0\_P      | 1.2V    |
| 14         | CSI0\_D0\_N      | 1.2V    |
| 15         | GND              | GND     |

### **Jetson CSI1**

| Pin Number | Signal Name      | Voltage |
| ---------- | ---------------- | ------- |
| 1          | 3V3              | 3.3V    |
| 2          | CAM1\_SDA        | 3.3V    |
| 3          | CAM1\_SCL        | 3.3V    |
| 4          | CAM1\_MCLK       | 1.8V    |
| 5          | CAM1\_PWDN\_3V3  | 3.3V    |
| 6          | GND              | GND     |
| 7          | CSI1\_CLK\_P     | 1.2V    |
| 8          | CSI1\_CLK\_N     | 1.2V    |
| 9          | GND              | GND     |
| 10         | CSI1\_D1\_P      | 1.2V    |
| 11         | CSI1\_D1\_N      | 1.2V    |
| 12         | GND              | GND     |
| 13         | CSI1\_D0\_P      | 1.2V    |
| 14         | CSI1\_D0\_N      | 1.2V    |
| 15         | GND              | GND     |

### **Jetson CSI2**

| Pin Number | Signal Name                                     | Voltage |
| ---------- | ----------------------------------------------- | ------- |
| 1          | 3V3                                             | 3.3V    |
| 2          | CAM2\_SDA                                       | 3.3V    |
| 3          | CAM2\_SCL                                       | 3.3V    |
| 4          | CAM2\_MCLK (GPIO01 GP65)                        | 1.8V    |
| 5          | CAM2\_PWDN\_3V3 (SPI1\_CS1\* GP40\_SPI3\_CS1)   | 3.3V    |
| 6          | GND                                             | GND     |
| 7          | CSI2\_CLK\_P                                    | 1.2V    |
| 8          | CSI2\_CLK\_N                                    | 1.2V    |
| 9          | GND                                             | GND     |
| 10         | CSI2\_D1\_P                                     | 1.2V    |
| 11         | CSI2\_D1\_N                                     | 1.2V    |
| 12         | GND                                             | GND     |
| 13         | CSI2\_D0\_P                                     | 1.2V    |
| 14         | CSI2\_D0\_N                                     | 1.2V    |
| 15         | GND                                             | GND     |

### **Jetson CSI3**

| Pin Number | Signal Name              | Voltage |
| ---------- | ------------------------ | ------- |
| 1          | 3V3                      | 3.3V    |
| 2          | CAM3\_SDA                | 3.3V    |
| 3          | CAM3\_SCL                | 3.3V    |
| 4          | CAM3\_MCLK (GPIO11 GP66) | 1.8V    |
| 5          | CAM3\_PWDN\_3V3 (GPIO06) | 3.3V    |
| 6          | GND                      | GND     |
| 7          | CSI3\_CLK\_P             | 1.2V    |
| 8          | CSI3\_CLK\_N             | 1.2V    |
| 9          | GND                      | GND     |
| 10         | CSI3\_D1\_P              | 1.2V    |
| 11         | CSI3\_D1\_N              | 1.2V    |
| 12         | GND                      | GND     |
| 13         | CSI3\_D0\_P              | 1.2V    |
| 14         | CSI3\_D0\_N              | 1.2V    |
| 15         | GND                      | GND     |
