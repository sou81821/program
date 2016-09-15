#!/usr/bin/env python
#-*- coding: utf-8 -*-

###########    特徴量をもとに，ある商品のクラスタリングを行う     #############

import math
import scipy
import numpy as np
import pandas as pd
import gensim
import gensim.parsing
from sklearn.cluster import KMeans
import pdb
import MeCab
from prettyprint import pp, pp_str
import plotly.plotly as py
from plotly.graph_objs import * 


tagger = MeCab.Tagger('mecabrc')


def tokenize(coupon):
	docs = []
	coupons = []
	for i in range(2000):
		text = coupon['XXXXX'][i] + coupon['XXXXX'][i]
		node = tagger.parseToNode(text)
		coupons.append([coupon['XXXXX'][i]])
		doc = ""

		while node:
			if node.feature.split(',')[0] == '名詞' and node.feature.split(',')[0] != ',':
				word = node.surface.decode('utf_8')
				if word != ',':     #指定語を除く
					doc = " ".join([doc, word])
			node = node.next

		#docs.append(doc[1:-1])
		docs.append(doc)

	return docs, coupons




def vec2dense(vec, num_terms):
	'''Convert from sparse gensim format to dense list of numbers'''
	return list(gensim.matutils.corpus2dense([vec], num_terms=num_terms).T[0])





if __name__ == '__main__':
	coupon = pd.read_csv('XXXXXXXXXX.tsv', delimiter='\t', usecols=["XXXXX", "XXXXX", "XXXXX", "XXXXX", "XXXXX"])
	
	#ジャンルをダミー変数に
	genre_dummy = pd.get_dummies(coupon["XXXXX"])
	genre_dummy *= 0.1

	#価格をビン化して，ダミー変数に
	bins = [0,1000,2000,3000,4000,5000,10000,15000,20000,40000,coupon["XXXXX"].max()]
	group_names = ["-1000", "1000-2000", "2000-3000", "3000-4000", "4000-5000", "5000-10000", "10000-15000", "15000-20000", "20000-40000", "40000-"]
	coupon["BIN_PRICE"] = pd.cut(coupon["XXXXX"], bins, labels=group_names)
	price_dummy = pd.get_dummies(coupon["XXXXX"])
	price_dummy *= 0.3


	### 価格帯のグラフを表示 ###
	# price = np.array(coupon["DISCOUNT_PRICE"])
	# low_price  = price[price<10000]
	# high_price = price[price>=10000]
	# high_price = high_price[high_price<40000]
	# high_price = high_price/10
	# low_price_count = np.bincount(low_price)
	# high_price_count = np.bincount(high_price)
	# #pdb.set_trace()
	# trace = Scatter(
	# 	x=np.arange(len(high_price_count)),
	# 	y=high_price_count
	# )
	# data = Data([trace])
	# unique_url = py.plot(data,filename="high_coupon_price")


	### couponのテキストを形態素解析する ###
	docs, coupons = tokenize(coupon)


	### ストップワードの除去 ###
	preprocessed_docs = {}
	for i in range(len(docs)):
		preprocessed = gensim.parsing.preprocess_string(docs[i])
		preprocessed_docs[i] = preprocessed
		#print i, ":", pp_str(preprocessed)

	
	### 辞書を作成し，低頻度と高頻度のワードを除く ###
	dct = gensim.corpora.Dictionary(preprocessed_docs.values())
	unfiltered = dct.token2id.keys()
	dct.filter_extremes(no_below=3, no_above=0.6)
	filtered = dct.token2id.keys()
	filtered_out = set(unfiltered) - set(filtered)


	### 辞書を保存 ###
	#dct.save_as_text("id2word.txt")


	### Bag of Words Vectorsの作成 ###
	bow_docs = {}
	bow_docs_all_zeros = {}

	for i in range(len(docs)):
		sparse = dct.doc2bow(preprocessed_docs[i])
		bow_docs[i] = sparse
		dense = vec2dense(sparse, num_terms=len(dct))
		#print i, ":", dense
		bow_docs_all_zeros[i] = all(d == 0 for d in dense)



	### 特徴ベクトルを次元削減（LDA, LSI） ###
	topic_docs = {}
	num_topics = 300     #特徴ベクトルの次元数（200〜500が一般的）
	
	# LSIによる次元削減
	topic_model = gensim.models.LsiModel(bow_docs.values(), id2word=dct, num_topics=num_topics)
	#topic_model = gensim.models.LsiModel(bow_docs.values(), id2word=dct.load_from_text("id2word.txt"), num_topics=num_topics)
	
	# LDAによる次元削減
	#topic_model = gensim.models.LdaModel(bow_docs.values(), id2word=dct, num_topics=num_topics)

	for i in range(len(docs)):
		vec = bow_docs[i]
		sparse = topic_model[vec]
		dense = vec2dense(sparse, num_topics)
		topic_docs[i] = sparse
		#print i, ":", dense
	#print pp_str(topic_model.print_topics())



	### 次元削減後のベクトルを正規化 ###
	unit_vecs = {}
	for i in range(len(docs)):
		vec = vec2dense(topic_docs[i], num_topics)
		norm = math.sqrt(sum(num**2 for num in vec))
		unit_vec = [num / norm for num in vec]
		unit_vecs[i] = unit_vec
		#print i, ":", unit_vec



	### テキストの特徴ベクトルに，価格とジャンルの情報も付け加える ###
	for i in range(len(docs)):
		unit_vecs[i].extend(np.array(genre_dummy.iloc[i]))
		unit_vecs[i].extend(np.array(price_dummy.iloc[i]))



	### k-meansでクラスタリング ###
	unit_vecs = np.nan_to_num(unit_vecs.values())
	Kmeans_model = KMeans(n_clusters=100, random_state=10).fit(unit_vecs)

	labels = Kmeans_model.labels_

	#各クラス数を数える
	class_count = np.bincount(labels)

	pdb.set_trace()










