#!/usr/bin/env python
#coding: UTF-8

def main():
	nums = []
	for i in range(2):
		nums.append(map(int, raw_input().split()))
	letter = raw_input()
	total = sum([sum(num) for _, num in enumerate(nums)])
	print total, letter

if __name__ == '__main__':
	main()