from datetime import datetime

try:
    from .weather_codes import weather_from_code
except ImportError:
    from weather_codes import weather_from_code


import requests
from environs import Env

env = Env()
env.read_env()

coordinates = (env.float('LATITUDE'), env.float('LONGITUDE'))


def get_weather():
    lat, lon = coordinates
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
        "timezone": "America/Los_Angeles",
        "forecast_days": 1,
    }
    headers = {
        'content-type': 'application/json'
    }
    response = requests.get(url, params, headers=headers)
    response.raise_for_status()

    data = response.json()
    weather_data = data['daily']
    return weather_data


def get_weather_message():
    weather_data = get_weather()

    weather_code = weather_data["weather_code"][0]
    condition = weather_from_code.get(weather_code, f"unknown ({weather_code})").lower()
    temp_c_high = weather_data["temperature_2m_max"][0]
    temp_c_low = weather_data["temperature_2m_min"][0]

    temp_f_high = c_to_f(temp_c_high)
    temp_f_low = c_to_f(temp_c_low)

    sunrise_data = weather_data['sunrise'][0]
    sunrise = datetime.fromisoformat(sunrise_data)
    sunset_data = weather_data['sunset'][0]
    sunset = datetime.fromisoformat(sunset_data)
    deg = '°'
    message = f"""<span>Today will be {condition}.
<strong>High:</strong> {round(temp_c_high)}{deg}C ({round(temp_f_high)}{deg}F)
<strong>Low:</strong> {round(temp_c_low)}{deg}C ({round(temp_f_low)}{deg}F)

☀️ {datetime.strftime(sunrise, '%-H:%M %p')}
🌙 {datetime.strftime(sunset, '%-I:%M %p')}
"""
    return message.strip()


def c_to_f(temp_c, decimals=1):
    temp_f = (temp_c * 9 / 5) + 32
    return round(temp_f, decimals)


if __name__ == '__main__':
    print(get_weather_message())
