import requests
import xlwt
import datetime
import os
from bs4 import BeautifulSoup


# 使用UTF-8编码
# res.encoding = 'UTF-8'


def get_url(url):
    urls = []
    i = 0
    for suburl in url:
        res = requests.get(suburl)
        res.encoding = 'gb2312'
        soup = BeautifulSoup(res.text, 'html.parser')

        for news in soup.select('.list_16'):
            j=0
            for x in news.select('a'):
                shuju = []
                y = news.select('em')[j].text
                print(y)
                shuju.append(y)
                index = (x['href'])
                title=x.text
                shuju.append(title)
                if index.find("http") == 0:
                    shuju.append(index)
                else:
                    index = "http://scitech.people.com.cn" + index
                    shuju.append(index)
                i = i+1
                j = j+1
                urls.append(shuju)
                print(urls)

    print(urls)
    print(i)
    get_info(urls)


def get_info(urls):
    i =0
    os.chdir("/home/yxj/PycharmProjects/test/人民网")
    data = {}
    today = datetime.date.today()
    week = today.weekday()
    oneday = datetime.timedelta(days=1)
    twoday = datetime.timedelta(days=2)
    threeday = datetime.timedelta(days=3)
    yesterday = today - oneday
    yesterday = yesterday.strftime('%Y-%m-%d')
    qiantian = today - twoday
    qiantian = qiantian.strftime('%Y-%m-%d')
    daqiantian = today - threeday
    daqiantian = daqiantian.strftime('%Y-%m-%d')
    filename = "人民网"+yesterday + ".xls"
    print(filename)
    workbook = xlwt.Workbook()
    table = workbook.add_sheet('test', cell_overwrite_ok=True)
    index = ["序号","网站","模块","日期","新闻标题","新闻网址","新闻内容"]
    for j,k in enumerate(index):
        table.write(i,j,k)
    i = 1
    filename = os.path.abspath(filename)
    workbook.save(filename)
    for url in urls:
        res = requests.get(url[2])
        print(url[2])
        # 使用UTF-8编码
        res.encoding = 'gb2312'
        # 使用剖析器为html.parser
        soup = BeautifulSoup(res.text, 'html.parser')
        print(url[0])
        newstime = url[0]
        if week ==0:
            if newstime == yesterday or newstime == qiantian or newstime ==daqiantian:
                j = 0
                data["xuhao"] = i
                data["website"] = "人民网"
                data["module"] = "科技-滚动"
                data["time"] = newstime
                data["site"] = url[2]
                data["title"] = url[1]
                for wenben in soup.select("#rwb_zw"):
                    wenben = wenben.text
                    wnnben = wenben.strip()
                    wenben.replace("\n", "")
                    wenben.replace(" ", "")
                    data["neirong"] =wenben
                print(data)
                for x in ["xuhao", "website", "module", "time", "title", "site","neirong"]:
                    table.write(i, j, data[x])
                    print(data[x])
                    j = j + 1
                i = i + 1
        else:
            if newstime == yesterday:
                j = 0
                data["xuhao"] = i
                data["website"] = "人民网"
                data["module"] = "科技-滚动"
                data["time"] = newstime
                data["site"] = url[2]
                data["title"] = url[1]
                for wenben in soup.select("#rwb_zw"):
                    print()
                    wenben = wenben.text
                    wnnben = wenben.strip()
                    wenben.replace("\n", "")
                    wenben.replace(" ", "")
                    data["neirong"] =wenben
                print(data)
                for x in ["xuhao","website","module","time","title","site","neirong"]:
                    table.write(i,j,data[x])
                    print(data[x])
                    j = j+1
                i =i +1
    workbook.save(filename)


def people():
    url = []
    url.append('http://scitech.people.com.cn/GB/1057/index.html')
    for k in range(1, 16):
        print(k)
        html = 'http://scitech.people.com.cn/GB/1057/index' + str(k) + '.html'
        print(html)
        url.append(html)
    print(url)
    get_url(url)

if __name__ == '__main__':
    url = []
    url.append('http://scitech.people.com.cn/GB/1057/index.html')
    for k in range(2,3):
        print(k)
        html = 'http://scitech.people.com.cn/GB/1057/index'+str(k)+'.html'
        print(html)
        url.append(html)
    print(url)
    get_url(url)