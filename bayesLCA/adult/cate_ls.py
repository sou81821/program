#!/usr/bin/env python
#coding: UTF-8

### 潜在クラスカテゴリのcsvファイルを作成するプログラム ###

import os
import sys
import math
import csv

#f = open('adult_model.pwz',"r")
#f = open('adult_10_discretization_model.pzd',"r")
#f = open('adult_mdlp_model.pzd',"r")
f = open('group_EOCa.txt',"r")
lines = f.readlines()

new = open('item_gruop_EOCa.csv','ab')
csvWriter = csv.writer(new)

#総潜在クラス数
lc = 25

#データ数
a = 1

for line in lines:
	#実際の潜在クラス用のリスト		
	category = [0]*23
	#data = [0,0]

	item_prob = line.split(",")

	for i in range(0,lc):
	 	if i == 0:
	 		max = float(item_prob[i])
	 		max_number = i
	 	else:
	 		if max <= float(item_prob[i]):
	 			max = float(item_prob[i])
	 			max_number = i


	if max_number == 0:
		category[0] = 1
	elif max_number == 1:
		category[1] = 1
	elif max_number == 2:
		category[2] = 1
	elif max_number == 3:
		category[3] = 1
	elif max_number == 4:
		category[4] = 1
	elif max_number == 5:
		category[5] = 1
	elif max_number == 6:
		category[6] = 1
	elif max_number == 7:
		category[7] = 1
	elif max_number == 8:
		category[8] = 1
	elif max_number == 9:
		category[9] = 1
	elif max_number == 10:
		category[10] = 1
	elif max_number == 11:
		category[11] = 1
	elif max_number == 12:
		category[12] = 1
	elif max_number == 13:
		category[13] = 1
	elif max_number == 14:
		category[14] = 1
	elif max_number == 15:
		category[15] = 1
	elif max_number == 16:
		category[16] = 1
	elif max_number == 17:
		category[17] = 1
	elif max_number == 18:
		category[18] = 1
	elif max_number == 19 or max_number == 21 or max_number == 23:
		category[19] = 1
	elif max_number == 20:
		category[20] = 1
	elif max_number == 22:
		category[21] = 1
	elif max_number == 24:
		category[22] = 1

	#print max_number

	a += 1

	#print item_prob[2]
	#print max_number

	csvWriter.writerow(category)     #1行書き込み
	line = f.readline()

f.close()



