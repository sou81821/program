#!/usr/bin/env python
#coding: UTF-8

'''
netkeibaから競馬データをスクレイピングする
'''

import urllib2 as ul
from lxml import html
import pandas as pd
import os
import re
import time
import datetime
import pdb
import csv
#import multiprocessing as mp
#from prettyprint import pp, pp_str


__PROC__ = 1


# dataをcsvファイルに出力
def data_to_csv(data, year):
	renames = []
	for i in range(len(data.columns)):
		renames.append(data.columns[i].encode('utf-8'))
	data.columns = renames
	for i in range(len(data)):
		data.iloc[i] = data.iloc[i].apply(lambda x: x.encode('utf-8') if type(x)!=float and type(x)!=int else x)
	data.to_csv("{0}_horse_table.csv".format(year), index=True, header=True)



# 馬の情報を集める
def makeHorseDB(year):
	horse_url = 'http://db.netkeiba.com/horse/'
	idx_from = 106637
	idx_to   = 106650
	#idx_to = 111000
	masta_data = {}
	performance_data = {}
	
	f = open('{0}_horse_performance.csv'.format(year), 'ab')
	csvWriter = csv.writer(f)
	header = ['horse_name', 'goal', 'race_date', 'area', 'whether', 'race_num', 'race_name', 'num_horses', 'waku_ban', 'uma_ban', 'odds', 'popularity', 'jockey', 'basis_w', 'race_type', 'distance', 'baba', 'race_time', 'arrive', 'passing', 'pace', 'last_time', 'horse_w', 'w_change', 'prize']
	csvWriter.writerow(header)

	prof_keys = [
		'馬名',
		'父',
		'母',
		'母父',
		'調教師',
		'馬主',
		'セリ取引価格'
	]


	for idx in range(idx_from, idx_to+1):
		try:
			# 過度なアクセスを抑えるために待ち時間を設定
			time.sleep(2)
			
			# webからhtmlを取得
			idx = str(year) + str(idx).zfill(6)
			url = horse_url + idx
			src_html = ul.urlopen(url).read()
			root = html.fromstring(src_html)

			# DBが存在しない場合
			if root.xpath('//title')[0].text.startswith(u' '):
				#print 'DB not found'
				continue

			horse_name = ""


			# プロフィール情報を取得
			masta_data[idx] = {}
			for prof_key in prof_keys:
				try:
					if prof_key == '馬名':
						# 地方馬なら
						if u'\u5730' == root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n')[1][2]:
							horse_name = root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n')[1].strip()[2:]
						else:
							horse_name = root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n')[1].strip()
							
						# 馬の評価が存在する場合
						horse_sex = ''
						if len(root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n'))==7:
							horse_status = root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n')[5].split()
						else:
							horse_status = root.xpath('//div[@class="horse_title"]')[0].text_content().split('\n')[3].split()
						for status in horse_status:
							if len(status)==1:
								horse_sex = status

						masta_data[idx][u'名前'] = horse_name
						masta_data[idx][u'性別'] = horse_sex
					
					elif prof_key == '父':
						masta_data[idx][u'父'] = root.xpath('//td[@rowspan="2"][@class="b_ml"]')[0].text_content().split('\n')[1]

					elif prof_key == '母':
						masta_data[idx][u'母'] = root.xpath('//td[@rowspan="2"][@class="b_fml"]')[0].text_content().split('\n')[1]

					elif prof_key == '母父':
						masta_data[idx][u'母父'] = root.xpath('//td[@class="b_ml"]')[2].text_content().split('\n')[1]

					elif prof_key == '調教師':
						masta_data[idx][u'調教師'] = root.xpath('//table[@class="db_prof_table"]/tr/td')[1].text_content()

					elif prof_key == '馬主':
						masta_data[idx][u'馬主'] = root.xpath('//table[@class="db_prof_table"]/tr/td')[2].text_content()

					elif prof_key == 'セリ取引価格':
						masta_data[idx][u'セリ取引価格'] = root.xpath('//table[@class="db_prof_table"]/tr/td')[5].text_content()
				except:
					pdb.set_trace()
					pass


			# 競走成績から情報を取得
			performance_data[idx] = {}
			r_hist = root.xpath('//table[@class="db_h_race_results nk_tb_common"]')
			if len(r_hist):
				r_hist_l = root.xpath('//table[@class="db_h_race_results nk_tb_common"]/tbody/tr')
				for race in r_hist_l:
					try:
						race = [race[i].text_content().encode('utf-8') for i in range(len(race))]
						race_date  = race[0]   # レース日付
						# 中央競馬のみ開催回数なども含まれる（例：3京都8）
						area       = race[1]          # 開催地
						whether    = race[2]          # 天気
						race_num   = int(race[3])     # レース番号
						race_name  = race[4]          # レース名
						num_horses = int(race[6])     # 出走頭数
						waku_ban   = int(race[7])     # 枠番
						uma_ban    = int(race[8])     # 魔版
						odds       = float(race[9])   # オッズ
						popularity = int(race[10])    # 人気
						goal       = int(race[11])    # 着順
						jockey     = race[12].strip() # 騎手
						basis_w    = float(race[13])  # 斤量
						race_type  = re.findall(r"[^0-9]*", race[14])[0]      # 芝orダート
						distance   = int(re.findall(r"[0-9]+", race[14])[0])  # 距離
						baba       = race[15]         # 馬場状況
						race_time  = float(race[17].split(':')[0])*60 + float(race[17].split(':')[1])  # レースタイム
						arrive     = float(race[18])  # 1着からの着差
						# 通過・ペースをコーナーごとに分ける
						passing    = race[20]         # 通過
						pace       = race[21]         # ペース
						last_time  = float(race[22])  # 上り
						horse_w    = int(race[23].split('(')[0])  # 馬体重
						w_change   = int(race[23].split('(')[1].replace(')',''))  # 前走からの体重差
						prize      = 0.0 if race[27]=='\xc2\xa0' else float(race[27].replace(',',''))  # 獲得賞金

						csvWriter.writerow([horse_name.encode('utf-8'), goal, race_date, area, whether, race_num, race_name, num_horses, waku_ban,uma_ban, odds, popularity, jockey, basis_w, race_type, distance, baba, race_time, arrive, passing, pace, last_time, horse_w, w_change, prize])
					
					except:
						# 出走取り消しになった場合や，属性にぬけがある場合
						pass


			# prize_all       = 0.0  # 総獲得賞金
			# rain_race_count = 0    # 重馬場出走回数
			# rain_record     = 0    # 重馬場合計着順

			# if len(r_hist) == 0:
			# 	masta_data[idx][u'獲得賞金'] = prize
			# else:
			# 	r_hist_l = root.xpath('//table[@class="db_h_race_results nk_tb_common"]/tbody/tr')
			# 	for race in r_hist_l:
			# 		if race.text_content().split('\n')[22] != '良'.decode('utf-8'):
			# 			rain_race_count += 1
			# 			rain_record += int(race.text_content().split('\n')[15])
			# 		try:
			# 			prize_all += float(race.text_content().split('\n')[-2].replace(',',''))
			# 		except:
			# 			pass

			# 	masta_data[idx][u'重馬場出走回数'] = '%d' % rain_race_count
			# 	masta_data[idx][u'重馬場合計着順'] = '%d' % rain_record
			# 	masta_data[idx][u'獲得賞金'] = '%.2f' % prize_all


			#print pp_str(masta_data[idx])

		except Exception as e:
			print idx, e.message


	# 馬の情報をcsv形式に出力
	horse_table = pd.DataFrame(masta_data).T
	data_to_csv(horse_table, year)
	#o_fname = 'horse_prof_%d.csv' % year
	#o_fpath = os.path.join(o_dname, o_fname)
	#horse_table.to_csv(o_fpath, encoding='utf-8')




# レース情報を集める
def makeRaceDB():
	race_url = 'http://db.netkeiba.com/race/'
	year  = [str(i) for i in range(2011, 2016)]
	# 1:札幌, 2:函館, 3:福島, 4:新潟, 5:東京, 6:中山, 7:中京, 8:京都, 9:阪神, 10:小倉
	place = [str(i).zfill(2) for i in range(1, 11)]
	time  = [str(i).zfill(2) for i in range(1, 7)]
	day   = [str(i).zfill(2) for i in range(1, 13)]
	race  = [str(i).zfill(2) for i in range(1, 13)]
	masta_data = {}


	try:
		url = race_url + "201505020611"
		src_html = ul.urlopen(url).read()
		root = html.fromstring(src_html)

		# DBが存在しない場合
		if root.xpath('//title')[0].text.startswith(u'\uff5c'):
			print 'DB not found'
			#continue

		race_data = root.xpath('//div[@class="data_intro"]')[0].text_content().split("\n")
		race_number = int(re.findall(r"[0-9]+", race_data[3].encode("utf-8"))[0])   # 第何レースか
		race_name = race_data[6]   # レース名
		race_type = race_data[9].split("/")[0][0]    # 芝 or ダート
		rotation  = race_data[9].split("/")[0][1]    # 左回り or 右回り
		distance  = int(re.findall(r"[0-9]+", race_data[9].split("/")[0].encode("utf-8"))[0])   # 距離
		whether   = race_data[9].split("/")[1].split(":")[1].strip()   # 天気
		ground    = race_data[9].split("/")[2].split(":")[1].strip()   # 馬場状況(不良・重・稍重・良)

		# 着順ごとのデータ
		race_result = root.xpath('//table[@class="race_table_01 nk_tb_common"]/tr')[1].text_content().split("\n")
		#pdb.set_trace()

	except Exception as e:
			print e.message


if __name__ == '__main__':
	year_l = [2010]
	#pool = mp.Pool(__PROC__)
	#pool.map(makeHorseDB, year_l)

	for i, year in enumerate(year_l):
		makeHorseDB(year)

	#makeRaceDB()








