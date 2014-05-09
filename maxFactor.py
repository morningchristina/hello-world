#!/usr/bin/env python

def getMaxFactor(num):
	count = num /2
	while count > 1:
		if num%count == 0:
			print 'the largest factor of %d is %d'%(num,count)
			break
			count = count -1
	else:
		print "%s"%(num),"is a prime"

for eachNum in range(10,21):
	getMaxFactor(eachNum)				
