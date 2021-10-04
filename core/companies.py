from db_config.connection import DatabaseConnection

database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def fetch_exchange_of_company(company_symbol):
    exchange = database.filter_data(
        "SELECT exchange FROM companies WHERE company_symbol=%s", (company_symbol,)
    )
    return [i[0] for i in exchange][0]
