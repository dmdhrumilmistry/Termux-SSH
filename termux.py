#!usr/bin/env python3
from prettytable import PrettyTable
import subprocess
import colorama
import re
from colorama import Style, Fore


# for terminal colors
colorama.init(autoreset=True)
BRIGHT_WHITE = Style.BRIGHT + Fore.WHITE
BRIGHT_YELLOW = Style.BRIGHT + Fore.YELLOW
BRIGHT_RED = Style.BRIGHT + Fore.RED
BRIGHT_GREEN = Style.BRIGHT + Fore.GREEN
RESET_COLORS = Style.RESET_ALL


# commands menu table
menu = PrettyTable(['command', 'description'])
menu.add_row(['start', 'starts SSH server'])
menu.add_row(['port', 'checks on which port server is running'])
menu.add_row(['user', 'get username'])
menu.add_row(['genpass', 'generates new password for user'])
menu.add_row(['wlan ip', 'get wlan ip of the device'])
menu.add_row(['connect cmd', 'connect to this using using command printed'])
menu.add_row(['restart', 'restarts ssh server'])
menu.add_row(['exit','stops ssh server and exit'])


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


def help():
    print(menu)


def get_user():
    return subprocess.check_output("whoami", shell=True).decode('utf-8').strip()


def generate_passwd():
    user = get_user()
    print(BRIGHT_WHITE + f"\n[!] Creating new password for user {user} ")
    print(BRIGHT_YELLOW  +"Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call('passwd', shell=True)


def install_termux_req():
    banner()
    print(BRIGHT_YELLOW + '\n[+] Installing required packages')
    
    print(BRIGHT_YELLOW + '\n[+] Updating...')
    subprocess.call("pkg update -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Upgrading...')
    subprocess.call("pkg upgrade -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Installing requirements ...')
    subprocess.call("pkg install nmap openssh termux-auth termux-api -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Installation completed!!\n')


def start_ssh():
    try:
        subprocess.call("sshd", shell=True)
        return True
    except Exception as e:
        Exception_Message(e)


def get_ssh_port():
    if start_ssh():
        port_result = subprocess.check_output("nmap localhost", shell=True).decode('utf-8')
        port_regex = r'(.*)(?:open\s*oa-system)'
        tcp_port_details = re.search(port_regex, port_result).group(0)
        tcp_port = re.search(r'\d*', tcp_port_details).group(0)
        return tcp_port


def get_wlan_ip():
    wlan_info = subprocess.check_output("ifconfig wlan0", shell=True).decode('utf-8')
    wlan_inet_regex = r'(?:inet\s*)(.*)(?:netmask)'
    wlan_inet_ip = re.search(wlan_inet_regex, wlan_info).group(1).strip()
    return wlan_inet_ip


def kill_ssh():
    try:
        subprocess.call("pkill ssh", shell=True)
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
    user = get_user()
    wlan_ip = get_wlan_ip()
    ssh_port = get_ssh_port()


    print(BRIGHT_WHITE + f'[+] USER : {user}')
    print(BRIGHT_WHITE +f'[+] IP : {wlan_ip}')
    print(BRIGHT_WHITE +f'[+] PORT : {ssh_port}')

    print(BRIGHT_WHITE +'Use below command to connect:')
    print(BRIGHT_YELLOW + f'ssh {user}@{wlan_ip} -p {ssh_port}')
