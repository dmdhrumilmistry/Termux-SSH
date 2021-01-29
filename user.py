#!usr/bin/env/ python
import subprocess


def get_user():
    user = subprocess.check_output(["whoami"])
    return user


def generate_passwd(user):
    print("[+] Creating password for user")
    print("Note: You will be asked to enter password, You must enter the same password while connecting.")
    subprocess.call(["passwd", user])
