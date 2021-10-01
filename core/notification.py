from db_config.connection import DatabaseConnection
from company_news import (
    is_latest_news_in_db,
    delete_recent_company_news,
    add_latest_news_to_db,
)
import feedparser

uk_news_url = "https://www.investegate.co.uk/Rss.aspx?company="
database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def send_push_notification():
    device_tokens = fetch_all_device_tokens_of("RMM")
    for device_token in device_tokens:
        print("Send Push Notification to: " + device_token)


def fetch_all_device_tokens_of(company_symbol):
    device_tokens = database.filter_data(
        "SELECT device_token FROM watchlist WHERE company_symbol=%s", (company_symbol,)
    )
    return [i[0] for i in device_tokens]


def check_company_latest_news():
    company_symbols = fetch_watchlist_companies()
    for company_symbol in company_symbols:
        fetch_company_latest_news(company_symbol)


def fetch_watchlist_companies():
    company_symbols = database.select_data(
        "SELECT DISTINCT company_symbol FROM watchlist"
    )
    return [i[0] for i in company_symbols]


def fetch_company_latest_news(company_symbol):
    lateset_feed = feedparser.parse(uk_news_url + company_symbol)["entries"][:1][0]
    title = lateset_feed["title"]
    pub_date = lateset_feed["published"]
    link = lateset_feed["link"]
    if is_latest_news_in_db(company_symbol, pub_date):
        print("no news - " + company_symbol)
    else:
        print("breaking news! - " + company_symbol)
        delete_recent_company_news(company_symbol)
        add_latest_news_to_db(company_symbol, pub_date, title)


send_push_notification()
