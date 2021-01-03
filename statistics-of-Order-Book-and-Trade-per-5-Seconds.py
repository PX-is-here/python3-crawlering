#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 23:11:16 2020

@author: chloelu
"""

import csv

fn = '../src/MI_5MINS_20201229.csv'
outputs = './MI_30MINS_outputs.csv'
with open(outputs, 'w', newline = '') as csvOut:
    csvWriter = csv.writer(csvOut)
    csvWriter.writerow(["Time", "Acc. Transaction"])
    with open(fn) as csvFile:
        csvReader = csv.reader(csvFile)
        listCsv = list(csvReader)
        csvData = listCsv[2:-8]
        for row in csvData:
            xmin = row[0][3:5]                  # 分
            xsec = row[0][6:]                   # 秒
            if xmin == '00' or xmin == '30':    # 每30mins
                if xsec == '00':                # True 時寫入時間和累積成交數
                    csvWriter.writerow([row[0], row[6]])