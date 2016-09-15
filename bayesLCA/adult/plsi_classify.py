#!/usr/bin/env python
#coding: UTF-8

#PLSIによって作成されたデータに対して，
#各潜在クラスにおけるデータの割合を求めるプログラム

import os
import sys
import math

#f = open('adult_model.pzd',"r")
#f = open('adult_10_discretization_model.pzd',"r")
f = open('adult_mdlp_50_model.pzd',"r")
lines = f.readlines()

#属性数
attribute = 11

#総潜在クラス数
lc = 50

#各潜在クラスに属する人の数
classification = [0] * 50
#classification = [0,0,0,0,0]

#各潜在クラスの割合
ratio = [0] * 50
#ratio = [0,0,0,0,0]

#人の総数
total = 0

#fo = open('plsi_classify',"w")

for line in lines:
	x = line.split(" ")
	#print type(x[2])

	for i in range(0,lc):
		if i == 0:
			max = float(x[i])
			max_number = i
		else:
			if max <= float(x[i]):
				max = float(x[i])
				max_number = i

	classification[max_number] += 1
	#print max_number

#print classification

for i in range(0,lc):
	total += classification[i]

for i in range(0,lc):
	ratio[i] = (float(classification[i]) / float(total)) * 100

print ratio

f.close()
#fo.close()