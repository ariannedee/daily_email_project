import requests

from pprint import pprint as pretty_print

from weather_codes import weather_from_code

DEBUG = False

base_url = 'https://api.open-meteo.com/v1/forecast'
headers = {
    'content-type': 'application/json'
}

class Weather:
    def __init__(self, lat, lon, tz="America/New_York"):
        self.lat = lat
        self.lon = lon
        self.tz = tz

        self.temp_high = None
        self.temp_low = None
        self.weather = None

    def get_params(self):
        return {
            'timezone': self.tz,
            'latitude': self.lat,
            'longitude': self.lon,
            'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
            'forecast_days': 1,
        }

    def gather_data(self):
        response = requests.get(base_url, params=self.get_params(), headers=headers)
        data = response.json()

        if DEBUG:
            print(response.url)
            pretty_print(data)

        today = data['daily']
        self.temp_high = today['temperature_2m_max'][0]
        self.temp_low = today['temperature_2m_min'][0]
        weathercode = today['weathercode'][0]
        self.weather = weather_from_code.get(weathercode, f"Code {weathercode} not found")

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.lat == other.lat and self.lon == other.lon

    def __str__(self):
        return f"Weather for ({self.lat}, {self.lon})"


if __name__ == "__main__":
    w = Weather(lat=42.9972, lon=-81.203)

    w.gather_data()
    print(w.tz)
    print(w.temp_high)
    print(w.temp_low)
    print(w.weather)