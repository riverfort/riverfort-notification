import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
db = os.path.dirname(currentdir)
sys.path.insert(0, db)

from db.db.conn import Conn

conn = Conn(
    host="localhost",
    port=5432,
    database="riverfort_notification",
    user="riverfort",
    password="rgctechnology",
)


def get_device_tokens_of(company_symbol):
    device_tokens = conn.get(
        "SELECT device_token FROM watchlist WHERE company_symbol=%s", company_symbol
    )
    result = [device_token[0] for device_token in device_tokens]
    return result


def get_companies():
    companies = conn.get("SELECT DISTINCT company_symbol FROM watchlist")
    result = [company[0] for company in companies]
    return result


result = get_companies()
print(result)
