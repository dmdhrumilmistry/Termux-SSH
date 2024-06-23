#!/bin/bash

echo -e "\033[33m[*] Starting installation...\033[0m"
apt update -y
apt install python git openssh termux-auth termux-api tor proxychains-ng -y
pip install git+https://github.com/dmdhrumilmistry/Termux-SSH.git
echo -e "\033[33m[*] Completed... Start Termux-SSH using python -m termux_ssh and use install command to complete setup.\033[0m";
