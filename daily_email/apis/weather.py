import requests

try:
    from .weather_codes import weather_from_code
except ImportError:
    from weather_codes import weather_from_code


WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

class APIError(Exception):
    pass


def get_weather_data(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
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
    weather = weather_from_code.get(weather_code, f"unknown ({weather_code})").lower()
    temp_max = data["daily"]["temperature_2m_max"][0]
    temp_min = data["daily"]["temperature_2m_min"][0]

    return weather, temp_max, temp_min  # TODO: classes


if __name__ == "__main__":
    weather, temp_high, temp_min = get_weather_data(0, 0)
    print(f"{weather=}\n{temp_high=}\n{temp_min=}")