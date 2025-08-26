import sys

from environs import Env

from apis import APIError
from apis.weather import WeatherData
from send_email import send_text_email

env = Env()
env.read_env()


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32

def main(name):
    # Content greeting
    content = f"Good morning, {name}!\n"

    errors = []

    lat = env.float('LATITUDE', default=49)
    lon = env.float('LONGITUDE', default=-123)

    try:
        data = WeatherData(lat, lon)
    except APIError as e:
        errors.append(str(e))
    else:
        temp_c_high = data.temp_high
        temp_c_low = data.temp_low
        content += f"""\nToday is going to be {data.weather}.
    
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

if __name__ == '__main__':
    receiver_name = " ".join(sys.argv[1:])

    if not receiver_name:
        receiver_name = input("Name: ")

    receiver_name = receiver_name.strip().title()
    main(receiver_name)