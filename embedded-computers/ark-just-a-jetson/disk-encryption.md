# Disk Encryption

The ARK Jetson image can put the root filesystem on an encrypted partition. The Jetson unlocks it by itself at every boot, with no passphrase to type, and an NVMe SSD removed from the carrier cannot be read on its own.

This is NVIDIA's [disk encryption](https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/SD/Security/DiskEncryption.html) for Orin NX and Orin Nano, packaged into the ARK flashing tools. NVIDIA's instructions target their developer kits and do not work as written on the Just a Jetson; use the steps below instead.

## What It Protects

| Situation | Protected? |
| --- | --- |
| SSD removed and read on another computer | Yes |
| SSD moved into another Jetson | Yes: it does not unlock there |
| Jetson module and SSD taken together | No, unless the module's security fuses are burned (see [Limitations](#limitations)) |
| Someone logged in to the running Jetson | No: the disk is unlocked while it runs |

The key that unlocks the SSD is derived inside the Jetson module's secure world (OP-TEE) from a disk key stored in the module's QSPI flash, the module's unique chip ID, and the partition's UUID. None of those are on the SSD. After boot the module stops handing out the passphrase, so nothing running later, including a root shell, can ask for it again.

## Flash an Encrypted Image

Put the Jetson in recovery mode as in the [Flashing Guide](flashing-guide.md#enter-recovery-mode), then add `--encrypt` to the usual command.

Prebuilt release:

```bash
./flash_from_package.sh jaj --encrypt
```

From source:

```bash
./flash.sh JAJ --encrypt
```

`flash_from_package.sh` installs `cryptsetup` on the host if it is missing. An encrypted flash takes longer than a plain one, and the board resets itself between steps, so no extra button presses are needed. Releases older than disk encryption support refuse `--encrypt` with a message; flash the latest release.

The root filesystem fills the whole SSD, as it does on a plain flash. Only the `/boot` partition (kernel and initrd, 400 MB) is left unencrypted. Unlocking at boot adds about 3 seconds.

## Back Up the Disk Key

Each encrypted flash generates a random disk key and saves two files on the host PC:

```
~/.ark-jetson-keys/jaj-<release>-<date>-<time>.key   # the disk key
~/.ark-jetson-keys/jaj-<release>-<date>-<time>.txt   # the module's chip ID and partition UUIDs
```

The Jetson does not need them to boot. Keep them somewhere safe and private: together they unlock that SSD on any Linux PC, and without them the SSD opens only inside the module it was flashed with.

To use your own key instead, pass a file holding 16 random bytes as 32 hex digits:

```bash
openssl rand -hex 16 > my-disk.key
./flash_from_package.sh jaj --encrypt --disk-key my-disk.key
```

## Check It on the Jetson

```bash
lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT /dev/nvme0n1
sudo cryptsetup status crypt_root
```

`nvme0n1p2` shows as `crypto_LUKS`, with `crypt_root` mounted at `/` underneath it, and `cryptsetup` reports `aes-xts-plain64`.

## Read the SSD on Another PC

With the SSD in a USB enclosure, and the `.key` and `.txt` files from the flashing PC:

```bash
# ecid= and rootfs_luks_uuid= come from the .txt file
python3 Linux_for_Tegra/tools/disk_encryption/gen_luks_passphrase.py \
    -k jaj-<release>-<date>-<time>.key -u -e <ecid> -c <rootfs_luks_uuid> \
    | sudo cryptsetup luksOpen /dev/sdX2 jetson_root
sudo mount /dev/mapper/jetson_root /mnt
```

`gen_luks_passphrase.py` is NVIDIA's; it is in every `Linux_for_Tegra` tree, including the flash package the script caches under `~/.ark-jetson-cache/`. Use the partition that `lsblk -f` lists as `crypto_LUKS`.

## Limitations

* **Module and SSD together are not protected** on a module whose fuses have not been burned: the disk key can be read back from the module's QSPI, and the unencrypted kernel and initrd are not signature-checked. Closing that needs NVIDIA's [Secure Boot](https://docs.nvidia.com/jetson/archives/r36.5/DeveloperGuide/SD/Security/SecureBoot.html) and a burned OEM_K1 key. Fuse burning is permanent and is not part of this flow.
* **A plain reflash replaces the disk key.** The old encrypted SSD will no longer unlock on that module.
* **Keep `nvidia-l4t-bootloader` held** (the ARK image holds it). A bootloader update from NVIDIA's apt repository rewrites the QSPI, including the disk key, and the next boot will not unlock. See [Apt: Hold Back Risky Packages](../../ark-os/apt-hold-back.md).

For how it works and what the flasher changes from NVIDIA's reference flow, see [docs/disk\_encryption.md](https://github.com/ARK-Electronics/ark_jetson_kernel/blob/main/docs/disk_encryption.md) in the ark\_jetson\_kernel repository.
