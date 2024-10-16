import sys

import apis
from apis.weather import (
    sunrise,
    temp_f_high as tfh,
    temp_f_low as tfl,
    weather,
)
from send_email import send_text_email

print(__name__)

def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected} but got {actual}"


def c_to_f(temp):
    return (temp * 9 / 5) + 32


assert_equals(c_to_f(0), 32)
assert_equals(round(c_to_f(36.5)), 98)


def f_to_c(temp):
    return (temp - 32) * 5 / 9


assert_equals(f_to_c(32), 0)
assert_equals(round(f_to_c(98), 2), 36.67)


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
Sunset: {apis.sunset}

Remember to:
{''.join([f"- {reminder}" for reminder in reminders])}

Have a great day!
"""

send_text_email(subject='An email', content=greeting)
