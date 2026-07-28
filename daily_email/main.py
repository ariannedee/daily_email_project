import sys

from apis.mantra import daily_mantra
from apis.weather import temp_c_high, temp_c_low, weather
from send_email import send_text_email


def c_to_f(temp_c: int | float) -> float:
    return (temp_c * 9 / 5) + 32

args = sys.argv[1:]
if args:
    name = " ".join(args)
else:
    name = input("Name: ").strip()

content = f"""Good morning, {name.title()}!

{daily_mantra}

Today is going to be {weather.lower()}.
High: {temp_c_high :.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low: {temp_c_low :.0f}°C ({c_to_f(temp_c_low):.0f}°F)

Remember to:
"""
with open("reminders.txt") as file:
    for reminder in file.readlines():
        content += "- " + reminder

send_text_email(subject='An email', content=content)
