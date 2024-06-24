# 파이썬 뉴스기사 크롤링
import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def main(keyword):

    url = "https://news.google.com/search?q=" + keyword + "=ko&gl=KR&ceid=KR%3Ako"

    try:

        with requests.Session() as s:
            r = s.get(url)
            soup = BeautifulSoup(r.text, "lxml")
            # print(soup)

            news_clipping = data_extract(soup)

            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")
                print()

    except HTTPError as e:
        print(e.code)


def data_extract(soup):

    articles = soup.select("div.UW0SDc article")
    base_url = "https://news.google.com"

    news = []
    news_items = {}

    for article in articles:
        # print(article)

        # 제목을 가지고 있는 요소 찾기
        link_title = article.select_one("div > div:nth-child(2) a")

        # print(link_title)

        # 제목 추출
        news_items["title"] = link_title.text

        # 뉴스기사 링크 추출
        news_items["href"] = base_url + link_title["href"][1:]

        # 작성자
        news_items["writer"] = article.select_one("div.a7P8l > div").text

        # 작성일자와 시간 2024-04-19T07:00:00Z
        # T 기준으로 분리
        report_date_time = article.select_one("time")
        # <time class="hvbAAd" datetime="2024-04-19T07:00:00Z">4월 19일</time>

        if report_date_time:
            # ['2024-04-19', '07:00:00Z']
            report_date_time = report_date_time["datetime"].split("T")
            news_items["report_date"] = report_date_time[0]
            news_items["report_time"] = report_date_time[1]
        else:
            news_items["report_date"] = ""
            news_items["report_time"] = ""

        # print(title, href, writer, report_date, report_time)

        news.append(news_items)
        news_items = {}

    # 확인
    print(news[:3])
    return news


# [
#     {"title":"오픈소스 커뮤니티 노리는 공급망 공격, 국내 연구팀 기술로 차단한다",
#      "href" : "",
#      "writer":"IT World",
#      "report_date":
#      "report_tite"
#      }

# ]

if __name__ == "__main__":
    main("아이폰")
