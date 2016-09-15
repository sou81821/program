#!/usr/bin/env python
#coding: UTF-8
import sys
import random

### お釣りの硬貨の枚数が最も少なくなる硬貨の組み合わせを表示する ###
### 硬貨は1円、5円、10円、50円、100円、500円の種類がある      ###
def charge():
	price = 521
	charge = 1000 - price
	moneys = [500,100,50,10,5,1]
	charge_numbers = [0] * 6
	for i, money in enumerate(moneys):
		if i == 0:
			charge_numbers[i] = charge // money
		else:
			charge_numbers[i] = (charge - sum([charge_numbers[j]*moneys[j] for j in range(0,i)])) // money
		print moneys[i], "*", charge_numbers[i]



if __name__=="__main__":
	charge()