#!usr/bin/env python3
import subprocess
import colorama
import re
from prettytable import PrettyTable
from colorama import Style, Fore
from sys import exit

# for terminal colors
colorama.init(autoreset=True)
BRIGHT_WHITE = Style.BRIGHT + Fore.WHITE
BRIGHT_YELLOW = Style.BRIGHT + Fore.YELLOW
BRIGHT_RED = Style.BRIGHT + Fore.RED
BRIGHT_GREEN = Style.BRIGHT + Fore.GREEN
BRIGHT_LYELLOW = Style.BRIGHT + Fore.LIGHTYELLOW_EX
RESET_COLORS = Style.RESET_ALL


# commands menu table
menu = PrettyTable(['command', 'description'])
menu.add_row(['install', 'installs required tools'])
menu.add_row(['start', 'starts SSH server'])
menu.add_row(['clear', 'clears console screen'])
menu.add_row(['port', 'checks on which port server is running'])
menu.add_row(['user', 'get username'])
menu.add_row(['genpass', 'generates new password for user'])
menu.add_row(['wlan ip', 'get wlan ip of the device'])
menu.add_row(['connect cmd', 'connect to this using using command printed'])
menu.add_row(['restart', 'restarts ssh server'])
menu.add_row(['close', 'exits Termux-SSH without stopping SSH server'])
menu.add_row(['exit','stops ssh server and exit'])


def cowsay_banner():
    '''
    description: prints cowsay banner
    '''
    print(BRIGHT_GREEN +  """
+-----------------------------+
|  ____________               |
|< Termux-SSH >               | 
| ------------                | 
|        \   ^__^             |
|         \  (oo)\_______     |
|            (__)\       )\/\ |
|                ||----w |    |
|                ||     ||    |
+-----------------------------+
|  A tool by Dhrumil Mistry   |
+-----------------------------+
""")


def help():
    '''
    description: prints help menu commands
    '''
    print(menu)


def clear_console():
    '''
    description: clears console
    '''
    subprocess.call('clear', shell=True)


def get_user():
    '''
    description: get username of the termux user
    returns: username(str)
    '''
    return subprocess.check_output("whoami", shell=True).decode('utf-8').strip()


def generate_passwd():
    '''
    description: create new password for the termux user
    '''
    user = get_user()
    print(BRIGHT_WHITE + f"\n[!] Creating new password for user {user} ")
    print(BRIGHT_YELLOW  +"Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call('passwd', shell=True)


def install_cmd():
    '''
    description: handles install command
    '''
    install_termux_req()
    generate_passwd()



def install_termux_req():
    '''
    description: installs requirements
    '''
    cowsay_banner()
    print(BRIGHT_YELLOW + '\n[+] Installing required packages')
    
    print(BRIGHT_YELLOW + '\n[+] Updating...')
    subprocess.call("pkg update -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Upgrading...')
    subprocess.call("pkg upgrade -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Installing requirements ...')
    subprocess.call("pkg install nmap openssh termux-auth termux-api -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[+] Installation completed!!\n')


def start_ssh():
    '''
    description: starts ssh server
    returns: bool
    '''
    try:
        subprocess.call("sshd", shell=True)
        return True
    except Exception as e:
        Exception_Message(e)
        return False


def get_ssh_port():
    '''
    description: get ssh server port
    returns: str or None
    '''
    if start_ssh():
        port_result = subprocess.check_output("nmap localhost", shell=True).decode('utf-8')
        port_regex = r'(.*)(?:open\s*oa-system)'
        tcp_port_details = re.search(port_regex, port_result).group(0)
        tcp_port = re.search(r'\d*', tcp_port_details).group(0)
        return tcp_port


def get_wlan_ip():
    '''
    description: get wlan0 device ip assigned by router/DHCP
    returns: str or None
    '''
    wlan_info = subprocess.check_output("ifconfig wlan0", shell=True).decode('utf-8')
    wlan_inet_regex = r'(?:inet\s*)(.*)(?:netmask)'
    wlan_inet_ip = re.search(wlan_inet_regex, wlan_info).group(1).strip()
    return wlan_inet_ip


def kill_ssh():
    '''
    description: kills ssh server
    returns: bool
    '''
    try:
        subprocess.call("pkill sshd", shell=True)
        return True
    except Exception as e:
        Exception_Message(e)
        return False


def restart_ssh():
    '''
    description: restarts ssh server
    '''
    if kill_ssh():
        print(Style.BRIGHT + '[+] SSH Server Successfully Killed.')
    if start_ssh():
        print(Style.BRIGHT + '[+] SSH Server Successfully Started.')


def Exception_Message(Exception):
    '''
    description: handles exception by printing message and exception
    '''
    print(BRIGHT_RED + '[-] An Error occured while running the script, please create an issue on github to resolve issue and make script better.')
    print(BRIGHT_YELLOW + '[+] Github URL: https://github.com/dmrdhrumilmistry/Termux-SSH ')
    print(BRIGHT_RED + Exception)


def exit_program(kill_ssh_server:bool = False):
    '''
    description: closes ssh server and exits the program
    '''
    print(BRIGHT_RED + '[+] Exiting Program... Please be patient...')
    if kill_ssh_server:
        kill_ssh()
    exit()


def show_connect_command():
    '''
    description: prints ssh command to help user to connect to the Termux terminal
    '''
    user = get_user()
    wlan_ip = get_wlan_ip()
    ssh_port = get_ssh_port()


    print(BRIGHT_WHITE + f'[+] USER : {user}')
    print(BRIGHT_WHITE +f'[+] IP : {wlan_ip}')
    print(BRIGHT_WHITE +f'[+] PORT : {ssh_port}')

    print(BRIGHT_WHITE +'Use below command to connect:')
    print(BRIGHT_LYELLOW + f'ssh {user}@{wlan_ip} -p {ssh_port}\n')
