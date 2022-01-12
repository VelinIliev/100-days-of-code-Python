import requests

URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = '************************'

params = {
    "lat": 42.6975,
    "lon": 23.3242,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
response = requests.get(URL, params=params)
response.raise_for_status()
weather_data = response.json()

for n in range(0,13):
    id = weather_data['hourly'][n]["weather"][0]["description"]
    if n == 0:
        print(f'now: {id}')
    elif n == 1:
        print(f'after {n} hour: {id}')
    else:
        print(f'after {n} hours: {id}')
    