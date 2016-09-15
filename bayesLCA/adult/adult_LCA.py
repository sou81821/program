#!/usr/bin/env python
#coding: UTF-8

##### データセット「adult」をBayesLCA用にカテゴリデータに変換するプログラム #####

import csv
import pandas as pd
import pdb

#ファイルの読み込み
f = open('adult.csv','r')
reader = csv.reader(f)

#デバック
#pdb.set_trace()


i = 0   #iterator
age          = []    #年齢
workclass    = []    #workclass
education    = []    #最終学歴
marry        = []    #married-status
occupation   = []    #職業
relationship = []    #家庭での関係
race         = []    #人種
sex          = []    #性別
capital_gain = []    #資産収入
capital_loss = []    #資産支出
hpw          = []    #週間労働時間
country      = []    #国籍
income       = []    #所得フラグ


#各属性のリストを作成
while line:
	Elements = line.strip().split(",")

	age.append(int(Elements[0][-2:]))
	workclass.append(Elements[1])
	education.append(Elements[3])
	marry.append(Elements[5])
	occupation.append(Elements[6])
	relationship.append(Elements[7])
	race.append(Elements[8])
	sex.append(Elements[9])
	capital_gain.append(int(Elements[10][1:]))
	capital_loss.append(int(Elements[11][1:]))
	hpw.append(int(Elements[12][1:]))
	country.append(Elements[13])
	income.append(Elements[14])
	money = 0

	line = f.readline()



##### カテゴリ変数に加工 #####
dum_workclass    = pd.get_dummies(workclass)
#dum_education    = pd.get_dummies(education)
#dum_marry        = pd.get_dummies(marry)
#dum_occupation   = pd.get_dummies(occupation)
#dum_relationship = pd.get_dummies(relationship)
#dum_race         = pd.get_dummies(race)
#dum_sex          = pd.get_dummies(sex)
#dum_country      = pd.get_dummies(country)
#dum_income       = pd.get_dummies(income)

dum_workclass.to_csv('workclass.csv')




##### 連続値を離散値に #####
#北米(3),アジア(12),ヨーロッパ(12),中南米(14)
if(Elements[13] == " United-States" or Elements[13] == " Canada" or Elements[13] == " Outlying-US(Guam-USVI-etc)"):
	Elements_new[63] = 1
elif(Elements[13] == " Cambodia" or Elements[13] == " India" or Elements[13] == " Japan" or Elements[13] == " South" or Elements[13] == " China" or Elements[13] == " Iran" or Elements[13] == " Philippines" or Elements[13] == " Vietnam" or Elements[13] == " Laos" or Elements[13] == " Taiwan" or Elements[13] == " Thailand" or Elements[13] == " Hong"):
	Elements_new[64] = 1
elif(Elements[13] == " England" or Elements[13] == " Germany" or Elements[13] == " Greece" or Elements[13] == " Italy" or Elements[13] == " Poland" or Elements[13] == " Portugal" or Elements[13] == " Ireland" or Elements[13] == " France" or Elements[13] == " Hungary" or Elements[13] == " Scotland" or Elements[13] == " Yugoslavia" or Elements[13] == " Holand-Netherlands"):
	Elements_new[65] = 1
elif(Elements[13] == " Puerto-Rico" or Elements[13] == " Cuba" or Elements[13] == " Honduras" or Elements[13] == " Jamaica" or Elements[13] == " Mexico" or Elements[13] == " Dominican-Republic" or Elements[13] == " Ecuador" or Elements[13] == " Haiti" or Elements[13] == " Columbia" or Elements[13] == " Guatemala" or Elements[13] == " Nicaragua" or Elements[13] == " El-Salvador" or Elements[13] == " Trinadad&Tobago" or Elements[13] == " Peru"):
	Elements_new[66] = 1
else:
	Elements_new[67] = 1


#ageの加工(0〜3)，NAなし, (MDLPによる離散化)
if(age < 22):
	Elements_new[0] = 1
elif(22 <= age and age < 28):
	Elements_new[1] = 1
elif(28 <= age and age < 65):
	Elements_new[2] = 1
else:
	Elements_new[3] = 1


#capital-gainの加工(68〜69), NAなし, (MDLPによる離散化)
if(capital_gain == 0):
	Elements_new[68] = 1
else:
	Elements_new[69] = 1


#capital-loseの加工(71〜72), NAなし
if(capital_loss == 0):
	Elements[11] = 71
elif(capital_loss <= 4356):
	Elements[11] = 72


#週間労働時間(house per week)の加工(72〜73)
if(hpw <= 30):
	Elements_new[70] = 1
elif(30 < hpw):
	Elements_new[71] = 1


f.close()

