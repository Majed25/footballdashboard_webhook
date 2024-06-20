import os
import json
from datetime import datetime



_ids_count_file = 'ids_count.json'

def trigger_webhook():
    matches = []
    with open(_ids_count_file, 'r') as f:
        ids_count = json.load(f)
    print(type(ids_count), ids_count)
  
    ids_count['ids_count'] = 888
    print(ids_count)
        # refresh ids counts
    with open(_ids_count, 'w') as f:
        json.dump(ids_count, f)

if __name__ == '__main__':
    trigger_webhook()
