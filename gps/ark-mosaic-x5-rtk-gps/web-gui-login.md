# Web GUI Login

The Septentrio mosaic-X5 module hosts a web interface for configuration, status, and diagnostics accessible via USB-C connector.

## Connect

1. Plug a USB-C cable from your computer to the USB-C port on the ARK MOSAIC-X5 RTK GPS.
2. Open a browser and go to [http://192.168.3.1](http://192.168.3.1).

## Log in

On recent Septentrio firmware the receiver enforces user authentication. The first time you connect, you will be prompted to create a new user account with a strong password.

Septentrio's factory credentials are:

* **User Name:** `RxAdmin`
* **Password:** `S3pt3ntr10`

Use these only to bootstrap the new account, then set your own credentials. Keep your new credentials in a safe place — if they are lost, the receiver must be reset following Septentrio's [Lost Administrative Credentials](https://customersupport.septentrio.com/s/article/Lost-Administrative-Credentials) procedure.

For the full procedure and rationale, see Septentrio's [Cybersecurity guidelines: Log-in procedure](https://customersupport.septentrio.com/s/article/Cybersecurity-guidelines-Log-in-procedure).

## Spectrum Analyzer

The web GUI includes a built-in RF spectrum analyzer under **GNSS > Spectrum**. It plots the live baseband spectrum at each GNSS band, which is the fastest way to spot in-band interference, jamming, or a mis-tuned antenna chain before it shows up as degraded fix quality. The AGC status for each band is shown under **GNSS > Spectrum > Status**.
