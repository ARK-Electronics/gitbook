# Ports and Serial

## USB C

The USB-C port supports dual role operation, functioning as both host and device. In device mode it provides networking, a serial console, and an `L4T-README` drive — see [Connect](setup/connect.md) and [USB-C Console](usb-c-console.md).

## Serial Ports

<table><thead><tr><th width="101">Connector</th><th width="152">Port</th><th width="198">Available Signals</th><th>Function</th></tr></thead><tbody><tr><td>UART0</td><td>/dev/ttyTHS3</td><td>RX/TX/RTS/CTS</td><td>User Available</td></tr><tr><td>UART1</td><td>/dev/ttyTHS1</td><td>RX/TX/RTS/CTS</td><td>User Available</td></tr><tr><td>UART2</td><td>/dev/ttyTHS2</td><td>RX/TX</td><td>Linux Console (Reserved)</td></tr></tbody></table>
