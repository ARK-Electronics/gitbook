---
description: This page explains the function of each ARK-OS service.
---

# Services

This collection of services is referred to as ARK-OS and is installed using the [ARK-OS repository](https://github.com/ARK-Electronics/ARK-OS). The services are installed as [systemd user services](https://www.unixsysadmin.com/systemd-user-services/) and follow the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/).

## Mavlink Router

The **mavlink-router** service routes the MAVLink data from the Pi USB port **/dev/ttyACM0** to user defined UDP endpoints. The Pi USB port is connected directly to the Flight Controller USB and is capable of 3Mbps.

{% hint style="warning" %}
The Pi Micro-USB is muxed with the Flight controller USB. The Flight Controller USB connection will not work while the Micro-USB is connected.
{% endhint %}

The configuration can be edited in the [ARK-UI](http://jetson.local/). The default configuration is found here:

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/ARK-OS/blob/main/platform/pi/main.conf" %}

***

## Logloader

The **logloader** service automatically downloads the PX4 **.ulg** flight logs from the Flight Controller SD card after each flight. It will automatically upload the log to a locally hosted [Flight Review ](https://review.px4.io/)server and optionally upload to a remotely hosted server.

The configuration can be edited in the [ARK-UI](http://jetson.local/). The default configuration is found here:

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/logloader/blob/main/config.toml" %}

***

## Flight Review

The **flight-review** service is a locally hosted instance of the [PX4 Flight Review](https://github.com/PX4/flight_review) web application for flight log plotting and analysis. It can be accessed at [http://pi6x.local/flight-review/](http://jetson.local/flight-review/). By default all logs downloaded by **logloader** will be visible on the local server.

***

## DDS Agent

The **dds-agent** service bridges the [PX4 uORB ](https://docs.px4.io/main/en/middleware/uorb.html)pub/sub system to ROS2 topics on the Pi. The bridged topics are defined in PX4 Firmware and can be [found here](https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/uxrce_dds_client/dds_topics.yaml).\
\
The **dds-agent** runs the [micro-xrce-dds-agent ](https://github.com/eProsima/Micro-XRCE-DDS-Agent)on the **/dev/ttyAMA4** serial port of the Pi. This serial port is connected directly to the Flight Controller **Telem2** port and is capable of 3Mbps.

The Flight Controller firmware needs to be configured by setting these parameters:

| Parameter       | Value   | Description |
| --------------- | ------- | ----------- |
| UXRCE\_DDS\_CFG | 102     |  TELEM 2    |
| SER\_TEL2\_BAUD | 3000000 | 3000000 8N1 |

For more information please see the official [PX4 docs for UXRCE DDS](https://docs.px4.io/main/en/middleware/uxrce_dds.html).

***

## Hostspot Control

The **hotspot-control** service configures the Pi as a hotspot if it is unable to connect to a WiFi network after 1 minute from booting. It will create a hotspot with the name **pi6x-\<serialnumber>** with a password of **password.** Once connected to the hotspot you can go to [http://pi6x.local](http://jetson.local/) to connect to your local network.

***

## Polaris

The **polaris** service provides a client interface to the Point One [Polaris RTK Correction Network](https://pointonenav.com/polaris). This service allows you to receive network RTK corrections over the internet with an active Point One subscription. This allows you to achieve centimeter precision position hold anywhere the network is available.\


The configuration can be edited in the [ARK-UI](http://jetson.local/). The default configuration is found here:

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/polaris-client-mavlink/blob/main/config.toml" %}

***

## RTSP Server

The **rtsp-server** service provides a RTSP Server for live streaming video. The server uses gstreamer and is currently only compatible with CSI cameras, for example **/dev/video0.** Stay tuned for future plans to support both CSI and USB cameras.

The configuration can be edited in the [ARK-UI](http://jetson.local/). The default configuration is found here:

{% @github-files/github-code-block url="https://github.com/ARK-Electronics/rtsp-server/blob/main/config.toml" %}

***

## ARK UI Backend

The **ark-ui-backend** service is a REST API backend for the ARK-UI. It provides API endpoints for managing services, querying device information, and updating the Flight Controller firmware.

***
