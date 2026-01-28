import sys

from content.weather import temp_high, temp_low, weather
from helpers import c_to_f
from send_email import send_text_email

args = sys.argv[1:]

if args:
    name = " ".join(args)
else:
    name = input("Name: ")

content = f"""Good morning, {name.strip().title()}!

Today there will be {weather.lower()}.
High: {temp_high :.0f}°C ({c_to_f(temp_high):.0f}°F)
Low: {temp_low :.0f}°C ({c_to_f(temp_low):.0f}°F)

Daily mantra:
{'Seize the day!'}

Remember to:
"""
with open("reminders.txt", "rt") as file:
    for reminder in file.readlines():
        content += f"- {reminder}"

send_text_email(subject='An email', content=content)
