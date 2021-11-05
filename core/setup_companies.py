from db_config.connection import DatabaseConnection
import csv


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)


def upsert_london_listed_companies():
    with open("companies_data_source/lse_shares.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            database.insert_data(
                """
                INSERT INTO companies (company_symbol, company_name, exchange) 
                VALUES (%s, %s, 'London')
                ON CONFLICT (company_symbol) DO UPDATE SET
                (company_symbol, company_name, exchange) = (EXCLUDED.company_symbol, EXCLUDED.company_name, 'London')
                RETURNING company_symbol
                """,
                (row[0], row[1]),
            )


upsert_london_listed_companies()
