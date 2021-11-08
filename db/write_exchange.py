from db.conn import Conn

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)

exchanges = ["London", "AQS"]

for exchange in exchanges:
    conn.write(
        """
        INSERT INTO exchanges (exchange) VALUES (%s)
        ON CONFLICT (exchange)
        DO UPDATE SET exchange = EXCLUDED.exchange
        RETURNING exchange
        """,
        exchange,
    )

conn.close()
