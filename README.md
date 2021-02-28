
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
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Laravel](https://laravel.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
### Hardware

Raspberry Pi 3 Model b
Unicorn Hat HD Matrix LED
https://github.com/pimoroni/unicorn-hat-hd


### Installation

1. Get latest rasbian OS  https://www.raspberrypi.org/software/operating-systems/

2. update and upgrade

   ```sh
   sudo apt update
   sudo apt full-upgrade
   ```
4. Install django

	```sh
	sudo pip3 install Django
	````

5. Install matrix led panel
```sh
 curl https://get.pimoroni.com/unicornhathd | bash
````

6. Clone the repo
   ```sh
   git clone https://github.com/kari-kalastaja/tour-tag
   ```




<!-- USAGE EXAMPLES -->
## Usage

1. Start django server

	```sh
   cd tour-tag
   python3 manage.py runserver 0:8000
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


