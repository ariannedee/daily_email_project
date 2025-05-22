from pprint import pprint

import requests

from weather_codes import weather_from_code


class Weather:
    base_url = f'https://api.open-meteo.com/v1/forecast'
    daily = ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset']
    headers = {
        'content-type': 'application/json'
    }

    def __init__(self, lat, lon, tz):
        self.params = {
            'latitude': lat,
            'longitude': lon,
            'timezone': tz,
            'daily': self.daily,
            'forecast_days': 1,
        }
        response = requests.get(self.base_url, self.params, headers=self.headers)

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            self.error = e
            self.data = response.text
        else:
            data = response.json()
            self.data = data['daily']
            self.error = None

    @property
    def condition(self):
        code = self.data['weathercode'][0]
        return weather_from_code[code]

    @property
    def high_temp(self):
        return self.data['temperature_2m_max'][0]

    @property
    def low_temp(self):
        return self.data['temperature_2m_min'][0]


if __name__ == '__main__':
    vancouver_weather = Weather(lat=49.2497, lon=-123.1193, tz='America/Los_Angeles')
    pprint(vancouver_weather.params)
    pprint(vancouver_weather.data)
    print(vancouver_weather.condition)
    print(vancouver_weather.high_temp)
    print(vancouver_weather.low_temp)

    bad_request = Weather(lat=49.2497, lon=-123.1193, tz='invalid')
    print(bad_request.error)
    print(bad_request.data)
