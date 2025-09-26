# Power Cycling USB Ports

The USB ports can be power cycled from the command line through using uhubctl for three of the ports and a GPIO for the fourth.

The single USB 2.0 port and the two USB 3 ports that are on the combined connector are controlled by the USB hub. Use uhubctl to cycle power on those ports. Ports 1 and 2 are the USB 3 connectors and port 3 is the USB 2.0 connector.

```
sudo uhubctl -l 1-2 -a off
sudo uhubctl -l 1-2 -a on
```

The standalone USB 3 port is controlled by GPIO12. Use the gpioset command as an open drain to drive low for a short amount of time. There is a pullup on the signal to 1.8V and it is also connected to the open drain FLG output of the current monitor to shut off the port in an over current event.

```
sudo gpioset --drive=open-drain --mode=time -s 1 gpiochip0 85=0
```
