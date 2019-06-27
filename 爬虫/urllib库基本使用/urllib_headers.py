import ssl
import urllib.request
import random


context = ssl._create_unverified_context()
url="http://www.baidu.com"

# 注：列表[]支持索引，元祖{}不支持索引
# 可以是User-Agent列表，也可以是代理列表
ua_list=[
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]
# 随机添加/修改User-Agent，在User-Agent列表里随机选择一个User-Agent
user_agent=random.choice(ua_list)

# 构造一个请求
request=urllib.request.Request(url)

# add_header()方法 添加/修改 一个HTTP报头
request.add_header("User-Agent",user_agent)

# get_header() 获取一个已有的HTTP报头的值，注意只能是第一个字母大写，其他的必须小写
request.get_header("User-agent")

response=urllib.request.urlopen(request,context=context)

print(response.read())

# 返回HTTP的状态码，成功返回200，4服务器页面出错，5服务器问题
print(response.getcode())

# 返回实际数据的实际URL，防止重定向问题
print(response.geturl())

# 返回服务器响应的HTTP报头
print(response.info())