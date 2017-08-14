import requests
import xlwt
import datetime
import os
from bs4 import BeautifulSoup


# 使用UTF-8编码
# res.encoding = 'UTF-8'


def get_url(url):
    res = requests.get(url)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    urls = []
    i = 0
    for news in soup.select('.fp_subtitle'):
        print(news)
        index = news.select('a')[0]['href']
        if index.find("http")==0:
            urls.append(index)
        else:
            index = "http://www.stdaily.com"+index
            urls.append(index)
        i = i+1
    print(urls)
    print(i)
    get_info(urls)


def get_info(urls):
    i =0
    os.chdir("/home/yxj/PycharmProjects/test/科技新闻")
    data = {}
    today = datetime.date.today()
    week = today.weekday()
    oneday = datetime.timedelta(days=1)
    twoday = datetime.timedelta(days=2)
    threeday = datetime.timedelta(days=3)
    yesterday = today - oneday
    yesterday = yesterday.strftime('%Y-%m-%d')
    qiantian = today - twoday
    daqiantian = today -threeday
    qiantian = qiantian.strftime('%Y-%m-%d')
    daqiantian = daqiantian.strftime('%Y-%m-%d')
    filename = "科技新闻"+yesterday + ".xls"
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
        res = requests.get(url)
        # 使用UTF-8编码
        res.encoding = 'UTF-8'
        # 使用剖析器为html.parser
        soup = BeautifulSoup(res.text, 'html.parser')
        # 遍历每一个class=news-item的节点
        # print(soup)
        for news in soup.select('.time'):
            newstime = news.text
            newstime =newstime[8:18]
            print(newstime)
        if week == 0:
            if newstime == yesterday or newstime == qiantian or newstime ==daqiantian:
                j = 0
                data["xuhao"] = i
                data["website"] = "中国科技网"
                data["module"] = "科技新闻频道"
                data["time"] = newstime
                data["site"] = url
                for title in soup.select("h1"):
                    print(title.text)
                    title = title.text
                    data["title"] = title
                for wenben in soup.select(".content"):
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
                data["website"] = "中国科技网"
                data["module"] = "科技新闻频道"
                data["time"] = newstime
                data["site"] = url
                for title in soup.select("h1"):
                    print(title.text)
                    title = title.text
                    data["title"] = title
                for wenben in soup.select(".content"):
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


def technews():
    url = 'http://www.stdaily.com/cxzg80/index.shtml'
    get_url(url)

if __name__ == '__main__':
    url = 'http://www.stdaily.com/cxzg80/index.shtml'
    get_url(url)