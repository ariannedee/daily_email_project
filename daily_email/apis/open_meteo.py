import requests
from environs import Env

from weather_codes import weather_from_code

BASE_URL = f'https://api.open-meteo.com/v1/forecast'

env = Env()
env.read_env()


class Weather:
    def __init__(self, celsius=True):
        if celsius:
            self.temp_units = 'C'
            api_temp_unit = 'celsius'
        else:
            self.temp_units = 'F'
            api_temp_unit = 'fahrenheit'

        params = {
            'timezone': 'America/New_York',
            'latitude': env('LATITUDE'),
            'longitude': env('LONGITUDE'),
            'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
            'forecast_days': 1,
            "temperature_unit": api_temp_unit,
        }
        headers = {
            'content-type': 'application/json'
        }
        response = requests.get(BASE_URL, headers=headers, params=params)

        self.data = response.json()
        self.condition = weather_from_code[self.data['daily']['weathercode'][0]]

    @property
    def temp_high(self):
        return self.data['daily']['temperature_2m_max'][0]

    @property
    def temp_low(self):
        return self.data['daily']['temperature_2m_min'][0]

    def __str__(self):
        return f"Todays's weather in {self.temp_units}"


if __name__ == '__main__':
    weather_today = Weather(celsius=False)
    temp_high = weather_today.temp_high
    temp_low = weather_today.temp_low
    print(temp_high)
    print(temp_low)
    print(weather_today)
