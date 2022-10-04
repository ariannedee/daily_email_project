from datetime import datetime, timezone
try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

import requests
from environs import Env

env = Env()
env.read_env()

coordinates = (env.float('LATITUDE'), env.float('LONGITUDE'))
tz = ZoneInfo(env.str("TIMEZONE", "America/Vancouver"))


def get_weather():
    lat, lon = coordinates
    params = {
        'units': 'metric',
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely,hourly,current',
        'appid': env('OPEN_WEATHER_APP_ID')
    }
    url = f'https://api.openweathermap.org/data/2.5/onecall'

    headers = {
        'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, params=params)

    data = response.json()
    weather = data['daily'][0]
    return weather


def get_weather_message():
    weather = get_weather()
    if isinstance(weather, str):
        return weather
    temp_hi_c = weather['temp']['max']
    temp_hi_f = c_to_f(temp_hi_c)
    temp_lo_c = weather['temp']['min']
    temp_lo_f = c_to_f(temp_lo_c)

    sunrise_utc = datetime.fromtimestamp(weather['sunrise'], tz=timezone.utc)
    sunrise = sunrise_utc.astimezone(tz)
    sunset_utc = datetime.fromtimestamp(weather['sunset'], tz=timezone.utc)
    sunset = sunset_utc.astimezone(tz)
    condition = weather['weather'][0]['description']
    deg = '°'
    message = f"""<span>Today there will be {condition}.
<strong>High:</strong> {round(temp_hi_c)}{deg}C ({round(temp_hi_f)}{deg}F)
<strong>Low:</strong> {round(temp_lo_c)}{deg}C ({round(temp_lo_f)}{deg}F)

☀️ {datetime.strftime(sunrise, '%-H:%M %p')}
🌙 {datetime.strftime(sunset, '%-I:%M %p')}
"""
    return message.strip()


def c_to_f(temp_c, decimals=1):
    temp_f = (temp_c * 9 / 5) + 32
    return round(temp_f, decimals)


if __name__ == '__main__':
    print(get_weather_message())
