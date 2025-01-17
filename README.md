
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#software">Software</a></li>
        <li><a href="#harware">Harware</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
 

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## 1. About The Project

Tour tag project is webserver running on raspberry pi and is powered by django framework. 
The main objectives of this project are to provide a system for every tour leader to gather statistical information, control rules, provide some guidance, and help tourists to make trips better.

User will be able to connect to the tour-tag WIFI access point by phone or laptop. Tour-tag will provide website service where user can see information about the trip. From website user can view estimated time of departure/arrival.


### Software

[Django](https://www.djangoproject.com/)

### Hardware

Raspberry Pi 3 Model b \
https://www.raspberrypi.org/ \
Unicorn Hat HD Matrix LED \
https://github.com/pimoroni/unicorn-hat-hd

<!-- GETTING STARTED -->
## 2. Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.



### Installation

1. Get latest rasberry OS  https://www.raspberrypi.org/software/operating-systems/

In addition you can enable SSH to control your Raspberry pi remotely. Instructions for enabling SSH can be found here https://www.raspberrypi.org/documentation/remote-access/ssh/.

2. update and upgrade

   ```sh
   sudo apt update
   sudo apt full-upgrade
   ```
3. Install django

	```sh
	sudo pip3 install Django
	```

4. Install matrix led panel

  ```sh
  curl https://get.pimoroni.com/unicornhathd | bash
  ```

5. Clone the repo

  ```sh
  git clone https://github.com/kari-kalastaja/tour-tag
  ```
6. Set wifi accespoint https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/183-raspberry-pi-automatic-hotspot-and-static-hotspot-installer

  ```sh
  curl "https://www.raspberryconnect.com/images/hsinstaller/AutoHotspot-Setup.tar.gz" -o AutoHotspot-Setup.tar.gz
  tar -xzvf AutoHotspot-Setup.tar.gz
  cd Autohotspot
  sudo ./autohotspot-setup.sh
  ```
  Choose option 3

7. Reboot

<!-- USAGE EXAMPLES -->
## 3. Usage 

1. Start django server

```sh
cd tour-tag
python3 manage.py runserver 0:8000
```

2. Connect to wifi accesspoint

3. Web servers are available in http://192.168.50.10/




