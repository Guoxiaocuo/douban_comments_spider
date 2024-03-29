import random
from bs4 import BeautifulSoup #解析包
import requests #请求包
import pandas as pd
import json
import time # 设置休眠时间，控制爬虫频率
User_Agents =[
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
]
allinfo = []
urls = ['https://movie.douban.com/subject/26354336/comments?start={}&limit=20&sort=new_score&status=P&comments_only=1'.format(number) for number in range(0,220,20)]
def getinfo(url):
    selnumber_data = []
    seltime_data = []
    selname_data = []
    selcomment_data = []
    for i in range(1, 21):
        selnumbers = '#comments > div:nth-child(' + str(i) + ') > div.comment > h3 > span.comment-vote'
        selnumber_data.append(selnumbers)
    for i in range(1, 21):
        seltimes = '#comments > div:nth-child(' + str(
            i) + ') > div.comment > h3 > span.comment-info > span.comment-time'
        seltime_data.append(seltimes)
    for i in range(1, 21):
        selnames = '#comments > div:nth-child(' + str(i) + ') > div.comment > h3 > span.comment-info > a'
        selname_data.append(selnames)
    for i in range(1, 21):
        selcomments = '#comments > div:nth-child(' + str(i) + ') > div.comment > p > span'
        selcomment_data.append(selcomments)
    for i in range(0, 20):
        wdata = requests.get(url, headers={'User-Agent': random.choice(User_Agents)})
        wsoup = BeautifulSoup(wdata.text, 'lxml')
        numbers = wsoup.select(selnumber_data[i])
        times = wsoup.select(seltime_data[i])
        names = wsoup.select(selname_data[i])
        comments = wsoup.select(selcomment_data[i])
        info = {
            'name': names[0].get_text() if names else "",
            'number': numbers[0].get_text() if numbers else "",
            'time': times[0].get_text() if times else "",
            'comment': comments[0].get_text() if comments else ""
        }
        allinfo.append(info)
        df = pd.DataFrame(allinfo)
        df.to_excel('jueji_douban.xlsx', sheet_name='Sheet1')
for url in urls:
    print(url)
    getinfo(url)
    seconds = random.uniform(3,4)
    time.sleep(seconds)