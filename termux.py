#!usr/bin/env python3

import subprocess
import colorama
from colorama import Style, Fore
colorama.init(autoreset=True)


def banner():
      print(Fore.GREEN + Style.BRIGHT +  """
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


def print_menu():
    subprocess.call(["clear"])
    banner()
    print(Fore.WHITE + Style.BRIGHT + """
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


def get_user():
    user = subprocess.check_output(["whoami"])
    return user.decode('utf-8')


def generate_passwd(user):
    print(Style.BRIGHT + "\n[+] Create password for user : ")
    print(Style.BRIGHT + Fore.YELLOW +"Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call(["passwd", user])


def install_req():
    banner()
    print(Fore.YELLOW + '[+] Installing required packages')
    print(Fore.YELLOW + '[+] Updating...')
    subprocess.call(["pkg", "update"])
    print(Fore.YELLOW + '[+] Upgrading...')
    subprocess.call(["pkg", "upgrade"])
    print(Fore.YELLOW + '[+] Installing requirements ...')
    subprocess.call(["pkg", "install", "nmap", "openssh", "python", "python","termux-auth" , "termux-api", "-y"])
    subprocess.call(["python", "-m", "pip", "install", "colorama"])
    print(Fore.YELLOW + '[+] Installation completed!!')


def start(choice):
    
    if choice == 1 and start_ssh():
        print(Style.BRIGHT + '[+] SSH server has been started successfully!')
        print(Style.BRIGHT + Fore.YELLOW + 'NOTE: Default Port in most cases 8022')
    elif choice == 2:
        check_port()
    elif choice == 3:
        print(get_user())
    elif choice == 4:
        get_wlan_info()
    elif choice == 5:
        restart_ssh()
    elif choice == 6:
            exit_program()
    else:
        print(Fore.RED + Style.BRIGHT + 'Enter valid choice mate!')

    input("[+] Press any key to continue....")

def start_ssh():
    subprocess.call(["sshd"])
    return True


def check_port():
    if start_ssh():
        print(subprocess.check_output(["nmap", "localhost"]).decode('utf-8'))

def get_wlan_info():
    print(subprocess.check_output(["ifconfig","wlan0"]).decode('utf-8'))


def restart_ssh():
    check_port()
    subprocess.call(["pkill","ssh"])
    print(Style.BRIGHT + '[+] SSH Server Successfully Killed.')
    if start_ssh():
        print(Style.BRIGHT + '[+] SSH Server Successfully Started.')


def Exception_Message(Exception):
    print(Fore.RED + Style.BRIGHT + '[-] An Error occured while running the script, please create an issue on github to resolve issue and make script better.')
    print(Fore.YELLOW + Style.BRIGHT + '[+] Github URL: https://github.com/dmrdhrumilmistry/Termux-SSH ')
    raise Exception

def exit_program():
    print(Fore.YELLOW + Style.BRIGHT + '[+] Exiting Program... Please be patient...')
    subprocess.call(["pkill","ssh"])

