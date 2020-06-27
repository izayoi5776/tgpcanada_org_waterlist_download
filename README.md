# Demo
check [here](https://izayoi5776.github.io/tgpcanada_org_waterlist_download/) to view result online



# get data yourself

If you want get data youself, 
### install 

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

### step4

fix date format, then you got `data2.json`, and `data2.csv`
```
python3 04_cleardata.py
```

### step5
run update every day
```
python3 05_update.py
```

### use c3 to load and show 

- json should use double quote

-----

# 追加分析

[demo page](demo2.html)

### install
```
pip3 install pandas
```

### 水库截面积

