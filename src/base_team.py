#!/usr/bin/python

import random

class BaseTeam:
    def __init__(self, name, play_by_play = False):
        self._name = name
        self._play_by_play = play_by_play

    def getName(self):
        return self._name

    def gameOffense(self, opponent):
        attempt_two = random.randint(0, 9) < 7
        if attempt_two:
            score = (random.randint(0, 99) < 48) * 2
            if self._play_by_play:
                print self._name, "attempt to shoots from inside arc"
                if score > 0:
                    print self._name, "scores 2 pts"
                else:
                    print self._name, "misses"
        else:
            score = (random.randint(0, 99) < 37) * 3
            if self._play_by_play:
                print self._name, "attempt to shoots from downtown"
                if score > 0:
                    print self._name, "scores 3 pts"
                else:
                    print self._name, "misses"
        clock = random.randint(5, 25)
        return score, clock 
