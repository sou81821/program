#!/usr/bin/env python
#coding: UTF-8
##### ヒープを作成するプログラム #####

import math

### ヒープの構築 ###
def upheap(heap, n):
	while True:
		p = (n-1) / 2
		if p < 0 or heap[p] <= heap[n]: break
		tmp = heap[n]
		heap[n] = heap[p]
		heap[p] = tmp
		n = p


### ヒープの再構築 ###
def downheap(heap, n):
	size = len(heap)
	while True:
		c = 2*n + 1
		if c >= size: break    #子が存在しない
		if c+1 < size:         #子が２つある場合
			if heap[c] > heap[c+1]: c+=1
		if heap[n] <= heap[c]: break    #ヒープの条件を満たしている
		temp = heap[n]
		heap[n] = heap[c]
		heap[c] = tmp
		n = c


















