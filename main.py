import os

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
print(ping)

#TODO add sql connect server and execute insert command