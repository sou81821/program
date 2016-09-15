#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pdb

n = 3

def move(log_list):
    if len(log_list) == n+1:
        return 1

    count = 0
    for move in [[0,1], [0,-1], [1,0], [-1,0]]:
        point = [log_list[-1][0] + move[0], log_list[-1][1] + move[1]]
        if not (point in log_list):
            #log_list.append(point)
            print log_list
            count += move(log_list + [point])
    print count

print move([[0,0]])
