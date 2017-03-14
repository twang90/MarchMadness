#!/usr/bin/python

import random

class Game:
    def __init__(self, home, away):
        _scoreboard = ScoreBoard()
        _hometeam = Team(home)
        _awayteam = Team(away)
        _clock = Clock("NCAA")

    def _get_defence(self, one_team):
        team_pair = [self._hometeam, self._awayteam]
        another_team = team_pair[1-team_pair.index(one_team)]
        return another_team
        
    def simulate(self):
        team_pair = [self._hometeam, self._awayteam]
        init_poss = random.choice(team_pair)
        offence_team = init_poss
        defence_team = self._get_defence(offence_team)
        while not self._clock.isFinished():
            score, clock = offence_team.offense(defence_team)
            self.
            self._clock.consume(clock)

