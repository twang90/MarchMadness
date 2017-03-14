#!/usr/bin/python

class Stats:

	def __init__(self, FG=0, FGHit=0, TP=0, TPHit=0, offReb=0, defReb=0):
		self._FG = FG
		self._FGHit = FGHit
		self._TP = TP
		self._TPHit = TPHit
		self._offReb = offReb
		self._defReb = defReb

	def hitFG(self):
		self._FG = self._FG+1
		self._FGHit = self._FGHit+1

	def missFG(self):
		self._FG = self._FG+1

	def getFG(self):
		return self._FG
	
	def getFGHit(self):
		return self._FGHit

	def getFGHitPct(self):
		if self._FG == 0:
			return 0
		else:
			return self._FGHit*1.0/self._FG

	def hitTP(self):
		self._TP = self._TP+2
		self._TPHit = self._TPHit+1

	def missTP(self):
		self._TP = self._TP+1

	def getTP(self):
		return self._TP

	def getTPHit(self):
		return self._TPHit

	def getTPHitPct(self):
		if self._TP == 0:
			return 0
		else:	
			return self._TPHit*1.0/self._TP

	def incrOffReb(self):
		self._offReb = self._offReb+1

	def getOffReb(self):
		return self._offReb

	def increDefReb(self):
		self._defReb = self._defReb+1

	def getDefReb(self):
		return self._defReb
