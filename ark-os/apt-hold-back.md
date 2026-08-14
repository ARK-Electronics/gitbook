# Apt Upgrade: Hold Back Risky Packages

Running `apt upgrade` on the ARK Jetson image can pull in NVIDIA kernel, firmware, or driver packages that overwrite the ARK kernel and device tree, breaking WiFi, cameras, or other carrier hardware.

The ARK image already pins its camera userspace packages. Before running a full `apt upgrade`, we recommend also holding the kernel and firmware packages:

```
sudo apt-mark hold linux-firmware nvidia-l4t-kernel nvidia-l4t-kernel-dtbs nvidia-l4t-firmware nvidia-l4t-kernel-headers nvidia-l4t-kernel-oot-headers wireless-regdb
```

Show packages on hold:

```
sudo apt-mark showhold
```

Remove a hold and upgrade a specific package:

```
sudo apt-mark unhold <package>
sudo apt upgrade <package>
```

To move to a newer JetPack release, re-flash with the latest ARK image instead of upgrading in place — see your carrier's Flashing Guide.
