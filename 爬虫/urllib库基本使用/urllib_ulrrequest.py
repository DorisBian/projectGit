# 导入urllib.request库
import urllib.request

# 通过urllib.request.Request()方法构造一个请求对象并返回对象
request=urllib.request.Request("http://www.baidu.com")

# Request对象作为urlopen()方法的参数，发送给服务器并接收响应
response=urllib.request.urlopen(request)

html=response.read()

print(html)

