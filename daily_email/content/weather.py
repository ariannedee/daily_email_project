from datetime import datetime
from pprint import pprint

import requests

try:
    from .weather_codes import weather_from_code
except ImportError:
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
    pprint(data)

today = data['daily']
temp_c_high = today['temperature_2m_max'][0]
temp_c_low = today['temperature_2m_min'][0]
weathercode = today['weathercode'][0]
weather = weather_from_code.get(weathercode, f"unknown condition for code {weathercode}")
sunrise = datetime.fromisoformat(today['sunrise'][0]).strftime("%-I:%M %p")
sunset = datetime.fromisoformat(today['sunset'][0]).strftime("%-I:%M %p")

if __name__ == "__main__":
    print(f"""High temp: {temp_c_high}°C
Low temp: {temp_c_low}°C
Weather: {weather}
""")