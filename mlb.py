import mlbgame
import json
from datetime import date

TEAM = "Nationals"
PLAYER_ID = 656941

def check_homer() -> int:
    today = date.today()

    # break down game(s) played into at bats. list comprehensions are very helpful here
    games = [game for game in mlbgame.day(today.year, today.month, today.day, home=TEAM, away=TEAM)]

    if len(games) == 0:
        return -1, None, None

    innings = [(inning.bottom, "bot") if game.home_team == TEAM else (inning.top, "top") for game in games for inning in mlbgame.game_events(game.game_id) if game.home_team == TEAM]
    at_bats = [(at_bat, inning[1]) for inning in innings for at_bat in inning[0]]

    for at_bat in at_bats:
        if at_bat[0].batter == PLAYER_ID and at_bat[0].event == 'Home Run':
            if at_bat[1] != "bot":
                return (1, games[0].home_team, at_bat[0].end_tfs_zulu)
            else:
                return (1, games[0].away_team, at_bat[0].end_tfs_zulu)
    if at_bats[0][0] != "bot":
        return (0, games[0].home_team, None)
    else:
        return(0, games[0].away_team, None)

if __name__ == "__main__":
    check_homer()