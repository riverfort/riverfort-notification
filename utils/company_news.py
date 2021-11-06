def insert_news(conn, company_symbol, pub_date, title):
    conn.write(
        "INSERT INTO company_news (company_symbol, pub_date, title) VALUES (%s, %s, %s) RETURNING company_symbol",
        company_symbol,
        pub_date,
        title,
    )


def delete_news_of(conn, company_symbol):
    conn.write("DELETE FROM company_news WHERE company_symbol=%s", company_symbol)


def news_exists(conn, company_symbol, pub_date):
    news = conn.get(
        "SELECT * FROM company_news WHERE company_symbol=%s AND pub_date=%s",
        company_symbol,
        pub_date,
    )
    return bool(news)
