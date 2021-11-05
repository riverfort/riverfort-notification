import psycopg2


class DB:
    def __init__(self, host, port, database, user, password):
        self._con = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )

    def close(self):
        self._con.close()

    def get(self, sql):
        cur = self._con.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close
        return result

    def write(self, sql, *args):
        cur = self._con.cursor()
        cur.execute(sql, args)
        print(cur.statusmessage)
        self._con.commit()
        cur.close
