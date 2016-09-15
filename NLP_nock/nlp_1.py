#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import random

# 5. n-gram
def n_gram(text, gram=2):
    num = len(text) - gram + 1
    gram_list = [text[i:i+gram] for i in range(num)]
    return gram_list

# 6. 2つの文字列の集合を求める
def make_set():
    text1 = "paraparaparadise"
    text2 = "paragraph"
    x = set(n_gram(text1, 2))
    y = set(n_gram(text2, 2))
    print x, y
    print "和集合：", x | y
    print "積集合：", x & y
    print "(X-Y)差集合：", x - y
    print "(Y-X)差集合：", y - x

# 8. 暗号文
def cipher(text):
    convert_text = ""
    for _, s in enumerate(text):
        if s.islower():
            convert_text += chr(219 - ord(s))
        else:
            convert_text += s
    return convert_text

# 9. Typoglycemia
def typoglycemia(text):
    words = text.split()
    convert_words = []
    for word in words:
        if len(word)>4:
            middle_list = list(word[1:-1])
            random.shuffle(middle_list)
            convert_words.append(word[0] + "".join(middle_list) + word[-1])
        else:
            convert_words.append(word)
    return " ".join(convert_words)


if __name__ == '__main__':
    #text = "".join(raw_input().split())
    #print n_gram(text)
    #print cipher( "Hi He Lied Because Boron Could Not Oxidize Fluorine.")
    print typoglycemia("name is konishi")
