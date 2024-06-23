import os
import requests
import json
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(filename='main.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_TOKEN = os.getenv('API_TOKEN')

Headers = {
    'X-Auth-Token': API_TOKEN
}

# Top 5 leagues
COMPETITIONS_IDS = {2021, 2014, 2015, 2019, 2002}
SEASON = 2023

_ids_count = 'ids_count.json'
time = datetime.now()


def trigger_webhook():
    logging.info('Starting the webhook trigger process')
    matches = []

    try:
        with open(_ids_count, 'r') as f:
            ids_count = json.load(f)
            logging.info('Loaded ids_count from file: %s', ids_count)
    except Exception as e:
        logging.error('Failed to load ids_count from file: %s', e)
        return

    '''Check for new IDs'''
    for comp_id in COMPETITIONS_IDS:
        logging.info('Checking competition ID: %s', comp_id)
        uri = f'http://api.football-data.org/v4/competitions/{comp_id}/matches?season={SEASON}&status=FINISHED'
        response = requests.get(uri, headers=Headers)

        if response.status_code == 200:
            logging.info('Successfully fetched data for competition ID: %s', comp_id)
            data = response.json()
            _matches = [match for match in data['matches']]
        else:
            logging.error('Failed to fetch data for competition ID: %s, Status code: %s', comp_id, response.status_code)
            _matches = []

        matches.extend(_matches)

    logging.info('Total matches fetched: %d', len(matches))
    match_ids = [match['id'] for match in matches]

    '''Trigger webhook if any new matches are played'''
    if len(match_ids) != ids_count['ids_count']:
        logging.info('New matches detected. Triggering webhook.')
        response = requests.post('https://fbtransfersdashboard.azurewebsites.net/refresh_dashboard')

        if response.status_code == 200:
            logging.info('Webhook triggered successfully. Response: %s', response.json())
            ids_count['ids_count'] = len(match_ids)

            try:
                with open(_ids_count, 'w') as f:
                    json.dump(ids_count, f)
                    logging.info('Updated ids_count in file: %s', ids_count)
            except Exception as e:
                logging.error('Failed to update ids_count in file: %s', e)
        else:
            logging.error('Failed to trigger webhook. Status code: %s', response.status_code)
    else:
        logging.info('No new matches detected. No webhook triggered.')


if __name__ == '__main__':
    trigger_webhook()
