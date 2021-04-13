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
    os.system('python speedtestNew.py --json > myoutput.json')

    with open('myoutput.json') as f:
        unfiltered = json.load(f)

    # TODO: Download and Upload values are too big for the database requirement
    data = {
        'Location': 'Point',
        'Download': unfiltered['download'] / 1000000,
        'Ping': unfiltered['ping'],
        'Upload': unfiltered['upload'] / 1000000,
        'times': unfiltered['timestamp']

    }

    base.enter_data(data=data)
    # results stores the query results as a dataFrame object

    results = base.extract_all(cols='*')
    print(results)

    results_json = results.to_json(orient='records')
    parsed = json.loads(results_json)
    with open(f'data.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)

    #
    # specific_results = base.loc(loc='Points')
    # print(specific_results)
    #
    # specific_json = specific_results.to_json(orient='records', date_format='iso')
    # parsed = json.loads(specific_json)
    # with open(f'specific data.json', 'w', encoding='utf-8') as f:
    #     json.dump(parsed, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
