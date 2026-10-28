---
metaLinks:
  alternates:
    - ../ark-jetson-pab-carrier/ports-and-serial.md
---

# Ports and Serial

## USB-C

The USB-C port supports dual role operation, functioning as both host and device. In device mode it provides networking, a serial login console, and an `L4T-README` drive — see [Connect](setup/connect.md) and [USB-C Console](micro-usb-console.md). It is also the recovery port for [flashing](flashing-guide.md) and the carrier's only USB 3.0 port; the two JST-GH USB ports and the Payload Bus USB are USB 2.0.

## Serial Ports

<table><thead><tr><th width="160">Connector</th><th width="140">Port</th><th width="160">Available Signals</th><th>Function</th></tr></thead><tbody><tr><td>Flight controller (internal)</td><td>/dev/ttyTHS1</td><td>RX/TX/RTS/CTS</td><td>FC TELEM2. The ARK-OS DDS agent uses it by default at 3 Mbaud.</td></tr><tr><td>UART2 (6-pin JST-SH)</td><td>/dev/ttyTCU0</td><td>RX/TX</td><td>Jetson debug UART and Linux console (Reserved)</td></tr><tr><td>M.2 Key E</td><td>/dev/ttyTHS3</td><td>RX/TX/RTS/CTS</td><td>Bluetooth UART of an M.2 card</td></tr></tbody></table>

The debug UART runs at 115200 8N1, 3.3 V, and carries bootloader, UEFI and kernel output plus a login prompt. Connector pins are on the [Pinout](pinout.md) page.

No Jetson UART reaches a general-purpose connector. An external flight controller connects over a JST-GH USB port.
