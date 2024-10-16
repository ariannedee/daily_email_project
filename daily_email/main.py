import sys

from apis.weather import (
    sunrise,
    sunset,
    temp_c_low as tcl,
    temp_c_high as tch,
    weather,
)
from send_email import send_text_email


def c_to_f(temp):
    return (temp * 9 / 5) + 32


def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected} but got {actual}"


assert_equals(c_to_f(0), 32)
assert_equals(round(c_to_f(36.5)),98)

if len(sys.argv) == 1:
    name = 'arianne'
else:
    name = ' '.join(sys.argv[1:])

with open('reminders.txt') as file:
    reminders = file.readlines()

greeting = f"""Good morning, {name.title()}!
Today will be {weather.lower()}.

High of {tch:.0f}°C ({c_to_f(tch):.0f}°F)
Low of {tcl:.0f}°C ({c_to_f(tcl):.0f}°F)

Sunrise: {sunrise}
Sunset: {sunset}

Remember to:
{''.join([f"- {reminder}" for reminder in reminders])}

Have a great day!
"""

send_text_email(subject='An email', content=greeting)
