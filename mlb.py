import mlbgame
import json
from datetime import date

TEAM = "Nationals"
PLAYER_ID = 656941

def check_homer() -> int:
    today = date.today()

    # break down game(s) played into at bats. list comprehensions are very helpful here
    games = [game for game in mlbgame.day(today.year, today.month, today.day, home=TEAM, away=TEAM)]

    if "PRE_GAME"in [game.game_status for game in games] or len(games) == 0:
        return -1

    # games = [game for game in mlbgame.day(today.year, today.month, today.day, home=TEAM, away=TEAM)]
    innings = [inning.bottom if game.home_team == TEAM else inning.top for game in games for inning in mlbgame.game_events(game.game_id) if game.home_team == TEAM]
    at_bats = [at_bat for inning in innings for at_bat in inning]

    for at_bat in at_bats:
        if at_bat.batter == PLAYER_ID and at_bat.event == 'Home Run':
            return 1
    return 0

if __name__ == "__main__":
    check_homer()