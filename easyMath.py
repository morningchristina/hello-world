#!/usr/bin/env python

from operator import add,sub
from random import randint,choice

ops = {'+':add,'-':sub}
MAXTRIES = 2

def doprob():
	op = choice('+-')
	nums = [randint(1,10) for i in range(2)]
	nums.sort(reverse=True)
	ans = ops[op](*nums)
	pr = '%d %s %d = ' % (nums[0],op,nums[1])
	oops = 0
	while True:
		try:
			if int(raw_input(pr)) == ans:
				print 'correct'
			break
		if
