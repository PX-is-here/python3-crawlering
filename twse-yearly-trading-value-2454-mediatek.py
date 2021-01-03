#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:18:56 2020

@author: chloelu
"""

import csv
import matplotlib.pyplot as plt
#from datetime import datetime

fn = '../src/FMNPTK_2454.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile) ; # 讀檔案, 建立Reader物件csvReader
    listCsv = list(csvReader) ; # 轉成串列
    csvData = listCsv[2:-5] ; # slice 掉非交易資訊
    years, highs, lows, prices = [], [], [], [] ; # 設定空串列
    for row in csvData:
        try:
            year = int(row[0])
            high = float(row[4]) ; # 設定最高價
            low = float(row[6]) ; # 設定最低價
            price = float(row[8]) ; # 設定收盤平均價
        except Exception:
            print ('missing value')
        else:
            highs.append(high)
            lows.append(low)
            prices.append(price)
            years.append(year)

fig = plt.figure(dpi=80, figsize=(12,8)) ; # 設定繪圖區
plt.plot(years, highs, '-*', label='High') ; # 繪製最高價
plt.plot(years, lows, '-o', label='Low') ; # 繪製最低價
plt.plot(years, prices, '-^', label='Price') ; # 繪製收盤平均價
plt.legend(loc='best')
fig.autofmt_xdate() ; # 日期旋轉 30度左右
plt.title("Mediatek", fontsize=20)
plt.xlabel("", fontsize=14)
plt.ylabel("Price", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()

            
