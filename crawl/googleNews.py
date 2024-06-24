# 파이썬으로 뉴스기사 출력
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
from xlxx_write import write_excel_template

from datetime import datetime


def main():
    url = "https://news.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&hl=ko&gl=KR&ceid=KR%3Ako"
    try:
        with requests.Session() as s:
            r =  s.get(url)
            soup = BeautifulSoup(r.text, "lxml")

            news_clliping = data_extract(soup)
            for news in news_clliping:
                for k,v in news.items():
                    print(f"{k}: {v}")
    except HTTPError as e:
        print(e.code)
    
def data_extract(soup):
    #yDmH0d > c-wiz:nth-child(25) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(1) > c-wiz > article
    base_url = "https://news.google.com/"
    articles = soup.select("div.UW0SDc article")
    # print(article)
    # for html in article:
    #     print(html)
    news = []
    for article in articles:

        link_title = article.select_one("div > div:nth-child(2) a")
        # print(link_title)

        # 제목 추출
        title = link_title.text

        href =base_url + link_title["href"][1:]

        # 회사
        # article > div.m5k28 > div.B6pJDd > div > div > div.oovtQ > div > div
        company = article.select_one("div.m5k28 > div.B6pJDd > div > div > div.oovtQ > div > div").text

        # 시간
        #yDmH0d > c-wiz:nth-child(25) > div > main > c-wiz > c-wiz > c-wiz:nth-child(21) > c-wiz > article > div.UOVeFe > time
        time = article.select_one("time")
        if time:
            time = time["datetime"].split("T")
            report_date = time[0]
            report_time = time[1]
        else:
            report_date = ""
            report_time = ""

        # print(f"기사제목 : {title} \n 링크 : {href} ")
        # print(f"회사 :{company}")
        # print(f"날짜 : {report_date} 시간 : {report_time}")
        
        news.append({"title" : title, "href" : href, "writer" :company, "report_date": report_date, "report_time" :report_time})
    print(news[:3])
    return news
    
main()

    
      
