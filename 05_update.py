## -*- coding: utf-8 -*-

import os
import json
from datetime import date
from datetime import timedelta
from datetime import datetime
import sys

s1 = __import__('01_getparm')
s3 = __import__('03_getdata')
s4 = __import__('04_cleardata')

if __name__ == '__main__':
  data = {}
  soup = s1.getPage1()
  s3.getDataFromSoup(soup, data)
  #print(data)

  data2 = {}
  with open('data2.json') as f:
    data2 = json.load(f)

  fmt = '%Y-%m-%d'
  s4.fixDataAfter941(data, data2, fmt)
  s4.fixDataLost(data2, fmt)
  s4.saveData(data2)
  #print(data2)

