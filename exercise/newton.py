#!/usr/bin/env python
#coding: UTF-8

import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time


### ニュートン法 ###
def newton():
	print "初期値を入力してください（2+√2以上）"
	x = float(input())

	print "収束判定定数を入力してください"
	ipsiron = float(input())

	print "反復回数の上限を入力してください"
	k_max = float(input())

	delta = 0     #xの変化量
	k = 0         #反復回数

	diff = 2*x - 2
	delta =  -(x**2 - 4*x + 2) / diff

	while math.fabs(delta) > ipsiron and k != k_max:
		diff = 2*x - 2
		delta =  -(x**2 - 4*x + 2) / diff
		x = x + delta
		k = k + 1
		#print delta

	if k == k_max:
		print "失敗！！"
	else:
		print x


if __name__=="__main__":
	newton()
