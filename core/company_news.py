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
