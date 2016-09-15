#!/usr/bin/env python
#coding: UTF-8
import sys


####### 10000以下の素数を表示するプログラム #######

def prime():
	prime_num = []  #素数リスト
	for i in range(2,10001):
		if i == 2:
			prime_num.append(i)
		else:
			prime_num_temp = prime_num
			try:
				for number in prime_num_temp:
					if(i % number == 0):
						raise Exception
				prime_num.append(i)
			except Exception:
				pass

	return prime_num


if __name__=="__main__":
	prime()