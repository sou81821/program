#!/usr/bin/env python
#coding: UTF-8

import pdb
import sys

# 10. 変換
def convert(lines):
    for line in lines:
        print line.replace("\t", " "),

# 12
def devide_file(lines):
    with open("col1.txt", "ab") as f1, open("col2.txt", "ab") as f2:
        for line in lines:
            line = line.split()
            line = [e+"\n" for e in line]
            f1.writelines(line[0])
            f2.writelines(line[1])

# 13
def merge_file():
    with open("col1.txt") as f1, open("col2.txt") as f2, open("merge.txt", "ab") as f3:
        lines1, lines2 = f1.readlines(), f2.readlines()
        for line1, line2 in zip(lines1, lines2):
            f3.writelines("\t".join([line1.rstrip(), line2]),)

# 14. 先頭からN文字出力
def head_print(lines):
    row_count = int(sys.argv[1])
    for line in lines[:row_count]:
        print line,

# 15. 末尾のN行を出力
def tail_print(lines):
    row_count = int(sys.argv[1])
    for line in lines[::-1][:row_count][::-1]:
        print line,

# 16. ファイルをN分割する（24/5 -> [5,5,5,5,4]）
def devide_n_file(lines):
    n_devide = int(sys.argv[1])
    each_counts = [len(lines)/n_devide] * n_devide
    for i in range(len(lines)%n_devide):
        each_counts[i] += 1
    f_list = [open("devide_{0}.txt".format(i+1), "ab") for i in range(n_devide)]
    count = 0
    for i in range(n_devide):
        for j in range(each_counts[i]):
            f_list[i].writelines(lines[j+count])
        count += each_counts[i]
    for i in range(n_devide):
        f_list[i].close

# 17. 1列目の文字列の異なり
def get_prefecture_set(lines):
    prefectures = set()
    for _, line in enumerate(lines):
        pref = line.split()[0]
        if not pref in prefectures:
            prefectures.add(pref)
    for pref in enumerate(prefectures):
        print pref[1]


if __name__ == '__main__':
    with open("hightemp.txt") as f:
        lines = f.readlines()
    #convert(lines)
    #devide_file(lines)
    #merge_file()
    #head_print(lines)
    #tail_print(lines)
    #devide_n_file(lines)
    get_prefecture_set(lines)
