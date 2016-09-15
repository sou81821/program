#!/usr/bin/env python
#coding: UTF-8

import sys

def colattu():
	count = 0
	for i in range(2,10002,2):
		ini = i
		i = i*3+1
		while (i != ini) and (i != 1):
			if i%2 == 0:
				i = i/2
			else:
				i = i*3+1
			if i==ini:
				count += 1
			#print i, ini

	print "個数は ", count


if __name__=="__main__":
	colattu()

