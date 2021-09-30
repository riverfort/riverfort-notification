from configuration.config import DatabaseConnection
import csv


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

with open("/Users/nieqiuyang/Desktop/lse_shares.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        database.insert_data(
            """
            INSERT INTO companies (company_symbol, company_name, exchange) 
            VALUES (%s, %s, %s) 
            RETURNING company_symbol
            """,
            (row[0], row[1], "LSE"),
        )
