#!usr/bin/env python3
from termux import start, exit_program 


IS_RUNNING = True
while(IS_RUNNING):
    start()
    check = input('[+] Press Any Key to continue, to exit enter 6:')
    if check == '6':
        IS_RUNNING = False
    

print('[+] Exiting... Please be patient...')
exit_program()
