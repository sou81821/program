#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
パラメータ最適化ライブラリ「hyperopt」の活用
'''

import numpy as np
import pdb
from hyperopt import fmin, tpe, hp, rand
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn import datasets


parameter_space_svc = {
	'C':hp.loguniform("C", np.log(1), np.log(100)),
	'kernel':hp.choice('kernel',['rbf','poly']),
	'gamma': hp.loguniform("gamma", np.log(0.001), np.log(0.1)),
}

digits = datasets.load_digits()

train_data   = digits.data[0:1300]
train_target = digits.target[0:1300]
test_data    = digits.data[1300:-1]
test_target  = digits.target[1300:-1]
pdb.set_trace()

count = 0

def function(args):
	print args
	clf = svm.SVC(**args)
	clf.fit(train_data, train_target)
	prediction = clf.predict(test_data)
	global count
	count = count + 1
	score = accuracy_score(test_target, prediction)
	print "%s回目の推測" % str(count),score
	return -accuracy_score(test_target, prediction)
	pdb.set_trace()

best = fmin(function, parameter_space_svc, algo=tpe.suggest, max_evals=100)
print "best estimate parameters", best

clf = svm.SVC(**best)
print clf