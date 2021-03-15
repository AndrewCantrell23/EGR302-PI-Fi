import os
from DatabaseConnection import DB
import json


def main():
    os.system('python speedtest-cli.py --json > myoutput.json')

if __name__ == '__main__':
    main()
