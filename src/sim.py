#!/usr/bin/python

from game import Game
from team import Team

duke = Team("Duke", 43,15,36.3,47.7,37.6, False)
unc = Team("UNC", 46,5,43.5,47.1,36.6, False)
rivalry = Game(duke, unc)

rivalry.simulate()
