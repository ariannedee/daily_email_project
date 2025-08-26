import requests


try:
    from .weather_codes import weather_from_code
except ImportError:
    from weather_codes import weather_from_code

try:
    from .errors import APIError
except ImportError:
    from errors import APIError


WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

class WeatherData:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.temp_low = None
        self.temp_high = None
        self.weather = None

        self.get_weather_data()

    def get_weather_data(self):
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
            "timezone": "America/Los_Angeles",
            "forecast_days": 1,
        }
        headers = {
            'content-type': 'application/json'
        }
        response = requests.get(WEATHER_URL, params, headers=headers)

        if response.status_code != 200:
            raise APIError(f"Error getting weather data from {WEATHER_URL} with {params}\n{response.url}")

        data = response.json()
        weather_code = data["daily"]["weather_code"][0]
        self.weather = weather_from_code.get(weather_code, f"unknown ({weather_code})").lower()
        self.temp_high = data["daily"]["temperature_2m_max"][0]
        self.temp_low = data["daily"]["temperature_2m_min"][0]


if __name__ == "__main__":
    wd = WeatherData(49, 50)
    print(wd.weather)
    print(wd.temp_high)
    print(wd.temp_low)