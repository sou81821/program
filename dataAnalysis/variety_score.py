#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
ある商品の推薦アウトプットにおける，推薦商品の種類数とジニ係数を求めるプログラム
'''

import sys
import pandas as pd
import numpy as np
import pdb
import csv
from collections import namedtuple, defaultdict



###  推薦クーポンの種類数・ジニ係数を求める  ###
def variety_score():
	#推薦クーポンファイル名
	file_name = sys.argv[1]
	recommend = pd.read_csv(filepath_or_buffer=file_name, delimiter=',', header=None)
	
	#推薦回数
	reco_length = len(recommend)*1.0
	
	#{ 推薦クーポン：推薦数 }の辞書
	reco_count = defaultdict(int)

	#{ ジャンル：推薦数 }の辞書
	#genre_count = defaultdict(int)
	
	for i in range(len(recommend)):
		reco_count[recommend.iloc[i][1]] += 1
		#genre_count[recommend.iloc[i][3]] += 1
	print "種類数：", len(reco_count)

	reco_count = sorted(reco_count.items(), key=lambda x:x[1])
	#genre_count = sorted(genre_count.items(), key=lambda x:x[1])

	#{ 推薦回数：その推薦回数のクーポン数 }
	reco_mean = defaultdict(int)
	for i in range(len(reco_count)):
		reco_mean[reco_count[i][1]] += 1

	coupon_t = len(reco_count)  #447
	reco_t = 0.0                #10432
	for k,v in reco_mean.items():
		reco_t += k

	ratio = 100/reco_t
	k_sum = 0.0
	k_sum_old = 0.0
	area = 0.0
	i = 0
	for k,v in reco_mean.items():
		k_sum += k
		if i==0:
			area = (v*100/coupon_t)*(k_sum*ratio)/2
		else:
			area += (v*100/coupon_t)*((k_sum_old*ratio)+(k_sum*ratio))/2
		k_sum_old = k_sum
		i += 1

	gini = 1.0 - (area/(100*100/2))
	print "ジニ係数（クーポンの）：", gini

	#ジャンルのジニ係数を求める


if __name__ == '__main__':
	variety_score()











