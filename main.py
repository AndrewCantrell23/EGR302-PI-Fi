import os
from DatabaseConnection import DB
import pandas as pd

#
# os.system('python speedtest-cli.py --json > myoutput.json')
#
# f = open("myoutput.json", "r")

# # read from json file
# line = f.readline()
# arr = line.split()
#
# # assign speed variables
# download = (str(arr[1]))[0:(len(arr[1]) - 1)]
# upload = (str(arr[3]))[0:(len(str(arr[3])) - 1)]
# ping = (str(arr[5]))[0:(len(str(arr[5])) - 1)]
#
# # for debugging purposes currently
# print(download)
# print(upload)
# print(ping + "ms")

# TODO add sql connect server and execute insert command


def main():
    base = DB()
    data = {  # this here should be the json file
        'Location': 'Point',
        'Ping': 5,
        'Download': 152.00,
        'Upload': 32.99
    }
    # base.enter_data(data=data)
    # results stores the query results as a dataFrame object
    results = base.extract(cols='*')
    print(results)

    # print(type(results))
    # results_json stores results in json format
    # results_json = pd.DataFrame.to_json(results)
    # print(results_json)


if __name__ == '__main__':
    main()
