# Connections

## USB C

The USB-C port supports dual role operation, functioning as both host and device. When connected to a host PC, it provides network connectivity and automatically assigns the IP address 192.168.55.100 to your computer, allowing you to SSH into the device:

```
ssh jetson@jetson.local
```

OR if you've changed either the username or hostname:

```
ssh <username>@192.168.55.1
```

It is also possible to share the internet connection of your host PC with the Jetson over this USB interface by enabling IP packet forwarding as seen in this [example script](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/share_wifi.sh).

## Serial Ports

<table><thead><tr><th width="101">Connector</th><th width="152">Port</th><th width="198">Available Signals</th><th>Function</th></tr></thead><tbody><tr><td>UART0</td><td>/dev/ttyTHS3</td><td>RX/TX/RTS/CTS</td><td>User Available</td></tr><tr><td>UART1</td><td>/dev/ttyTHS1</td><td>RX/TX/RTS/CTS</td><td>User Available</td></tr><tr><td>UART2</td><td>/dev/ttyTHS2</td><td>RX/TX</td><td>Linux Console (Reserved)</td></tr></tbody></table>

