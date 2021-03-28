import os
from DatabaseConnection import DB
import json
from datetime import datetime


def main():
    base = DB()
    os.system('python speedtest-cli.py --json > myoutput.json')

    with open('myoutput.json') as f:
        unfiltered = json.load(f)

    # TODO: Download and Upload values are too big for the database requirement
    data = {
        'Location': 'AAA',
        'Download': unfiltered['download']/1000000,
        'Ping': unfiltered['ping'],
        'Upload': unfiltered['upload']/1000000,
        'times': unfiltered['timestamp']

    }

    time = data['times'][11:23] + "Z"
    print(time)
    d = datetime.strptime(time, "%H:%M:%S.%fZ")
    print(d)
    d.strftime("%I:%M %p")
    print("---------------")
    print(d)
    # want is useless
    want = {  # this here should be the json file
        'Location': 'Point',
        'Ping': 50000,
        'Download': 152.0000,
        'Upload': 32.90009
    }
    base.enter_data(data=data)
    # results stores the query results as a dataFrame object

    for item in data:
        print(f"{item}: {data[item]}")

    print("\n\nDATABASE STUFF")

    results = base.extract(cols='*')
    print(results)

    results_json = results.to_json(orient='records')
    parsed = json.loads(results_json)
    with open(f'data.json', 'w', encoding='utf-8') as f:
        json.dump(parsed, f, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
    main()
