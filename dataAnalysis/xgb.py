#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
xgboostによる学習
'''

import numpy as np
import pandas as pd
import xgboost as xgb
import pdb
from hyperopt import fmin, tpe, hp, rand, STATUS_OK, Trials
from sklearn import datasets, cross_validation
from sklearn.metrics import confusion_matrix, log_loss
from sklearn.cross_validation import KFold
from sklearn import preprocessing


iris = datasets.load_iris()
trainX = iris.data[0::2,:]
trainY = iris.target[0::2]
testX  = iris.data[1::2,:]
testY  = iris.target[1::2]

skf = cross_validation.StratifiedKFold(trainY, n_folds=3, shuffle=True, random_state=123)



def score(params):
	print "Training with params : "
	print params
	Sum = 0.0
	ite = 0.0
	for train, test in skf:
		x_train, x_test, y_train, y_test = trainX[train], trainX[test], trainY[train], trainY[test]
		dtrain = xgb.DMatrix(x_train, label=y_train)
		dvalid = xgb.DMatrix(x_test, label=y_test)
		#early stoppingを用いる際に必要
		watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
		model = xgb.train(params, dtrain, num_boost_round=150, evals=watchlist, early_stopping_rounds=10)
		predictions = model.predict(dvalid).reshape((x_test.shape[0], 3))
		ite += model.best_iteration
		Sum += model.best_score
		#pdb.set_trace()
	Sum /= len(skf)
	ite /= len(skf)
	print "\tAverage of best iteraion {0}\n".format(ite)
	print "\tScore {0}\n\n".format(Sum)
	return {'loss': Sum, 'status': STATUS_OK}




def optimize(trials):
	space = {
		'eta' : hp.quniform('eta', 0.1, 0.5, 0.05),
		'max_depth' : hp.uniform('max_depth', 1, 10, 1),
		'min_child_weight' : hp.quniform('min_child_weight', 1, 10, 1),
		'subsample' : hp.quniform('subsample', 0.5, 1, 0.05),
		'gamma' : hp.quniform('gamma', 0, 1, 0.05),
		'colsample_bytree' : hp.quniform('colsample_bytree', 0.5, 1, 0.05),
		'num_class' : 3,
		'eval_metric' : 'mlogloss',
		'objective' : 'multi:softprob',
		'lambda' : 1e-5,
		'alpha' : 1e-5,
		'silent' : 1
	}
	#pdb.set_trace()
	best = fmin(score, space, algo=tpe.suggest, trials=trials, max_evals=100)
	print best





if __name__ == '__main__':
	np.random.seed(123)

	params = {'objective': 'multi:softprob',
			  'eval_metric': 'mlogloss',
			  'eta': 0.35,
			  'max_depth': 3,
			  'gamma': 0.15,
			  'min_child_weight': 1,
			  'subsample': 0.85,
			  'colsample_bytree': 1,
			  'lambda': 1e-5,
			  'alpha': 1e-5,
			  'num_class': 3
			 }

	trials = Trials()
	optimize(trials)

	score(params)
	
	trainX = pd.DataFrame(trainX)
	testX  = pd.DataFrame(testX)
	dtrain = xgb.DMatrix(trainX.as_matrix(), label=trainY.tolist())
	dtest  = xgb.DMatrix(testX.as_matrix())

	bst  = xgb.train(params, dtrain, num_boost_round=23)
	pred = bst.predict(dtest)
	pred = pd.DataFrame(pred)
	print confusion_matrix(testY, pred.idxmax(axis=1))


	#pdb.set_trace()













