#!usr/bin/env python3
from termux import get_user, generate_passwd, banner, install_req


install_req()
generate_passwd(get_user())
