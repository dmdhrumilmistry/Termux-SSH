#!usr/bin/env python3
from termux import *
from os import name
from sys import exit

if name == 'nt':
    print(BRIGHT_RED + '[-] Termux-SSH is created for Termux Application on Android.')
    print(BRIGHT_YELLOW + '[!] Exiting Termux-SSH')
    exit()


banner()
print(BRIGHT_YELLOW + "[Note] Termux-SSH only works in Termux Android Application.")

IS_RUNNING = True
while(IS_RUNNING):
    try:
        cmd = input(BRIGHT_YELLOW +  "Termux-SSH >> " + RESET_COLORS).lower().strip()

        if cmd == 'exit':
            exit_program()
            IS_RUNNING = False

        elif cmd == 'help':
            help()

        elif cmd == 'start':
            if start_ssh():
                print(BRIGHT_WHITE + '[*] SSH started successfully')
            else:
                print(BRIGHT_RED + '[-] Cannot Start SSH Server')

        elif cmd == 'port':
            ssh_port = get_ssh_port()
            if ssh_port:
                print(BRIGHT_WHITE + f'[*] PORT : {ssh_port}')
            else:
                print(BRIGHT_YELLOW + '[!] Start SSH server before finding the port')

        elif cmd == 'user':
            username = get_user()
            print(BRIGHT_WHITE + f'[*] USER : {username}')   

        elif cmd == 'genpass':
            generate_passwd()

        elif cmd == 'wlan ip':
            wlan_ip = get_wlan_ip()
            print(BRIGHT_WHITE + f'[*] WLAN IP : {wlan_ip}')

        elif cmd == 'connect cmd':
            show_connect_command()

        elif cmd == 'restart':
            restart_ssh()

        else:
            print(BRIGHT_RED + '[!] INVALID COMMAND')

    except Exception as e:
        Exception_Message(e)
