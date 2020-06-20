#!/usr/bin/env python3

import sys
import os

basedir = os.getcwd()
basedir = basedir[:basedir.find('CTF')+3]
sys.path.append(basedir)

from utils.base import check_os

def main():
    installed_os = check_os(basedir)
    

if __name__ == "__main__":
    main()
