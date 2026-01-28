import requests

from pprint import pprint as pretty_print

from weather_codes import weather_from_code

DEBUG = False
base_url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'timezone': 'America/New_York',
    'latitude': 42.997262156214305,
    'longitude': -81.20390128320294,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
    'forecast_days': 1,
}
headers = {
    'content-type': 'application/json'
}
response = requests.get(base_url, params=params, headers=headers)
data = response.json()

if DEBUG:
    print(response.url)
    pretty_print(data)

today = data['daily']
temp_high = today['temperature_2m_max'][0]
temp_low = today['temperature_2m_min'][0]
weathercode = today['weathercode'][0]
weather = weather_from_code.get(weathercode, f"Code {weathercode} not found")
