import sys

from helpers import c_to_f
from send_email import send_text_email
from weather import Weather

args = sys.argv

if len(args) > 1:
    name = ' '.join(args[1:]).title()
else:
    name = input("Name: ").strip().title()

my_weather = Weather(lat=49.2497, lon=-123.1193, tz='America/Los_Angeles')
content = f"""Good morning, {name}!

Today's condition: {my_weather.condition.lower()}.

High: {my_weather.high_temp}°C ({c_to_f(my_weather.high_temp)}°F)
Low: {my_weather.low_temp}°C ({c_to_f(my_weather.low_temp)}°F)

Remember to:
"""

with open('reminders.txt') as file:
    for line in file.readlines():
        content += '- ' + line

send_text_email(subject=f'Hello {name.title()}', content=content)
