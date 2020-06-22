# tgpcanada_org_waterlist_download
download tgpcanada.org/waterlist.aspx

# install 

```
pip3 install beautifulsoup4
pip3 install html5lib
```

# run
### step1

```bash
python3 01_getparm.py
```

get result like this. value="xxx" will be used next.

```html
[<input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="xxx"/>]
[<input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="yyy"/>]
<a class="paginator" href="javascript:__doPostBack('AspNetPager1','zzz')">末页</a>
```

### step2


 ```bash
 python3 02_download.py xxx yyy 1 zzz

 ```
1 indicate start page number
zzz indicate last page number last(include)

### step3
Now you have all data in folder `html/*.html`
let's pick it out.

```
python3 03_getdata.py
```

you will get `data.json` as output

