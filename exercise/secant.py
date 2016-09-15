#!/usr/bin/env python
#coding: UTF-8

import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time


### 割線法 ###
def secant():
	print "初期値を２つ入力してください（2+√2以上）"
	x0 = float(input())
	x1 = float(input())

	print "収束判定定数を入力してください"
	ipsiron = float(input())

	print "反復回数の上限を入力してください"
	k_max = float(input())

	delta = 0     #xの変化量
	k = 1         #反復回数

	delta =  x0 - x1
	y0 = x0**2 - 4*x0 + 2

	while math.fabs(delta) > ipsiron and k != k_max:
		y1 = x1**2 - 4*x1 + 2
		delta =  -delta * y1 / (y1 - y0)
		x1 = x1 + delta
		y0 = y1
		k = k + 1
		#print delta

	if k == k_max:
		print "失敗！！"
	else:
		print x1


if __name__=="__main__":
	secant()