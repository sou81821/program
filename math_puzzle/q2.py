#!/usr/bin/env python
#coding: UTF-8

import re

sisoku = ["+","-","*","/",""]

for i in range(1000,10000):

	st = str(i)
	pattern = re.compile(r'0[0-9]+')
	print pattern

	for j in range(len(sisoku)):
		for k in range(len(sisoku)):
			for l in range(len(sisoku)):
				tmp = st[0] + sisoku[j] + st[1] + sisoku[k] + st[2] + sisoku[l] + st[3]
				if ("/0" in tmp) or (len(tmp) == 4) or (pattern.match(tmp)):
					break
				if i == eval(tmp):
					print i




