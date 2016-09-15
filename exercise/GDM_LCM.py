#!/usr/bin/env python
#coding: UTF-8
import sys

####### ２つの自然数の最大公約数、最小公倍数を求めるプログラム #######

def GCD_LCM():

	print "１つ目の自然数を入力してください"
	data1 = int(input())
	print "２つ目の自然数を入力してください"
	data2 = int(input())
	data_product = data1 * data2

	while 1:
		if data1 <= data2:
			data = data1
			data1 = data2
			data2 = data
		#print "%d %d" % (data1,data2)
		if data1 == data2:
			GCD = data1
			LCM = data_product / GCD
			print "最大公約数は %d" % GCD
			print "最小公倍数は %d" % LCM
			break
		elif data1 > data2:
			data1 = data1 - data2


if __name__=="__main__":
	GCD_LCM()