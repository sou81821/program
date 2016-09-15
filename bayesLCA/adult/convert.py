#!/usr/bin/env python
#coding: UTF-8

##### csvファイルの改行コードをMacに対応させる #####

import csv
import pdb
#ファイルの読み込み
f=open('group_EOCa.csv','r')
#f=open('c50.txt','r')

#デバック
#pdb.set_trace()

#csvファイルに出力
#new = open('income2.txt','ab')
#csvWriter = csv.writer(new,lineterminator='\n')
#new = open('adult_discretization.csv','ab')
#new = open('money.csv','ab')

for line in f.readlines():
	line = line.replace("\r","\n")
	#Elements = line.split(",")

	#Elements = line.split(",")
	#print Elements[12][1:]
	#Elements[1] =  Elements[1][1:]
	#print Elements[2]
	#print 1
	#print line
	
	#csvWriter.writerow(Elements)     #1行書き込み
	#print 1
	print line

f.close()
