## -*- coding: utf-8 -*-

import os
import json
from datetime import date
from datetime import timedelta
from datetime import datetime
import sys

def genData3(data2, keystart, keyend, data3):
  '''
    [开始高度，终了高度，开始日期，终了日期，时间秒, 流速, 体积, 截面积]
  '''
  rec = [0, 0, 0, '', '', 0, 0, 0]
  try:
    d1 = data2[keystart]
    d2 = data2[keyend]
    rec[0] = d1[1]
    rec[1] = d2[1]
    rec[2] = keystart
    rec[3] = keyend
    rec[4] = (date.fromisoformat(keyend) - date.fromisoformat(keystart)).total_seconds() # 时间秒
    rec[5] = (d1[3] + d2[3] - d1[4] - d2[4]) / 2 # 流速
    rec[6] = rec[5] * rec[4]                     # 体积 = 流速 x 时间秒
    rec[7] = abs(rec[6] / (rec[1] - rec[0]))     # 截面积
    #print("getData3() keystart=" + keystart + " keyend=" + keyend)
    data3.append(rec)
  except:
    pass

def compOneLine(d, yyyy, data4):
  keystart = str(d[0])  # 开始高度
  d4 = {}
  if yyyy in data4:
    d4 = data4[yyyy]
    if keystart in d4:
      t = d4[keystart]
      t[0] += d[7] # 先算和，最后再除次数，避免累积计算误差
      t[1] += 1
    else:
      d4[keystart] = [
        d[7],
        1
      ]
  else:
    data4[yyyy] = {
      str(keystart):[
        d[7],
        1
      ]
    }

def fixData3(data3, data4):
  '''
  yyyy:{
    开始高度:[
      截面积(平均),
      次数
    ]
  }
  '''
  for d in data3:
    compOneLine(d, d[2][0:4], data4)
    compOneLine(d, 'all', data4)

  # 求平均
  for yyyy in data4:
    for keystart in data4[yyyy]:
      a = data4[yyyy][keystart][0]
      n = data4[yyyy][keystart][1]
      data4[yyyy][keystart][0] = a / n / 1000000  # 单位变为平方公里

  #for d in data4:
  #  print("\"" + str(d) + "\":", end='')
  #  print(data4[d])

def save2csv(data4):
  yearall = 'all'
  keys = list(data4[yearall].keys())
  keys.sort()
  with open('data3.csv', 'w') as f:
    # head
    print('x' + ',', end='', file=f)
    for key in keys:
      print(str(key) + ',', end='', file=f)
    print('', file=f)

    # all
    print(yearall + ',', end='', file=f)
    for key in keys:
      print(str(data4[yearall][key][0]) + ',', end='', file=f)
    print('', file=f)

    # each year
    for yyyy in data4:
      if yyyy=='all':
        pass
      else:
        print(yyyy + ',', end='', file=f)
        for key in keys:
          t = ''
          if key in data4[yyyy]:
            t = str(data4[yyyy][key][0])
          print(t + ',', end='', file=f)
        print('', file=f)

# c3要求csv是列方向的
def save2csvCol(data4):
  yearall = 'all'
  keys = list(data4[yearall].keys())
  keys.sort()
  with open('data3.csv', 'w') as f:
    # head
    print('x' + ',', end='', file=f)
    for d in data4:
      print(str(d) + ',', end='', file=f)
    print('', file=f)

    # data
    for key in keys:
      print(key + ',', end='', file=f)
      for yyyy in data4:
        t = ''
        if key in data4[yyyy]:
          t = str(data4[yyyy][key][0])
        print(t + ',', end='', file=f)
      print('', file=f)



if __name__ == '__main__':
  '''
  # INPUT data2.json FORMAT
  {
    "yyyy-mm-dd": [水情信息回次, 上游水位, 下游水位, 三峡入库, 三峡出库, 修正数据标记],
  }
  '''
  data2 = {}
  with open('data2.json') as f:
    data2 = json.load(f)

  keys = list(data2.keys())
  keys.sort()

  data3 = []
  keystart = ''
  #keyend = ''
  for key in keys:
    #print(key + " " + str(data2[key]))
    dt2cur = data2[key]
    if dt2cur[0] == -1 or (dt2cur[5]!="" and dt2cur[5]!="2"):
      # 修补过的数据不要，但是不计算下游水位，所以欠损2数据没关系
      pass
    else:
      if keystart=='':
        keystart = key
      else:
        #keyend = key
        genData3(data2, keystart, key, data3)
        keystart = ''
      pass

  data4 = {}
  fixData3(data3, data4)
  save2csvCol(data4)
  #with open('data3.csv', 'w') as f:
  #  for d in data3:
  #   print(str(d[0]) + ',', end='', file=f)
  # print('', file=f)
  #  for d in data3:
  #    print(str(d[7]) + ',', end='', file=f)
  #  print('', file=f)

  #for d in data4:
  #  print(d + "=" + str(data4[d]))