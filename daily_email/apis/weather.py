import requests

from weather_codes import weather_from_code

base_url = f'https://api.open-meteo.com/v1/forecast'
params = {
    'timezone': 'America/New_York',
    'latitude': 42.997262156214305,
    'longitude': -81.20390128320294,
    'daily': ['weathercode', 'temperature_2m_max', 'temperature_2m_min', 'sunrise', 'sunset'],
    'forecast_days': 1,
    "temperature_unit": "fahrenheit",
}
headers = {
    'content-type': 'application/json'
}
response = requests.get(base_url, headers=headers, params=params)
data = response.json()
weathercode = data['daily']['weathercode'][0]
weather = weather_from_code[weathercode]
temp_f_high = data['daily']['temperature_2m_max'][0]
temp_f_low = data['daily']['temperature_2m_min'][0]
sunrise_str = data['daily']['sunrise'][0]
sunset_str = data['daily']['sunset'][0]
sunrise = sunrise_str.split('T')[1]
sunset = sunset_str.split('T')[1]

print(__name__)

if __name__ == '__main__':
    print(data)
    print(temp_f_high)
    print(temp_f_low)