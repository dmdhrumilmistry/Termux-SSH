from os import name
from sys import exit

from .termux import (
    BRIGHT_RED,
    BRIGHT_YELLOW,
    RESET_COLORS,
    BRIGHT_WHITE,
    BRIGHT_GREEN,
    clear_console,
    cowsay_banner,
    exception_message,
    exit_program,
    get_ssh_port,
    get_user,
    generate_passwd,
    get_tor_hostname,
    get_wlan_ip,
    restart_ssh,
    show_connect_command,
    start_ssh,
    start_tor_ssh,
    stop_tor,
    install_cmd,
)


if name == 'nt':
    print(BRIGHT_RED + '[-] Termux-SSH is created for Termux Application on Android.')
    print(BRIGHT_YELLOW + '[!] Exiting Termux-SSH')
    exit()


clear_console()
cowsay_banner()
print(BRIGHT_YELLOW + "[Note] Termux-SSH only works in Termux Android Application.")


while True:
    try:

        cmd = input(BRIGHT_YELLOW +  "Termux-SSH >> " + RESET_COLORS).lower().strip()

        match cmd:
            case 'exit':
                exit_program(kill_ssh_server=True, kill_tor_server=True)

            case 'close':
                exit_program()

            case 'help':
                help()

            case 'clear':
                clear_console()
        
            case 'install':
                install_cmd()

            case 'start':
                if start_ssh():
                    print(BRIGHT_WHITE + '[*] SSH started successfully')
                else:
                    print(BRIGHT_RED + '[-] Cannot Start SSH Server')

            case 'port':
                ssh_port = get_ssh_port()
                if ssh_port:
                    print(BRIGHT_WHITE + f'[*] PORT : {ssh_port}')
                else:
                    print(BRIGHT_YELLOW + '[!] Start SSH server before finding the port')

            case 'user':
                username = get_user()
                print(BRIGHT_WHITE + f'[*] USER : {username}')   

            case 'genpass':
                generate_passwd()

            case 'wlanip':
                wlan_ip = get_wlan_ip()
                print(BRIGHT_WHITE + f'[*] WLAN IP : {wlan_ip}')

            case 'conncmd':
                show_connect_command()
            
            case 'torssh':
                start_tor_ssh()
                print(BRIGHT_GREEN + "[*] SSH can be connected over TOR.")
            
            case 'torhost':
                hostname = get_tor_hostname()
                if hostname != "":
                    print(BRIGHT_GREEN + f"[*] Hostname : {hostname}")
                else:
                    print(BRIGHT_RED + "[X] Cannot find hostname, try using install command.")

            case 'torstop':
                stop_tor()
                print(BRIGHT_GREEN + "[*] SSH over TOR stopped successfully.")

            case 'restart':
                restart_ssh()

            case _:
                print(BRIGHT_RED + '[!] INVALID COMMAND')

    except (EOFError, KeyboardInterrupt):
        print(BRIGHT_RED + "\n[-] User interruption detected! Services will be running in background")
        exit_program()

    except Exception as e:
        exception_message(e)
