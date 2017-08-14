import requests
import xlwt
import datetime
import re
import  os
import xlrd
from bs4 import BeautifulSoup

# os.chdir("/home/yxj/PycharmProjects/test")

def getdate():
    today = datetime.date.today()
    week = today.weekday()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    yesterday = yesterday.strftime('%Y-%m-%d')
    return yesterday



def combile(key,mulu):
    i =1
    # test
    print(mulu[0])
    os.chdir("/home/yxj/PycharmProjects/test/result")
    time = getdate()
    filename = "综合" + time + ".xls"
    workbook = xlwt.Workbook()
    zonghetable = workbook.add_sheet('test', cell_overwrite_ok=True)
    index = ["序号", "网站", "模块", "日期", "新闻标题", "新闻网址", "关键字"]
    for j, k in enumerate(index):
        zonghetable.write(0, j, k)
    filename = os.path.abspath(filename)
    workbook.save(filename)
    for x in mulu:
        data = xlrd.open_workbook(x)
        table = data.sheets()[0]
        for xuhao in range(1,table.nrows):
            str = table.row_values(xuhao)
            for j,index in enumerate(str):
                if j ==0:
                    zonghetable.write(i, j, i)
                if j>0 and j<6:
                    zonghetable.write(i,j,index)
                if j ==6:
                    data = xlrd.open_workbook(key)
                    qiyetable = data.sheets()[0]
                    word = ""
                    for k in range(1,qiyetable.nrows):
                        str1=qiyetable.row(k)[1].value
                        str2=qiyetable.row(k)[2].value
                        print(str1 ,str2)
                        if str1 in index:
                            word = word+str1+ " "
                        if str2 in index:
                            word = word+str2+ " "
                    zonghetable.write(i, j, word)
            i = i +1
            print(str)
    print("successful")
    workbook.save(filename)



def acombile():
    time = getdate()
    mulu = []
    print("start")
    os.chdir("/home/yxj/PycharmProjects/test")
    for x in ["新浪", "人民网", "国际科技", "科学网", "科技世界", "科技新闻"]:
        index = x + '/' + x + time + '.xls'
        index = os.path.abspath(index)
        mulu.append(index)
        print(mulu)
    key = os.path.abspath("企业列表.xlsx")
    combile(key, mulu)


if __name__ == '__main__':
    time = getdate()
    mulu = []
    print("start")
    os.chdir("/home/yxj/PycharmProjects/test")
    for x in ["新浪","人民网","国际科技","科学网","科技世界","科技新闻"]:
        index = x + '/'+x +time+'.xls'
        index = os.path.abspath(index)
        mulu.append(index)
        print(mulu)
    key = os.path.abspath("企业列表.xlsx")
    combile(key,mulu)