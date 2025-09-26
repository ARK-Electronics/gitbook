---
description: >-
  This section guides you through setting up log encryption in PX4 on our flight
  controllers, and then explains how to access, decrypt, and view the encrypted
  logs.
---

# PX4 Log Encryption

{% embed url="https://www.youtube.com/watch?v=ixmzCn4nH9c" %}

### Creating PX4 Board files for Encrypted logs

```
git clone --recurse-submodules git@github.com:PX4/PX4-Autopilot.git
```

Generate your Private and Public Key

```
cd PX4-Autopilot/Tools/log_encryption
python3 generate_keys.py
```

You can find your keys in

```
PX4-Autopilot/
│
├── keys/ 
│ ├── private/
│ │ ├── private_key.pem # RSA private key (2048-bit)
│ │
│ ├── public/ 
│ │ ├── public_key.der # Public key in DER format
│ │ ├── public_key.pub # Public key in hex format
```

The ARK flight controllers have targets setup for encryption

You should navigate to

```
PX4-Autopilot/boards/ark
```

* ARK FPV
* ARKV6X
* ARKPI6X

You should replace the Dummy Key with your own Public Key in the following file

```
encrypted_logs.px4board
```

```
CONFIG_PUBLIC_KEY1="../../../keys/public/public_key.pub"
```

Then you can go ahead and make your board file

```
make ark_fpv_encrypted_logs
OR
make ark_fmu-v6x_encrypted_logs
OR
make ark_pi6x_encrypted_logs
```

Once that is done you can find your build file in

```
PX4-Autopilot/build/*.px4
```

You can go ahead and flash it on your flight controller.

### Downloading and Decrypting log files

The encrypted logs can be found on the SD card in .ulge format.

You can either extract the files directly from the SD card our use the log tool provided below

Addresses might need to be adjusted

```
cd PX4-Autopilot/Tools/log_encryption

python3 download_logs.py /dev/ttyACM0 --baudrate 57600

OR

python3 download_logs.py udp:0.0.0.0:14550
```

To Decrypt the logs you can use

```
cd PX4-Autopilot/Tools/log_encryption

AND
# Uses default key + default folder
python3 decrypt_logs.py

OR
# Use --help to get all the options
python3 decrypt_logs.py --help
```

Your logs can be found in the following structure

```
PX4-Autopilot/
│
├── logs/ 
│ ├── encrypted/ 
│ │ ├── log-YYYY-MM-DD_HH-MM-SS_ID.ulge 
│ │
│ ├── decrypted/
│ │ ├── log-YYYY-MM-DD_HH-MM-SS_ID.ulg
```

Once you've decrypted your logs, you can view them using your preferred method.

### Flight Review

{% embed url="https://www.youtube.com/watch?v=Dhd3jYyHgI0&t=1s" %}

If you choose to use Flight Review, you can embed your Private Key on your local Flight Review server, allowing your encrypted logs to be decrypted automatically when the .ulge is uploaded .

```
git clone --recurse-submodules git@github.com:PX4/flight_review.git
```

You should follow these steps

```
cd flight_review/app
pip install -r requirements.txt
# Note: preferably use a virtualenv
./app/setup_db.py
```

Add your Private Key to

```
flight_review/app/private_key/private_key.pem
```

Then you need to edit, the config file. There you can define your own network setup (Domain, VPN, etc).

```
flight_review/app/config_default.ini
```

You have to update the Private Key path with your own.

```
ulge_private_key = ../private_key/private_key.pem
```

Once you are done you can just open your server using

```
cd app
./serve.py --show
```

Once you have your server ready you can upload the Encrypted logs and view them.

Optionally you can also integrate logloader developed by ARK.

The repository can be found here:

[https://github.com/ARK-Electronics/logloader](https://github.com/ARK-Electronics/logloader)

You should specify your server in the config file

```
logloader/config.toml
```

