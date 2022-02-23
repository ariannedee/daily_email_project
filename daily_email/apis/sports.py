import datetime

import requests

url = 'https://www.balldontlie.io/api/v1/games/'
team_id = 28  # Toronto Raptors


def get_next_game():
    params = {
        'team_ids[]': team_id,
        'start_date': (datetime.date.today()).strftime('%Y-%m-%d')
    }

    headers = {
        'content-type': 'application/json'
    }

    response = requests.get(url, headers=headers, params=params)

    games = response.json()['data']
    games.sort(key=lambda g: g['date'])

    next_game = games[0]

    home_team = next_game['home_team']['full_name']
    away_team = next_game['visitor_team']['full_name']
    status = next_game['status']

    date_str = next_game['date'].split('T')[0]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    next_game_day_diff = (date - datetime.date.today()).days
    if next_game_day_diff == 0:
        date_string = 'Today'
    elif next_game_day_diff == 1:
        date_string = 'Tomorrow'
    else:
        date_string = f'In {next_game_day_diff} days'

    message = f"""{date_string} @ {status}
<strong>Home:</strong> {home_team}
<strong>Away:</strong> {away_team}"""

    return message


if __name__ == '__main__':
    print(get_next_game())
