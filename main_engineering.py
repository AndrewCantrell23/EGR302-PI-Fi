import os
from DatabaseConnection import DB
import json
from datetime import datetime
import pytz
from schedule import every, repeat, run_pending
import time


@repeat(every(1).hour)
def job():
    entering_data = DB()
    os.system('python speedtestNew.py --json > myoutput.json')

    with open('myoutput.json') as f:
        unfiltered = json.load(f)

    data = {
        'Location': 'Smith',
        'Ping': unfiltered['ping'],
        'Download': unfiltered['download'] / 1000000,
        'Upload': unfiltered['upload'] / 1000000,
        'Times': datetime.strptime(unfiltered['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    }

    entering_data.enter_data(data=data)
    entering_data.closing()


def main():
    while True:
        run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
