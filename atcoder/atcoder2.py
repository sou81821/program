#!/usr/bin/env python
#coding: UTF-8

import numpy as np

def to_num(a):
	if a == "A":
		a = 10
	elif a == "B":
		a = 11
	elif a == "C":
		a = 12
	elif a == "D":
		a = 13
	elif a == "E":
		a = 14
	elif a == "F":
		a = 15
	return int(a)

def to_hexa(ex):
	if ex >= 17:
		ex -= 16

	if ex == 10:
		ex = "A"
	elif ex == 11:
		ex = "B"
	elif ex == 12:
		ex = "C"
	elif ex == 13:
		ex = "D"
	elif ex == 14:
		ex = "E"
	elif ex == 15:
		ex = "F"
	elif ex == 16:
		ex = 0
	return str(ex)

def incomplete_sum(ex1, ex2):
	letters = []
	for (a, b) in zip(ex1, ex2):
		a = to_num(a)
		b = to_num(b)
		ex = a + b
		ex = to_hexa(ex)
		letters.append(ex)
	return "".join(letters)

def main():
	num_p, num_q = map(int, raw_input().split())
	patterns = []
	querys   = []
	for i in range(num_p):
		patterns.append(raw_input())
	for i in range(num_q):
		querys.append(map(int, raw_input().split()))
	
	querys = np.array(querys)
	querys[:,1:] -= 1
	for _, query in enumerate(querys):
		ex1 = patterns[query[1]][query[4]:query[4]+query[0]]
		ex2 = patterns[query[2]][query[5]:query[5]+query[0]]
		ex4 = incomplete_sum(ex1, ex2)
		goal = []
		count = 0
		for i in range(len(patterns[query[3]])):
			if query[6] <= i <= query[6]+query[0]-1:
				goal.append(ex4[count])
				count += 1
			else:
				goal.append(patterns[query[3]][i])
		patterns[query[3]] = "".join(goal)

	for _, result in enumerate(patterns):
		print str(result)


if __name__ == '__main__':
	main()