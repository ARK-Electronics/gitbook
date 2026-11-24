# Apt Upgrade: Hold Back Risky Packages

The ARK image keeps NVIDIA's apt repo enabled. NVIDIA's packages own the kernel, device tree and bootloader files, so an `apt upgrade` without holds replaces ARK's builds with stock ones and breaks carrier hardware.

The image holds these packages:

| Packages | Held since | Why |
| --- | --- | --- |
| `nvidia-l4t-kernel`, `nvidia-l4t-kernel-dtbs`, `nvidia-l4t-kernel-headers`, `nvidia-l4t-kernel-oot-headers`, `nvidia-l4t-kernel-oot-modules`, `nvidia-l4t-display-kernel` | 6.2.2.7 | ARK's kernel and device tree. The out-of-tree modules must match the kernel, so these move as one set. |
| `nvidia-l4t-bootloader` | 6.2.2.7 | Its install rewrites the QSPI that holds ARK's boot-time pinmux. |
| `nvidia-l4t-initrd` | 6.2.2.9 | It carries the kernel's NVMe and PCIe modules, so it moves with the kernel. |
| `nvidia-l4t-kernel-module-configs`, `nvidia-l4t-kernel-nvgpu`, `nvidia-l4t-kernel-openrm`, `nvidia-l4t-kernel-partitions`, `nvidia-l4t-bootloader-utils` | 7.2.1.1 | The rest of JetPack 7's boot chain, which ARK builds with its kernel. |
| `nvidia-l4t-camera`, `nvidia-l4t-multimedia`, `nvidia-l4t-multimedia-utils`, `nvidia-l4t-gstreamer` | 6.2.2.5, JetPack 6 only | Pinned to the 36.4.4 camera stack. NVIDIA's 36.5 stack crashes `nvargus-daemon` on camera relaunch. |

JetPack 7 images don't hold the camera stack, because JetPack 7's own stack relaunches cleanly.

On an image older than 6.2.2.7, hold the boot chain yourself before upgrading:

```
sudo apt-mark hold nvidia-l4t-kernel nvidia-l4t-kernel-dtbs nvidia-l4t-kernel-headers nvidia-l4t-kernel-oot-headers nvidia-l4t-kernel-oot-modules nvidia-l4t-display-kernel nvidia-l4t-bootloader
```

Show packages on hold:

```
sudo apt-mark showhold
```

To move to a newer JetPack release, reflash with the latest ARK image instead of upgrading in place; see your carrier's Flashing Guide.

## Install NVIDIA JetPack

On JetPack 7, `sudo apt install nvidia-jetpack` returns before Docker is installed. NVIDIA's `nv-install-docker` service then installs Docker CE from Docker's apt repo in the background, and removes Ubuntu's `docker.io` if you have it. Wait for the service to finish before you reboot. It prints `activating` until it is done:

```bash
systemctl is-active nv-install-docker
```

If the Jetson rebooted before the service finished, apt reports that dpkg was interrupted, or Docker is missing. Finish the install:

```bash
sudo dpkg --configure -a
sudo systemctl start nv-install-docker
```

The service adds the `nvidia` runtime to Docker's configuration but doesn't restart Docker. Restart it once before you run a container with `--runtime nvidia`:

```bash
sudo systemctl restart docker
```
