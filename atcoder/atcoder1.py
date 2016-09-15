#!/usr/bin/env python
#coding: UTF-8

import pdb

def convert_point(point):
	if point == 1:
		point = 15
	elif point == 2:
		point = 30
	elif point == 3:
		point = 40
	return point

def main():
	letters = raw_input()
	a_point = b_point = 0
	a_game  = b_game  = 0
	a_set   = b_set   = 0
	for _, letter in enumerate(letters):
		if letter == "A":
			a_point += 1
		else:
			b_point += 1
		
		if a_point == 4:
			a_game += 1
			a_point = 0
			b_point = 0
		elif b_point == 4:
			b_game += 1
			a_point = 0
			b_point = 0
		
		if a_game == 6:
			a_set += 1
			a_game = 0
			b_game = 0
		elif b_game == 6:
			b_set += 1
			a_game = 0
			b_game = 0

	a_point = convert_point(a_point)
	b_point = convert_point(b_point)
	print "PScore", "-".join([str(a_point), str(b_point)])
	print "Game", "-".join([str(a_game), str(b_game)])
	print "Set", "-".join([str(a_set), str(b_set)])


if __name__ == '__main__':
	main()