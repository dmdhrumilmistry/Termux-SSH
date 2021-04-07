#!usr/bin/env python3
import subprocess

def get_user():
    user = subprocess.check_output(["whoami"])
    return user


def generate_passwd(user):
    print("[+] Creating password for user")
    print("Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call(["passwd", user])


def install_req():
    print("""
------------------------------------------------------------
 _____                                _____ _____ _   _ 
|_   _|                              /  ___/  ___| | | |
  | | ___ _ __ _ __ ___  _   ___  __ \ `--.\ `--.| |_| |
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /  `--. \`--. \  _  |
  | |  __/ |  | | | | | | |_| |>  <  /\__/ /\__/ / | | |
  \_/\___|_|  |_| |_| |_|\__,_/_/\_\ \____/\____/\_| |_/
                                A tool by Dhrumil Mistry
------------------------------------------------------------
A tool Specially Designed for Termux
------------------------------------------------------------
""")
    print('[+] Installing required packages')
    print('------------------------------------------------------------')
    subprocess.call(["pkg", "update"])
    subprocess.call(["pkg", "upgrade"])
    subprocess.call(["pkg", "install", "nmap", "openssh", "-y"])


install_req()
generate_passwd(get_user())

