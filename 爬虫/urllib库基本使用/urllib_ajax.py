# AJAX方式加载的页面，数据来源一定是json
# 拿到json,就是拿到了网页的数据

import ssl
import urllib.request
import urllib.parse

context = ssl._create_unverified_context()

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"20"
    }

data = urllib.parse.urlencode(formdata)
request=urllib.request.Request(url,data=data.encode(encoding='utf8'),headers=headers)
response=urllib.request.urlopen(request,context=context)

print(response.read())