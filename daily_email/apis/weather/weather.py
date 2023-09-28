"""Get weather details from Open-Meteo"""

from pprint import pprint

import requests

try:
    from weather_codes import weather_from_code
except ModuleNotFoundError:
    from .weather_codes import weather_from_code

DEBUG = False


def c_to_f(temp_c):
    """Convert temperature from Celsius to Fahrenheit"""
    return (temp_c * 9 / 5) + 32


def get_message():
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

    todays_data = data['daily']
    today_code = todays_data['weathercode'][0]
    today_weather = weather_from_code[today_code].lower()
    temp_c_high = todays_data['temperature_2m_max'][0]
    temp_c_low = todays_data['temperature_2m_min'][0]

    return f"""Today is going to be {today_weather}.

High of {temp_c_high}°C ({c_to_f(temp_c_high)}°F) 
Low of {temp_c_low}°C ({c_to_f(temp_c_low)}°F) """


if __name__ == '__main__':
    print(get_message())
