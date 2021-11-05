from db_config.connection import DatabaseConnection

database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def fetch_exchange_of_company(company_symbol):
    exchange = database.filter_data(
        "SELECT exchange FROM companies WHERE company_symbol=%s", (company_symbol,)
    )
    return [i[0] for i in exchange][0]


def fetch_company_symbols():
    company_symbols = database.select_data("SELECT company_symbol FROM companies")
    symbols = [i[0] for i in company_symbols]
    symbol_list = list(map(lambda symbol: symbol + ".L", symbols))
    result = ",".join(symbol_list)
    print(result)


fetch_company_symbols()
