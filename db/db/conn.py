import psycopg2


class Conn:
    def __init__(self, host, port, database, user, password):
        self._conn = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

    def close(self):
        self._conn.close()

    def get(self, sql, *args):
        cur = self._conn.cursor()
        cur.execute(sql, args)
        result = cur.fetchall()
        cur.close
        return result

    def write(self, sql, *args):
        cur = self._conn.cursor()
        cur.execute(sql, args)
        print(cur.statusmessage)
        self._conn.commit()
        cur.close
