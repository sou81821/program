#!/usr/bin/env python
#coding: UTF-8

##### じゃんけんをしたときの手の組み合わせを全て出力するプログラム #####
##### 　　　　　　　　人数はコマンド引数で受け取る　　　　　　　　 #####


import sys
import itertools

hands = ["gu", "tyoki", "pa"]

print "人数を選択してください"
count = int(raw_input())

for i in itertools.product(hands, repeat=count):
	print i



