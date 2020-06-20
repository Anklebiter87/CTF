#!/usr/bin/env python3

import sys
import os

basedir = os.getcwd()
basedir = basedir[:basedir.find('CTF')+3]
sys.path.append(basedir)

from utils.base import check_os

def main():
    if len(sys.argv) < 2:
        print("Give a ctf to add")
        sys.exit(1)
    ctf = sys.argv[1]
    installed_os = check_os(basedir)
    try:
        newdir = installed_os.newctf(ctf)
        print(f"Created {ctf}")
    except FileExistsError:
        print("CTF is alread there")

if __name__ == "__main__":
    main()
