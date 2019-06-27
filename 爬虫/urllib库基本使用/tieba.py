# 批量爬取贴吧数据
import urllib.request
import urllib.parse

def load_page(url,filename):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
        filename : 处理的文件名
    """
    print("正在下载"+filename)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    request=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(request)
    return response.read()

def write_page(html,filename):
    """
       作用：将html内容写入到本地
       html：服务器相应文件内容
    """
    print("正在保存"+filename)
    # 用With管理器不需要做文件关闭操作
    with open(filename,"wb") as f:
        f.write(html)
    print("-"*30)



def tieba_spider(url,begin_page,end_page):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        begin_page : 起始页
        end_page : 结束页
    """
    for page in range(begin_page,end_page+1):
        pn=(page-1)*50

        filename="第"+str(page)+"页.html"
        # 组合为完整的 url，并且pn值每次增加50
        full_url=url+"&pn="+str(pn)
        # print(full_url)

        # 调用loadPage()发送请求获取HTML页面
        html=load_page(full_url,filename)
        # 将获取到的HTML页面写入本地磁盘文件
        # print(html)
        write_page(html,filename)
        print("谢谢使用")


if __name__=="__main__":
    kw=input("请输入需要爬取的贴吧：")
    # 输入起始页和终止页，str转成int类型
    begin_page=int(input("请输入起始页："))
    end_page=int(input("请输入结束页："))

    url="http://tieba.baidu.com/f?"
    key=urllib.parse.urlencode({"kw":kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url=url+key
    tieba_spider(url,begin_page,end_page)