import requests
from bs4 import BeautifulSoup

query_word = '王晓晨'
news_base_url = 'http://news.baidu.com/ns?tn=news'

news_url = news_base_url + query_word
parameters = {'word': query_word}

# 获取 JSON 数据
r = requests.get(news_base_url, params=parameters)
# print(r.url)

soup = BeautifulSoup(r.text, 'lxml')
news_html_list = soup.select('div.result')
news_list = []
for news_html in news_html_list:
    news = {}
    news['标题'] = news_html.a.get_text().strip()
    news['链接'] = news_html.a['href']
    source = news_html.find('p', 'c-author').get_text().strip().replace('\xa0\xa0', ' ').split(' ')
    news['来源'] = source[0]
    news['发布日期'] = source[1]

    news_list.append(news)

for news in news_list:
    print(news)
