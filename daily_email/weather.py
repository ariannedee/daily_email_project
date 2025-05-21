from pprint import pprint

import requests

from weather_codes import weather_from_code

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
response = requests.get(base_url, params, headers=headers)
data = response.json()
today = data['daily']
temp_hi = today['temperature_2m_max'][0]
temp_lo = today['temperature_2m_min'][0]
code = today['weathercode'][0]
condition = weather_from_code[code]

if __name__ == '__main__':
    pprint(data)
