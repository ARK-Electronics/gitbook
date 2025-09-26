---
description: >-
  This guide outlines the steps to configure a Jetson device with an ARK M.2 LTE
  modem and a Ground Control Station (GCS) to connect through an OpenVPN Access
  Server on AWS.
---

# OpenVPN

### Prerequisites

* OpenVPN Access Server set up on AWS EC2 (refer to [OpenVPN AWS EC2 Setup Guide](https://openvpn.net/as-docs/aws-ec2.html)).
* Jetson device with ARK M.2 LTE modem for internet connectivity.
* Ground Control Station running Linux with QGroundControl installed.
* Internet access for both devices

### OpenVPN Access Server setup

1.  Access the OpenVPN Admin Panel. Open a browser and login using your admin credentials. The default admin user is **openvpn**.

    ```vbnet
    https://<AWS-instance-public-IP>/admin
    ```
2. Under **Configuration -> VPN Settings -> Static IP Address Network** section, set up the subnet:
   * Network Address: `172.27.17.0`
   * Netmask Bits: `24`
3. Add the Subnet **172.27.17.0/24** to the **Routing** table:
4. Create Jetson user and assign a static IP
   1. Under **User Management** -> **User Permissions** create new user `jetson`. Ensure **Allow auto-login** is selected for both `jetson` and `openvpn` users and click **Save Settings.**
   2. On the `jetson` user click **More Settings** and under **IP Addressing** select **Use Static**. Assign a static IP address in the subnet 172.27.17.0. For example **172.27.17.10**
5. Create user profiles for Jetson and GCS
   1. Under **User Management** -> **User Profiles** create a new profile for the openvpn and jetson users. Ensure **Autologin** is selected..
   2. After creating the profile, the **.ovpn** configuration file will download automatically. This will will only be downloaded once. You must delete and recreate the profile if you lose this file.

### Configure OpenVPN clients

Perform these steps on both the Jetson and GCS, using the **.ovpn** file for each device. This will install OpenVPN and configure it to start automatically at boot using systemd.

1.  Install OpenVPN:

    ```bash
    sudo apt install openvpn -y
    ```
2.  Transfer the Jetson **.ovpn** file from the Host PC to the Jetson

    ```bash
    scp /path/to/jetson.ovpn jetson@jetson.local:/home/jetson/
    ```
3.  Move and rename the OpenVPN configuration:

    ```bash
    sudo mv ~/<config_file>.ovpn /etc/openvpn/client.conf
    ```
4.  Enable the service to start automatically on boot:

    ```bash
    sudo systemctl enable openvpn@client
    ```
5.  Start the OpenVPN Service:

    ```bash
    sudo systemctl start openvpn@client
    ```
6.  Verify VPN Connection:

    ```bash
    ip addr show tun0
    ```

### Verify VPN Connection Between Jetson and GCS

You should now be able to ping the Jetsons VPN IP addresss from the GCS and vice versa:

*   On the **Jetson**:

    ```bash
    ping <gcs-vpn-ip>
    ```
*   On the **GCS**:

    ```bash
    ping <jetson-vpn-ip>
    ```

### Troubleshooting

* **Connected but clients cant ping?** Under **VPN Settings - Routing**, ensure clients are given access to the subnet.
