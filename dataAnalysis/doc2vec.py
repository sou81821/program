#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Doc2Vecにより，テキストをベクトル化し，クラスタリングを行う
'''

import pandas as pd
import numpy as np
import gensim.models
import MeCab
import pdb
import csv
import scipy
from scipy.cluster.vq import vq, kmeans, whiten
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from prettyprint import pp, pp_str
from collections import namedtuple, defaultdict, Counter
from sklearn.feature_extraction.text import TfidfVectorizer


tagger = MeCab.Tagger('mecabrc')


#クーポンを形態素解析で単語の辞書に
def tokenize():
	coupon = pd.read_csv('XXXXXXX.tsv', delimiter='\t')
	coupon = coupon[['XXXXX', 'XXXXX']]
	docs = []
	coupons = []
	for i in range(len(coupon)):
		text = coupon['XXXXX'][i]
		node = tagger.parseToNode(text)
		coupons.append([coupon['XXXXX'][i]])
		doc = []

		while node:
			if node.feature.split(',')[0] == '名詞' and node.feature.split(',')[0] != ',':
				word = node.surface.decode('utf_8')
				if word != ',':     #指定語を除く
					doc.append(word)
				#pdb.set_trace()
			node = node.next

		docs.append(doc[1:-1])

	return docs, coupons



class LabeledLineSentence(object):

	def __init__(self, docs):
		self.docs = docs

	def __iter__(self):
		for i, doc in enumerate(self.docs):
			#print pp_str(gensim.models.doc2vec.LabeledSentence(doc, ['SENT_%s' % i]))
			yield gensim.models.doc2vec.LabeledSentence(doc, ['SENT_%s' % i])
			# yield gensim.models.doc2vec.TaggedDocument(namedtuple(doc, ['SENT_%s' % i]))


#Doc2vecで取得した各文章の類似度、代表ワードを求める
def create_sim_vec(model, n_sent):
	base_name = 'SENT_'
	sim_matrix = []      #類似度行列
	word_matrix = []     #各文章の代表ワード
	for i in range(n_sent):
		#pdb.set_trace()
		sim_vec = np.zeros(n_sent)
		#word_list = []
		#print model.docvecs.most_similar(base_name+str(i))
		for j in range(len(model.docvecs.most_similar(base_name + str(i)))):
			jid, sim = model.docvecs.most_similar(base_name + str(i))[j]
			sim_vec[jid] = sim
		sim_matrix.append(sim_vec)
		#word_matrix.append(word_list)
	return sim_matrix, word_matrix


###  Doc2vecでテキスト分類  ###
def cluster_doc2vec():
	docs, coupons = tokenize()
	sentences = LabeledLineSentence(docs)
	model = gensim.models.Doc2Vec(alpha=0.025, min_alpha=0.025)
	model.build_vocab(sentences)
	pdb.set_trace()


	#model.save('.d2v')                                   #model save
	#model_loaded = gensim.models.Doc2vec.load('.d2v')    #model load

	epoch = 10
	for _ in range(epoch):
		model.train(sentences)
		model.alpha -= 0.002
		model.min_alpha = model.alpha
	print 'done training'

	pdb.set_trace()



if __name__ == '__main__':
	cluster_doc2vec()

	'''
	ベクトル確認
	model.docvecs[0]

	コサイン類似度の計算
	print 1 - scipy.spatial.distance.cosine(x, y)
	'''
