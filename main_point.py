import os
from DatabaseConnection import DB
import json
from datetime import datetime
import pytz
from schedule import every, repeat, run_pending
import time


def change_timezone_to_pst(utc_datetime_object):
    pst = pytz.timezone("Us/Pacific")
    return utc_datetime_object.astimezone(pst).strftime('%D %I:%M:%S %p')


def replace_datetime_formats(parsed_list):
    for speedtest_object in parsed_list:
        for dictPair in speedtest_object:
            if dictPair == "Times":
                datetime_object = datetime.strptime(speedtest_object.get(dictPair), "%Y-%m-%dT%H:%M:%S.000Z")
                updated_date = change_timezone_to_pst(datetime_object)
                speedtest_object.update({dictPair: updated_date})


@repeat(every(1).minute)
def job():
    base = DB()
    os.system('python speedtestNew.py --json > myoutput.json')

    with open('myoutput.json') as f:
        unfiltered = json.load(f)

    data = {
        'Location': 'Point',
        'Ping': unfiltered['ping'],
        'Download': unfiltered['download'] / 1000000,
        'Upload': unfiltered['upload'] / 1000000,
        'Times': datetime.strptime(unfiltered['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    }

    base.enter_data(data=data)


def main():
    base = DB()
    while True:
        run_pending()
        time.sleep(1)

    specific_1_hour_results = base.cream_of_the_crop(hours=1)
    print(specific_1_hour_results)

    specific_json = specific_1_hour_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    replace_datetime_formats(parsed)

    with open(f'webpages/json data/recent one hour all location speeds.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)

    specific_5_hour_results = base.cream_of_the_crop(hours=5)
    print(specific_5_hour_results)

    specific_json = specific_5_hour_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    replace_datetime_formats(parsed)

    with open(f'webpages/json data/recent five hours all location speeds.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
