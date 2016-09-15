#!/usr/bin/env python
#coding: UTF-8

#####  10進数, 2進数, 8進数のいずれで表現しても回文数となる数のうち、  #####
#####  10進数の10以上で最小の値を求める                            #####

i = 11

while True:
	tmp1 = str(i)
	if tmp1 == tmp1[::-1]:
		tmp2 = bin(i)
		if tmp2[2:] == tmp2[2:][::-1]:
			tmp3 = oct(i)
			if tmp3[1:] == tmp3[1:][::-1]:
				print i
				break
	i += 1


