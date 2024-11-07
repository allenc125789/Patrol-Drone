# Security Drone (Prototype) | Motherboard - RaspberryPi 5

> Storage: SD card(+100gb)
>
> OS: RaspberryPi OS

## 1: OS Installation:
+ Write the RaspberryPi OS from the [Official RPI Imaging software](https://www.raspberrypi.com/software/)).

## 2: WiFi Setup:
+ **Run the following as Root**
+ Install packages:
  +  `apt install network-manager`
+ Connect to wifi, replacing the SSID and PSK with your wifi's:
  + `nmcli device wifi connect "SSID" password "PSK"`

## 3: Software Installation:
+ **Run the following as Root**
+ Install packages:
  +  `apt install git`
+ Install program:
  + `git clone https://allenc125789:@github.com/allenc125789/SecurityDrone-Prototype.git -b motherboard-OrangePi3b && bash ./SecurityDrone-Prototype/setup.sh`
