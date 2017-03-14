#!/usr/bin/python

import csv
from team import Team

class DataBase:
    _brackets = {}
    def __init__(self, filename):
        self._stream = open(filename, 'rb')
        self._brackets['East'] = {}
        self._brackets['West'] = {}
        self._brackets['Midwest'] = {}
        self._brackets['South'] = {}
        self._parse()

    def _parse(self):
        lines = [x for x in csv.reader(self._stream)]
        for line in lines[1:]:
            region = line[0]
            assert region in self._brackets
            seed = int(line[1])
            assert seed in range(16)
            team = Team(seed, line[2], int(line[5]), int(line[7]), float(line[8]), float(line[9]), float(line[10]), False)
            self._brackets[region][seed] = team

    def _printTeams(self, region):
        print region, 'Region:'
        for seed in self._brackets[region]:
            print '%d %s' % (seed, self._brackets[region][seed].getTeamName())

    def _printAllTeams(self):
        self._printTeams('East')
        self._printTeams('West')
        self._printTeams('Midwest')
        self._printTeams('South')

    def getBrackets(self):
        return self._brackets

    def getTeam(self, team_name):
        for region in ['East', 'West', 'Midwest', 'South']:
            for seed in self._brackets[region]:
                #print team_name, self._brackets[region][seed].getTeamName()
                if self._brackets[region][seed].getTeamName() == team_name:
                    return self._brackets[region][seed]
        return None
