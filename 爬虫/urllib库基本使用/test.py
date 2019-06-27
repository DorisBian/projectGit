import ssl
import urllib.request

# 使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
context = ssl._create_unverified_context()

ua_header={"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
request=urllib.request.Request("http://www.baidu.com/",headers=ua_header)
response=urllib.request.urlopen(request,context=context)
print(response.read())

# 返回HTTP的状态码，成功返回200，4服务器页面出错，5服务器问题
print(response.getcode())

# 返回实际数据的实际URL，防止重定向问题
print(response.geturl())

# 返回服务器响应的HTTP报头
print(response.info())