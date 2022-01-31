<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sahussawud/bombbot">
    <img src="https://user-images.githubusercontent.com/43010244/151778822-cc50b16e-3a01-4655-8824-038b7d731b0c.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Bombbot Autoclick</h3>

  <p align="center">
    An awesome bot for automated your BombHero!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/sahussawud/bombbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/sahussawud/bombbot/issues">Request Feature</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

Automated your BOMBHERO, and go to sleep. Support Windows 10, MAC, Ubuntu (Not Test)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Python 3.7 ++ (Recommended) <a href="https://www.youtube.com/watch?v=VWgs_iTojoA"><strong>Install Python Guild »</strong></a>
* Python library : pyautogui, requests, opencv-python, Pillow
* Line Token (Optional) <a href="https://www.smith.in.th/%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-line-notify-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-post-%E0%B8%A5%E0%B8%87%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1"><strong>generate token »</strong></a>

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Download Python 3.7++ and check
      ```sh
      python 
      ```
      Interactive shell work, and exit() 
      ```
      Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
      Type "help", "copyright", "credits" or "license" for more information.
      >>> exit() 
      ```
 
2. Check pip to check python lib install 
     ```sh
     pip list
     ```
 
3. Install PIP install
      ```sh
      pip install pyautogui, requests, opencv-python, Pillow
      ```
   
4. Generate Line Token to recieve screenshots in Line Notify (Optional) <a href="https://www.smith.in.th/%E0%B8%AA%E0%B8%A3%E0%B9%89%E0%B8%B2%E0%B8%87-line-notify-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-post-%E0%B8%A5%E0%B8%87%E0%B8%81%E0%B8%A5%E0%B8%B8%E0%B9%88%E0%B8%A1"><strong>generate token »</strong></a>

5. Download Bombbot [Master Branch]  <a href="https://github.com/sahussawud/bombbot/archive/refs/heads/master.zip"><strong> Download Link »</strong></a>

5. Create file **secret.txt** in root folder, paste token and save it

6. Capture your own button component to images folder (suggest Snipping Tools on Windows) and replace the old files in folder. because it's may some error when difference pixel size.

![image](https://user-images.githubusercontent.com/43010244/151783938-41fbf804-18e2-4b06-a4b3-f08f009249bd.png)


<!-- USAGE EXAMPLES -->
## Usage

0. BEFORE RUN THE PROGRAM, YOU SHOULD OPEN THERSURE HUNT PAGE, AND REST ALL BOMBHERO
![image](https://user-images.githubusercontent.com/43010244/151785343-1acd3db9-ba1d-4d26-8855-fdad95f29a6b.png)


2. Open CMD or powershell (Win) or TERMINAL (Mac) and go to bombbot directory

    ```sh
    cd {your bomb directory}\bombbot-main
    python prototype.py
    ```
2. Interactive Shell open and input cycle time (time that you want bot will re-run process) and ENTER
    ```
    C:\Users\dodo\OneDrive\เดสก์ท็อป\bombbot-main>py prototype.py
    Program bot for bormcrypto start
    Open browser for program one by one
    Keep all hero to rest
    After open 'Treasure Hunt' page and wait for end process
    Input cycle time (Min.): 
    ```
    
    OUTPUT
    ```
    result_click_btn_work None
    result_click_btn_work None
    result_click_btn_work None
    Ready to start...
    Find close button
    Find start button
    Program ready running re process in (Min) 60
    {'imageFile': <_io.BufferedReader name='capture.png'>}
    b'{"status":200,"message":"ok"}'
    round {} remainder {}  (6, 0)
    accumulate sleep for  0  second
    ```
    
<!-- ROADMAP -->
## Roadmap

- [x] Single screen auto-click
- [x] Add notify features
- [x] Add readme.md
- [ ] Add GUI screen
- [ ] Multiple Screen Auto-Click


See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact
Email : sahussawud@hotmail.com

## Buy me a coffee
BSC Smart Chain (BEP-20): 0x474E81759b0Edd44c93f97d745c64ccbF0015c79


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

Thank for initiative from : https://www.facebook.com/groups/bombcryptothailand/posts/630609488123266/



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/sahussawud/bombbot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/sahussawud/bombbot/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/sahussawud/bombbot/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/sahussawud/bombbot/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/sahussawud/bombbot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sahussawud
