import os
import requests
import json
from datetime import datetime

Headers = {
'X-Auth-Token': 'fd3e3c8fccfb418ea187aba67e985377'
}
# Top 5 leagues
COMPETITIONS_IDS = {2021, 2014, 2015, 2019, 2002}
SEASON = 2023

_ids_count = 'ids_count.json'
time = datetime.now()

def trigger_webhook():
    matches = []
    with open(_ids_count, 'r') as f:
        ids_count = json.load(f)
        print(type(ids_count), ids_count)
    '''Check for new IDs'''
    for comp_id in COMPETITIONS_IDS:
        uri = f'http://api.football-data.org/v4/competitions/{comp_id}/matches?season={SEASON}&status=FINISHED'
        response = requests.get(uri, headers=Headers)
        if response.status_code == 200:
            print('Success')
            data = response.json()
            _matches = [match for match in data['matches']]
        else:
            print(response.status_code)
        matches.extend(_matches)
    print(len(matches))
    match_ids = [match['id'] for match in matches]
    '''Trigger webhook if any new mathces are played '''
    if len(match_ids) != ids_count['ids_count']:
        response = requests.post('https://footballdashboard.azurewebsites.net/refresh_dashboard')
        if response.status_code == 200:
            print(response.json())
            ids_count['ids_count'] = len(match_ids)
            print(ids_count)
            # refresh ids counts
            with open(_ids_count, 'w') as f:
                json.dump(ids_count, f)



if __name__ == 'main':
    trigger_webhook()






