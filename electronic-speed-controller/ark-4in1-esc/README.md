---
description: >-
  NDAA compliant, made in the USA, 4 in 1 electronic speed controller running
  open source AM32 firmware.
cover: ../../.gitbook/assets/IMG_3371 edited (Large).JPG
coverY: -23.514666666666663
---

# ARK 4IN1 ESC

{% hint style="danger" %}
**Before first use**, configure **KV** and **Pole Count** for each motor channel in the AM32 Configurator. The defaults will not match your motor and the ESC will not run correctly. See [AM32 Configuration](am32-configuration.md).
{% endhint %}

**Specifications:**

* Voltage
  * 3s – 8s Lithium Polymer Battery Input
  * 6V Minimum
  * 65V Absolute Maximum
* Current Per Motor
  * 50A Continuous
  * 75A Burst Current
* Input Protocols
  * Dshot (300, 600)
    * Bi-directional Dshot
    * KISS Serial Telemetry
  * PWM
* Dimensions
  * 43.00mm x 40.50mm x 7.60mm
  * 30.5mm Mounting Pattern
* Weight
  * 14.5g

**Capacitance:**

The ARK 4IN1 ESC has 450µF of bulk capacitance built in, which is sufficient for most 3S–6S installations with short battery leads.

{% hint style="warning" %}
For 8S and above, add an external bulk capacitor across the battery input to keep switching and inrush transients below the 65V absolute maximum. Long battery leads increase inductance and make transients worse at any voltage.
{% endhint %}

{% content-ref url="pinout.md" %}
[pinout.md](pinout.md)
{% endcontent-ref %}

{% content-ref url="firmware/" %}
[firmware](firmware/)
{% endcontent-ref %}

{% content-ref url="pwm-calibration.md" %}
[pwm-calibration.md](pwm-calibration.md)
{% endcontent-ref %}

{% content-ref url="3d-models.md" %}
[3d-models.md](3d-models.md)
{% endcontent-ref %}
