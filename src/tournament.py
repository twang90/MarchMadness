#!/usr/bin/python

from database import DataBase
from game import Game

class Tournament:
    def __init__(self):
        database = DataBase('../data/NCAA-17.csv')
        self._brackets = database.getBrackets()

    def simulate(self):
        east_winner = self.simulate_region('East')
        west_winner = self.simulate_region('West')
        midwest_winner = self.simulate_region('Midwest')
        south_winner = self.simulate_region('South')
        print "Final four teams are:"
        print east_winner.getTeamName()
        print west_winner.getTeamName()
        print midwest_winner.getTeamName()
        print south_winner.getTeamName()

    def simulate_region(self, region):
        assert region in self._brackets
        bracket = self._brackets[region]
        winner = self.simulate_bracket(bracket)
        print winner.getTeamName(), 'won', region, 'Region'
        return winner
        
    def simulate_bracket(self, bracket):
        winners = []
        for i in range(1, 17):
            if i in bracket:
                winners.append(bracket[i])
            else:
                winners.append(None)
        round = 0
        while len(winners) > 1:
            round += 1
            to_next_round = []
            teams = len(winners)
            print "Round %d" % (round)
            for i in range(teams/2):
                if winners[i] == None:
                    assert winners[teams-1-i] != None
                    print "Seed #%d %s wins" % (winners[teams-1-i].getSeed(), winners[teams-1-i].getTeamName())
                    to_next_round.append(winners[teams-1-i])
                elif winners[teams-1-i] == None:
                    print "Seed #%d %s wins" % (winners[i].getSeed(), winners[i].getTeamName())
                    to_next_round.append(winners[i])
                else:
                    print "Seed #%d vs Seed #%d: %s vs %s" \
                        % (winners[i].getSeed(),
                           winners[teams-1-i].getSeed(),
                           winners[i].getTeamName(), 
                           winners[teams-1-i].getTeamName()
                           )
                    game = Game(winners[i], winners[teams-1-i])
                    to_next_round.append(game.simulate())
            winners = to_next_round
        return winners[0]



            
                
