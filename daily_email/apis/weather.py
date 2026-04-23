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


class Weather:
    def __init__(self, coords, day=0):
        lat, lon = coords
        self.params = {
            'timezone': 'America/Los_Angeles',
            'latitude': lat,
            'longitude': lon,
            'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
            'forecast_days': day + 1,
        }
        self.data = self.get_weather_data()
        today = self.data['daily']
        self.temp_c_high = today['temperature_2m_max'][day]
        self.temp_c_low = today['temperature_2m_min'][day]
        weather_code = today['weathercode'][day]
        self.condition = weather_codes.get(weather_code)

    def get_weather_data(self):
        base_url = 'https://api.open-meteo.com/v1/forecast'

        headers = {
            'content-type': 'application/json'
        }

        response = requests.get(base_url, params=self.params, headers=headers)
        data = response.json()

        if DEBUG:
            print(response.url)
            pprint(data)

        return data


if __name__ == '__main__':
    today_weather = Weather((0, -123.1193), day=1)

    content = f"""Today is going to be {today_weather.condition.lower()}.

    High: {today_weather.temp_c_high}°C
    Low: {today_weather.temp_c_low}°C"""

    print(content)