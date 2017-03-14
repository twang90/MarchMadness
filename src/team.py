#!/usr/bin/python

import random
from stats import Stats

class Team:
	def __init__(self, seed, teamName, defRank, offRank, rebounds, fGPct, tPointPct, printComments=True):
		self._seed = seed
		self._teamName = teamName
		self._defRank = defRank
		self._offRank = offRank
		self._rebounds = rebounds	
		self._fGPct = fGPct
		self._tPointPct = tPointPct
		self._printComments = printComments
		self._stats = Stats()

	def getSeed(self):
		return self._seed

	def getDefRank(self):
		return self._defRank

	def getRebounds(self):
		return self._rebounds

	def getTeamName(self):
		return self._teamName

	def getStats(self):
		return self._stats

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
			#hit
			if random.randint(0,10000) <= hitPct*100:
				if twoPoints:
					self._stats.hitFG()
					if self._printComments:
						print "%s 2-point shoot and they did it!" %(self._teamName)
						print "offense time for this play is %d seconds" %(offenseTime) 
					return 2, totalOffenseTime
				else :
					self._stats.hitTP()
					if self._printComments:
						print "%s 3-point shoot and they did it!" %(self._teamName)
						print "offense time for this play is %d seconds" %(offenseTime) 
					return 3, totalOffenseTime
			#miss
			else:
				defRebPct = 0.8 + 0.01*(self._rebounds - opponent.getRebounds())
				getReb = random.randint(0, 10) > defRebPct*10
				if twoPoints:
					self._stats.missFG()
					if self._printComments:
						print "%s 2-point shoot, but they missed" %(self._teamName)
				else:
					self._stats.missTP()
					if self._printComments: 
						print "%s 3-point shoot, but they missed" %(self._teamName)
				if getReb:
					self._stats.incrOffReb()
					if self._printComments:
						print "Oh %s get the offense rebound" %(self._teamName)
				else: 
					opponent.getStats().increDefReb()
					if self._printComments:
						print "%s get the rebound" %(opponent.getTeamName())
						print "offense time for this play is %d seconds" %(offenseTime)
						print "defensive rebounds %d" %(opponent.getStats().getDefReb()) 
					return 0, totalOffenseTime


	def printStats(self):
	
		print "%s field goal number %d, hit %d, hit rate %2.2f %%" %(self._teamName, self._stats.getFG(), self._stats.getFGHit(), self._stats.getFGHitPct()*100)
		print "%s 3-point number %d, hit %d, hit rate %2.2f %%" %(self._teamName, self._stats.getTP(), self._stats.getTPHit(), self._stats.getTPHitPct()*100)
		print "%s offensive rebounds %d" %(self._teamName, self._stats.getOffReb())
		print "%s defensive rebounds %d" %(self._teamName, self._stats.getDefReb())


