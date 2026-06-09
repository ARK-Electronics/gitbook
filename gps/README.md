# GPS

ARK GPS and RTK GPS modules for precision navigation.

{% content-ref url="ark-dan-gps/" %}
[ark-dan-gps](ark-dan-gps/)
{% endcontent-ref %}

{% content-ref url="ark-g5-rtk-gps/" %}
[ark-g5-rtk-gps](ark-g5-rtk-gps/)
{% endcontent-ref %}

{% content-ref url="ark-gps/" %}
[ark-gps](ark-gps/)
{% endcontent-ref %}

{% content-ref url="ark-mosaic-x5-rtk-gps/" %}
[ark-mosaic-x5-rtk-gps](ark-mosaic-x5-rtk-gps/)
{% endcontent-ref %}

{% content-ref url="ark-rtk-base/" %}
[ark-rtk-base](ark-rtk-base/)
{% endcontent-ref %}

{% content-ref url="ark-rtk-gps/" %}
[ark-rtk-gps](ark-rtk-gps/)
{% endcontent-ref %}

{% content-ref url="ark-sam-gps/" %}
[ark-sam-gps](ark-sam-gps/)
{% endcontent-ref %}

{% content-ref url="ark-teseo-gps/" %}
[ark-teseo-gps](ark-teseo-gps/)
{% endcontent-ref %}

{% content-ref url="ark-x20-rtk-gps.md" %}
[ark-x20-rtk-gps.md](ark-x20-rtk-gps.md)
{% endcontent-ref %}

## Comparison

| Product                                            | GNSS Receiver            | Bands    | RTK                              | Heading                                 | Spoofing/Jamming Resistance                                    | Interface                 | Onboard Sensors              |
| -------------------------------------------------- | ------------------------ | -------- | -------------------------------- | --------------------------------------- | -------------------------------------------------------------- | ------------------------- | ---------------------------- |
| [ARK SAM GPS](ark-sam-gps/)                        | u-blox SAM-M10Q          | L1       | —                                | —                                       | Jamming detection                                              | UART + I2C (6-pin JST-GH) | Magnetometer                 |
| [ARK DAN GPS](ark-dan-gps/)                        | u-blox DAN-F10N          | L1/L5    | —                                | —                                       | Jamming/spoofing detection, dual-band resilience               | UART + I2C (6-pin JST-GH) | Magnetometer                 |
| [ARK GPS](ark-gps/)                                | u-blox NEO-M9N           | L1       | —                                | —                                       | Jamming/spoofing detection                                     | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK TESEO GPS](ark-teseo-gps/)                    | ST Teseo-LIV4F           | L1/L5    | —                                | —                                       | Jamming/spoofing detection, dual-band resilience               | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK RTK GPS](ark-rtk-gps/)                        | u-blox ZED-F9P           | L1/L2    | Yes                              | Moving baseline (two units)             | Jamming/spoofing detection, dual-band resilience               | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK X20 RTK GPS](ark-x20-rtk-gps.md)              | u-blox ZED-X20P          | L1/L2/L5 | Yes                              | —                                       | Advanced anti-jamming/anti-spoofing, triple-band resilience    | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK MOSAIC-X5 RTK GPS](ark-mosaic-x5-rtk-gps/)    | Septentrio mosaic-X5     | L1/L2/L5 | Yes                              | —                                       | AIM+ anti-jamming/anti-spoofing, OSNMA, triple-band resilience | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK G5 RTK GPS](ark-g5-rtk-gps/)                  | Septentrio mosaic-G5 P3  | L1/L5    | Yes                              | —                                       | AIM+ anti-jamming/anti-spoofing, OSNMA, dual-band resilience   | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK G5H RTK Heading GPS](ark-g5-rtk-heading-gps/) | Septentrio mosaic-G5 P3H | L1/L5    | Yes                              | Dual antenna (internal moving baseline) | AIM+ anti-jamming/anti-spoofing, OSNMA, dual-band resilience   | DroneCAN                  | Magnetometer, barometer, IMU |
| [ARK RTK Base](ark-rtk-base/)                      | u-blox ZED-F9P           | L1/L2    | Base station or standalone rover | —                                       | Jamming/spoofing detection, dual-band resilience               | USB-C, UART               | —                            |

The serial modules (SAM, DAN) connect to a flight controller GPS port over UART and expose their magnetometer on I2C. The DroneCAN modules connect over CAN and publish GPS, magnetometer, barometer, and IMU data on the bus. The ARK RTK Base provides RTCM corrections for the RTK rovers from the ground side, and can also be used as a standalone RTK GPS rover.
