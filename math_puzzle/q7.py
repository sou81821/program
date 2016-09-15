#!/usr/bin/env python
#coding: UTF-8

import datetime

def daterange(start, end):
	for i in range((end-start).days):
		day_str         = start.strftime('%Y%m%d')
		day_bin         = str(bin(int(day_str))[2:])
		day_bin_reverse = day_bin[::-1]
		day_reverse     = int(day_bin_reverse, 2)
		day_reverse_str = str(day_reverse)
		if day_str == day_reverse_str:
			print day_str
		start += datetime.timedelta(days=1)


if __name__=="__main__":
	start = datetime.datetime.strptime('1964/10/10', '%Y/%m/%d')
	end   = datetime.datetime.strptime('2020/07/24', '%Y/%m/%d')

	daterange(start, end)

