# Pinout

### PWM

10 pin JST-GH&#x20;

| Pin | Signal        | Voltage       |
| --- | ------------- | ------------- |
| 1   | VDD\_SERVO\_1 | VDD\_SERVO\_1 |
| 2   | CH0\_EXT      | +3.3V         |
| 3   | CH1\_EXT      | +3.3V         |
| 4   | CH2\_EXT      | +3.3V         |
| 5   | CH3\_EXT      | +3.3V         |
| 6   | CH4\_EXT      | +3.3V         |
| 7   | CH5\_EXT      | +3.3V         |
| 8   | CH6\_EXT      | +3.3V         |
| 9   | CH7\_EXT      | +3.3V         |
| 10  | GND           | GND           |

### PWM

10 pin JST-GH&#x20;

| Pin | Signal        | Voltage       |
| --- | ------------- | ------------- |
| 1   | VDD\_SERVO\_2 | VDD\_SERVO\_2 |
| 2   | CH8\_EXT      | +3.3V         |
| 3   | CH9\_EXT      | +3.3V         |
| 4   | CH10\_EXT     | +3.3V         |
| 5   | CH11\_EXT     | +3.3V         |
| 6   | CH12\_EXT     | +3.3V         |
| 7   | CH13\_EXT     | +3.3V         |
| 8   | CH14\_EXT     | +3.3V         |
| 9   | CH15\_EXT     | +3.3V         |
| 10  | GND           | GND           |

### I2C

4 pin JST-GH&#x20;

| Pin | Signal   | Voltage |
| --- | -------- | ------- |
| 1   | 5V\_IN   | +5.0V   |
| 2   | I2C\_SCL | +3.3V   |
| 3   | I2C\_SDA | +3.3V   |
| 4   | GND      | GND     |

### Resistor Settings

VDD\_SERVO\_1 and VDD\_SERVO\_2 can be connected together by shorting the pads of the large unpopulated resistor. Either with solder or a 0 Ohm 0805 resistor.

The I2C address can be changed by moving the resistors from the left position to the right position to change the bit from 0 to 1.&#x20;

<figure><img src="../../.gitbook/assets/Bottom Settings.png" alt=""><figcaption></figcaption></figure>
