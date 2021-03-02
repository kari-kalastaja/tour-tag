
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

tag project 

Here's why:
* Your time should be focusded n creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Django](https://www.djangoproject.com/)




<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites TODO

This is an example of how to list things you need to use the software and how to install them.
* npm?
  ```sh
  add something
  ```
### Hardware

Raspberry Pi 3 Model b
Unicorn Hat HD Matrix LED
https://github.com/pimoroni/unicorn-hat-hd


### Installation

1. Get latest rasberry OS  https://www.raspberrypi.org/software/operating-systems/

2. update and upgrade

   ```sh
   sudo apt update
   sudo apt full-upgrade
   ```
3. Install django

	```sh
	sudo pip3 install Django
	```

4. Install matrix led panel (TODO)

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
## Usage test

1. Start django server

```sh
cd tour-tag
python3 manage.py runserver 0:8000
```

2. Connect to wifi accesspoint

ap name: tourtag
password: tourtag

<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


