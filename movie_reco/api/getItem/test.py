#!/usr/bin/env python 
# coding: utf-8

import sys
import json
import random
import glob
import collections
from collections import defaultdict
from math import sqrt

movies = ['GTO', 'Onmyoji', 'Led Zeppelin', 'Dragon Ball', 'Sex and the City', 'Chaplin', 'KILL BILL', 'THE MATRIX', 'Alice in Wonderland', 'Yu-Yu hakusho', 'Hamlet', 'Spider-Man2', 'Lupin the Third', 'GHOST SHIP']

imgs = ['img/gto.jpg', 'img/onmyoji.jpg', 'img/ledzeppelin.jpg', 'img/dragonball.jpg', 'img/sexandthecity.jpg', 'img/chaplin.jpg', 'img/killbill.jpg', 'img/matrix.jpg', 'img/aliceinwonderland.jpg', 'img/yuyuhakusho.jpg', 'img/hamlet.jpg', 'img/spiderman2.jpg', 'img/lupinthethird.jpg', 'img/ghostship.jpg']

ids = ['135', '210', '238', '263', '270', '370', '457', '468', '596', '724', '903', '1551', '1691', '2617'];


num = [0] * len(movies)           #リストの初期化
for n in range(len(movies)-1):
	a = random.randint(0, len(movies)-1)
	if n != 0:                  #最初でなければ
		while a in num:     #aがリストnumに存在していると
			a = random.randint(0, len(movies) - 1)
	num[n] = a	

args = ''
if len(sys.argv) > 0:
	for i in xrange(len(sys.argv) - 1):
		args += sys.argv[i + 1]

Movie1 = {}
Movie2 = {}
Movie2 = defaultdict(dict)        #同一keyでも処理できるように
Movie3 = {}                       #相関係数が最も高いユーザーの辞書
Colleration = {}                  #ユーザーがkey,相関係数がvalueの辞書
Colleration = defaultdict(dict)
col = []                          #相関係数を格納しておくためのリスト
recommend_movies = []             #最終的に推薦する映画のリスト

#利用者登録
splitword = '&'
if args.find("&amp;"):
	splitword = '&amp;'
Movie1 = args.replace("+"," ").split(splitword)
keys = 1
for line in Movie1:
	elements = line.split("=")
	if elements[0] == movies[0]:
		movie_ID = ids[0]
	elif elements[0] == movies[1]:
                movie_ID = ids[1]
	elif elements[0] == movies[2]:
                movie_ID = ids[2]
	elif elements[0] == movies[3]:
                movie_ID = ids[3]
	elif elements[0] == movies[4]:
                movie_ID = ids[4]
	elif elements[0] == movies[5]:
                movie_ID = ids[5]
	elif elements[0] == movies[6]:
                movie_ID = ids[6]
	elif elements[0] == movies[7]:
                movie_ID = ids[7]
	elif elements[0] == movies[8]:
                movie_ID = ids[8]
	elif elements[0] == movies[9]:
                movie_ID = ids[9]
	elif elements[0] == movies[10]:
                movie_ID = ids[10]
	elif elements[0] == movies[11]:
                movie_ID = ids[11]
	elif elements[0] == movies[12]:
                movie_ID = ids[12]
	elif elements[0] == movies[13]:
                movie_ID = ids[13]

	movie_rate = elements[1]
	Movie2[keys].update({int(movie_ID):int(movie_rate)})


#標本者（他のユーザ）登録
for file in glob.glob('*.txt'):  #ファイルの読み込み
    for line in open(file, 'r'):
	Elements = line.replace(":"," ").strip().split(",")
	if len(Elements) == 1:
		movie_ID = Elements
	else:
		customer_ID = Elements[0]
		movie_rate = Elements[1]
		key = int(customer_ID)
		Movie2[key].update({int(movie_ID[0]):int(movie_rate[0])})


#p1とp2の相関係数を求める関数
def sim_pearson(movie,p1,p2):
    
    items = {}
    for item in movie[p1]:
        if item in movie[p2]:
            items[item]=1
    n = len(items)         #共通アイテムの数

    if n == 0: return 0    #共通アイテムがなければ終了
 
    #計算
    ave1 = sum([movie[p1][it] for it in items])/float(n)
    var1 = sqrt(sum([pow(movie[p1][it]-ave1,2) for it in items]))
 
    ave2 = sum([movie[p2][it] for it in items])/float(n)
    var2 = sqrt(sum([pow(movie[p2][it]-ave1,2) for it in items]))

    cov = sum([(movie[p1][it]-ave1)*(movie[p2][it]-ave2) for it in items])

    if var1*var2 == 0: return 0      #分母が0の場合
    colleration = cov/(var1*var2)    #相関係数
    col.append(colleration)    
    Colleration.update({p2:colleration})


for k,v in Movie2.iteritems():
    if k != 1:
	sim_pearson(Movie2,1,k)

for k,v in Colleration.iteritems():
	if v == max(col):               #相関係数が一番高い人の場合
		Movie3 = Movie2[k]
        for k1,v1 in sorted(Movie3.items(),key=lambda x:x[1], reverse = True):
        	recommend_movies.append(str(k1))
		#if i == 0:
		#	Movie3 = Movie2[k]
		#	for k1,v1 in sorted(Movie3.items(),key=lambda x:x[1], reverse = True):
		#		recommend_movies.append(str(k1))
		#else :
		#	Movie3 = Movie2[k]
		#	if len(recommend_movies) < len(Movie3):
		#		del recommend_movies
		#		recommend_movies = []
		#		for k1,v1 in sorted(Movie3.items(),key=lambda x:x[1], reverse = True):
		#			recommend_movies.append(str(k1))
		#i += 1
	if recommend_movies != []:
		break

total = len(recommend_movies)       #レコメンドする映画数

movieItems =  {
		'selectItems' : [
				 {
				 'id' : ids[num[0]],
				 'title' : movies[num[0]],
				 'img' : imgs[num[0]],
				 'total' : total
				 },
				 {
				 'id' : ids[num[1]],
				 'title' : movies[num[1]],
				 'img' : imgs[num[1]]
				 }
	      		        ],
	        'recoItems' : []
	      }	

for id in recommend_movies:
	item = {}
	if str(id) == ids[0]:
		item = {'id' : int(ids[0]),'title' : movies[0],'img' : imgs[0]}
	elif str(id) == ids[1]:
                item = {'id' : int(ids[1]),'title' : movies[1],'img' : imgs[1]}
	elif str(id) == ids[2]:
		item = {'id' : int(ids[2]),'title' : movies[2],'img' : imgs[2]}
        elif str(id) == ids[3]:
		item = {'id' : int(ids[3]),'title' : movies[3],'img' : imgs[3]}
        elif str(id) == ids[4]:
		item = {'id' : int(ids[4]),'title' : movies[4],'img' : imgs[4]}
	elif str(id) == ids[5]:
                item = {'id' : int(ids[5]),'title' : movies[5],'img' : imgs[5]}
	elif str(id) == ids[6]:
		item = {'id' : int(ids[6]),'title' : movies[6],'img' : imgs[6]}
	elif str(id) == ids[7]:
                item = {'id' : int(ids[7]),'title' : movies[7],'img' : imgs[7]}
	elif str(id) == ids[8]:
		item = {'id' : int(ids[8]),'title' : movies[8],'img' : imgs[8]}
	elif str(id) == ids[9]:
		item = {'id' : int(ids[9]),'title' : movies[9],'img' : imgs[9]}
	elif str(id) == ids[10]:
		item = {'id' : int(ids[10]),'title' : movies[10],'img' : imgs[10]}
	elif str(id) == ids[11]:
		item = {'id' : int(ids[11]),'title' : movies[11],'img' : imgs[11]}
	elif str(id) == ids[12]:
		item = {'id' : int(ids[12]),'title' : movies[12],'img' : imgs[12]}
	elif str(id) == ids[13]:
		item = {'id' : int(ids[13]),'title' : movies[13],'img' : imgs[13]}
	

	movieItems['recoItems'].append(item)

print json.dumps(movieItems['selectItems'] + movieItems['recoItems'] , indent=8)
