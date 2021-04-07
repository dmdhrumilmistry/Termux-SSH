#!usr/bin/env python3
from termux import start, print_menu, exit_program 


IS_RUNNING = True
while(IS_RUNNING):
    try:
        print_menu()
        choice = int(input("[+] Command > "))
        start(choice)

        if choice == 6:
            IS_RUNNING = False
    except Exception:
        print("[-] An Error Occured, Report to developer by creating an issue on github.")
        print("[+] github repository url: https://github.com/dmdhrumilmistry/Termux-SSH ")
        raise Exception
    

print('[+] Exiting... Please be patient...')
exit_program()
