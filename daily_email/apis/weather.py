import requests

from .weather_codes import weather_from_code


WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

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
        # TODO: raise custom exception
        raise Exception(f"Error getting weather data from {WEATHER_URL} with {params}\n{response.url}")

    data = response.json()
    weather_code = data["daily"]["weather_code"][0]
    weather = weather_from_code.get(weather_code, f"unknown ({weather_code})").lower()
    temp_max = data["daily"]["temperature_2m_max"][0]
    temp_min = data["daily"]["temperature_2m_min"][0]

    return weather, temp_max, temp_min  # TODO: classes

# TODO: run file as a script to test it