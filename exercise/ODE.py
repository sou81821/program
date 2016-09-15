#!/usr/bin/env python
#coding: UTF-8
import sys


####### フィボナッチ数列を2**31より小さい範囲まで表示するプログラム #######

def ODE():
	fp = open('a.txt','r')
	for line in fp:
		Elements = line.strip().split(",")
		f = map(float,Elements[1:])
		e = [0] * 4
		for i in range(4):
			e[i] = (f[i] - f[4])/f[4]
		print e
	fp.close()


if __name__=="__main__":
	ODE()