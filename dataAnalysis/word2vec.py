#!/usr/bin/env python
#coding: UTF-8

import gensim
import pdb

'''
使い方例
（"単語" or "単語".decode("utf-8")）

・単語のベクトル化　 ：　model["単語"]
・2つの単語の類似度　：　model.similarity("単語1", "単語2")
・似ている単語の探索 ：　model.most_similar("単語")
・単語の足し引き　　 ：　model.most_similar(positive=["woman", "king"], negative=["man"])
'''

def main():
	# モデルの読み込み(少し時間かかる)
	model = gensim.models.word2vec.Word2Vec.load("model/wikipedia.model")
	pdb.set_trace()


if __name__ == '__main__':
	main()