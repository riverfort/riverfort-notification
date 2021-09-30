from db_config.connection import DatabaseConnection
import feedparser

uk_news_url = "https://www.investegate.co.uk/Rss.aspx?company="
database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def fetch_watchlist_companies():
    company_symbols = database.select_data(
        "SELECT DISTINCT company_symbol FROM watchlist"
    )
    for company_symbol in company_symbols:
        print(company_symbol[0])


def is_news_in_db(company_symbol, pub_date):
    result = database.filter_data(
        "SELECT * FROM company_news WHERE company_symbol=%s AND pub_date=%s",
        (company_symbol, pub_date),
    )
    if result == []:
        return False
    else:
        return True


def add_news_to_db(company_symbol, pub_date, title):
    database.insert_data(
        "INSERT INTO company_news (company_symbol, pub_date, title) VALUES (%s, %s, %s) RETURNING company_ticker",
        (company_symbol, pub_date, title),
    )


def delete_all_news(company_symbol):
    database.delete(
        "DELETE FROM company_news WHERE company_ticker=%s", (company_symbol,)
    )


def read_news(company_symbol):
    feeds = feedparser.parse(uk_news_url + company_symbol)["entries"]
    for feed in feeds:
        title = feed["title"]
        pub_date = feed["published"]
        link = feed["link"]
        if is_news_in_db(company_symbol, pub_date):
            print("No new announcement: " + company_symbol)
        else:
            print("New announcement: " + company_symbol)


fetch_watchlist_companies()
