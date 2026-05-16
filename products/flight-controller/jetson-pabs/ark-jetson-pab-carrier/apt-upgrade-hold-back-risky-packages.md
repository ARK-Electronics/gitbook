# Apt Upgrade Hold Back Risky Packages

### Overview

The apt-mark hold command is used in Debian-based systems, such as Ubuntu or NVIDIA's Linux for Tegra (L4T) on Jetson platforms, to prevent specific packages from being upgraded or removed during apt update or apt upgrade. This is particularly useful when certain packages, such as kernel, firmware, or driver packages, could break critical functionality like Wi-Fi or GPU support if updated to incompatible versions.

### Why Use apt-mark hold?

* **Prevent Breakage**: Avoid updating packages that might introduce incompatibilities (e.g., linux-firmware or nvidia-l4t-kernel breaking Wi-Fi on a Jetson Orin Nano/NX).
* **Stabilize System**: Maintain a known-working configuration for critical components during system upgrades.
* **Selective Upgrades**: Allow other packages to update while protecting specific ones.

### Recommended packages to hold

The following packages are recommended to hold to prevent issues when updating. These are set when running the ARK OS install.

```
sudo apt-mark hold linux-firmware nvidia-l4t-kernel nvidia-l4t-kernel-dtbs nvidia-l4t-firmware nvidia-l4t-kernel-headers nvidia-l4t-kernel-oot-headers wireless-regdb
```

### Show packages on hold

```
sudo apt-mark showhold
```

### Remove packages on hold and upgrade

```
sudo apt-mark unhold <package>
sudo apt upgrade <package>
```
