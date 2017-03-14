#!/usr/bin/python

import random
class Team:
	def __init__(self, teamName, defRank, offRank, rebounds, fGPct, tPointPct, printComments=True):
		self._teamName = teamName
		self._defRank = defRank
		self._offRank = offRank
		self._rebounds = rebounds	
		self._fGPct = fGPct
		self._tPointPct = tPointPct
		self._printComments = printComments

	def getDefRank(self):
		return self._defRank

	def getRebounds(self):
		return self._rebounds

	def getTeamName(self):
		return self._teamName

	def offense(self, opponent):
		totalOffenseTime = 0
		while 1:
			offenseTime = random.randint(5, 25)
			totalOffenseTime += offenseTime
			#suppose 3-point percentage is 30% for every team
			twoPoints = random.randint(1, 10) > 3
			#offense rank is smaller than opponent's defense rank, increase 0.5% hit percentage
			if twoPoints:
				hitPct = self._fGPct + (self._offRank - opponent.getDefRank())*0.005
			else:
				hitPct = self._tPointPct + (self._offRank - opponent.getDefRank())*0.005
			if random.randint(0,10000) <= hitPct*100:
				if twoPoints:
					if self._printComments:
						print "%s 2-point shoot and they did it!" %(self._teamName)
						print "offense time for this play is %d seconds" %(offenseTime) 
					return 2, totalOffenseTime
				else :
					if self._printComments:
						print "%s 3-point shoot and they did it!" %(self._teamName)
						print "offense time for this play is %d seconds" %(offenseTime) 
					return 3, totalOffenseTime
			else:
				defRebPct = 0.8 + 0.01*(self._rebounds - opponent.getRebounds())
				getReb = random.randint(0, 10) > defRebPct
				if twoPoints:
					if self._printComments:
						print "%s 2-point shoot, but they missed" %(self._teamName)
				else:
					if self._printComments: 
						print "%s 3-point shoot, but they missed" %(self._teamName)
				if getReb:
					if self._printComments:
						print "Oh %s get the offense rebound" %(self._teamName)
				else: 
					if self._printComments:
						print "%s get the rebound" %(opponent.getTeamName())
						print "offense time for this play is %d seconds" %(offenseTime) 
					return 0, totalOffenseTime




