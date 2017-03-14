#!/usr/bin/python

class ScoreBoard:
    def __init__(self, home, away):
        self._homescore = 0
        self._awayscore = 0
        self._homename = home
        self._awayname = away
    
    def score(self, isHome, score):
        if isHome:
            self._homescore += score
        else:
            self._awayscore += score
    
    def getScore(self):
        return str(self._homescore)+":"+str(self._awayscore)

    def getWinner(self):
        if self._homescore == self._awayscore:
            return ""
        elif self._homescore > self._awayscore:
            return self._homename
        else:
            return self._awayname
