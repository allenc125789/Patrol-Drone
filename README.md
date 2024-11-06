> [!NOTE]
> **Current Status:** Under Development. Researching face recognition, path detection, and preparing code to be used by the motherboard. Specifically, a booting phase to intially recognize an admin, then go into a path scanning mode.
>
> Main goal is to develop an automated drone that can configure itself for scanning and patrolling various environments.


# Security Drone (Prototype)

## About
Home-page for my attempt to make a "security drone", that will accomplish basic physical security tasks.

This drone will involve an `stm32` as a flight controller, and a Linux compatible SBC as a motherboard for processing deep-learning with computer vision. Files for both of these devices along with schematics can be found within this repository.

***Hardware Needed:***
+ Mini USB to TTL Serial Converter
+ STM32F10C8T6 **[Flight Controller]**
+ Linux-Based SBC **[Motherboard]**
+ GY-521 MPU-6050 3 Axis Accelerometer/Gyroscope
+ HappyModel EX1102 13500Kv (1.5mm Shaft) Whoop/Micro Motor [x4]
+ 40mm 1.5mm Bi-Blade [x4]

## Instructions
1: See the compataible SBC's, and select the one you'll be setting up.
+ [Motherboard Selection](https://github.com/allenc125789/SecurityDrone-Prototype/blob/main/docs/motherboard-list.md)

## Resources
### Drone Construction
+ [Joop Brokking: STM32 Drone Playlist](https://www.youtube.com/watch?v=MLEQk73zJoU&list=PL0qFkFQLP5BCzOatRLFr15el1dSjvn--E)
+ [DroneBot Workshop: Getting Started with LIDAR](https://www.youtube.com/watch?v=VhbFbxyOI1k)

### Computer Vision
+ [freeCodeCamp.org: Advanced Computer Vision with Python - Full Course](https://youtu.be/01sAkU_NvOY?si=-z81XHAHfTIwfk2N)
+ [Rob Mulla: Open Source Face Analysis with Python](https://www.youtube.com/watch?v=n84hBgtzvxo&t=201s)

### Tensorflow/Deep-Learning
+ [sentdex: Facial Recognition with Python and the face_recognition library](https://www.youtube.com/watch?v=535acCxjHCI)
+ [sentdex: Facial Recognition on Video with Python](https://youtu.be/PdkPI92KSIs?si=bd_g_af1rScWe-Eq)
+ [Dan Fleisch: What's a Tensor?](https://www.youtube.com/watch?v=f5liqUk0ZTw)
+ [Daniel Bourke: Learn TensorFlow and Deep Learning fundamentals with Python (code-first introduction) Part 1/2](https://youtu.be/tpCFfeUEGs8?si=7dZBGBJo5kr7hvSh)
+ [sentdex: Practical Machine Learning Tutorial with Python Playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v)
+ [sentdex: Loading in your own data - Deep Learning basics with Python, TensorFlow and Keras Playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN)
