#!/usr/bin/python

from base_team import BaseTeam as Team
class Tournament:
    def __init__(self, teams):
        self._teams = []
        for name in teams:
            self._teams.append(Team(name))
    
