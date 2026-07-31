# Power Cycling USB Ports

The hub-connected USB ports can be power cycled from the command line with [uhubctl](https://github.com/mvp/uhubctl).

List the hubs and ports that support power switching:

```
sudo uhubctl
```

Cycle power on a port:

```
sudo uhubctl -l <hub> -p <port> -a off
sudo uhubctl -l <hub> -p <port> -a on
```
