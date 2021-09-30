from configuration.config import DatabaseConnection


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

# Exchange naming references Yahoo Finance
exchanges = ["London", "AQS"]


def upsert_exchanges():
    for exchange in exchanges:
        database.insert_data(
            """
            INSERT INTO exchanges (exchange) VALUES (%s)
            ON CONFLICT (exchange)
            DO UPDATE SET exchange = EXCLUDED.exchange
            RETURNING exchange
            """,
            (exchange,),
        )


upsert_exchanges()