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
def fixDataAfter941(data, data2, fmt):
  keys = list(data.keys())
  keys.sort(key=float)
  for i in range(941, int(keys[len(keys)-1])+1):
    try:
      d = data[str(i)]
      dt = datetime.strptime(d[4], '%d/%m/%Y')
      data2[dt.strftime(fmt)] = [i, d[0], d[1], d[2], d[3]]
    except KeyError:
      pass
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

def fixDataBefore941(data, data2, fmt):
  dt = date(2015, 8, 1)  # for key 941
  for i in range(940, 0, -1):
    dt = dt + timedelta(days=-1)
    try:
      d = data[str(i)]
      dt = fixDate(dt, d[4][0:2], i)           # '31日20时'

      data2[dt.strftime(fmt)] = [i, d[0], d[1], d[2], d[3]]
      #print(str(i) + " " + str(d))
    except Exception as ex:
      print("skip i=" + str(i) + " ex=" + str(sys.exc_info()))
      pass

def fixDataLost(data2, fmt):
  '''
  add lost date
  '''
  keys = list(data2.keys())
  keys.sort()
  dt = date(datetime.strptime(keys[0], fmt).year, 1, 1)
  end  = datetime.strptime(keys[len(keys)-1], fmt).date()
  last = [-1, 0, 0, 0, 0]
  while dt < end:
    key = dt.strftime(fmt)
    if key in data2:
      if data2[key][1] == 0:
        data2[key][1] = last[1]
      if data2[key][2] == 0:
        data2[key][2] = last[2]
      if data2[key][3] == 0:
        data2[key][3] = last[3]
      if data2[key][4] == 0:
        data2[key][4] = last[4]
      last = data2[key]
    else:
      data2[key] = last
      data2[key][0] = -1


    dt = dt + timedelta(days=1)

def saveData(data2):
  '''
  # OUTPUT data2.json FORMAT
  {
    "yyyy-mm-dd": [水情信息回次, 上游水位, 下游水位, 三峡入库, 三峡出库],
  }
  '''
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


if __name__ == '__main__':
  with open('data.json') as f:
    '''
    # INPUT data.json FORMAT
    {
      "水情信息": [上游水位, 下游水位, 三峡入库, 三峡出库, "时间"],
    }
    '''
    data = json.load(f)

  #print(json.dumps(data))
  #for i in data:
  #  print("'" + i + "':" + str(data[i]))
  
  data2 = {}
  fmt = '%Y-%m-%d'

  fixDataAfter941(data, data2, fmt)
  fixDataBefore941(data, data2)
  fixDataLost(data2, fmt)
  saveData(data2)

