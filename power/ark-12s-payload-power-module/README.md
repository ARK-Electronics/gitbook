---
cover: ../../.gitbook/assets/IMG_4889 edited.JPG
coverY: -9.684210526315788
---

# ARK 12S Payload Power Module

The ARK 12S Payload Power Module is rated for 100A continuous battery current at 20C ambient. It is recommended to run multiple power modules in parallel if more than 100A continuous current is required.

The board uses an INA238 digital power monitor with a 0.1mΩ shunt to measure voltage and current over I2C. A 5.2V 6A regulator outputs power to the avionics using a 6 pin Molex CLIK-Mate connector that matches the pinout on the ARK PAB Carriers. A 12V 6A regulator outputs power to payloads using a 4 pin Molex CLIK-Mate connector.

{% content-ref url="px4-instructions.md" %}
[px4-instructions.md](px4-instructions.md)
{% endcontent-ref %}

{% content-ref url="ardupilot-instructions.md" %}
[ardupilot-instructions.md](ardupilot-instructions.md)
{% endcontent-ref %}

{% content-ref url="3d-model.md" %}
[3d-model.md](3d-model.md)
{% endcontent-ref %}

### Cooling

When operating at high battery current and/or high 5V/12V regulator output current, it is recommended to actively cool the board.

### Pinout

#### 5V/I2C - 6 Pin Molex CLIK-Mate

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VBRICK</td><td>5.2V</td></tr><tr><td>2</td><td>VBRICK</td><td>5.2V</td></tr><tr><td>3</td><td>SCL</td><td>3.3V</td></tr><tr><td>4</td><td>SDA</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

#### 12V - 4 Pin Molex CLIK-Mate

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>12V</td><td>12.0V</td></tr><tr><td>2</td><td>12V</td><td>12.0V</td></tr><tr><td>3</td><td>GND</td><td>GND</td></tr><tr><td>4</td><td>GND</td><td>GND</td></tr></tbody></table>
