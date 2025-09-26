---
description: >-
  This guide will help you set up the ARK Jetson PAB Carrier with the RC7611 LTE
  module.
cover: ../../.gitbook/assets/IMG_2982 edited (Large).JPG
coverY: -14
---

# ARK M.2 LTE

### Prerequisites

* A nano-SIM card with a data plan.
* The ARK M.2 LTE module.
* Correct antennas connected
* A Kernel with QMI\_WWAN support (already included in the [ARK Jetson Kernel](https://github.com/ARK-Electronics/ark_jetson_kernel))

### 1. Install the Nano-SIM

Insert the nano-SIM into the ARK M.2 LTE module.

### 2. Build and Flash the Kernel

Skip this step if you purchased a pre-flashed ARK Jetson Bundle.

The RC7611 requires the QMI\_WWAN kernel module, which is not included by default in Jetpack 6. You will need to manually build and flash the kernel onto the Jetson device.

1.  Clone the kernel repository:

    ```bash
    git clone https://github.com/ARK-Electronics/ark_jetson_kernel
    ```
2.  Use the **setup\_source\_build.sh** script to enable the necessary kernel modules.

    [Follow the instructions in the ARK Jetson Kernel repository](https://github.com/ARK-Electronics/ark_jetson_kernel?tab=readme-ov-file#building-from-source)

Once the kernel is built and flashed, boot up the Jetson device.

### 3. Connect to the Device

Connect a Micro USB cable and SSH in:

```
ssh jetson@jetson.local
```

### 4. Determine the Modem Instance Number

Run the following command to list the modem instances:

```bash
mmcli -L
```

You should see something like:

> /org/freedesktop/ModemManager1/Modem/0 \[Sierra Wireless, Incorporated] RC7611

Take note of the **instance number** of the modem (in this case, `0`).

### 5. Configure Initial EPS Bearer Settings

Set the initial EPS bearer settings to register the device with the network:

```bash
sudo mmcli -m 0 --3gpp-set-initial-eps-bearer-settings="apn=<your_apn>"
```

{% hint style="info" %}
T-Mobile APN: **fast.t-mobile.com**

AT\&T APN: **broadband**
{% endhint %}

If successful, it will print:

> Successfully set initial EPS bearer properties

### 6. Connect the Modem to the Network

Run the following command to connect your device to the network. For example using T-Mobile:

```bash
sudo mmcli -m 0 --simple-connect="apn=fast.t-mobile.com,ip-type=ipv4v6"
```

If successful, it will print:

> Successfully connected the modem

### 7. Verify the Modem Status

To check the modem’s status, run:

```bash
mmcli -m 0
```

Ensure that the state is **connected** and the packet service state is **attached**. Note the first Bearer path at the bottom to determine the Bearer Index:

> ***
>
> Bearer | paths: /org/freedesktop/ModemManager1/Bearer/1

In our case the Bearer Index is 1.

### 8. Query Bearer Settings

Use the index of the first bearer path to query the bearer settings.

```bash
mmcli -m 0 --bearer=1
```

Take note of the IPv4 configuration

```
  ------------------------------------
  IPv4 configuration |         method: static
                     |        address: 162.177.172.180
                     |         prefix: 29
                     |        gateway: 162.177.172.181
                     |            dns: 10.177.0.34, 10.177.0.210
                     |            mtu: 1500
  ------------------------------------
```

### 9. Set Up the Wireless Interface

Use the values from the above IPv4 configuration for **address**, **prefix**, **gateway**, and **mtu.**

1.  Bring up the **wwan0** interface:

    ```bash
    sudo ip link set wwan0 up
    ```
2.  Assign the IP address:

    ```bash
    sudo ip addr add <address>/<prefix> dev wwan0
    ```
3.  Disable ARP on **wwan0**:

    ```bash
    sudo ip link set dev wwan0 arp off
    ```
4.  Set the MTU:

    ```bash
    sudo ip link set wwan0 mtu <mtu>
    ```
5.  Add a default route:

    ```bash
    sudo ip route add default via <gateway> dev wwan0 metric 4294967295
    ```

{% hint style="info" %}
The **metric** option ensures links like WiFi or Ethernet are prioritized ahead of LTE
{% endhint %}

### 10. Configure DNS (Optional)

To use the DNS servers provided by the cellular connection, run the following commands:

```bash
sudo sh -c "echo 'nameserver 10.177.0.34' >> /etc/resolv.conf"
sudo sh -c "echo 'nameserver 10.177.0.210' >> /etc/resolv.conf"
```

### 11. Test the Connection

```bash
ping -4 -c 4 -I wwan0 8.8.8.8
```

### Troubleshooting

* **Modem not registering?** Double-check the APN value.
* **Modem not detected?** Ensure the required kernel modules are enabled.
* **SIM card inactive?** Make sure your SIM has a valid data plan.

## 3D Model

Find the 3D model at [https://github.com/ARK-Electronics/ARK\_M.2\_LTE](https://github.com/ARK-Electronics/ARK_M.2_LTE)
