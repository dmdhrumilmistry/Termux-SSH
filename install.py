#!usr/bin/env/ python
import subprocess
import user


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
user.generate_passwd(user.get_user())
