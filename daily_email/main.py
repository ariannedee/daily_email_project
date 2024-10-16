import sys

from apis.open_meteo import Weather
from helpers import f_to_c
from send_email import send_text_email

weather = Weather(celsius=False)
print(weather)
print(type(weather))

if len(sys.argv) == 1:
    name = 'arianne'
else:
    name = ' '.join(sys.argv[1:])

with open('reminders.txt') as file:
    reminders = file.readlines()

temp_high = weather.temp_high
temp_low = weather.temp_low

greeting = f"""Good morning, {name.title()}!
Today will be {weather.condition.lower()}.

High of {temp_high :.0f}°F ({f_to_c(temp_high):.0f}°C)
Low of {temp_low :.0f}°F ({f_to_c(temp_low):.0f}°C)

Remember to:
{''.join([f"- {reminder}" for reminder in reminders])}

Have a great day!
"""

send_text_email(subject='An email', content=greeting)
