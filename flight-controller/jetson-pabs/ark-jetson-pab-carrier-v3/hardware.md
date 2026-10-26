---
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/hardware.md
---

# Hardware Reference

* [Pinout](pinout.md)
* [Block Diagram](block-diagram.md)
* [3D Model](3d-models-and-case-files.md)
* [GPIO Control](gpio-control.md)
* [Camera Overlays](camera-overlays.md)
* [Power Cycling USB Ports](power-cycling-usb-ports.md)

## Temperature

| Specification | Value |
|---------------|-------|
| Operating temperature | −10 °C to +60 °C, carrier only |
| Storage temperature | −10 °C to +60 °C, carrier only |

The RTC backup supercapacitor sets both ranges. The next limit is the USB hub's crystal and the blue status LED, −20 °C to +80 °C. Jetson Orin NX and Orin Nano modules are rated −25 °C to +105 °C junction.
