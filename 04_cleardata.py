## -*- coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import os
import json
from datetime import date
from datetime import timedelta
from datetime import datetime
import sys

# 从 914 开始的 data 是带有 dd/mm/yyyy 日期的
# 去重复
def fixDataAfter941(data, data2):
  keys = list(data.keys())
  keys.sort(key=float)
  for i in range(941, int(keys[len(keys)-1])+1):
    try:
      d = data[str(i)]
      dt = datetime.strptime(d[4], '%d/%m/%Y')
      data2[dt.strftime('%Y-%m-%d')] = [i, d[0], d[1], d[2], d[3]]
    except Exception as ex:
      print("skip i=" + str(i) + " ex=" + str(sys.exc_info()))
      pass

# 日付調整
def fixDate(dt, day, key):
  dt1 = dt
  while dt1.day != int(day):
    dt1 = dt1 + timedelta(days=1)
  dt2 = dt
  while dt2.day != int(day):
    dt2 = dt2 + timedelta(days=-1)

  if dt1 - dt > dt - dt2:
    ret = dt2
  else:
    ret = dt1
  if ret != dt:
    print(str(key) + " fixDate " + str(dt) + " to " + str(ret))
  return ret

def fixDataBefore941(data, data2):
  dt = date(2015, 8, 1)  # for key 941
  for i in range(940, 0, -1):
    dt = dt + timedelta(days=-1)
    try:
      d = data[str(i)]
      dt = fixDate(dt, d[4][0:2], i)           # '31日20时'

      data2[dt.strftime('%Y-%m-%d')] = [i, d[0], d[1], d[2], d[3]]
      #print(str(i) + " " + str(d))
    except Exception as ex:
      print("skip i=" + str(i) + " ex=" + str(sys.exc_info()))
      pass

if __name__ == '__main__':
  with open('data.json') as f:
    data = json.load(f)

  #print(json.dumps(data))
  #for i in data:
  #  print("'" + i + "':" + str(data[i]))
  
  data2 = {}
  fixDataAfter941(data, data2)
  fixDataBefore941(data, data2)
  keys = list(data2.keys())
  keys.sort()
  with open('data2.json', 'w') as f:
    print(json.dumps(data2, sort_keys=True, indent=2), file=f)

  with open('data2.csv', 'w') as f:
    for i in keys:
      print(i + ",", end='', file=f)
    print('', file=f)
    for i in range(0,5):
      for key in keys:
        print(str(data2[key][i]) + ',', end='', file=f)
      print('', file=f)


