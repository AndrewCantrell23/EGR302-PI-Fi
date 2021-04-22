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


def database_queries(filename, amount):
    base = DB()
    specific_results = base.cream_of_the_crop(hours=amount)
    base.closing()
    
    specific_json = specific_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    replace_datetime_formats(parsed)

    with open(f'webpages/json data/{filename}', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)


@repeat(every(1).hour)
def job():
    database_queries(filename='recent one hour all location speeds.json', amount=1)
    database_queries(filename='five hours all location speeds.json', amount=5)


def main():
    while True:
        run_pending()
        time.sleep(120)


if __name__ == '__main__':
    main()
