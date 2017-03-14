#!/usr/bin/python

from game import Game
from team import Team

#duke = Team("Duke", 43,15,36.3,47.7,37.6, False)
#unc = Team("UNC", 46,5,43.5,47.1,36.6, False)
#rivalry = Game(duke, unc)
#rivalry.simulate()

from tournament import Tournament

#tourney = Tournament()
#tourney.simulate()

from database import DataBase
database = DataBase('../data/NCAA-17.csv')
duke = database.getTeam('Duke')
print duke.getTeamName()
unc = database.getTeam('North Carolina')
print unc.getTeamName()
assert duke != None and unc != None
rivalry = Game(duke, unc)
rivalry.simulate()
print "Duke stats"
duke.printStats()
print "UNC stats"
unc.printStats()

'''
import csv

f = open('../data/NCAA-17.csv', 'rb')
rows = csv.reader(f)
for row in rows:
    print row
'''
