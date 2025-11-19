import sys
from datetime import datetime

from environs import Env

from content.weather import Forecast
from send_email import send_text_email

env = Env()
env.read_env()

def c_to_f(temp: float):
    return (temp * 9 / 5) + 32


name_args = sys.argv[1:]

if name_args:
    name = " ".join(name_args).title()
else:
    name = input("Name: ").strip().title()

coords = env('LATITUDE'), env('LONGITUDE')
weather = Forecast(coords, units="metric")

content = f"""Good morning, {name}.

Today is going to be {weather.weather.lower()}.
High temp: {weather.temp_high :.0f}°C ({c_to_f(weather.temp_high):.0f}°F)
Low temp: {weather.temp_low :.0f}°C ({c_to_f(weather.temp_low):.0f}°F)

Remember to:
"""

with open('todos.txt') as file:
    for todo in file.readlines():
        content += f"- {todo.strip()}\n"

send_text_email(subject=f'Daily email for {datetime.today().strftime("%b %-d")}', content=content)
