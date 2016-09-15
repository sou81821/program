#!/usr/bin/env python 
# coding: utf-8

import sys
import re
import glob
import linecache
from collections import defaultdict
import math
import random
import json


### movieIDリストを作成 ###
def make_movieIds():
	movie_ids = []
	txt_list = glob.glob('mv*')
	for i in range(len(txt_list)):
		words = re.split('[._]', txt_list[i])
		movie_ids.append(int(words[1]))
	return movie_ids



### movieTitleリストを作成 ###
def make_movieTitles(movie_ids):
	movie_titles = []
	for i in range(len(movie_ids)):
		line = linecache.getline('movie_titles.txt', movie_ids[i])
		movie = line.strip().split(",")
		movie_titles.append(movie[2])
	return movie_titles



### movieImgのpathリストを作成 ###
def make_movieImgs(movie_titles):
	movie_imgs = []
	for i in range(len(movie_titles)):
		path = "img/" + movie_titles[i] + ".png"
		movie_imgs.append(path)
	return movie_imgs



### 標本者（他のユーザー）の映画の評価値辞書を作成 ###
def make_users():
	users_rate = defaultdict(dict)
	for file in glob.glob('mv*.txt'):
		for line in open(file, 'r'):
			Elements = line.replace(":","").strip().split(",")
			if len(Elements) == 1:    #映画IDの場合
				movie_ID = Elements
			else:
				customer_ID = Elements[0]
				rate = Elements[1]
				date = Elements[2]
				key = int(customer_ID)
				users_rate[key].update({int(movie_ID[0]):int(rate)})
	return users_rate



### ユーザー同士の相関係数（ピアソン相関）を求める ###
def cor_pearson(movie,p1,p2):
	movies_common = []      #ユーザーp1,p2が共に見た映画のリスト
	for m in movie[p1]:
		if m in movie[p2]:
			movies_common.append(m)
	n_common = len(movies_common)   #共通映画数

	if n_common==0: return 0

	#ave: 評価の平均値, var: 標準偏差
	ave1 = sum([movie[p1][it] for it in movies_common]) / float(n_common)
	ave2 = sum([movie[p2][it] for it in movies_common]) / float(n_common)
	var1 = math.sqrt(sum([pow((movie[p1][it]-ave1),2) for it in movies_common]))
	var2 = math.sqrt(sum([pow((movie[p2][it]-ave2),2) for it in movies_common]))
	cov  = sum([(movie[p1][it]-ave1)*(movie[p2][it]-ave2) for it in movies_common])

	if var1*var2==0: return 0     #分母が0なら終了

	cor = cov/(var1*var2)    #相関係数
	return cor



### 選択映画・推薦映画をjson形式で出力 ###
def print_json(movie_ids, movie_titles, movie_imgs, recommend_movies):
	rand1 = random.randint(0,12)
	rand2 = random.randint(0,12)
	while rand1 == rand2:
		rand2 = random.randint(0,12)

	movieItems = {
		'selectItems' : [
				{
				'id' : movie_ids[rand1],
				'title' : movie_titles[rand1],
				'img' : movie_imgs[rand1],
				'total' : len(recommend_movies)
				},
				{
				'id' : movie_ids[rand2],
				'title' : movie_titles[rand2],
				'img' : movie_imgs[rand2]
				}
		],
		'recoItems' : []
	}

	for id in recommend_movies:
		for i, j in enumerate(movie_ids):
			if id == j:
				movie = {'id' : movie_ids[i],'title' : movie_titles[i],'img' : movie_imgs[i]}
				movieItems['recoItems'].append(movie)

	print json.dumps(movieItems['selectItems'] + movieItems['recoItems'], indent=8)






if __name__ == '__main__':
	movie_ids    = make_movieIds()                #映画IDリスト
	movie_titles = make_movieTitles(movie_ids)    #映画のタイトルリスト
	movie_imgs   = make_movieImgs(movie_titles)   #映画の画像のpathリスト
	users_rate   = make_users()                   #標本者（他のユーザー）の映画の評価値辞書を作成

	#利用者登録
	keys = 1     #利用者ID
	args = ''
	if len(sys.argv) > 0:
		for i in xrange(len(sys.argv)-1):
			args += sys.argv[i+1]
	Movie = {}
	splitword = '&'
	if args.find("&amp;"):
		splitword = '&amp;'
	Movie = args.replace("+"," ").split(splitword)
	for line in Movie:
		elements = line.split("=")
		print elements
		for i, j in enumerate(movie_titles):
			if elements[0] == j:
				movie_ID = movie_ids[i]
		rate = elements[1]
		users_rate[key].update({int(movie_ID):int(rate)})


	cor_dict = {}     #利用者と各標本者の相関係数dict
	for user in users_rate:
		cor = cor_pearson(users_rate, 1, user)
		if cor != 0:
			cor_dict.update({user:cor})
	max_user = max([(v,k) for k,v in cor_dict.items()])[1]     #相関係数が一番高いユーザー
	recommend_movies = [key for key in users_rate[max_user]]   #推薦する映画IDのリスト

	print_json(movie_ids, movie_titles, movie_imgs, recommend_movies)




















