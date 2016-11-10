#!/usr/bin/env python
#coding: UTF-8

import json
import pdb
import re

def search_from_json(title):
    with open("jawiki-country.json") as f:
        article_json = f.readline()
        while article_json:
            article = json.loads(article_json)
            if article["title"] == title.decode("utf-8"):
                return article["text"]
            article_json = f.readline()

# 22. カテゴリ名のみの抽出
def extract_category(text):
    for line in text:
        category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]", line)
        if category_line:
            print category_line.group(1)

# 23. セクション構造
def extract_section(text):
    for line in text:
        section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
        if section_line:
            print section_line.group(2), len(section_line.group(1))

# 24. ファイル参照の抽出
def extract_mediaFile(text):
    for line in text:
        media_line = re.search(u"(File|ファイル):(.*?)\|", line)
        if media_line:
            print media_line.group(2)

# 25. テンプレートの抽出


if __name__ == '__main__':
    text = search_from_json("イギリス").split("\n")
    pdb.set_trace()
    extract_category(text)
    #extract_section(text)
    #extract_mediaFile(text)
