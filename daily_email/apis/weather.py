from pprint import pprint

import requests

try:
    from weather_codes import weather_from_code
except ImportError:
    from .weather_codes import weather_from_code

DEBUG = False

base_url = 'https://api.open-meteo.com/v1/forecast'

class Weather:
    def __init__(self, latitude, longitude, timezone='America/Los_Angeles'):
        self.lat = latitude
        self.lon = longitude
        self.tz = timezone

        self.temp_c_high = None
        self.temp_c_low = None
        self.condition = None
        
        self._call_api()

    def get_params(self):
        params = {
            'timezone': self.tz,
            'latitude': self.lat,
            'longitude': self.lon,
            'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
            'forecast_days': 1,
        }
        return params

    def _call_api(self):
        headers = {'content-type': 'application/json'}
        response = requests.get(
            base_url,
            params=self.get_params(),
            headers=headers
        )

        data = response.json()

        if DEBUG:
            pprint(data)

        today = data['daily']
        self.temp_c_high = today['temperature_2m_max'][0]
        self.temp_c_low = today['temperature_2m_min'][0]
        weathercode = today['weathercode'][0]
        self.condition = weather_from_code.get(weathercode, f"[unknown weather for code {weathercode}]")

    def __str__(self):
        return f"Weather object for ({self.lat}, {self.lon})"


if __name__ == "__main__":
    w = Weather(49.2497, -123.1193)
    print(w.condition)
    print(w)
    print(w.temp_c_high)
    print(w.temp_c_low)
