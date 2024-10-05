> [!NOTE]
> **Current Status:** Under Development. Working on face detection, path detection, and preparing code to be used by the motherboard. Specifically, a booting phase to intially recognize an admin, then go into a path scanning mode.
>
> The goal is to automate the drone to be able to automatically ready itself after booting. Immediately being ready to start acting as a security drone that scans the envireonment for unfamiliar faces while following a scanned map of the area.


# Security Drone (Prototype)

## About
Home-page for my attempt to make a "security drone", that will accomplish basic physical security tasks. Some tasks include facial detection,

This drone will involve an `stm32` as a flight controller, and a Linux compatible SBC as a motherboard for processing deep-learning with computer vision. Files for both of these devices along with schematics can be found within this repository.

*Hardware Needed:*
+ Mini USB to TTL Serial Converter
+ STM32F10C8T6
+ Linux-Based SBC
+ GY-521 MPU-6050 3 Axis Accelerometer/Gyroscope
+ HappyModel EX1102 13500Kv (1.5mm Shaft) Whoop/Micro Motor [x4]
+ 40mm 1.5mm Bi-Blade [x4]

**Motherboard (Linux-ARM SBC) Files:** https://github.com/allenc125789/SecurityDrone-Prototype/tree/motherboard

## Instructions
**Motherboard:**
+ Install Debian
+ After install, run this command as root: `git clone https://allenc125789:@github.com/allenc125789/SecurityDrone-Prototype.git -b motherboard && bash ./SecurityDrone-Prototype/setup.sh`

## Resources
### Drone Construction
+ [Joop Brokking: STM32 Drone Playlist](https://www.youtube.com/watch?v=MLEQk73zJoU&list=PL0qFkFQLP5BCzOatRLFr15el1dSjvn--E)
+ [DroneBot Workshop: Getting Started with LIDAR](https://www.youtube.com/watch?v=VhbFbxyOI1k)

### Computer Vision
+ [freeCodeCamp.org: Advanced Computer Vision with Python - Full Course](https://youtu.be/01sAkU_NvOY?si=-z81XHAHfTIwfk2N)
+ [Rob Mulla: Open Source Face Analysis with Python](https://www.youtube.com/watch?v=n84hBgtzvxo&t=201s)
+ [sentdex: Practical Machine Learning Tutorial with Python](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v)
+ [sentdex: Loading in your own data - Deep Learning basics with Python, TensorFlow and Keras](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN)

### Tensorflow/Deep-Learning
+ [Dan Fleisch: What's a Tensor?](https://www.youtube.com/watch?v=f5liqUk0ZTw)
+ [Daniel Bourke: Learn TensorFlow and Deep Learning fundamentals with Python (code-first introduction) Part 1/2](https://youtu.be/tpCFfeUEGs8?si=7dZBGBJo5kr7hvSh)
