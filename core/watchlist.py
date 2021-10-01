from db_config.connection import DatabaseConnection

database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def fetch_all_device_tokens_of(company_symbol):
    device_tokens = database.filter_data(
        "SELECT device_token FROM watchlist WHERE company_symbol=%s", (company_symbol,)
    )
    return [i[0] for i in device_tokens]


def fetch_watchlist_companies():
    company_symbols = database.select_data(
        "SELECT DISTINCT company_symbol FROM watchlist"
    )
    return [i[0] for i in company_symbols]
