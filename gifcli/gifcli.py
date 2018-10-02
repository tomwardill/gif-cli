import json
import os
import random
import sys

import requests


API_BASE = 'https://api.giphy.com/v1/gifs/search'


def get_config():
    config_dir = os.path.abspath(os.environ.get('SNAP_USER_COMMON', '.'))
    config_path = os.path.join(config_dir, 'gif-cli.json')
    with open(config_path) as config_file:
        config = json.load(config_file)
        return config

def run():
    search_string = ' '.join(sys.argv[1:])

    config = get_config()

    response = requests.get(
        API_BASE,
        params={
            'api_key': config['api_key'],
            'q': search_string,
        }
    )

    if response.status_code != 200:
        print("Error {} from giphy".format(response.status_code))
        sys.exit(1)

    payload = response.json()
    number_in_result = payload['pagination']['count']
    chosen = random.randint(0, number_in_result - 1)
    result = payload['data'][chosen]
    print(result['images']['original']['url'])
