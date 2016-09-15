#!/usr/bin/env python
#coding: UTF-8

### 各潜在クラスにおける各属性（９種類，計73）の割合を求めるプログラム ###

import os
import sys
import math

#f = open('adult_model.pwz',"r")
#f = open('adult_10_discretization_model.pwz',"r")
f = open('adult_mdlp_50_model.pwz',"r")
lines = f.readlines()

#総潜在クラス数
lc = 0

for line in lines:
	lc += 1
	x = line.split(" ")
	#print type(x[2])

	#age
	for i in range(0,4):
		if i == 0:
			age_max = float(x[i])
			age_max_number = i
		else:
			if age_max <= float(x[i]):
				age_max = float(x[i])
				age_max_number = i

	#workclass
	for i in range(4,13):
		if i == 4:
			workclass_max = float(x[i])
			workclass_max_number = i
		else:
			if workclass_max <= float(x[i]):
				workclass_max = float(x[i])
				workclass_max_number = i

	#education
	for i in range(13,29):
		if i == 13:
			education_max = float(x[i])
			education_max_number = i
		else:
			if education_max <= float(x[i]):
				education_max = float(x[i])
				education_max_number = i

	#marital-status
	for i in range(29,36):
		if i == 29:
			marital_max = float(x[i])
			marital_max_number = i
		else:
			if marital_max <= float(x[i]):
				marital_max = float(x[i])
				marital_max_number = i

	#occupation
	for i in range(36,50):
		if i == 36:
			occupation_max = float(x[i])
			occupation_max_number = i
		else:
			if occupation_max <= float(x[i]):
				occupation_max = float(x[i])
				occupation_max_number = i

	#relationship
	for i in range(50,56):
		if i == 50:
			relationship_max = float(x[i])
			relationship_max_number = i
		else:
			if relationship_max <= float(x[i]):
				relationship_max = float(x[i])
				relationship_max_number = i

	#race
	for i in range(56,61):
		if i == 56:
			race_max = float(x[i])
			race_max_number = i
		else:
			if race_max <= float(x[i]):
				rece_max = float(x[i])
				race_max_number = i

	#sex
	for i in range(61,63):
		if i == 61:
			sex_max = float(x[i])
			sex_max_number = i
		else:
			if sex_max <= float(x[i]):
				sex_max = float(x[i])
				sex_max_number = i

	#native-country
	for i in range(63,68):
		if i == 63:
			country_max = float(x[i])
			country_max_number = i
		else:
			if country_max <= float(x[i]):
				country_max = float(x[i])
				country_max_number = i


	#capital-gain
	for i in range(68,70):
		if i == 68:
			capital_gain_max = float(x[i])
			capital_gain_max_number = i
		else:
			if capital_gain_max <= float(x[i]):
				capital_gain_max = float(x[i])
				capital_gain_max_number = i


	#capital-loss
	#for i in range(71,73):
	#	if i == 71:
	#		capital_loss_max = float(x[i])
	#		capital_loss_max_number = i
	#	else:
	#		if capital_loss_max <= float(x[i]):
	#			capital_loss_max = float(x[i])
	#			capital_loss_max_number = i


	#年収
	for i in range(70,72):
		if i == 70:
			money_max = float(x[i])
			money_max_number = i
		else:
			if money_max <= float(x[i]):
				money_max = float(x[i])
				money_max_number = i




	#classification[max_number] += 1
	#print "age:%d workclass:%d education:%d" % (age_max_number, workclass_max_number, education_max_number)
	#print "marital:%d occupation:%d relationship:%d" % (marital_max_number, occupation_max_number, relationship_max_number)
	#print "race:%d sex:%d country:%d" % (race_max_number, sex_max_number, country_max_number)
	#print "\n"
	print "グループ %d" % lc

	#if(age_max_number == 0):
	#	print "age : 10代"
	#elif(age_max_number == 1):
	#	print "age : 20代"
	#elif(age_max_number == 2):
	#	print "age : 30代"
	#elif(age_max_number == 3):
	#	print "age : 40代"
	#elif(age_max_number == 4):
	#	print "age : 50代"
	#elif(age_max_number == 5):
	#	print "age : 60代"
	#elif(age_max_number == 6):
	#	print "age : 70代"
	#elif(age_max_number == 7):
	#	print "age : 80代"
	#elif(age_max_number == 8):
	#	print "age : 90代"


	if(age_max_number == 0):
		print "age : 21歳以下"
	elif(age_max_number == 1):
		print "age : 22〜27歳"
	elif(age_max_number == 2):
		print "age : 28〜64歳"
	elif(age_max_number == 3):
		print "age : 65歳以上"


	if(workclass_max_number == 4):
		print "workclass : Private"
	elif(workclass_max_number == 5):
		print "workclass : Self-emp-not-inc"
	elif(workclass_max_number == 6):
		print "workclass : Self-emp-inc"
	elif(workclass_max_number == 7):
		print "workclass : Federal-gov"
	elif(workclass_max_number == 8):
		print "workclass : Local-gov"
	elif(workclass_max_number == 9):
		print "workclass : State-gov"
	elif(workclass_max_number == 10):
		print "workclass : Without-pay"
	elif(workclass_max_number == 11):
		print "workclass : Never-worked"
	elif(workclass_max_number == 12):
		print "workclass : NA"


	if(education_max_number == 13):
		print "education : Bachelors"
	elif(education_max_number == 14):
		print "education : Some-college"
	elif(education_max_number == 15):
		print "education : 11th"
	elif(education_max_number == 16):
		print "education : HS-grad"
	elif(education_max_number == 17):
		print "education : Prof-school"
	elif(education_max_number == 18):
		print "education : Assoc-acdm"
	elif(education_max_number == 19):
		print "education : Assoc-voc"
	elif(education_max_number == 20):
		print "education : 9th"
	elif(education_max_number == 21):
		print "education : 7th-8th"
	elif(education_max_number == 22):
		print "education : 12th"
	elif(education_max_number == 23):
		print "education : Masters"
	elif(education_max_number == 24):
		print "education : 1st-4th"
	elif(education_max_number == 25):
		print "education : 10th"
	elif(education_max_number == 26):
		print "education : Doctorate"
	elif(education_max_number == 27):
		print "education : 5th-6th"
	elif(education_max_number == 28):
		print "education : Preschool"


	if(marital_max_number == 29):
		print "marital-status : Married-civ-spouse"
	elif(marital_max_number == 30):
		print "marital-status : Divorced"
	elif(marital_max_number == 31):
		print "marital-status : Never-married"
	elif(marital_max_number == 32):
		print "marital-status : Separated"
	elif(marital_max_number == 33):
		print "marital-status : Widowed"
	elif(marital_max_number == 34):
		print "marital-status : Married-spouse-absent"
	elif(marital_max_number == 35):
		print "marital-status : Married-AF-spouse"


	if(occupation_max_number == 36):
		print "occupation : Tech-support"
	elif(occupation_max_number == 37):
		print "occupation : Craft-repair"
	elif(occupation_max_number == 38):
		print "occupation : Other-service"
	elif(occupation_max_number == 39):
		print "occupation : Sales"
	elif(occupation_max_number == 40):
		print "occupation : Exec-managerial"
	elif(occupation_max_number == 41):
		print "occupation : Prof-specialty"
	elif(occupation_max_number == 42):
		print "occupation : Machine-op-inspct"
	elif(occupation_max_number == 43):
		print "occupation : Adm-clerical"
	elif(occupation_max_number == 44):
		print "occupation : Farming-fishing"
	elif(occupation_max_number == 45):
		print "occupation : Transport-moving"
	elif(occupation_max_number == 46):
		print "occupation : Priv-house-serv"
	elif(occupation_max_number == 47):
		print "occupation : Protective-serv"
	elif(occupation_max_number == 48):
		print "occupation : Armed-Forces"
	elif(occupation_max_number == 49):
		print "occupation : NA"


	if(relationship_max_number == 50):
		print "relationship : Wife"
	elif(relationship_max_number == 51):
		print "relationship : Own-child"
	elif(relationship_max_number == 52):
		print "relationship : Husband"
	elif(relationship_max_number == 53):
		print "relationship : Not-in-family"
	elif(relationship_max_number == 54):
		print "relationship : Other-relative"
	elif(relationship_max_number == 55):
		print "relationship : Unmarried"


	if(race_max_number == 56):
		print "race : White"
	elif(race_max_number == 57):
		print "race : Asian-Pac-Islander"
	elif(race_max_number == 58):
		print "race : Amer-Indian-Eskimo"
	elif(race_max_number == 59):
		print "race : Other"
	elif(race_max_number == 60):
		print "race : Black"


	if(sex_max_number == 61):
		print "sex : Female（女性）"
	elif(sex_max_number == 62):
		print "sex : Male（男性）"


	if(country_max_number == 63):
		print "native-country : 北米"
	elif(country_max_number == 64):
		print "native-country : アジア"
	elif(country_max_number == 65):
		print "native-country : ヨーロッパ"
	elif(country_max_number == 66):
		print "native-country : 中南米"
	elif(country_max_number == 67):
		print "native-country : NA"


	if(capital_gain_max_number == 68):
		print "capital_gain : なし"
	elif(capital_gain_max_number == 69):
		print "capital_gain : あり"
	#elif(capital_gain_max_number == 70):
	#	print "capital_gain : ＄９９９９９　以上"


	#if(capital_loss_max_number == 71):
	#	print "capital_loss : なし"
	#elif(capital_loss_max_number == 72):
	#	print "capital_loss : あり（＄４３５６　以下）"


	if(money_max_number == 70):
		print "＄５０K / 年　を超えない"
	elif(money_max_number == 71):
		print "＄５０K / 年　を超える"

	print("\n\n")





#print classification

f.close()