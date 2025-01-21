from pprint import pprint

import requests

from daily_email.weather_codes import weather_from_code

DEBUG = False
base_url = f'https://api.open-meteo.com/v1/forecast'
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
response = requests.get(base_url, headers=headers, params=params)
data = response.json()

if DEBUG:
    print(response.url)
    pprint(data)

today = data['daily']
high_temp_c = today['temperature_2m_max'][0]
low_temp_c = today['temperature_2m_min'][0]
weather_code = today['weathercode'][0]
weather = weather_from_code[weather_code].lower()


if __name__ == "__main__":
    print(f"{high_temp_c=}")
    print(f"{low_temp_c=}")
    print(f"{weather=}")
