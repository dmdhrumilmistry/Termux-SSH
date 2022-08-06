__version__ = '0.1'
__author__ = 'dmdhrumilmistry'

def cowsay_banner():
    '''
    description: prints cowsay banner
    '''
    print(f"""
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
|Author:      {__author__} |
|Version:     {__version__}             |
+-----------------------------+
""")

cowsay_banner()