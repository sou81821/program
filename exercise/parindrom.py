#!/usr/bin/env python
#coding: UTF-8

import sys

### 回文を判断する関数 ###
def palindrom():
	print "文字列を入力してください"
	sentence = raw_input()
	print True if sentence==sentence[::-1] else False
	# middle = len(sentence)/2
	# for start, end in zip(sentence[:middle], reversed(sentence[middle+1:])):
	# 	if start != end:
	# 		print False
	# print True




