# Ports and Serial

## Micro USB

Plugging in the Micro USB port disconnects the flight controller's USB from the Jetson and puts the Jetson in device mode, providing networking, a serial login console, and an `L4T-README` drive — see [Connect](setup/connect.md) and [Micro USB Console](micro-usb-console.md). It is also the recovery port for [flashing](flashing-guide.md).

## Serial Ports

<table><thead><tr><th width="160">Connector</th><th width="140">Port</th><th width="160">Available Signals</th><th>Function</th></tr></thead><tbody><tr><td>Flight controller (internal)</td><td>/dev/ttyTHS1</td><td>RX/TX/RTS/CTS</td><td>FC TELEM2. The ARK-OS DDS agent uses it by default at 3 Mbaud.</td></tr><tr><td>Jetson Debug (6-pin JST-SH)</td><td>/dev/ttyTCU0</td><td>RX/TX</td><td>Jetson debug UART and Linux console (Reserved)</td></tr><tr><td>M.2 Key E</td><td>/dev/ttyTHS3</td><td>RX/TX/RTS/CTS</td><td>Bluetooth UART of an M.2 card</td></tr></tbody></table>

The debug UART runs at 115200 8N1, 3.3 V, and carries bootloader, UEFI and kernel output plus a login prompt. Connector pins are on the [Pinout](pinout.md) page.
