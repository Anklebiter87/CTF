import sys
import os

try:
    from utils import base
except ModuleNotFoundError:
    sys.path.append('utils')
    from utils import base

def main():
    os = base.check_os()
    print(os.getcwd())

if __name__ == "__main__":
    main()
