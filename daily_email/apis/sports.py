try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo

from datetime import datetime, timezone

import requests
from environs import Env

env = Env()
env.read_env()


tz = ZoneInfo(env.str("TIMEZONE", "America/Vancouver"))
my_team = env.str("TEAM", "TOR")

now = datetime.now(tz=tz)
today = now.date()
season = today.year
if today.month >= 7:
    season = today.year
else:
    season = today.year - 1

url = f"https://data.nba.net/prod/v2/{season}/schedule.json"


def get_game_messages():
    headers = {
        'content-type': 'application/json'
    }
    response = requests.get(url, headers=headers)

    all_games = response.json()["league"]["standard"]

    if len(all_games) == 0:
        return "No upcoming games"

    last_game = None
    next_game = None

    def game_deets(game_dict, game_date, game_teams):
        is_home = True if my_team == game_teams[1] else False
        return {
            "date": game_date,
            "game": game_dict,
            "homeTeam": game_teams[1],
            "awayTeam": game_teams[0],
            "isHome": is_home,
        }

    for game in all_games:
        game_id = game["gameUrlCode"]  # 20220930/TORLAC
        if my_team not in game_id:
            continue
        date_code, team_code = game_id.split("/")
        teams = (team_code[:3], team_code[3:])
        y = int(date_code[:4])
        m = int(date_code[4:6])
        d = int(date_code[6:8])
        date = datetime(y, m, d, tzinfo=tz).date()
        if date >= today:
            next_game = game_deets(game, date, teams)
            break
        if last_game is None or last_game["date"] < date:
            last_game = game_deets(game, date, teams)

    if not next_game:
        return "No upcoming games"

    time_utc = datetime.fromisoformat(next_game["game"]["startTimeUTC"].strip("Z")).replace(tzinfo=timezone.utc)
    time_str = time_utc.astimezone(tz).strftime("%-I:%M %p")

    next_game_day_diff = (next_game["date"] - today).days
    if next_game_day_diff == 0:
        date_string = 'today'
    elif next_game_day_diff == 1:
        date_string = 'tomorrow'
    else:
        date_string = f'in {next_game_day_diff} days'

    message = f"""<strong>Next game</strong> - {date_string} @ {time_str}
{next_game["awayTeam"]} at {next_game["homeTeam"]}
"""
    team_stat = last_game["game"]["hTeam"] if last_game["isHome"] else last_game["game"]["vTeam"]
    other_team = last_game["awayTeam"] if last_game["isHome"] else last_game["homeTeam"]
    other_team_stat = last_game["game"]["vTeam"] if last_game["isHome"] else last_game["game"]["hTeam"]
    last_game = f"""
<strong>Last game</strong> - {last_game["date"].strftime("%A, %B %-d")}
{my_team} {team_stat["score"]} - {other_team} {other_team_stat["score"]}
{team_stat["win"]} - {team_stat["loss"]}
"""
    return message + last_game


if __name__ == '__main__':
    print(get_game_messages())
