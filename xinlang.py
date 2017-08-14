import requests
import xlwt
import os
import datetime
from bs4 import BeautifulSoup


# 使用UTF-8编码
# res.encoding = 'UTF-8'


def get_url(url):
    res = requests.get(url)
    res.encoding = 'UTF-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    urls = []
    for news in soup.select('.news-item'):
        print("hghjgjhgjh")
        # print("444444444")
        h2 = news.select('h2')
        # 只选择长度大于0的结果
        if len(h2) > 0:
            title = h2[0].text
            # 新闻链接
            href = h2[0].select('a')[0]['href']
            # 打印
            print(href)
            urls.append(href)
    print(urls)
    get_info(urls)


def get_info(urls):
    i =0
    os.chdir("/home/yxj/PycharmProjects/test/新浪")
    data = {}
    today = datetime.date.today()
    week = today.weekday()
    oneday = datetime.timedelta(days=1)
    twoday = datetime.timedelta(days=2)
    threeday = datetime.timedelta(days=3)
    yesterday = today - oneday
    filename = yesterday.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y年%m月%d日')
    qiantian = today - twoday
    daqiantian = today -threeday
    qiantian = qiantian.strftime('%Y年%m月%d日')
    daqiantian = daqiantian.strftime('%Y年%m月%d日')
    filename = "新浪"+filename + ".xls"
    print(filename)
    workbook = xlwt.Workbook()
    table = workbook.add_sheet('test', cell_overwrite_ok=True)
    index = ["序号","网站","模块","日期","新闻标题","新闻网址","新闻内容"]
    for j,k in enumerate(index):
        table.write(i,j,k)
    i = 1
    filename=os.path.abspath(filename)  #绝对路径
    # m=os.path.dirname(filename) #相对路径
    # print(m)
    # print(n)
    # workbook.save(filename)
    for url in urls:
        res = requests.get(url)
        # 使用UTF-8编码
        res.encoding = 'UTF-8'
        # 使用剖析器为html.parser
        soup = BeautifulSoup(res.text, 'html.parser')
        # 遍历每一个class=news-item的节点
        # print(soup)
        for news in soup.select('.titer'):
            newstime = news.text
            newstime = newstime[0:11]
            print(newstime)
        if week == 0:
            if newstime == yesterday or newstime == qiantian or newstime == daqiantian:
                j = 0
                data["xuhao"] = i
                data["website"] = "新浪科技"
                data["module"] = "科学探索-科技前沿"
                data["time"] = newstime
                data["site"] = url
                for title in soup.select("#main_title"):
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
                data["website"] = "新浪科技"
                data["module"] = "科学探索-科技前沿"
                data["time"] = newstime
                data["site"] = url
                for title in soup.select("#main_title"):
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

def xinlang():
    url = 'http://tech.sina.com.cn/discovery/invention/'
    get_url(url)

if __name__ == '__main__':
    url = 'http://tech.sina.com.cn/discovery/invention/'
    get_url(url)