def get_device_tokens_of(conn, company_symbol):
    device_tokens = conn.get(
        "SELECT device_token FROM watchlist WHERE company_symbol=%s", company_symbol
    )
    result = [device_token[0] for device_token in device_tokens]
    return result


def get_company_symbols(conn):
    companies = conn.get("SELECT DISTINCT company_symbol FROM watchlist")
    result = [company[0] for company in companies]
    return result
