#!usr/bin/env python3

import subprocess
import colorama
import re
from colorama import Style, Fore
colorama.init(autoreset=True)

BRIGHT_WHITE = Style.BRIGHT + Fore.WHITE
BRIGHT_YELLOW = Style.BRIGHT + Fore.YELLOW
BRIGHT_RED = Style.BRIGHT + Fore.RED
BRIGHT_GREEN = Style.BRIGHT + Fore.GREEN



def banner():
      print(BRIGHT_GREEN +  """
-------------------------------------------------------------
| _____                                _____ _____ _   _    |
||_   _|                              /  ___/  ___| | | |   |
|  | | ___ _ __ _ __ ___  _   ___  __ \ `--.\ `--.| |_| |   |
|  | |/ _ \ '__| '_ ` _ \| | | \ \/ /  `--. \`--. \  _  |   |
|  | |  __/ |  | | | | | | |_| |>  <  /\__/ /\__/ / | | |   |
|  \_/\___|_|  |_| |_| |_|\__,_/_/\_\ \____/\____/\_| |_/   |
|                                A tool by Dhrumil Mistry   |
-------------------------------------------------------------
~ ~ ~ ~ ~ A tool Specially Designed for Termux ~ ~ ~ ~ ~ ~ ~
-------------------------------------------------------------
""")


def print_menu():
    subprocess.call("clear", shell=True)
    banner()
    print(BRIGHT_WHITE + """
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
    return subprocess.check_output("whoami", shell=True).decode('utf-8').strip()


def generate_passwd(user):
    print(BRIGHT_WHITE + "\n[+] Create password for user : ")
    print(BRIGHT_YELLOW  +"Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call('passwd', shell=True)


def install_req():
    banner()
    print(BRIGHT_YELLOW + '[+] Installing required packages')
    
    print(BRIGHT_YELLOW + '[+] Updating...')
    subprocess.call("pkg update -y", shell=True)
    
    print(BRIGHT_YELLOW + '[+] Upgrading...')
    subprocess.call("pkg upgrade -y", shell=True)
    
    print(BRIGHT_YELLOW + '[+] Installing requirements ...')
    subprocess.call("pkg install nmap openssh termux-auth termux-api -y", shell=True)
    
    print(BRIGHT_YELLOW + '[+] Installation completed!!')


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
    subprocess.call("sshd", shell=True)
    return True


def check_port():
    if start_ssh():
        nmap_output = subprocess.check_output("nmap localhost", shell=True).decode('utf-8')
        return nmap_output


def get_wlan_info():
    return subprocess.check_output("ifconfig wlan0", shell=True).decode('utf-8')


def kill_ssh():
    try:
        subprocess.call(["pkill","ssh"], shell=True)
        return True
    except Exception as e:
        Exception_Message(e)
        return False


def restart_ssh():
    if kill_ssh():
        print(Style.BRIGHT + '[+] SSH Server Successfully Killed.')
    if start_ssh():
        print(Style.BRIGHT + '[+] SSH Server Successfully Started.')


def Exception_Message(Exception):
    print(BRIGHT_RED + '[-] An Error occured while running the script, please create an issue on github to resolve issue and make script better.')
    print(BRIGHT_YELLOW + '[+] Github URL: https://github.com/dmrdhrumilmistry/Termux-SSH ')
    print(BRIGHT_RED + Exception)


def exit_program():
    print(BRIGHT_RED + '[+] Exiting Program... Please be patient...')
    kill_ssh()


def show_connect_command():
    banner()
    user = get_user()

    wlan_info = get_wlan_info()
    wlan_inet_regex = r'(?:inet\s*)(.*)(?:netmask)'
    inet_ip = re.search(wlan_inet_regex, wlan_info).group(1).strip()

    port_result = check_port()
    port_regex = r'(.*)(?:open\s*oa-system)'
    tcp_port_details = re.search(port_regex, port_result).group(0)
    tcp_port = re.search(r'\d*', tcp_port_details).group(0)


    print(BRIGHT_WHITE + f'[+] USER : {user}')
    print(BRIGHT_WHITE +f'[+] IP : {inet_ip}')
    print(BRIGHT_WHITE +f'[+] PORT : {tcp_port}')

    print(BRIGHT_WHITE +'Connect to this device wirelessly using below command in terminal:')
    print(BRIGHT_YELLOW + f'ssh {user}@{inet_ip} -p {tcp_port}')
