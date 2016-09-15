#!/usr/bin/env python
#coding: UTF-8

##### データセット「adult」をC5.0用に変換するプログラム #####

import csv
import pdb
#ファイルの読み込み
f=open('adult.csv','r')

#デバック
#pdb.set_trace()

#csvファイルに出力
new = open('c50.csv','ab')

csvWriter = csv.writer(new,lineterminator='\n')

for line in f.readlines():
	Elements = line.strip().split(",")

	#年齢上１ケタ
	age = int(Elements[0][-2:])

	#capital-gain
	capital_gain = int(Elements[10][1:])

	#capital-loss
	capital_loss = int(Elements[11][1:])

	if(age < 22):
		Elements[0] = 0
	elif(22 <= age and age < 28):
		Elements[0] = 1
	elif(28 <= age and age < 65):
		Elements[0] = 2
	else:
		Elements[0] = 3

	Elements[9] = Elements[9][1:]

	if(capital_gain == 0):
		Elements[10] = 68
	else:
		Elements[10] = 69

	#所得の加工(70〜71), NAなし
	if(Elements[14] == " <=50K"):
		Elements[14] = 70
	elif(Elements[14] == " >50K"):
		Elements[14] = 71

	csvWriter.writerow(Elements)     #1行書き込み
	#csvWriter.writerow(money)
	line = f.readline()

f.close()