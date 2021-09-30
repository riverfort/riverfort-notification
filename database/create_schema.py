from configuration.config import DatabaseConnection


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

print("Creating table device_tokens...")
database.create_table(
    "CREATE TABLE IF NOT EXISTS device_tokens (device_token VARCHAR(200) PRIMARY KEY)"
)

print("Creating table exchanges...")
database.create_table(
    """
    CREATE TABLE IF NOT EXISTS exchanges 
    (exchange VARCHAR(200) PRIMARY KEY)
    """
)

print("Creating table companies...")
database.create_table(
    """
    CREATE TABLE IF NOT EXISTS companies (
    company_symbol VARCHAR(200) PRIMARY KEY,
    company_name VARCHAR(200),
    exchange VARCHAR(200) NOT NULL REFERENCES exchanges (exchange) ON UPDATE CASCADE ON DELETE CASCADE)
    """
)

print("Creating table watchlist...")
database.create_table(
    """
    CREATE TABLE IF NOT EXISTS watchlist (
    device_token VARCHAR(200) NOT NULL REFERENCES device_tokens (device_token) ON UPDATE CASCADE ON DELETE CASCADE, 
    company_symbol VARCHAR(200) NOT NULL REFERENCES companies (company_symbol) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT watchlist_pkey PRIMARY KEY (device_token, company_symbol))
    """
)

print("Creating table company_news...")
database.create_table(
    """
    CREATE TABLE IF NOT EXISTS company_news (
    company_symbol VARCHAR(200) REFERENCES companies (company_symbol),
    pub_date TIMESTAMP NOT NULL,
    title VARCHAR(200) NOT NULL,
    PRIMARY KEY (company_symbol, pub_date))
    """
)
