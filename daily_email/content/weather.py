from datetime import datetime
from pprint import pprint

import requests

try:
    from .weather_codes import weather_from_code
except ImportError:
    from weather_codes import weather_from_code

DEBUG = False


class Forecast:
    def __init__(self, coordinates, units="metric"):
        self.lat, self.lon = coordinates
        self.units = units
        self.weather = "sunny"
        self.temp_high = None
        self.temp_low = None
        self.base_url = 'https://api.open-meteo.com/v1/forecast'

        self.load_weather_data()

    def load_weather_data(self):
        params = {
            'timezone': 'America/New_York',
            'latitude': self.lat,
            'longitude': self.lon,
            'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
            'forecast_days': 1,
        }
        if self.units == "imperial":
            params["temperature_unit"] = "fahrenheit"

        headers = {
            'content-type': 'application/json'
        }
        response = requests.get(self.base_url, params=params, headers=headers)
        data = response.json()

        if DEBUG:
            print(response.url)
            pprint(data)

        today = data['daily']
        self.temp_high = today['temperature_2m_max'][0]
        self.temp_low = today['temperature_2m_min'][0]
        weathercode = today['weathercode'][0]
        self.weather = weather_from_code.get(weathercode, f"unknown condition for code {weathercode}")

    def __str__(self):
        return f"Forecast object for ({self.lat}, {self.lon}) in {self.units}"


if __name__ == "__main__":
    forecast = Forecast((1.2, 3.4), units="imperial")
    print(forecast)

    print(f"""High temp: {forecast.temp_high}°F
Low temp: {forecast.temp_low}°F
Weather: {forecast.weather}
""")