import os
from DatabaseConnection import DB
import json
from datetime import datetime
from crontab import CronTab


def main():
    # cron = CronTab(tabfile='file.tab')
    # job = cron.new(command="example", comment="printing")
    # job.minute.every(1)
    #
    #
    # job = cron.new(command='echo hello world')
    # job.minute.every(1)
    base = DB()
    # os.system('python speedtestNew.py --json > myoutput.json')
    #
    # with open('myoutput.json') as f:
    #     unfiltered = json.load(f)

    # base.enter_data(data=data)
    # results stores the query results as a dataFrame object


    specific_1_hour_results = base.cream_of_the_crop(hours=1)
    print(specific_1_hour_results)

    specific_json = specific_1_hour_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    with open(f'webpages/json data/recent one hour all location speeds.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)

    specific_5_hour_results = base.cream_of_the_crop(hours=5)
    print(specific_5_hour_results)

    specific_json = specific_5_hour_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    with open(f'webpages/json data/recent five hours all location speeds.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
