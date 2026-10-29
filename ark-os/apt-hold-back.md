# Apt Upgrade: Hold Back Risky Packages

The ARK image keeps NVIDIA's apt repo enabled. NVIDIA's packages own the kernel, device tree and bootloader files, so an `apt upgrade` without holds replaces ARK's builds with stock ones and breaks carrier hardware.

The image holds these packages:

| Packages | Held since | Why |
| --- | --- | --- |
| `nvidia-l4t-camera`, `nvidia-l4t-multimedia`, `nvidia-l4t-multimedia-utils`, `nvidia-l4t-gstreamer` | 6.2.2.5 | Pinned to the 36.4.4 camera stack; NVIDIA's 36.5 stack crashes `nvargus-daemon` on camera relaunch. |
| `nvidia-l4t-kernel`, `nvidia-l4t-kernel-dtbs`, `nvidia-l4t-kernel-headers`, `nvidia-l4t-kernel-oot-headers`, `nvidia-l4t-kernel-oot-modules`, `nvidia-l4t-display-kernel` | 6.2.2.7 | ARK's kernel and device tree. The out-of-tree modules must match the kernel, so these move as one set. |
| `nvidia-l4t-bootloader` | 6.2.2.7 | Its install rewrites the QSPI that holds ARK's boot-time pinmux. |

On an image older than 6.2.2.7, hold the boot chain yourself before upgrading:

```
sudo apt-mark hold nvidia-l4t-kernel nvidia-l4t-kernel-dtbs nvidia-l4t-kernel-headers nvidia-l4t-kernel-oot-headers nvidia-l4t-kernel-oot-modules nvidia-l4t-display-kernel nvidia-l4t-bootloader
```

Show packages on hold:

```
sudo apt-mark showhold
```

To move to a newer JetPack release, reflash with the latest ARK image instead of upgrading in place; see your carrier's Flashing Guide.
