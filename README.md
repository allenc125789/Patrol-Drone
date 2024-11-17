# Security Drone (Prototype) | Motherboard - RaspberryPi 5

> Storage: SD card(+100gb)
>
> OS: RaspberryPi OS

## Install: Source

### 1: OS Imaging:
+ Download the [Official RPI Imaging software](https://www.raspberrypi.com/software/).
+ Select the 64-bit RaspberryPi image to your SD card, and click next.
+ In the OS-Custimization pop-up, edit settings, and set the username: `drone`, with an easy to remember password.
+ (Optional) Set your wifi.
+ Write to SD.
  

### 2: Software Installation:
+ **Run the following as Root**
+ Install packages:
  +  `sudo apt install git`
+ Install program:
  + `sudo git clone https://allenc125789:@github.com/allenc125789/SecurityDrone-Prototype.git -b motherboard-RaspberryPi5 && sudo bash ./SecurityDrone-Prototype/setup.sh`
