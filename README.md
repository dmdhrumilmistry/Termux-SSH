<!-- Termux-SSH -->

# Termux-SSH

```
+-----------------------------------------------------------+
| _____                                _____ _____ _   _    |
||_   _|                              /  ___/  ___| | | |   |
|  | | ___ _ __ _ __ ___  _   ___  __ \ `--.\ `--.| |_| |   |
|  | |/ _ \ '__| '_ ` _ \| | | \ \/ /  `--. \`--. \  _  |   |
|  | |  __/ |  | | | | | | |_| |>  <  /\__/ /\__/ / | | |   |
|  \_/\___|_|  |_| |_| |_|\__,_/_/\_\ \____/\____/\_| |_/   |
|                                A tool by Dhrumil Mistry   |
+-----------------------------------------------------------+
| ~ ~ ~ ~ ~ A tool Specially Designed for Termux ~ ~ ~ ~ ~  |
+-----------------------------------------------------------+
```

Termux SSH helps user to setup SSH server on termux android application, which will help them to execute commands remotely using a command line.
If your device is rooted then you can have full control over the android smartphone. You can take screenshots, record and capture audio, video, images remotely using termux apis.

> This feature might not work on few devices. Refer [Termux-API documentation](https://wiki.termux.com/wiki/Termux:API) for more information.

## Screenshot

![Termux-SSH](https://github.com/dmdhrumilmistry/Termux-SSH/blob/main/.images/Termux-SSH-v1.1.0.png?raw=true)

## Installation

### Using bash script

- Execute command in Termux App

  ```bash
  cd $HOME && mkdir tmp && cd tmp && curl -O https://raw.githubusercontent.com/dmdhrumilmistry/Termux-SSH/main/install.sh && chmod +x $HOME/tmp/install.sh && ./install.sh; cd $HOME ;rm -rf $HOME/tmp
  ```

### Maually

- Open Termux terminal

- Install Python and git packages

  ```bash
  pkg install python git -y
  ```

- Install required packages

  ```bash
  pip install git+https://github.com/dmdhrumilmistry/Termux-SSH.git
  ```

- Start Termux-SSH and Install required tools

  ```bash
  python -m termux_ssh
  ```

  ```bash
  install
  ```

## Commands List

| command | description                                  |
| :-----: | :------------------------------------------- |
| install | installs required tools                      |
|  start  | starts SSH server                            |
|  clear  | clears console screen                        |
|  port   | checks on which port server is running       |
|  user   | get username                                 |
| genpass | generates new password for user              |
| wlanip  | get wlan ip of the device                    |
| conncmd | connect to this using using command printed  |
| torssh  | start ssh service on tor network             |
| torhost | get TOR network hostname                     |
| torstop | exit tor network                             |
| restart | restarts ssh server                          |
|  close  | exits Termux-SSH without stopping SSH server |
|  exit   | stops ssh server and exit                    |

### Features

- Helps user to setup basic SSH server
- Automated Setup
- Instructed Steps
- Secure script

### Dependencies

**`Termux-SSH`** requires following programs to run properly -

- `Python`
  - `subprocess module`
  - `colorama`
  - `prettytable`
  - `netifaces`
- `OpenSSH`
- `Nmap`
- `termux-api`
- `termux-auth`

> All the dependencies will be installed automatically when you run install.py script

## [License](https://github.com/dmdhrumilmistry/Termux-SSH/blob/main/LICENSE)

MIT License

### Have any Issues?

Create an issue from **_[Issues Tab](https://github.com/dmdhrumilmistry/Termux-SSH/issues)_**

## Leave A Star⭐

## Video Tutorial

- For Previous Version
  <a href = "https://www.youtube.com/watch?v=V_m3vHmOY3c" target = "_blank"><img src = "https://img.shields.io/badge/YouTube%20Video-For%20video%20click%20here-bd2c00"></a><br>

### Support Me on

|                                                               Platforms                                                                |                                                                                                                       |
| :------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: |
|             [![GithubBadge](https://img.shields.io/badge/Github-dmdhrumilmistry-333)](https://github.com/dmdhrumilmistry)              | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0)](https://linkedin.com/in/dmdhrumilmistry) |
|       [![Instagram](https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4)](https://www.instagram.com/dmdhrumilmistry/)        |    [![Twitter](https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0)](https://twitter.com/dmdhrumilmistry)     |
| [![YouTube](https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical)](https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ) |   [![BlogSpot](https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00)](https://dmdhrumilmistry.github.io/blog)    |
