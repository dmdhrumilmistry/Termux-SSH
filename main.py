#!usr/bin/env python3
from termux import start, start_ssh, check_port, get_wlan_info, restart_ssh, exit_program 


check = 'y'
while(check in ('Y','y')):
    start()
    check = input('[+] Would you like to continue? (y/n): ')

exit_program()
