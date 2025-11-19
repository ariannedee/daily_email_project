import sys
from datetime import datetime

from content.weather import temp_c_high, temp_c_low, weather, sunrise, sunset
from send_email import send_text_email


def c_to_f(temp: float):
    return (temp * 9 / 5) + 32


name_args = sys.argv[1:]

if name_args:
    name = " ".join(name_args).title()
else:
    name = input("Name: ").strip().title()

content = f"""Good morning, {name}.

Today is going to be {weather.lower()}.
High temp: {temp_c_high :.0f}°C ({c_to_f(temp_c_high):.0f}°F)
Low temp: {temp_c_low :.0f}°C ({c_to_f(temp_c_low):.0f}°F)

Sunrise: {sunrise}
Sunset: {sunset}

Remember to:
"""

with open('todos.txt') as file:
    for todo in file.readlines():
        content += f"- {todo.strip()}\n"

send_text_email(subject=f'Daily email for {datetime.today().strftime("%b %-d")}', content=content)
