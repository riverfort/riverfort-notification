from db_config.connection import DatabaseConnection
import feedparser

uk_news_url = "https://www.investegate.co.uk/Rss.aspx?company="
database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


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


def is_latest_news_in_db(company_symbol, pub_date):
    result = database.filter_data(
        "SELECT * FROM company_news WHERE company_symbol=%s AND pub_date=%s",
        (company_symbol, pub_date),
    )
    if result == []:
        return False
    else:
        return True


def add_latest_news_to_db(company_symbol, pub_date, title):
    database.insert_data(
        "INSERT INTO company_news (company_symbol, pub_date, title) VALUES (%s, %s, %s) RETURNING company_symbol",
        (company_symbol, pub_date, title),
    )


def delete_recent_company_news(company_symbol):
    database.delete(
        "DELETE FROM company_news WHERE company_symbol=%s", (company_symbol,)
    )


check_company_latest_news()
