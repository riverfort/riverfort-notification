from db.db import DB

db = DB(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

db.write(
    "CREATE TABLE IF NOT EXISTS device_tokens (device_token VARCHAR(200) PRIMARY KEY)"
)
db.write("CREATE TABLE IF NOT EXISTS exchanges (exchange VARCHAR(200) PRIMARY KEY)")
db.write(
    """
    CREATE TABLE IF NOT EXISTS companies (
    company_symbol VARCHAR(200) PRIMARY KEY,
    company_name VARCHAR(200),
    exchange VARCHAR(200) NOT NULL REFERENCES exchanges (exchange) ON UPDATE CASCADE ON DELETE CASCADE)
    """
)
db.write(
    """
    CREATE TABLE IF NOT EXISTS watchlist (
    watchlist_id SERIAL PRIMARY KEY,
    device_token VARCHAR(200) NOT NULL REFERENCES device_tokens (device_token) ON UPDATE CASCADE ON DELETE CASCADE, 
    company_symbol VARCHAR(200) NOT NULL REFERENCES companies (company_symbol) ON UPDATE CASCADE ON DELETE CASCADE,
    UNIQUE (device_token, company_symbol))
    """
)
db.write(
    """
    CREATE TABLE IF NOT EXISTS company_news (
    company_symbol VARCHAR(200) REFERENCES companies (company_symbol),
    pub_date TIMESTAMP NOT NULL,
    title VARCHAR(200) NOT NULL,
    PRIMARY KEY (company_symbol, pub_date))
    """
)

db.close()