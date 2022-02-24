import csv
import os
from datetime import datetime


def get_absolute_path(filename):
    this_directory = os.path.dirname(__file__)
    full_path = os.path.join(this_directory, filename)
    return full_path


def get_reminders_html():
    weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    weekday_int = datetime.today().weekday()
    weekday_str = weekdays[weekday_int]
    reminders = []
    with open(get_absolute_path('../data/reminders.csv')) as file:
        reader = csv.DictReader(file)
        for reminder in reader:
            if reminder[weekday_str] == '1':
                reminders.append('- ' + reminder["Item"])
    return '\n'.join(reminders)


if __name__ == '__main__':
    print(get_reminders_html())