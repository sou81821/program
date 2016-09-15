#!/usr/bin/env python
#coding: UTF-8

import csv
import pandas as pd


if __name__ == '__main__':

	f = open('adult.csv', 'rU')
	reader = csv.reader(f)

	graduate = []

	for line in reader:
		if len(line) == 15:
			graduate.append(line[3])

	dum = pd.get_dummies(graduate)
	dum.to_csv('example.csv')

	f.close()



