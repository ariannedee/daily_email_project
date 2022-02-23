#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# -*- coding: utf-8 -*-

import sys

from send_email import send_html_email
from apis.joke import get_joke
from apis.quote import get_quote
from apis.sports import get_next_game
from apis.weather import get_weather_message

args = sys.argv
assert len(args) == 2, 'You must provide a "name" argument'

name = args[1].strip()

greeting = f"<h1>Good morning, {name.capitalize()} 👋</h1>"

content_list = [greeting]
try:
    weather = f"<h2>Today's weather ☁️</h2><p>{get_weather_message()}</p>"
    content_list.append(weather)
except Exception:
    pass
try:
    joke = f"<h2>Joke of the day 🤣</h2><p>{get_joke()}</p>"
    content_list.append(joke)
except Exception:
    pass
try:
    quote = f"<h2>Quote of the day 💬</h2><p>{get_quote()}</p>"
    content_list.append(quote)
except Exception:
    pass
try:
    next_game = f"<h2>Next game 🏀</h2><p>{get_next_game()}</p>"
    content_list.append(next_game)
except Exception:
    pass

content = ''.join(content_list)
content = content.replace('\n', '<br>')

send_html_email(f"{name.capitalize()}'s daily email", content)