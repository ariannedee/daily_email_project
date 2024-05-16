import sys
from pprint import pprint

from apis.weather import get_message


def main():
    args = sys.argv
    if len(args) > 1:
        name = ' '.join(args[1:]).title()
    else:
        name = input('Name: ')

    greeting = f"""Good morning, {name.strip().title()}

{get_message()}

Remember to:
"""

    with open('reminders.txt') as file:
        for reminder in file.readlines():
            greeting += f"- {reminder}"

    print(greeting)
    # send_text_email(subject='Daily email', content=greeting)


if __name__ == '__main__':
    main()
