# Power Cycling USB Ports

The V3's USB 2.0 ports run through an onboard USB hub and can be power cycled from the command line with [uhubctl](https://github.com/mvp/uhubctl).

List the hubs and ports that support power switching:

```
sudo uhubctl
```

Cycle power on a port:

```
sudo uhubctl -l <hub> -p <port> -a off
sudo uhubctl -l <hub> -p <port> -a on
```
