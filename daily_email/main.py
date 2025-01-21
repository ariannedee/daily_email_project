import sys

from helpers import c_to_f
from weather_api import high_temp_c, low_temp_c, weather
from send_email import send_text_email


def main():
    args = sys.argv[1:]
    if len(args) > 0:
        name = ' '.join(args).strip().title()
    else:
        name = input("Name: ").strip().title()

    message = f"""Good morning {name}!
    
    Today will be {weather}.
    
    High: {high_temp_c:.1f}°C ({c_to_f(high_temp_c):.1f}°F)
    Low: {low_temp_c:.1f}°C ({c_to_f(low_temp_c):.1f}°F)
    
    Remember to:
    """
    with open('reminders.txt') as file:
        for reminder in file.readlines():
            message += f"- {reminder}"

    send_text_email(subject='Daily email', content=message)


if __name__ == '__main__':
    main()
