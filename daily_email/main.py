import sys

from environs import Env

from daily_email.apis.weather import get_weather_data
from send_email import send_text_email

env = Env()
env.read_env()


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


name = " ".join(sys.argv[1:])

if not name:
    name = input("Name: ")

name = name.strip().title()

# Content greeting
content = f"Good morning, {name}!\n"

errors = []

weather, temp_c_high, temp_c_low = get_weather_data(env.float('LATITUDE', default=49), env.float('LONGITUDE', default=-123))

# Content weather
# TODO: handle exceptions
content += f"""\nToday is going to be {weather}.

High: {temp_c_high :.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low :.0f}°C ({c_to_f(temp_c_low):.0f}°F)
\n"""

# Content todos
content += "Remember to:"

with open("reminders.txt") as file:
    for reminder in file.readlines():
        content += "\n- " + reminder.strip().capitalize()

# Content errors
if errors:
    content += "\n\nERRORS -"
    for error in errors:
        content += f"\n[Error]: {error}"

send_text_email(subject='An email', content=content)
