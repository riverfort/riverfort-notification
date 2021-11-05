from db.db import DB

db = DB(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

exchanges = ["London", "AQS"]

for exchange in exchanges:
    db.write(
        """
        INSERT INTO exchanges (exchange) VALUES (%s)
        ON CONFLICT (exchange)
        DO UPDATE SET exchange = EXCLUDED.exchange
        RETURNING exchange
        """,
        (exchange,),
    )

db.close()
