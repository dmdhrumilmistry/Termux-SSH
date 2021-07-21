#!usr/bin/env python3
from termux import get_user, generate_passwd, install_termux_req

install_termux_req()
generate_passwd(get_user())
