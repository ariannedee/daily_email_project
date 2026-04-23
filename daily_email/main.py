import sys

from environs import Env

from apis.ai_mantra import mantra
from apis.weather import Weather


env = Env()
env.read_env()

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:]).strip().title()
else:
    name = input("Name: ").strip().title()

def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

assert c_to_f(0) == 32, f"Expected {32} but got {c_to_f(0)}"
assert round(c_to_f(36.5)) == 98, f"Expected {98} but got {round(c_to_f(36.5))}"

with open("todos.txt") as file:
    todos = list(file.readlines())

today_weather = Weather((env('LATITUDE'), env('LONGITUDE')), 0)

content = f"""Good morning, {name}!
Today is going to be {today_weather.condition.lower()}.
High: {today_weather.temp_c_high}°C ({c_to_f(today_weather.temp_c_high):.0f}°F)
Low: {today_weather.temp_c_low}°C ({c_to_f(today_weather.temp_c_low):.0f}°F)

{mantra}

Remember to:"""

for todo in todos:
    content += "\n- " + todo.strip()

print(content)

# send_text_email(subject='An email', content='This is a test email')
