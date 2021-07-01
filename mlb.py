import mlbgame
import json
from datetime import datetime, timezone, timedelta

TEAM = "Nationals"
PLAYER_ID = 656941

def check_homer() -> tuple:
    today = datetime.now(timezone(-timedelta(hours=4)))

    # break down game(s) played into at bats. list comprehensions are very helpful here
    games = [game for game in mlbgame.day(today.year, today.month, today.day, home=TEAM, away=TEAM)]
    if len(games) > 0:
        if games[0].home_team == TEAM:
            opposing_team = games[0].away_team
        else:
            opposing_team = games[0].home_team

        if games[0].game_status == "FINAL":
            final = True
        else:
            final = False

    if len(games) == 0:
        return -1, None, None

    innings = [inning.bottom if game.home_team == TEAM else inning.top for game in games for inning in mlbgame.game_events(game.game_id) if game.home_team == TEAM]
    at_bats = [at_bat for inning in innings for at_bat in inning]

    for at_bat in at_bats:
        try:
            if at_bat.batter == PLAYER_ID and at_bat.event == 'Home Run':
                return (1, opposing_team, at_bat.end_tfs_zulu)
        except AttributeError:
            pass
    if final:
        return (2, opposing_team, None)
    return (0, opposing_team, None)

if __name__ == "__main__":
    check_homer()