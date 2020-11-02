import os
from uty.weather import qrypm25

dict_temp = {}
try:
  with open('citys.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        name = line.split(' ')[0]
        date = line.split(' ')[1].strip()
        dict_temp[name] = date
except Exception as e:
    print('讀取失敗')
    exit()

cityname = str(input("請輸入您想查詢 PM2.5 的城市:")).strip()
while cityname != "":
  qrypm25(dict_temp,cityname)
  cityname = str(input("請輸入您想查詢 PM2.5 的城市:")).strip()
f.close()