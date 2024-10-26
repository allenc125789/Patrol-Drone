# Security Drone (Prototype) | Motherboard

> Model: OrangePi 3b
>
> Storage: SD card(+100gb)
>
> OS: Armbian

## Setup:
+ Download Armbian(Minimal/IOT) from the [armbian website](https://www.armbian.com/orangepi3b/).
+ Install the armbian img file onto the SD card with imaging software. (I used the [Official RPI Imaging software](https://www.raspberrypi.com/software/)).
+ Boot the SBC, connect to ssh with the `root` user. Setup password is `1234`.
+ Complete the requested setup when connected.


**Run as Root:** `git clone https://allenc125789:@github.com/allenc125789/SecurityDrone-Prototype.git -b motherboard && bash ./SecurityDrone-Prototype/setup.sh`
