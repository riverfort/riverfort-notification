from db_config.connection import DatabaseConnection
from company_news import (
    is_latest_news_in_db,
    delete_recent_company_news,
    add_latest_news_to_db,
    CompanyNews,
)
from companies import fetch_exchange_of_company
from watchlist import fetch_all_device_tokens_of, fetch_watchlist_companies
from datetime import datetime
import apns
import asyncio
import feedparser

uk_news_url = "https://www.investegate.co.uk/Rss.aspx?company="
database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def check_company_latest_news():
    company_symbols = fetch_watchlist_companies()
    for company_symbol in company_symbols:
        fetch_company_latest_news(company_symbol)


def fetch_company_latest_news(company_symbol):
    exchange = fetch_exchange_of_company(company_symbol)
    lateset_feed = feedparser.parse(uk_news_url + company_symbol)["entries"][:1][0]
    company_news = CompanyNews(
        title=lateset_feed["title"],
        company_symbol=company_symbol,
        company_name=lateset_feed["investegate_company"],
        exchange=exchange,
        headline=lateset_feed["investegate_headline"],
        pub_date=lateset_feed["published"],
        link=lateset_feed["link"],
    )
    if is_latest_news_in_db(company_symbol, company_news.pub_date):
        print("no news - " + company_symbol)
    else:
        print("breaking news! - " + company_symbol)
        delete_recent_company_news(company_symbol)
        add_latest_news_to_db(company_symbol, company_news.pub_date, company_news.title)
        send_push_notification(company_symbol, company_news)


def is_news_today(pub_date):
    article_pub_date = datetime.strptime(pub_date, "%d %b, %Y %H:%M:%S").date()
    today = datetime.today().date()
    if article_pub_date == today:
        return True
    else:
        return False


def send_push_notification(company_symbol, company_news):
    if is_news_today(company_news.pub_date):
        device_tokens = fetch_all_device_tokens_of(company_symbol)
        for device_token in device_tokens:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(apns.run(device_token, company_news))


check_company_latest_news()
