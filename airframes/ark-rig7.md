---
icon: drone
cover: ../.gitbook/assets/rig7 frame.JPG
coverY: -727.1453590192643
---

# ARK RIG7

The ARK RIG7 is a 7 inch quadcopter reference design for developing on ARK electronics, built around the ARK Jetson PAB Carrier. ARK does not sell the frame or a kit. Cut the two carbon fiber plates from the design files, print the plastic parts and add the parts listed below.

## Design Files

| Files | Contents |
| ----- | -------- |
| [Fusion 360 design](https://a360.co/4703jjy) | Top and bottom frame plates |
| [ARK\_RIG7/printed\_parts in ark-hardware](https://github.com/ARK-Electronics/ark-hardware/tree/main/ARK_RIG7/printed_parts) | Landing gear and prop guard STL files |

## Parts List

### Frame and Hardware

| Part                           | Quantity | Used for                            |
| ------------------------------ | -------- | ----------------------------------- |
| Carbon fiber bottom plate      | 1        | Frame                               |
| Carbon fiber top plate         | 1        | Frame                               |
| M3x45 Standoff                 | 8        | Frame                               |
| M3x8 Screw                     | 32       | Frame/ESC/FPV FC/Jetson PAB carrier |
| M3x16 Screw                    | 20       | ARK Flow/Landing Gear/Prop Guards   |
| M3 Locknut                     | 20       | ARK Flow/Landing Gear/Prop Guards   |
| M2x16 Screw                    | 4        | GPS                                 |
| M2 Locknut                     | 4        | GPS                                 |
| M3x10 Male-Female standoff     | 4        | Connecting FPV-ESC                  |
| M3x10 Female-Female standoff   | 4        | Connecting ESC-Frame                |
| M2.5x10 Female-Female Standoff | 4        | Connecting PAB                      |
| M2.5x8 Screw                   | 8        | Connecting PAB                      |
| Printed landing gear           | 4        | Frame                               |
| Printed prop guard             | 4        | Frame                               |

### ARK Electronics

Pick one flight controller, one ESC and one GPS. The optical flow sensor is optional.

| Role              | Options |
| ----------------- | ------- |
| Flight controller | [ARKV6X](https://arkelectron.com/product/arkv6x/) on an [ARK Jetson PAB Carrier](https://arkelectron.com/product/ark-jetson-pab-carrier/), [ARKV6X Bundle](https://arkelectron.com/product/arkv6x-bundle/), [ARK FPV Flight Controller](https://arkelectron.com/product/ark-fpv-flight-controller/), [ARK Pi6X Flow](https://arkelectron.com/product/ark-pi6x-flow/), [ARK Pi6X](https://arkelectron.com/product/ark-pi6x/) |
| ESC               | [ARK 4IN1 ESC](https://arkelectron.com/product/ark-4in1-esc/), [ARK 4IN1 ESC CONS](https://arkelectron.com/product/ark-4in1-esc-cons/) |
| GPS               | [ARK GPS](https://arkelectron.com/product/ark-gps/), [ARK RTK GPS](https://arkelectron.com/product/ark-rtk-gps/), [ARK SAM GPS](https://arkelectron.com/product/ark-sam-gps/), [ARK TESEO GPS](https://arkelectron.com/product/ark-teseo-gps/), [ARK SAM GPS MINI](https://arkelectron.com/product/ark-sam-gps-mini/), [ARK DAN GPS](https://arkelectron.com/product/ark-dan-gps/) |
| Optical flow      | [ARK Flow](https://arkelectron.com/product/ark-flow/), [ARK Flow MR](https://arkelectron.com/product/ark-flow-mr/) |

### Other Parts

| Part           | Quantity | Recommended |
| -------------- | -------- | ----------- |
| Motor          | 4        | iFlight XING2 3110 1250KV |
| Propeller      | 4        | 7050 three-blade |
| Battery        | 1        | 6S LiPo |
| RC receiver    | 1        | ExpressLRS |
| WiFi telemetry | 1        | [DroneBridge](https://drone-bridge.com/). Not needed with an ARK Jetson PAB Carrier or a Pi based flight controller. |

## Gallery

<figure><img src="../.gitbook/assets/rig7 angled.JPG" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/rig7 front.JPG" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/rig7 side.JPG" alt=""><figcaption></figcaption></figure>
