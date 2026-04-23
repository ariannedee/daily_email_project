"""
Get weather details
"""

from pprint import pprint

import requests

try:
    from .weather_codes import weather_from_code as weather_codes
except ImportError:
    from weather_codes import weather_from_code as weather_codes

DEBUG = False


def get_weather_data():
    base_url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'timezone': 'America/Los_Angeles',
        'latitude': 49.2497,
        'longitude': -123.1193,
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

    return data


data = get_weather_data()
today = data['daily']
temp_c_high = today['temperature_2m_max'][0]
temp_c_low = today['temperature_2m_min'][0]
weather_code = today['weathercode'][0]
weather = weather_codes.get(weather_code)


if __name__ == '__main__':
    content = f"""Today is going to be {weather.lower()}.
    
    High: {temp_c_high}°C
    Low: {temp_c_low}°C
    """

    print(content)