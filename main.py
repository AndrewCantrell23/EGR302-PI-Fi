import os
from DatabaseConnection import DB
import json


def main():
    base = DB()
    os.system('python speedtest-cli.py --json > myoutput.json')

    with open('myoutput.json') as f:
        unfiltered = json.load(f)

    # TODO: Download and Upload values are too big for the database requirement
    data = {
        'Location': 'Lancer Arms',
        'Download': unfiltered['download'],
        'Ping': unfiltered['ping'],
        'Upload': unfiltered['upload'],
        'times': unfiltered['timestamp']

    }
#     want is useless
    want = {  # this here should be the json file
        'Location': 'Point',
        'Ping': 50000,
        'Download': 152.0000,
        'Upload': 32.90009
    }
    base.enter_data(data=data)
    # results stores the query results as a dataFrame object
    results = base.extract(cols='*')
    print(results)

    results_json = results.to_json(orient='records')
    with open(f'data.json', 'w', encoding='utf-8') as f:
        json.dump(results_json, f, ensure_ascii=False, indent=4)
    

if __name__ == '__main__':
    main()
