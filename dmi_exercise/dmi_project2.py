import requests
import json

KEY = "bf39b989-b47c-4557-abfd-5b3b492aca36"


def fetch_data(key=KEY):
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=100&api-key=" + key
    response = requests.get(url)
    data = json.loads(response.text)
    print(f'{data=}')

if __name__ == "__main__":  # Executed when invoked directly
    print(fetch_data(KEY))

# https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?datetime=2018-02-12T00:00:00Z/2018-03-18T00:00:00Z&api-key=bf39b989-b47c-4557-abfd-5b3b492aca36