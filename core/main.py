import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from datetime import datetime
from db.db.conn import Conn
from models.company_news import CompanyNews
import client.news_feed as news_feed_client
import utils.companies as companies
import utils.company_news as company_news
import utils.watchlist as watchlist
import apns.apns as apns
import asyncio

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

watchlist_company_symbols = watchlist.get_company_symbols(conn=conn)
for company_symbol in watchlist_company_symbols:
    news_feed = news_feed_client.get_recent_news(company_symbol=company_symbol)
    exchange = companies.get_exchange(conn=conn, company_symbol=company_symbol)
    title = news_feed["title"]
    company_name = news_feed["investegate_company"]
    headline = news_feed["investegate_headline"]
    pub_date = news_feed["published"]
    link = news_feed["link"]

    companyNews = CompanyNews(
        title=title,
        company_symbol=company_symbol,
        company_name=company_name,
        exchange=exchange,
        headline=headline,
        pub_date=pub_date,
        link=link,
    )

    company_news_exists = company_news.news_exists(
        conn=conn, company_symbol=company_symbol, pub_date=pub_date
    )

    if company_news_exists:
        print(f"INFO: no news: {company_symbol} - {pub_date}")
    else:
        print(f"INFO: breaking news!: {company_symbol} - {pub_date}")
        company_news.delete_news_of(conn=conn, company_symbol=company_symbol)
        company_news.insert_news(
            conn=conn, company_symbol=company_symbol, pub_date=pub_date, title=title
        )
        formated_pub_date = datetime.strptime(pub_date, "%d %b, %Y %H:%M:%S").date()
        today = datetime.today().date()
        if formated_pub_date == today:
            device_tokens = watchlist.get_device_tokens_of(
                conn=conn, company_symbol=company_symbol
            )
            for device_token in device_tokens:
                print(f"INFO: sending notifications to {device_token}")
                loop = asyncio.get_event_loop()
                loop.run_until_complete(apns.run(device_token, companyNews))


conn.close()
