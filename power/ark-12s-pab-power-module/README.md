---
cover: ../../.gitbook/assets/IMG_4984 edited.JPG
coverY: 0
---

# ARK 12S PAB Power Module

The ARK 12S PAB Power Module is rated for 100A continuous battery current at 20C ambient. It is recommended to run multiple power modules in parallel if more than 100A continuous current is required.

The board uses an INA238 digital power monitor with a 0.1mΩ shunt to measure voltage and current over I2C. A 5.2V 6A regulator outputs power to the avionics using a 6 pin Molex CLIK-Mate connector that matches the pinout on the ARK PAB Carriers.

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

When operating at high battery current and/or high 5V regulator output current, it is recommended to actively cool the board.

### Pinout

#### 5V/I2C - 6 Pin Molex CLIK-Mate

<table><thead><tr><th width="134">Pin Number</th><th width="237">Signal Name</th><th>Voltage</th></tr></thead><tbody><tr><td>1</td><td>VBRICK</td><td>5.2V</td></tr><tr><td>2</td><td>VBRICK</td><td>5.2V</td></tr><tr><td>3</td><td>SCL</td><td>3.3V</td></tr><tr><td>4</td><td>SDA</td><td>3.3V</td></tr><tr><td>5</td><td>GND</td><td>GND</td></tr><tr><td>6</td><td>GND</td><td>GND</td></tr></tbody></table>

### Capacitor and TVS Diode

<figure><img src="../../.gitbook/assets/IMG_3824 edited.JPG" alt=""><figcaption><p>12S with Capacitor and TVS Diode</p></figcaption></figure>

When operating with 12S batteries, it is recommended to solder the included capacitor and TVS diode to the output side of the board. The negative of the capacitor is indicated on the cylinder. The cathode(line) on the TVS diode should be soldered to the positive side of the output.

