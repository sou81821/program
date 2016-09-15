#!/usr/bin/env python
#coding: UTF-8

##### データセット「adult」を決定木(C4.5)により分類するプログラム #####

import csv
import pdb
import math

#csvファイルに出力
#new = open('adult_count','ab')
#csvWriter = csv.writer(new)

attribute = ["age","edu","mar","ocu","sex","cap","cou","income"]
attribute2 = ["age","edu","mar","ocu","sex","cap","cou"]

#データ数
total = 32561

### csvファイル「adult」を読み込み，各属性の要素数をカウントする関数
def readCount():
	number = [4,16,7,14,2,2,5,2]
	data = {}
	data2 = {}

	for index, k in enumerate(attribute):
		data[k] = [0] * number[index]

	for index, k in enumerate(attribute2):
		data2[k] = [0] * (number[index] * 2)

	#ファイルの読み込み
	f = open('money_net_2.csv','r')

	for line in f.readlines():
		Elements = line.strip().split(",")
		#print int(Elements[7][2:3])
		#print Elements

		for i in range(0,32561):
			if i == 0:
				age = int(Elements[0])
			else:
				age = int(Elements[i*7 + 0][2:3])
			#print len(Elements[0])
			education = int(Elements[i*7 + 1])
			marital = int(Elements[i*7 + 2])
			occupation = int(Elements[i*7 + 3])
			sex = int(Elements[i*7 + 4])
			capital = int(Elements[i*7 + 5])
			country = int(Elements[i*7 + 6])
			income = int(Elements[i*7 + 7][:1])
			#print Elements

			
			data["age"][age] += 1
			data["edu"][education] += 1
			data["mar"][marital] += 1
			data["ocu"][occupation] += 1
			data["sex"][sex] += 1
			data["cap"][capital] += 1
			data["cou"][country] += 1
			data["income"][income] += 1

			data2["age"][(age * 2) + income] += 1
			data2["edu"][(education * 2) + income] += 1
			data2["mar"][(marital * 2) + income] += 1
			data2["ocu"][(occupation * 2) + income] += 1
			data2["sex"][(sex * 2) + income] += 1
			data2["cap"][(capital * 2) + income] += 1
			data2["cou"][(country * 2) + income] += 1

	#pdb.set_trace()
	#sorted(data.items(), key=lambda x: x[0])
	return data, data2

	f.close()

def entropy(data,data2):
	#分類クラスのエントロピーを求める
	ent_c = 0
	c = data["income"]
	for i in range(0,len(c)):
		p_c = float(c[i]) / total
		ent_c += p_c * math.log(p_c,2)
	entropy_c = 0 - ent_c

	#各属性における条件付エントロピーを求める
	data3 = {}
	for k in attribute:
		if k != "income":
			ent_cf = 0
			f = data[k]
			for i in range(0,len(f)):
				#p(f)
				p_f = float(f[i]) / total
				#p(f,c)
				p_fc0 = float(data2[k][i*2]) / total
				p_fc1 = float(data2[k][i*2 + 1]) / total
				
				ent_cf += p_fc0 * math.log((p_fc0 / p_f) , 2)
				if p_fc1 != 0:
					ent_cf += p_fc1 * math.log((p_fc1 / p_f) , 2)

			entropy_cf = 0 - ent_cf
			data3[k] = entropy_cf

		#count = 0
		#for v2 in data2[k]:
			#p(f)
		#	p_f = float(f[0]) / total
			#p(f,c)
		#	p_fc = float(data2[k][0]) / total

	return entropy_c, data3

if __name__ == '__main__':
	data, data2 = readCount()
	entropy_c, data3 = entropy(data,data2)
	print entropy_c, data3
	#for k, v in data2.items():
	#	print k, v

