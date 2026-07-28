import sys

from apis import daily_mantra, Weather
from send_email import send_text_email


def c_to_f(temp_c: int | float) -> float:
    return (temp_c * 9 / 5) + 32

args = sys.argv[1:]
if args:
    name = " ".join(args)
else:
    name = input("Name: ").strip()

weather = Weather(49.2497, -123.1193)

content = f"""Good morning, {name.title()}!

{daily_mantra}

Today is going to be {weather.condition.lower()}.
High: {weather.temp_c_high :.0f}°C ({c_to_f(weather.temp_c_high):.0f}°F)
Low: {weather.temp_c_low :.0f}°C ({c_to_f(weather.temp_c_low):.0f}°F)

Remember to:
"""
with open("reminders.txt") as file:
    for reminder in file.readlines():
        content += "- " + reminder

send_text_email(subject='An email', content=content)
