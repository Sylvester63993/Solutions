import requests
import json

KEY = "bf39b989-b47c-4557-abfd-5b3b492aca36"


def fetch_data(key=KEY):
    start = input("Indtast start kalenderår: ")
    end = input("Indtast slut kalenderår: ")
    date = "datetime=" + start + "-01-01T00:00:00%2B02:00/" + end + "-01-01T00:00:00%2B02:00"
    url = "https://dmigw.govcloud.dk/v2/lightningdata/collections/observation/items?limit=100&bbox=7,54,16,58&" + date + "&api-key=" + key
    response = requests.get(url)
    data = json.loads(response.text)
    print(f'{data=}')
    print(data)
    print("URL: " + url)
    print("Date: " + date)


if __name__ == "__main__":  # Executed when invoked directly
    print(fetch_data(KEY))
    # start = input("Indtast start kalenderår: ")
    # end = input("Indtast slut kalenderår: ")
    # date = start + "-01-01T00:00:00%2B02:00/" + end + "-01-01T00:00:00%2B02:00"
    # print(date)
