import requests
import xlwt
import datetime
import re
import os
from bs4 import BeautifulSoup


# 使用UTF-8编码
# res.encoding = 'UTF-8'


def get_url(url):
    urls = []
    i = 0
    titleset= []
    for suburl in url:
        res = requests.get(suburl)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        for news in soup.find_all(href=re.compile("/htmlnews")):
            try:
                print(news['href'])
                index = news['href']
            except  Exception as e:
                # print(e)
                continue
            index = "http://news.sciencenet.cn" + index
            title = news.text
            title = title.strip()
            print(title)
            titleset.append(title)
            urls.append(index)

    print(urls)
    print(titleset)
    print(i)
    get_info(urls,titleset)


def get_info(urls,titleset):
    i = 0
    jishu = 0
    os.chdir("/home/yxj/PycharmProjects/test/科学网")
    data = {}
    today = datetime.date.today()
    week = today.weekday()
    oneday = datetime.timedelta(days=1)
    twoday = datetime.timedelta(days=2)
    threeday = datetime.timedelta(days=3)
    yesterday = today - oneday
    filename = yesterday.strftime('%Y-%m-%d')
    yesterday = yesterday.strftime('%Y/%-m/%-d')
    qiantian = today - twoday
    qiantian = qiantian.strftime('%Y/%-m/%-d')
    daqiantian = today - threeday
    daqiantian = daqiantian.strftime('%Y/%-m/%-d')
    filename = "科学网" + filename + ".xls"
    print(filename)
    workbook = xlwt.Workbook()
    table = workbook.add_sheet('test', cell_overwrite_ok=True)
    index = ["序号", "网站", "模块", "日期", "新闻标题", "新闻网址","新闻内容"]
    for j, k in enumerate(index):
        table.write(i, j, k)
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
        for newstime in soup.find_all(text=re.compile("发布时间")):
            newstime = newstime[6:14]
            print(newstime)
            print(yesterday)
            print(qiantian)
        if week == 0:
            if newstime == yesterday or newstime == qiantian or newstime == daqiantian:
                j = 0
                str =""
                data["xuhao"] = i
                data["website"] = "科学网"
                data["module"] = "每日全部咨询"
                data["time"] = newstime
                data["site"] = url
                data["title"] = titleset[jishu]
                for wenben in soup.select('div[id="content1"] p'):
                    wenben = wenben.text
                    wnnben = wenben.strip()
                    wenben.replace("\n", "")
                    wenben.replace(" ", "")
                    str = str + wenben
                data["neirong"] =str
                print(data)
                for x in ["xuhao", "website", "module", "time", "title", "site","neirong"]:
                    table.write(i, j, data[x])
                    print(data[x])
                    j = j + 1
                i = i + 1
        else:
            if newstime == yesterday:
                j = 0
                str =""
                data["xuhao"] = i
                data["website"] = "科学网"
                data["module"] = "每日全部咨询"
                data["time"] = newstime
                data["site"] = url
                data["title"] = titleset[jishu]
                for wenben in soup.select('div[id="content1"] p'):
                    wenben = wenben.text
                    wnnben = wenben.strip()
                    wenben.replace("\n", "")
                    wenben.replace(" ", "")
                    str = str + wenben
                data["neirong"] =str
                print(data)
                for x in ["xuhao", "website", "module", "time", "title", "site","neirong"]:
                    table.write(i, j, data[x])
                    print(data[x])
                    j = j + 1
                i = i + 1
        jishu = jishu +1
    workbook.save(filename)


def tech():
    url = []
    for k in range(1, 10):
        print(k)
        html = 'http://news.sciencenet.cn/todaynews-' + str(k) + '.aspx'
        print(html)
        url.append(html)
    #
    # res = requests.get(url)
    # res.encoding = 'gb2312'
    get_url(url)

if __name__ == '__main__':
    url = []
    for k in range(1,10):
        print(k)
        html = 'http://news.sciencenet.cn/todaynews-'+str(k)+'.aspx'
        print(html)
        url.append(html)
    #
    # res = requests.get(url)
    # res.encoding = 'gb2312'
    get_url(url)