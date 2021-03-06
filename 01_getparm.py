# coding: UTF-8

import urllib.request, urllib.error
from bs4 import BeautifulSoup


def printHeader(soup):
    #print(soup.find_all('input#__VIEWSTATE'))
    print(soup.select('input#__VIEWSTATE'))
    print(soup.select('input#__VIEWSTATEGENERATOR'))
    tags = soup.select('a.paginator');
    print(tags[len(tags)-1])

def getPage1():
  url = "http://tgpcanada.org/waterlist.aspx"
  with urllib.request.urlopen(url) as res:
    html = res.read()
    soup = BeautifulSoup(html, "html5lib")
    return soup

if __name__ == '__main__':
  soup = getPage1()
  printHeader(soup)

