import requests
import json
from requests.exceptions import HTTPError

def fetch_data():
    for url in ['http://sspcodingexercise.s3-website-us-west-2.amazonaws.com/Sample.json']:
        try:
            response = requests.get(url)

            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')
            with open('data/data.json', 'w') as outfile:
                json.dump(response.json(), outfile)