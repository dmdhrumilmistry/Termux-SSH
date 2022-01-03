#!/bin/bash

echo -e "\033[33m[*] Starting installation...\033[0m"
# update and upgrade
pkg update -y && pkg upgrade -y

# upgrade requirements
pkg install python git nmap openssh termux-auth termux-api -y

# install Termux-SSH using github repo
pip install git+https://github.com/dmdhrumilmistry/Termux-SSH.git
