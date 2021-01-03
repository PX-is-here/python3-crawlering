#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:07:59 2021

@author: chloelu
"""

# 繪製折線圖 (Line Chart)
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = './Crawler/MI_30MINS_outputs.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    listCsv = list(csvReader)
    csvData = listCsv[1:] 
    times, items = [], [] ; # 設定為空字串
    for row in csvData:
        try:
            time = row[0] ; # 時間
            item = row[1] ; # 累積成交量
        except Exception:
            print('missing value...')
        else:
            times.append(time) ; # 儲存時間
            items.append(item) ; # 儲存累積成交量
            
fig = plt.figure(dpi=100, figsize=(12,8))
plt.plot(times, items, '-*')
fig.autofmt_xdate()
plt.title("Accumulated deal erery 30 mins", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Accumulated deal", fontsize=14)
plt.tick_params(axis="both", labelsize=12, color='blue')
plt.show()
