from configuration.config import DatabaseConnection


database = DatabaseConnection(
    "riverfort_notification", "riverfort", "rgctechnology", "localhost", 5432
)

exchanges = ["London", "AQS"]

for exchange in exchanges:
    database.insert_data(
        """
        INSERT INTO exchanges (exchange) VALUES (%s)
        RETURNING exchange
        """, (exchange,)
    )
