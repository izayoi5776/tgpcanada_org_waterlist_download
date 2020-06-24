# coding: UTF-8

import urllib.request, urllib.error
from bs4 import BeautifulSoup
import os
import json

def getdatafromhtml(name, data):
  with open(name) as f:
    print(name)
    soup = BeautifulSoup(f, "html5lib")
    for tr in soup.select('tr'):
      tds = tr.select('td')
      if len(tds) == 1:           
        key = tds[0].get_text().replace('——水情信息', '') # 178——水情信息
      elif len(tds) == 3:
        try:
          t0 = tds[0].get_text()  # title
          t1 = float(tds[1].get_text())  # data
          t2 = tds[2].get_text()  # dd/mm/yyyy
          # [上游水位, 下游水位, 三峡入库, 三峡出库, 时间]
          #print(name + "," + t0 + "," + t1 + "," + t2)
          if t0 == '上游水位':
            if key in data:
              data[key][0] = t1
            else:
              data[key] = [t1, 0, 0, 0, t2]
          elif t0 == '下游水位':
            if key in data:
              data[key][1] = t1
            else:
              data[key] = [0, t1, 0, 0, t2]
          elif t0 == '三峡入库':
            if key in data:
              data[key][2] = t1
            else:
              data[key] = [0, 0, t1, 0, t2]
          elif t0 == '三峡出库':
            if key in data:
              data[key][3] = t1
            else:
              data[key] = [0, 0, 0, t1, t2]
        except Exception as ex:
          #print(ex)
          pass
      #else:
        #print(tr)

if __name__ == '__main__':
  data = {}
  base = os.path.abspath(os.path.dirname(__file__))
  path = os.path.join(base, "html")
  #name = "1.html"
  #getdatafromhtml(os.path.join(path, name), data)
  for name in os.listdir(path):
    if name.endswith(".html"):
      getdatafromhtml(os.path.join(path, name), data)

  with open(os.path.join(base, 'data.json'), 'w') as f:
    print(json.dumps(data), file=f)

