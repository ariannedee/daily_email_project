#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime

from send_email import send_html_email
from content.fun_fact import get_fact
from content.weather import get_weather_message
from content.ai_content import get_quote
from reminders import get_reminders_html

args = sys.argv
assert len(args) == 2, 'You must provide a "name" argument'

name = args[1].strip()

greeting = f"<h1>Good morning, {name.capitalize()} 👋</h1>"

content_list = [greeting]
errors = {}
api_content = [
    {'name': 'weather', 'heading': "Today's weather ⛅️", 'function': get_weather_message},
    {'name': 'fact', 'heading': "Fun fact 🤓", 'function': get_fact},
    {'name': 'message', 'heading': "Daily quote 🌈", 'function': get_quote},
    {'name': 'reminders', 'heading': "Remember to ✅", 'function': get_reminders_html},
]

for content_dict in api_content:
    try:
        content = content_dict['function']()
        html_content = f"<h2>{content_dict['heading']}</h2><p>{content}</p>".replace('\n', '<br>')
        content_list.append(html_content)
    except Exception as e:
        errors[content_dict['name']] = e

content = ''.join(content_list)
error_msgs = ''
if errors:
    for section, message in errors.items():
        error_msgs += f'\nError getting {section}: {repr(message)}\n'
    print(error_msgs)
    content += error_msgs

today = datetime.today()
send_html_email(subject=f"Daily email for {today.strftime('%A, %B %-d')}", content=content)

print('Sent email:')
print(content)
