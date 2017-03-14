#!/usr/bin/python

from team import Team

t1 = Team("Duke",43,15,36.3,47.7,37.6)
t2 = Team("UNC",46,5,43.5,47.1,36.6)

i = 0
while i < 30:
	if i%2 == 0:
		t1.offense(t2)
	else:
		t2.offense(t1)
	i = i+1


#print stats
print "\n\n"
t1.printStats()
t2.printStats()





	
