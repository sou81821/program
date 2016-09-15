#!/usr/bin/env python
#coding: UTF-8

import sys
import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time


### 二分法アルゴリズム ###
def bisection():

	print "端点を入力してください（１つは2-√2 以上 2+√2以下）"
	a = float(input())
	b = float(input())

	print "許容誤差を入力してください"
	error = float(input())

	#f(x) = x^2-4x+2   (x<2+√2)
	y = a**2 - 4*a + 2
	z = b**2 - 4*b + 2

	if y > 0 or z < 0:
		boxA = a
		boxB = y
		a = b
		y = z
		b = boxA
		z = boxB

	#反復回数
	n = math.ceil(math.log( (math.fabs(a-b) / error) , 2)) - 1
	n = int(n)

	for i in range(1,n+1):
		c = (a + b)/2   #中間値
		w = c**2 - 4*c + 2

		#f(中間値)に応じて端点を更新
		if w >= 0:
			b = c
			z = w
		else:
			a = c
			y = w
		#print c

	c = (a+b)/2
	print c


if __name__=="__main__":
	bisection()