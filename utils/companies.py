def get_company_symbols(conn):
    symbols = conn.get("SELECT company_symbol FROM companies")
    result = [symbol[0] for symbol in symbols]
    return result


def get_exchange(conn, company_symbol):
    exchange = conn.get(
        "SELECT exchange FROM companies WHERE company_symbol=%s", company_symbol
    )
    return exchange[0][0]
