import os
from DatabaseConnection import DB
import json
from datetime import datetime


def main():
    base = DB()
    # os.system('python speedtest-cli.py --json > myoutput.json')
    #
    # with open('myoutput.json') as f:
    #     unfiltered = json.load(f)
    #
    # # # TODO: Download and Upload values are too big for the database requirement
    # data = {
    #     'Location': 'Points',
    #     'Download': unfiltered['download']/1000000,
    #     'Ping': unfiltered['ping'],
    #     'Upload': unfiltered['upload']/1000000
    #     # 'times': unfiltered['timestamp']
    #
    # }

    # want is useless
    want = {  # this here should be the json file
        'Location': 'Points',
        'Ping': 170,
        'Download': 420.0000,
        'Upload': 37.90009
    }
    base.enter_data(data=want)
    # results stores the query results as a dataFrame object

    for item in want:
        print(f"{item}: {want[item]}")

    print("\n\nDATABASE STUFF")

    results = base.extract(cols='*')
    print(results)

    results_json = results.to_json(orient='records')
    parsed = json.loads(results_json)
    with open(f'data.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)

    specific_results = base.loc(loc='Points')
    print(specific_results)

    specific_json = specific_results.to_json(orient='records', date_format='iso')
    parsed = json.loads(specific_json)
    with open(f'specific data.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
    main()
