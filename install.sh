#!/bin/bash

echo -e "\033[33m[*] Starting installation...\033[0m";apt update -y && apt upgrade -y;apt install python git nmap openssh termux-auth termux-api -y;pip install git+https://github.com/dmdhrumilmistry/Termux-SSH.git;echo "\033[33m[*] Completed... Start Termux-SSH using python -m termux_ssh and use install command to complete setup.\033[0m";
