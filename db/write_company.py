from db.db import DB
import csv

db = DB(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

csvfile = open("companies_data_source/lse_shares.csv", "r")
reader = csv.reader(csvfile)
for row in reader:
    company_symbol = row[0]
    company_name = row[1]
    db.write(
        """
        INSERT INTO companies (company_symbol, company_name, exchange) 
        VALUES (%s, %s, 'London')
        ON CONFLICT (company_symbol) DO UPDATE SET
        (company_symbol, company_name, exchange) = (EXCLUDED.company_symbol, EXCLUDED.company_name, 'London')
        RETURNING company_symbol
        """,
        company_symbol,
        company_name,
    )

db.close()
