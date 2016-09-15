#!/usr/bin/env python
#coding: UTF-8


def exchange(money):
	money_list = [500,100,50,10]
	count = 0

	for i in range(money/money_list[0]+1):
		for j in range((money-500*i)/money_list[1]+1):
			for k in range((money-500*i-100*j)/money_list[2]+1):
				for l in range((money-500*i-100*j-50*k)/money_list[3]+1):
					if (i+j+k+l) <= 15 and ((money-500*i-100*j-50*k-10*l) == 0):
						count += 1
						print "500:", i, "100:", j, "50:", k, "10:", l

	print count


if __name__=="__main__":
	exchange(2000)


