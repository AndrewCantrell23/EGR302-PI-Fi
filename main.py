import os
from DatabaseConnection import DB
import pandas


os.system('python speedtest-cli.py --json > myoutput.json')

f = open("myoutput.json", "r")

# read from json file
line = f.readline()
arr = line.split()

# assign speed variables
download = (str(arr[1]))[0:(len(arr[1]) - 1)]
upload = (str(arr[3]))[0:(len(str(arr[3])) - 1)]
ping = (str(arr[5]))[0:(len(str(arr[5])) - 1)]

# for debugging purposes currently
print(download)
print(upload)
print(ping + "ms")

# TODO add sql connect server and execute insert command


def main():
    base = DB()
    data = {  # this here should be the json file
        'Location': 'Smith',
        'Times': '2021-01-01 12:01:00',
        'Ping': 344,
        'Down': 3.44,
        'Upload': 23.99
    }
    base.enter_data(data=data)
    results = base.extract(cols='*')
    print(results.head())


if __name__ == '__main__':
    main()
