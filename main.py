#!usr/bin/env python3
from termux import start, start_ssh, check_port, get_wlan_info, restart_ssh, exit_program 


IS_RUNNING = True
while(IS_RUNNING):
    try:
        start()
        check = choice = int(input("[+] Command >"))
        if check == '6':
            IS_RUNNING = False
    except Exception:
        print("[-] An Error Occured, Report to developer by creating an issue on github.")
        print("[+] github repository url: https://github.com/dmdhrumilmistry/Termux-SSH")
        raise Exception
    

print('[+] Exiting... Please be patient...')
exit_program()
