#!/usr/bin/env python
#coding: UTF-8

#「adult.py」で加工したcsvファイルをPLSI用に変換するプログラム

import os
import sys
import math

#f = open('adult_test.csv',"r")
f = open('adult_discretization_test.csv',"r")
lines = f.readlines()

#fo = open('inputData',"w")
fo = open('inputData_discretization',"w")

for line in lines:
	#x = line.replace(",",":1 ")
	x = line.split(",")
	#print x[40]
	# x[0] age
	# x[1] workclass
	# x[2] education
	# x[3] marital-class
	# x[4] occupation
	# x[5] relationship
	# x[6] race
	# x[7] sex
	# x[8] native-country + age

	for i in range(0,32562):
		#print x[8]
		if i == 0:
			fo.write(x[(i*10) + 0] + ":1 ")
			fo.write(x[(i*10) + 1] + ":1 ")
			fo.write(x[(i*10) + 2] + ":1 ")
			fo.write(x[(i*10) + 3] + ":1 ")
			fo.write(x[(i*10) + 4] + ":1 ")
			fo.write(x[(i*10) + 5] + ":1 ")
			fo.write(x[(i*10) + 6] + ":1 ")
			fo.write(x[(i*10) + 7] + ":1 ")
			fo.write(x[(i*10) + 8] + ":1 ")
			fo.write(x[(i*10) + 9] + ":1 ")
			fo.write(x[(i*10) + 10][:2] + ":1\n")
			#fo.write(x[(i*11) + 11][:2] + ":1\n")
		else:
			fo.write(x[(i*10) + 0][3:4] + ":1 ")
			fo.write(x[(i*10) + 1] + ":1 ")
			fo.write(x[(i*10) + 2] + ":1 ")
			fo.write(x[(i*10) + 3] + ":1 ")
			fo.write(x[(i*10) + 4] + ":1 ")
			fo.write(x[(i*10) + 5] + ":1 ")
			fo.write(x[(i*10) + 6] + ":1 ")
			fo.write(x[(i*10) + 7] + ":1 ")
			fo.write(x[(i*10) + 8] + ":1 ")
			fo.write(x[(i*10) + 9] + ":1 ")
			fo.write(x[(i*10) + 10][:2] + ":1\n")
			#fo.write(x[(i*11) + 11][:2] + ":1\n")


	#line = f.readline()

f.close()
fo.close()