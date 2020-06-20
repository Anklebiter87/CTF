#!/usr/bin/env python3

import sys 
from os import getcwd


basedir = getcwd()
basedir = basedir[:basedir.find('CTF')+3]
sys.path.append(basedir)

from utils.base import check_os

def main():
    if len(sys.argv) < 2:
        print("Give a challenge to add")
        sys.exit(1)
    chall = sys.argv[1]
    installed_os = check_os(basedir)
    try:
        newdir = installed_os.newchallenge(sys.argv[1])
        print(f"Created {newdir}")

    except FileExistsError:
        print("Challenge is alread there")

if __name__ == "__main__":
    main()
