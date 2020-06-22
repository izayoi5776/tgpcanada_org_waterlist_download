# coding: UTF-8
import urllib.request, urllib.error
import os
import sys
import time

def downloadHtml(vs, vsg, n):
  url = "http://tgpcanada.org/waterlist.aspx"
  path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "html")
  name = os.path.join(path, str(n) + ".html")

  os.makedirs(path, exist_ok=True)
  ret = ""
  if os.path.exists(name):
    print("skip     " + url + " => " + name)
  else:
    try:
      values = {
        "__VIEWSTATE": vs,
        "__VIEWSTATEGENERATOR": vsg,
        "__EVENTTARGET": "AspNetPager1",
        "__EVENTARGUMENT": n,
        "AspNetPager1_input": n-1,
      }
      data = urllib.parse.urlencode(values)
      data = data.encode('ascii') # data should be bytes
      req = urllib.request.urlretrieve(url, name, data=data)

      print("download " + url + " => " + name)
      time.sleep(1)
    except Exception as ex:
      #print("download " + url + " -- FAILED")
      print(ex)


'''
download 
'''
if __name__ == '__main__':
  for n in range(int(sys.argv[3]), int(sys.argv[4])+1):
    downloadHtml(sys.argv[1], sys.argv[2], n)



