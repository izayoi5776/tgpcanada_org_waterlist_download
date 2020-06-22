# tgpcanada_org_waterlist_download
download tgpcanada.org/waterlist.aspx

# install 

```
pip3 install beautifulsoup4
pip3 install html5lib
```

# run

```bash
python3 01_getparm.py
```

get result like this. value="xxx" will be used next.

```html
[<input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="xxxxxx"/>]
[<input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="yyyyyy"/>]
<a class="paginator" href="javascript:__doPostBack('AspNetPager1','zzz')">末页</a>
```

then

 ```bash
 python3 02_download.py xxxxxx yyyyyy 1 zzz

 ```
 xxxxxx, yyyyyy from 01 result
 1 means start page number
 zzz indicate last page number last(include)
