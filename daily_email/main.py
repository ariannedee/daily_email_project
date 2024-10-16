import sys

from apis.weather import (
    sunrise,
    sunset,
    temp_f_high as tfh,
    temp_f_low as tfl,
    weather,
)
from helpers import f_to_c
from send_email import send_text_email


if len(sys.argv) == 1:
    name = 'arianne'
else:
    name = ' '.join(sys.argv[1:])

with open('reminders.txt') as file:
    reminders = file.readlines()

greeting = f"""Good morning, {name.title()}!
Today will be {weather.lower()}.

High of {tfh:.0f}°F ({f_to_c(tfh):.0f}°C)
Low of {tfl:.0f}°F ({f_to_c(tfl):.0f}°C)

Sunrise: {sunrise}
Sunset: {sunset}

Remember to:
{''.join([f"- {reminder}" for reminder in reminders])}

Have a great day!
"""

send_text_email(subject='An email', content=greeting)
