#!usr/bin/env python3
import textwrap
from colorama import Style, Fore
from prettytable import PrettyTable
from sys import exit


import colorama
import  os
import re
import subprocess
import time
import netifaces as nic


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
menu.add_row(['wlanip', 'get wlan ip of the device'])
menu.add_row(['conncmd', 'connect to this using using command printed'])
menu.add_row(['torssh','start ssh service on tor network'])
menu.add_row(['torhost','get TOR network hostname'])
menu.add_row(['stoptor','exit tor network'])
menu.add_row(['restart', 'restarts ssh server'])
menu.add_row(['close', 'exits Termux-SSH without stopping SSH server'])
menu.add_row(['exit','stops ssh server and exit'])


# tor commands and confs
HOME = os.environ["HOME"]
ALIAS_FILE = os.path.join(HOME, ".tor_ssh_aliases")
SHELL = os.environ['SHELL'].split('/')[-1]

TOR_SSH_DIR = os.path.join(os.environ['PREFIX'], "var", 'lib','tor','hidden_ssh')
HOSTNAME_FILE = os.path.join(TOR_SSH_DIR, "hostname")
TORRC_FILE = os.path.join(TOR_SSH_DIR, 'torrc')
tor_start = f'tor -f {TORRC_FILE} &; sshd &'
tor_stop=f'pkill -9 tor'


# functions
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
    clear_console()
    install_termux_req()
    conf_tor()
    generate_passwd()



def install_termux_req():
    '''
    description: installs requirements
    '''
    cowsay_banner()
    print(BRIGHT_YELLOW + '\n[*] Installing required packages')
    
    print(BRIGHT_YELLOW + '\n[*] Updating...')
    subprocess.call("pkg update -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[*] Upgrading...')
    subprocess.call("pkg upgrade -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[*] Installing requirements ...')
    subprocess.call("pkg install nmap openssh termux-auth termux-api tor proxychains-ng -y", shell=True)
    
    print(BRIGHT_YELLOW + '\n[*] Installation completed!!\n')
    
    print(BRIGHT_YELLOW + "[*] Clearing Screen in...", end="")
    for _ in range(5, 0, -1):
        print(_, end="...")
        time.sleep(0.35)
    print()
    clear_console()
    cowsay_banner()


def conf_tor():
    '''
    description: configure termux-ssh for tor network
    returns: bool
    '''
    # delete and create new directory
    os.system(f"rm -rf {TOR_SSH_DIR}")
    os.system(f"mkdir -p {TOR_SSH_DIR}")

    # configure shell
    shell_conf = {'bash':'.bashrc', 'zsh':'.zshrc'}
    SHELL_RC_FILE = os.path.join(HOME, shell_conf.get(SHELL, ''))
    
    # create aliases
    print(BRIGHT_YELLOW + "[*] Generating aliases...")
    aliases = textwrap.dedent(f'''
    ###################
    # TOR SSH aliases

    alias tor-ssh-start="{tor_start}"
    alias tor-ssh-stop="{tor_stop}"''')
    with open(ALIAS_FILE, 'w') as f:
        f.write(aliases)

    if SHELL_RC_FILE != "":
        with open(SHELL_RC_FILE, 'a+') as f:
            f.write(f'\nsource {ALIAS_FILE}\n')
        print(BRIGHT_YELLOW + "[*] Restart Termux before using SSH over TOR.")
    else:
        print(BRIGHT_RED + f"[X] add alias file {ALIAS_FILE} to .bashrc/.zshrc file manually.")

    # TORRC CONF
    print(BRIGHT_YELLOW + '\n[*] Generating torrc file ...')

    torrc = textwrap.dedent(f'''
    ## Enable TOR SOCKS proxy
    SOCKSPort 127.0.0.1:9050

    ## Hidden Service: SSH
    HiddenServiceDir {TOR_SSH_DIR}
    HiddenServicePort 22 127.0.0.1:8022\n\n''')

    # write conf file to torrc
    with open(TORRC_FILE, 'w+') as conf_file:
        conf_file.write(torrc)
    
    print(BRIGHT_YELLOW + '\n[*] Generating hostname for TOR Network ...')
    os.system(f'tor -f {TORRC_FILE} &')

    print(BRIGHT_YELLOW + '\n[*] Waiting for 30s for hostname to be generated ...')
    time.sleep(30)

    print(BRIGHT_YELLOW + '\n[*] Killing TOR service ...')
    os.system("pkill -9 tor")

    print(BRIGHT_YELLOW + '\n[*] Extracting hostname ...')
    if os.path.isfile(HOSTNAME_FILE):
        with open(HOSTNAME_FILE, 'r') as f:
            hostname = f.read()
            if hostname != "":
                print(BRIGHT_GREEN + f"HOSTNAME : {hostname}")
                return True
    print(BRIGHT_RED + "Hostname has not been generated. run tor manually to generate hostname")
    return False


def get_tor_hostname():
    '''
    description: gets tor hostname which will be used to connect
    '''
    return subprocess.check_output(f"cat {HOSTNAME_FILE}", shell=True, executable=os.environ["SHELL"]).decode('utf-8')


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
    return nic.ifaddresses('wlan0')[nic.AF_INET][0]['addr']


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
        print(Style.BRIGHT + '[*] SSH Server Successfully Killed.')
    if start_ssh():
        print(Style.BRIGHT + '[*] SSH Server Successfully Started.')


def Exception_Message(Exception):
    '''
    description: handles exception by printing message and exception
    '''
    print(BRIGHT_RED + '[-] An Error occured while running the script, please create an issue on github to resolve issue and make script better.')
    print(BRIGHT_YELLOW + '[*] Github URL: https://github.com/dmrdhrumilmistry/Termux-SSH ')
    print(f'{BRIGHT_RED}{Exception}')


def exit_program(kill_ssh_server:bool = False):
    '''
    description: closes ssh server and exits the program
    '''
    print(BRIGHT_RED + '[*] Exiting Program... Please be patient...')
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


def start_tor_ssh():
    '''
    description: starts ssh over 
    '''
    subprocess.call(tor_start, shell=True, executable=os.environ["SHELL"])


def stop_tor():
    '''
    description: stops tor network
    '''
    subprocess.call(tor_stop, shell=True, executable=os.environ["SHELL"])