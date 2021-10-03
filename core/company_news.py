from db_config.connection import DatabaseConnection

database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


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


class CompanyNews:
    def __init__(self, title, company_symbol, company_name, headline, pub_date, link):
        super().__init__()
        self.title = title
        self.company_symbol = company_symbol
        self.company_name = company_name
        self.headline = headline
        self.pub_date = pub_date
        self.link = link

    def __str__(self):
        return f"""CompanyNews: 
        - title: {self.title}
        - company_symbol: {self.company_symbol}
        - company_name: {self.company_name}
        - headline: {self.headline}
        - pub_date: {self.pub_date}
        - link: {self.link}
        """
