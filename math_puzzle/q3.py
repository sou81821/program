#!/usr/bin/env python
#coding: UTF-8

### カードを裏返す問題 ###

import numpy as np

card = np.array([False]*100)

for i in range(1,101):
	step = i
	for j in range(100/step):
		if i < 100:
			card_tmp = np.logical_not(card)
			card[i] = card_tmp[i]
			i += (step+1)

print np.where(np.logical_not(card))[0]+1


