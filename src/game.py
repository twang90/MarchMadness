#!/usr/bin/python

import random
from base_team import BaseTeam as Team
from scoreboard import ScoreBoard
from clock import Clock 

class Game:
    def __init__(self, home, away, play_by_play = False):
        self._scoreboard = ScoreBoard(home, away)
        self._hometeam = Team(home)
        self._awayteam = Team(away)
        self._initposs = random.choice([self._hometeam, self._awayteam])
        self._play_by_play = play_by_play

    def _getAnother(self, one_team):
        team_pair = [self._hometeam, self._awayteam]
        another_team = team_pair[1-team_pair.index(one_team)]
        return another_team
        
    def _period(self, initPoss, regular = True):
        #Start a new period
        if regular:
            _clock = Clock("NCAA Regular")
        else:
            _clock = Clock("NCAA Overtime")
        _clock.start()
        team_pair = [self._hometeam, self._awayteam]
        offense_team = initPoss
        defense_team = self._getAnother(offense_team)
        if self._play_by_play:
            print offense_team.getName(), "starts with the ball"
            print defense_team.getName(), "plays defense"
        while not _clock.isFinished():
            score, clock = offense_team.gameOffense(defense_team)
            self._scoreboard.score(offense_team == self._hometeam, score)
            _clock.consume(clock)
            if self._play_by_play:
                if score == 2:
                    print _clock.getClock(), offense_team.getName(), "scores 2 pts"
                elif score == 3:
                    print _clock.getClock(), offense_team.getName(), "scores 3 pts"
                else:
                    print _clock.getClock(), offense_team.getName(), "misses"
            offense_team = defense_team
            defense_team = self._getAnother(offense_team)
            if self._play_by_play:
                print offense_team.getName(), "gets the the ball"
                print defense_team.getName(), "plays defense"
        print "Score:", self._scoreboard.getScore()

    def simulate(self):
        #Start a new game
        #First half
        print "First half begins"
        self._period(self._initposs)
        #Second half
        print "Second half begins"
        self._period(self._getAnother(self._initposs))
        print "Regular time ends"
        #If it's a tie, we need overtime
        num_ot = 0
        while self._scoreboard.getWinner() == "":
            poss = random.choice([self._hometeam, self._awayteam])
            self._period(poss, regular = False)
            num_ot += 1
            print "OT #%d begins" % (num_ot)
        print "Game ends"
        print "The winner is", self._scoreboard.getWinner()

