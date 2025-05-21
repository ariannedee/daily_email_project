import sys

from helpers import c_to_f
from send_email import send_text_email
from weather import (
    condition,
    temp_hi as high_temp,
    temp_lo as low_temp,
)

args = sys.argv

if len(args) > 1:
    name = ' '.join(args[1:]).title()
else:
    name = input("Name: ").strip().title()

content = f"""Good morning, {name}!

Today's condition: {condition.lower()}.

High: {high_temp}°C ({c_to_f(high_temp)}°F)
Low: {low_temp}°C ({c_to_f(low_temp)}°F)

Remember to:
"""

with open('reminders.txt') as file:
    for line in file.readlines():
        content += '- ' + line

send_text_email(subject=f'Hello {name.title()}', content=content)
