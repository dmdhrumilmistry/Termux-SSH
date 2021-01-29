#!usr/bin/env/python

import subprocess

def get_user():
    user = subprocess.check_output(["whoami"])
    return user


def generate_passwd(user):
    print("[+] Creating password for user")
    print("Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call(["passwd", user])


def print_menu():
    subprocess.call(["clear"])
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
~~~~~~~~~~ A tool Specially Designed for Termux ~~~~~~~~~~~~
------------------------------------------------------------
MENU:
[1] - Start SSH server
[2] - check port on which server is running
[3] - get user
[4] - get Wlan info (for wlan0 inet) 
[5] - restart SSH server
[6] - exit
------------------------------------------------------------
[*] How to connect to termux terminal using cmd command:
1. <user>@<wlan0_inet> -p <port>
2. Enter password for user
------------------------------------------------------------
    """)

def start():
    print_menu()
    choice = input("What would you like to perform?")
    choices = (1,2,3,4,5,6)
    if choice in choices:
        if choice == 1 and start_ssh():
            print('[+] SSH server has been successfully started \nNOTE: Default Port in most cases 8022')
        if choice == 2:
            check_port()
        if choice == 3:
            print(get_user())
        if choice == 4:
            get_wlan_info()
        if choice == 5:
            restart_ssh()
        if choice == 6:
            exit_program()
    else:
        print('Enter valid choice mate!')


def start_ssh():
    subprocess.call(["sshd"])
    return True


def check_port():
    if start_ssh():
        print(str(subprocess.check_output(["nmap", "localhost"])))

def get_wlan_info():
    print(str(subprocess.check_output(["ifconfig","wlan0"])))


def restart_ssh():
    check_port()
    subprocess.call(["pkill","ssh"])
    print('[+] SSH Server Successfully Killed.')
    if start_ssh():
        print('[+] SSH Server Successfully Started.')


def exit_program():
    subprocess.call(["pkill","ssh"])

check = 'y'
while(check in ('Y','y')):
    start()
    check = input('[+] Would you like to continue? (y/n): ')

exit_program()

def get_user():
    user = subprocess.check_output(["whoami"])
    return user


def generate_passwd(user):
    print("[+] Creating password for user")
    print("Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call(["passwd", user])
