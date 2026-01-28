import sys

from content import Weather
from helpers import c_to_f
from send_email import send_text_email

args = sys.argv[1:]

if args:
    name = " ".join(args)
else:
    name = input("Name: ")

w = Weather(lat=49.2827, lon=-123.1207, tz="America/Los_Angeles")
w.gather_data()

content = f"""Good morning, {name.strip().title()}!

Today there will be {w.weather.lower()}.
High: {w.temp_high :.0f}°C ({c_to_f(w.temp_high):.0f}°F)
Low: {w.temp_low :.0f}°C ({c_to_f(w.temp_low):.0f}°F)

Daily mantra:
{'Seize the day!'}

Remember to:
"""
with open("reminders.txt", "rt") as file:
    for reminder in file.readlines():
        content += f"- {reminder}"

send_text_email(subject='An email', content=content)
